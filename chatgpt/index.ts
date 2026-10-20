// Sparrow: MCP server for ChatGPT (Apps SDK / MCP Apps).
// Stateless streamable-HTTP JSON-RPC. Stores nothing, no auth, no external calls.
import { WIDGET_HTML, WIDGET_URI } from "./widget.ts";
import { CARD, HAND_IDS, variants, score, passes, sortRack, tileName, groupLabel, ALL_TYPES } from "./engine.ts";

const SERVER_INFO = { name: "sparrow-mahjong", title: "Sparrow Mahjong Coach", version: "1.0.0" };
const SUPPORTED = ["2025-11-25", "2025-06-18", "2025-03-26", "2024-11-05"];
const APP_URL = "https://apps.apple.com/app/id6819738312";

const INSTRUCTIONS =
  "Sparrow helps beginners at American mahjong. Use show_card_line when someone types a line from their card and asks what it means or what tiles it needs. " +
  "Use check_rack when someone lists the tiles on their rack and asks what hand to go for or what to pass in the Charleston. " +
  "Use show_practice_card to show example hands from Sparrow's own practice card. " +
  "Never recite, reproduce or guess lines of the official National Mah Jongg League card; work only from the line the user gives you. " +
  "Keep explanations short and plain, for someone new to the game.";

const LINE_TILES = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "flower", "north", "east", "west", "south", "dragon", "soap"];
const TOOL_META = (invoking: string, invoked: string) => ({
  ui: { resourceUri: WIDGET_URI },
  "openai/outputTemplate": WIDGET_URI,
  "openai/toolInvocation/invoking": invoking,
  "openai/toolInvocation/invoked": invoked,
});
const RO = { readOnlyHint: true, destructiveHint: false, openWorldHint: false, idempotentHint: true };

const TOOLS = [
  {
    name: "show_card_line",
    title: "Turn a card line into tiles",
    description:
      "Shows one line of an American mahjong card as real tiles, group by group, with each group named (pair, pung, kong, quint). " +
      "Use when someone types a line from their card, like 'FF 2222 0000 6666', and asks what it means. " +
      "On a printed card, color means suit: same color, same suit; different colors, different suits. Give each color its own suit letter A, B or C. " +
      "'D' is a dragon and belongs to that group's suit. '0' is the Soap (white dragon) and counts as zero. 'F' is a flower. N, E, W, S are winds. " +
      "The groups must add up to exactly 14 tiles. Only use the line the user typed.",
    inputSchema: {
      type: "object",
      properties: {
        title: { type: "string", maxLength: 60, description: "Short label, e.g. the hand's section on the card" },
        line: { type: "string", maxLength: 60, description: "The line exactly as the user typed it, e.g. 'FF 2222 0000 6666'" },
        concealed: { type: "boolean", description: "True if the line is marked C (concealed)" },
        groups: {
          type: "array", minItems: 1, maxItems: 8,
          items: {
            type: "object",
            properties: {
              tile: { type: "string", enum: LINE_TILES, description: "A number 1 to 9, or flower, north, east, west, south, dragon, soap" },
              count: { type: "integer", minimum: 1, maximum: 5, description: "How many of that tile" },
              suit: { type: "string", enum: ["A", "B", "C"], description: "Required for numbers and dragons. Same letter means same suit (same color on the card)." },
            },
            required: ["tile", "count"],
            additionalProperties: false,
          },
        },
      },
      required: ["groups"],
      additionalProperties: false,
    },
    annotations: { title: "Turn a card line into tiles", ...RO },
    _meta: TOOL_META("Laying out the tiles", "Tiles ready"),
  },
  {
    name: "check_rack",
    title: "Check a mahjong rack",
    description:
      "Takes the 13 or 14 tiles on a player's rack and shows the three closest hands on Sparrow's practice card, how many tiles each needs, and which tiles to pass in the Charleston (never a joker). " +
      "Tile codes: B1 to B9 for Bams, C1 to C9 for Craks, D1 to D9 for Dots, N E W S for winds, R red dragon, G green dragon, O soap (white dragon), F flower, J joker.",
    inputSchema: {
      type: "object",
      properties: {
        tiles: { type: "array", minItems: 13, maxItems: 14, items: { type: "string", maxLength: 12 }, description: "13 or 14 tile codes" },
      },
      required: ["tiles"],
      additionalProperties: false,
    },
    annotations: { title: "Check a mahjong rack", ...RO },
    _meta: TOOL_META("Reading the rack", "Rack checked"),
  },
  {
    name: "show_practice_card",
    title: "Show Sparrow practice hands",
    description:
      "Shows hands from Sparrow's own practice card (original hands made for learning, not the official League card), drawn as tiles with the rule for each. " +
      "Leave hand_id empty to show the whole practice card.",
    inputSchema: {
      type: "object",
      properties: { hand_id: { type: "string", enum: HAND_IDS, description: "One practice hand to show" } },
      additionalProperties: false,
    },
    annotations: { title: "Show Sparrow practice hands", ...RO },
    _meta: TOOL_META("Pulling the practice card", "Practice card ready"),
  },
];

const RESOURCE_META = {
  ui: { prefersBorder: true, csp: { connectDomains: [], resourceDomains: [] } },
  "openai/widgetDescription": "Mahjong tiles laid out by group, with plain explanations and a link to practice in Sparrow.",
  "openai/widgetPrefersBorder": true,
  "openai/widgetCSP": { connect_domains: [], resource_domains: [] },
};

const fail = (text: string) => ({ isError: true, content: [{ type: "text", text }] });
const clean = (s: unknown, max: number) => String(s ?? "").replace(/[\u0000-\u001f]/g, " ").trim().slice(0, max);

// ---------- show_card_line ----------
const SUIT_OF: Record<string, string> = { A: "B", B: "C", C: "D" };
const DRAGON_OF: Record<string, string> = { B: "G", C: "R", D: "O" };
const HONOR_OF: Record<string, string> = { flower: "F", north: "N", east: "E", west: "W", south: "S", soap: "O" };

function cardLine(a: any) {
  if (!a || !Array.isArray(a.groups) || !a.groups.length) return fail("Give the line as groups of tiles.");
  const groups: any[] = [];
  let total = 0;
  for (const g of a.groups.slice(0, 8)) {
    const tile = String(g?.tile || "").toLowerCase();
    const k = Math.round(Number(g?.count));
    if (!LINE_TILES.includes(tile)) return fail(`Unknown tile "${clean(g?.tile, 12)}".`);
    if (!(k >= 1 && k <= 5)) return fail("Each group needs a count from 1 to 5.");
    let t: string;
    if (/^[1-9]$/.test(tile) || tile === "dragon") {
      const s = SUIT_OF[String(g?.suit || "").toUpperCase()];
      if (!s) return fail("Numbers and dragons need a suit letter A, B or C.");
      t = tile === "dragon" ? DRAGON_OF[s] : s + tile;
    } else t = HONOR_OF[tile];
    total += k;
    groups.push({ t, k, label: groupLabel(k), name: tileName(t) });
  }
  if (total !== 14) return fail(`That line adds up to ${total} tiles. A full hand is exactly 14. Check the groups and try again.`);
  const suits = [...new Set(groups.map((g) => g.t).filter((t) => t.length === 2).map((t) => t[0]))];
  const concealed = !!a.concealed;
  const W = ["", "one", "two", "three", "four", "five"];
  const steps = groups.map((g) => `${g.label} (${W[g.k]} ${g.name})`);
  const notes: string[] = [];
  if (suits.length > 1) notes.push(`This line uses ${suits.length} different suits. Shown here as ${suits.map((s) => ({ B: "Bams", C: "Craks", D: "Dots" } as any)[s]).join(" and ")}, but any suits work as long as they differ.`);
  else if (suits.length === 1) notes.push("All numbers are in one suit. Shown in Bams, but any one suit works.");
  if (groups.some((g) => g.t === "O")) notes.push("The Soap doubles as zero in year hands.");
  notes.push(concealed ? "Concealed: you must draw every tile yourself, no calling discards." : "Jokers can stand in for tiles in any group of 3 or more, never in a pair or single.");
  return {
    structuredContent: { mode: "line", title: clean(a.title, 60) || "Your card line", line: clean(a.line, 60), concealed, groups, notes, app_url: APP_URL },
    content: [{ type: "text", text: `Shown as tiles: ${steps.join(", ")}. ${notes.join(" ")}` }],
  };
}

// ---------- check_rack ----------
const WORDS: Record<string, string> = {
  north: "N", east: "E", west: "W", south: "S", red: "R", green: "G", soap: "O", white: "O", flower: "F", joker: "J",
  bam: "B", bams: "B", bamboo: "B", crak: "C", craks: "C", crack: "C", character: "C", dot: "D", dots: "D", circle: "D",
};
function normTile(raw: string): string | null {
  const s = raw.trim().toUpperCase().replace(/\s+/g, "");
  if (ALL_TYPES.includes(s)) return s;
  let m = s.match(/^([1-9])([BCD])$/); if (m) return m[2] + m[1];
  const w = raw.trim().toLowerCase().replace(/dragon/g, "").trim();
  if (WORDS[w] && WORDS[w].length === 1 && !"BCD".includes(WORDS[w])) return WORDS[w];
  m = w.match(/^([1-9])\s*([a-z]+)$/) || w.match(/^([a-z]+)\s*([1-9])$/);
  if (m) {
    const [n, word] = /\d/.test(m[1]) ? [m[1], m[2]] : [m[2], m[1]];
    const su = WORDS[word];
    if (su && "BCD".includes(su)) return su + n;
  }
  return null;
}

function checkRack(a: any) {
  const raw = Array.isArray(a?.tiles) ? a.tiles : [];
  if (raw.length < 13 || raw.length > 14) return fail("A rack is 13 tiles (14 if it's your turn). List every tile.");
  const rack: string[] = [];
  for (const r of raw) {
    const t = normTile(String(r));
    if (!t) return fail(`I couldn't read "${clean(r, 12)}". Use codes like B3, C7, D1, N, R, F or J.`);
    rack.push(t);
  }
  const cnt: Record<string, number> = {};
  for (const t of rack) {
    cnt[t] = (cnt[t] || 0) + 1;
    const max = t === "F" || t === "J" ? 8 : 4;
    if (cnt[t] > max) return fail(`A set only has ${max} of the ${tileName(t)}.`);
  }
  const ranked = CARD.map((h) => ({ h, s: score(rack, h) }))
    .sort((x, y) => y.s.total - x.s.total || y.h.pts - x.h.pts)
    .slice(0, 3);
  const best = ranked.map(({ h, s }) => {
    const left: Record<string, number> = Object.assign({}, s.used);
    const tiles: { t: string; have: boolean }[] = [];
    s.groups.forEach((g) => { for (let i = 0; i < g.k; i++) { const have = (left[g.t] || 0) > 0; if (have) left[g.t]--; tiles.push({ t: g.t, have }); } });
    return { id: h.id, name: h.name, pts: h.pts, rule: h.rule, concealed: !!h.conc, have: s.total, need: Math.max(0, 14 - s.total), jokers_used: s.j, groups: s.groups, tiles };
  });
  const pass = passes(rack, ranked[0].s.used).slice(0, 3);
  const top = best[0];
  const text =
    `Closest practice hand: ${top.name} (${top.have} of 14, needs ${top.need}${top.jokers_used ? `, counting ${top.jokers_used} joker${top.jokers_used > 1 ? "s" : ""}` : ""}). ` +
    `Next: ${best.slice(1).map((b) => `${b.name} (${b.have} of 14)`).join(", ")}. ` +
    (pass.length ? `Charleston: pass ${pass.map(tileName).join(", ")}. Never pass a joker.` : "Every tile helps the top hand.") +
    " This uses Sparrow's practice card, not the official card.";
  return {
    structuredContent: { mode: "rack", rack: sortRack(rack), best, passes: pass, app_url: APP_URL },
    content: [{ type: "text", text }],
  };
}

// ---------- show_practice_card ----------
function practiceCard(a: any) {
  const id = a?.hand_id;
  if (id !== undefined && !HAND_IDS.includes(id)) return fail("Unknown practice hand.");
  const list = (id ? CARD.filter((h) => h.id === id) : CARD).map((h) => ({
    id: h.id, name: h.name, pts: h.pts, rule: h.rule, concealed: !!h.conc, groups: variants(h)[0], ways: variants(h).length,
  }));
  return {
    structuredContent: { mode: "card", hands: list, app_url: APP_URL },
    content: [{ type: "text", text: (id ? `Practice hand ${list[0].name}: ${list[0].rule}` : `Sparrow practice card, ${list.length} hands.`) + " These are Sparrow's own learning hands, not the official League card." }],
  };
}

// ---------- JSON-RPC ----------
const ok = (id: unknown, result: unknown) => ({ jsonrpc: "2.0", id, result });
const err = (id: unknown, code: number, message: string) => ({ jsonrpc: "2.0", id: id ?? null, error: { code, message } });
const HANDLERS: Record<string, (a: any) => unknown> = { show_card_line: cardLine, check_rack: checkRack, show_practice_card: practiceCard };

function handle(msg: any): object | null {
  if (!msg || msg.jsonrpc !== "2.0" || typeof msg.method !== "string") return err(msg?.id, -32600, "Invalid Request");
  const isNotification = msg.id === undefined || msg.id === null;
  const p = msg.params ?? {};
  switch (msg.method) {
    case "initialize": {
      const protocolVersion = SUPPORTED.includes(p.protocolVersion) ? p.protocolVersion : SUPPORTED[0];
      return ok(msg.id, {
        protocolVersion,
        capabilities: { tools: { listChanged: false }, resources: { listChanged: false }, extensions: { "io.modelcontextprotocol/ui": {} } },
        serverInfo: SERVER_INFO,
        instructions: INSTRUCTIONS,
      });
    }
    case "ping": return isNotification ? null : ok(msg.id, {});
    case "tools/list": return ok(msg.id, { tools: TOOLS });
    case "tools/call": {
      const h = HANDLERS[p.name];
      if (!h) return err(msg.id, -32602, `Unknown tool: ${p.name}`);
      return ok(msg.id, h(p.arguments ?? {}));
    }
    case "resources/list":
      return ok(msg.id, { resources: [{ uri: WIDGET_URI, name: "sparrow-tiles", title: "Sparrow tiles", mimeType: "text/html;profile=mcp-app", _meta: RESOURCE_META }] });
    case "resources/templates/list": return ok(msg.id, { resourceTemplates: [] });
    case "resources/read":
      if (p.uri !== WIDGET_URI) return err(msg.id, -32002, "Resource not found");
      return ok(msg.id, { contents: [{ uri: WIDGET_URI, mimeType: "text/html;profile=mcp-app", text: WIDGET_HTML, _meta: RESOURCE_META }] });
    case "prompts/list": return ok(msg.id, { prompts: [] });
    default:
      if (isNotification) return null;
      return err(msg.id, -32601, `Method not found: ${msg.method}`);
  }
}

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, GET, DELETE, OPTIONS",
  "Access-Control-Allow-Headers": "content-type, accept, authorization, mcp-session-id, mcp-protocol-version, last-event-id",
  "Access-Control-Expose-Headers": "mcp-session-id",
};

export async function serve(req: Request): Promise<Response> {
  if (req.method === "OPTIONS") return new Response(null, { status: 204, headers: CORS });
  if (req.method !== "POST") return new Response("Method Not Allowed", { status: 405, headers: { ...CORS, Allow: "POST" } });
  const len = Number(req.headers.get("content-length") || 0);
  if (len > 32 * 1024) return Response.json(err(null, -32600, "Request too large"), { status: 413, headers: CORS });
  let body: any;
  try { body = JSON.parse(await req.text()); } catch {
    return Response.json(err(null, -32700, "Parse error"), { status: 400, headers: CORS });
  }
  const batch = Array.isArray(body);
  const out = (batch ? body.slice(0, 20) : [body]).map((m: any) => {
    try { return handle(m); } catch (e) {
      console.error("handler error", m?.method, (e as Error)?.message);
      return err(m?.id, -32603, "Internal error");
    }
  }).filter((r: unknown) => r !== null);
  if (out.length === 0) return new Response(null, { status: 202, headers: CORS });
  return Response.json(batch ? out : out[0], { headers: CORS });
}

if (typeof Deno !== "undefined" && (Deno as any).serve) Deno.serve(serve);
