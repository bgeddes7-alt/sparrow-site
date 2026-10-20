// sparrow-site worker: serves the static site, and forwards /mcp (the ChatGPT app) to the
// sparrow-chatgpt edge function. Holds no secrets and stores nothing.
const UPSTREAM = "https://wqvdvtcwzzfcnxmklbla.supabase.co/functions/v1/sparrow-chatgpt";
const MAX_BODY = 32 * 1024;
const SEC = { "Strict-Transport-Security": "max-age=31536000; includeSubDomains", "X-Content-Type-Options": "nosniff", "Referrer-Policy": "no-referrer", "Cache-Control": "no-store" };
const json = (o, status = 200) => new Response(JSON.stringify(o), { status, headers: { "Content-Type": "application/json", ...SEC } });

async function mcp(request) {
  if (request.method === "OPTIONS") return new Response(null, { status: 204, headers: SEC });
  if (request.method === "GET") return json({ name: "Sparrow", endpoint: "POST /mcp (MCP Streamable HTTP, JSON responses)" }, 405);
  if (request.method !== "POST") return json({ error: "Method not allowed" }, 405);
  if (!(request.headers.get("content-type") || "").toLowerCase().includes("application/json")) return json({ error: "Use application/json" }, 415);
  const body = await request.arrayBuffer();
  if (body.byteLength > MAX_BODY) return json({ error: "Request too large" }, 413);
  const fwd = { "Content-Type": "application/json", Accept: "application/json, text/event-stream" };
  const pv = request.headers.get("mcp-protocol-version");
  if (pv) fwd["MCP-Protocol-Version"] = pv.slice(0, 20);
  let res;
  try { res = await fetch(UPSTREAM, { method: "POST", headers: fwd, body, signal: AbortSignal.timeout(25000) }); }
  catch { return json({ jsonrpc: "2.0", id: null, error: { code: -32603, message: "Sparrow is busy. Try again in a minute." } }, 502); }
  return new Response(res.body, { status: res.status, headers: { ...SEC, "Content-Type": res.headers.get("content-type") || "application/json" } });
}

export default {
  async fetch(request, env) {
    const p = new URL(request.url).pathname;
    if (p === "/mcp" || p === "/mcp/") return mcp(request);
    return env.ASSETS.fetch(request);
  },
};
