// Sparrow practice card and scoring engine, ported from the Sparrow iOS app (www/index.html).
// Original practice hands only. Never the NMJL card.

export type Group = { t: string; k: number };
type HandDef = { id: string; name: string; pts: number; rule: string; conc?: boolean; nr?: [number, number]; g: any[] };

export const SUITS: Record<string, string> = { B: "Bam", C: "Crak", D: "Dot" };
export const HONORS: Record<string, string> = {
  N: "North", E: "East", W: "West", S: "South", R: "Red Dragon", G: "Green Dragon", O: "Soap", F: "Flower", J: "Joker",
};
export function tileName(c: string): string {
  if (SUITS[c[0]] && c.length === 2) return c[1] + " " + SUITS[c[0]];
  return HONORS[c] || c;
}
export const ALL_TYPES: string[] = [];
["B", "C", "D"].forEach((s) => { for (let n = 1; n <= 9; n++) ALL_TYPES.push(s + n); });
["N", "E", "W", "S", "R", "G", "O", "F", "J"].forEach((h) => ALL_TYPES.push(h));
const ORDER: Record<string, number> = Object.fromEntries(ALL_TYPES.map((t, i) => [t, i]));
export const sortRack = (r: string[]) => r.slice().sort((a, b) => ORDER[a] - ORDER[b]);

const DR: Record<string, string> = { B: "G", C: "R", D: "O" };
export const CARD: HandDef[] = [
  { id: "stair", name: "Stair Step", pts: 25, rule: "One suit. Four numbers in a row.", nr: [1, 6],
    g: [{ h: "F", k: 2 }, { s: "x", n: 0, k: 3 }, { s: "x", n: 1, k: 4 }, { s: "x", n: 2, k: 3 }, { s: "x", n: 3, k: 2 }] },
  { id: "sevens", name: "Lucky Sevens", pts: 25, rule: "Sevens in all three suits.",
    g: [{ s: "x", n: 7, k: 4 }, { s: "y", n: 7, k: 4 }, { s: "z", n: 7, k: 3 }, { h: "F", k: 3 }] },
  { id: "winds", name: "Four Winds", pts: 30, rule: "All four winds. No suits at all.",
    g: [{ h: "N", k: 3 }, { h: "E", k: 4 }, { h: "W", k: 4 }, { h: "S", k: 3 }] },
  { id: "evens", name: "Evens Up", pts: 25, rule: "One suit, even numbers, plus that suit's dragon.",
    g: [{ s: "x", n: 2, k: 2 }, { s: "x", n: 4, k: 3 }, { s: "x", n: 6, k: 4 }, { s: "x", n: 8, k: 3 }, { dr: "x", k: 2 }] },
  { id: "odd", name: "Odd Couple", pts: 25, rule: "Two suits, odd numbers.",
    g: [{ s: "x", n: 1, k: 3 }, { s: "x", n: 3, k: 3 }, { s: "y", n: 5, k: 4 }, { s: "y", n: 7, k: 4 }] },
  { id: "dragons", name: "Dragon Party", pts: 30, rule: "All three dragons plus any one number.", nr: [1, 9],
    g: [{ h: "R", k: 3 }, { h: "G", k: 3 }, { h: "O", k: 3 }, { h: "F", k: 2 }, { s: "x", n: 0, k: 3 }] },
  { id: "year", name: "Twenty Twenty-Six", pts: 25, rule: "Soap counts as zero. 2s and 6s in different suits.",
    g: [{ h: "F", k: 2 }, { s: "x", n: 2, k: 4 }, { h: "O", k: 4 }, { s: "y", n: 6, k: 4 }] },
  { id: "like", name: "Like Numbers", pts: 25, rule: "Any one number in all three suits.", nr: [1, 9],
    g: [{ h: "F", k: 2 }, { s: "x", n: 0, k: 4 }, { s: "y", n: 0, k: 4 }, { s: "z", n: 0, k: 4 }] },
  { id: "tworun", name: "Two-Suit Run", pts: 25, rule: "Four numbers in a row, split across two suits.", nr: [1, 6],
    g: [{ s: "x", n: 0, k: 4 }, { s: "x", n: 1, k: 4 }, { s: "y", n: 2, k: 3 }, { s: "y", n: 3, k: 3 }] },
  { id: "steps", name: "Three Steps", pts: 25, rule: "Three numbers in a row, one per suit, plus flowers.", nr: [1, 7],
    g: [{ h: "F", k: 3 }, { s: "x", n: 0, k: 3 }, { s: "y", n: 1, k: 4 }, { s: "z", n: 2, k: 4 }] },
  { id: "bigrun", name: "Big Run", pts: 30, rule: "One suit, four in a row, ending in a quint. Jokers help.", nr: [1, 6],
    g: [{ s: "x", n: 0, k: 2 }, { s: "x", n: 1, k: 3 }, { s: "x", n: 2, k: 4 }, { s: "x", n: 3, k: 5 }] },
  { id: "pungdragon", name: "Pungs and a Dragon", pts: 25, rule: "Two numbers in a row with that suit's dragon, plus a kong in another suit.", nr: [1, 8],
    g: [{ s: "x", n: 0, k: 3 }, { s: "x", n: 1, k: 3 }, { dr: "x", k: 4 }, { s: "y", n: 0, k: 4 }] },
  { id: "windnum", name: "Winds and a Pair", pts: 30, rule: "A pung of each wind plus any pair.", nr: [1, 9],
    g: [{ h: "N", k: 3 }, { h: "E", k: 3 }, { h: "W", k: 3 }, { h: "S", k: 3 }, { s: "x", n: 0, k: 2 }] },
  { id: "ns", name: "North and South", pts: 25, rule: "Kongs of North and South plus any number in two suits.", nr: [1, 9],
    g: [{ h: "N", k: 4 }, { h: "S", k: 4 }, { s: "x", n: 0, k: 3 }, { s: "y", n: 0, k: 3 }] },
  { id: "ew", name: "East and West", pts: 25, rule: "Kongs of East and West plus two numbers in a row.", nr: [1, 8],
    g: [{ h: "E", k: 4 }, { h: "W", k: 4 }, { s: "x", n: 0, k: 3 }, { s: "x", n: 1, k: 3 }] },
  { id: "three69", name: "3-6-9", pts: 25, rule: "Threes, sixes and nines in two suits, plus flowers.",
    g: [{ h: "F", k: 3 }, { s: "x", n: 3, k: 3 }, { s: "x", n: 6, k: 4 }, { s: "y", n: 9, k: 4 }] },
  { id: "garden", name: "Flower Garden", pts: 25, rule: "A kong of flowers and three in a row in one suit.", nr: [1, 7],
    g: [{ h: "F", k: 4 }, { s: "x", n: 0, k: 4 }, { s: "x", n: 1, k: 3 }, { s: "x", n: 2, k: 3 }] },
  { id: "twodragons", name: "Two Dragons", pts: 25, rule: "Two suits, each with its own dragon, same number.", nr: [1, 9],
    g: [{ dr: "x", k: 3 }, { dr: "y", k: 3 }, { s: "x", n: 0, k: 4 }, { s: "y", n: 0, k: 4 }] },
  { id: "pairs", name: "Seven Pairs", pts: 50, rule: "Concealed. Pairs only, so no jokers.", conc: true, nr: [1, 3],
    g: [{ s: "x", n: 0, k: 2 }, { s: "x", n: 1, k: 2 }, { s: "x", n: 2, k: 2 }, { s: "y", n: 3, k: 2 }, { s: "y", n: 4, k: 2 }, { s: "z", n: 5, k: 2 }, { s: "z", n: 6, k: 2 }] },
];
export const HAND_IDS = CARD.map((h) => h.id);

const PERMS = [["B", "C", "D"], ["B", "D", "C"], ["C", "B", "D"], ["C", "D", "B"], ["D", "B", "C"], ["D", "C", "B"]];
const VCACHE = new Map<string, Group[][]>();
export function variants(h: HandDef): Group[][] {
  const hit = VCACHE.get(h.id);
  if (hit) return hit;
  const out: Group[][] = [], seen = new Set<string>();
  const nr = h.nr || [0, 0];
  PERMS.forEach((p) => {
    const m: Record<string, string> = { x: p[0], y: p[1], z: p[2] };
    for (let base = nr[0]; base <= nr[1]; base++) {
      const groups = h.g.map((g: any) => {
        let t: string;
        if (g.h) t = g.h; else if (g.dr) t = DR[m[g.dr]]; else t = m[g.s] + (h.nr ? base + g.n : g.n);
        return { t, k: g.k };
      });
      const key = groups.map((g: Group) => g.t + g.k).join("|");
      if (!seen.has(key)) { seen.add(key); out.push(groups); }
    }
  });
  VCACHE.set(h.id, out);
  return out;
}

export function score(rack: string[], h: HandDef) {
  const cnt: Record<string, number> = {};
  rack.forEach((t) => (cnt[t] = (cnt[t] || 0) + 1));
  const jokers = cnt.J || 0;
  let best: { total: number; groups: Group[]; used: Record<string, number>; j: number } | null = null;
  variants(h).forEach((groups) => {
    const left: Record<string, number> = Object.assign({}, cnt);
    let nat = 0, jEligible = 0;
    const used: Record<string, number> = {};
    groups.forEach((g) => {
      const have = Math.min(left[g.t] || 0, g.k);
      left[g.t] = (left[g.t] || 0) - have; nat += have; used[g.t] = (used[g.t] || 0) + have;
      if (g.k >= 3 && !h.conc) jEligible += g.k - have;
    });
    const j = Math.min(jokers, jEligible);
    const total = nat + j;
    if (!best || total > best.total) best = { total, groups, used, j };
  });
  return best!;
}

export function groupLabel(k: number): string {
  return ({ 1: "single", 2: "pair", 3: "pung", 4: "kong", 5: "quint" } as Record<number, string>)[k] || k + " of a kind";
}

// Charleston: tiles the best hand does not use. Never a joker.
export function passes(rack: string[], used: Record<string, number>): string[] {
  const u = Object.assign({}, used);
  const out: string[] = [];
  for (const t of sortRack(rack)) {
    if (t === "J") continue;
    if ((u[t] || 0) > 0) { u[t]--; continue; }
    out.push(t);
  }
  return out;
}
