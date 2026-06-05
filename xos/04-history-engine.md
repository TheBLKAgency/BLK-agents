# 04 · The History Engine — How Xos Makes (and Records) History

This is the heart of the sandbox. The engine answers one question, over and over,
forever: **"What happens in the next year?"**

It uses a **hybrid** approach:

- **Systems** (deterministic code) decide *what is true* — the hard facts of the world.
- **Agents** (LLM personas drawn from this repo) decide *what to do about it* — and tell
  the story.
- **The Chronicle** writes everything down, permanently.

```
 ┌──────────────────────────────────────────────────────────────────┐
 │                         ONE TICK = ONE YEAR                       │
 │                                                                    │
 │  PHASE 1  SYSTEMS RESOLVE  (deterministic, seeded RNG)             │
 │    population → climate → agriculture → economy → tech →           │
 │    disease → migration → resolve pending wars                      │
 │           │  emits: world facts + "pressures" + auto-events        │
 │           ▼                                                        │
 │  PHASE 2  AGENTS DECIDE     (LLM personas, one per polity)         │
 │    each leader agent gets a BRIEF (its state + pressures + news)   │
 │    → returns 1–3 ACTIONS (structured) + a short in-character note  │
 │           │  actions are validated against rules (no cheating)     │
 │           ▼                                                        │
 │  PHASE 3  ACTIONS RESOLVE   (deterministic again)                  │
 │    diplomacy, declarations of war, building, reforms, trade        │
 │    deals → update world state; queue multi-year actions            │
 │           │                                                        │
 │           ▼                                                        │
 │  PHASE 4  CHRONICLE         (record everything)                    │
 │    write events, decisions, narration → append-only history        │
 │           │                                                        │
 │           ▼                                                        │
 │  advance tick_index += 1 ;  year -= 1 (toward 0, then AD)          │
 └──────────────────────────────────────────────────────────────────┘
```

---

## Determinism contract (why this stays coherent for 1,000 years)

- The world has a single **master seed**. All randomness derives from
  `hash(master_seed, tick_index, system_name, entity_id)`. → Same seed + same agent
  decisions = **same history, replayable.**
- **Agents are the only non-deterministic input.** We log every agent prompt and response,
  so even agent-driven history is **reproducible from the logs** (re-run = replay; new
  run with `temperature>0` = a fresh timeline).
- **Systems never read the chronicle narration** — only structured facts. Flavor text can
  never corrupt the simulation. (See the "fixed vs. evolves" contract in `01` §6.)

---

## Phase 1 · The deterministic systems

Each system is a pure function: `(world_state, rng) → (world_state', events[])`. They run
in this order every tick.

### A. Population
- Each region has **population** and a **carrying capacity** (from climate + tech + land).
- Growth: logistic toward capacity. `Δpop = pop * r * (1 - pop/capacity)` where `r`
  rises with stability and food surplus, falls with war, famine, plague.
- Overshoot (`pop > capacity`) → emits a **migration pressure** and raises famine odds.

### B. Climate & weather events
- Each region's climate band (`01` §5) sets baseline temperature/rainfall.
- Per tick, sample anomalies: drought, flood, harsh winter, good years. Probabilities are
  band-specific (deserts → drought-prone; monsoon → flood-prone).
- Emits weather **events** that feed Agriculture.

### C. Agriculture & food
- Food output = `f(suitable_crops, climate_this_year, tech, labor, infrastructure)`.
- Surplus → population growth + economy boost + supports cities.
- Deficit → famine event, population loss, **stability hit**, unrest pressure.

### D. Economy & trade
- Each polity has a **treasury** and **income** (tax of production + trade route tolls).
- Trade routes are edges between regions; they carry goods, **wealth, tech, religion, and
  disease**. Sea routes need ships; caravan routes cross steppe/desert.
- Wealth funds armies, buildings, and agent ambitions. Bankruptcy → instability events.

### E. Technology
- Tech is a lightweight **tree** (e.g., ironworking → steel; sailing → deep-ocean
  navigation; writing → bureaucracy → printing; etc.).
- Progress per tick ∝ economy × stability × population × "openness" (trade contacts).
- Tech **diffuses** along trade and across borders: neighbors of an advanced polity catch
  up over time. Conquest transfers tech instantly. Isolation (Itzalan) slows it.

### F. Disease
- Endemic loads by biome (jungle malaria-analog in Murunga; crowd diseases in dense
  Zhang-Lu cities).
- **Epidemics**: triggered by trade contact between disease pools, crowding, war. A plague
  can cross the map along trade routes — a major historical force, not a footnote.

### G. Migration & frontier
- Migration pressures (from overshoot, war, climate) move population along the map:
  Voskar → south, steppe → settled lands, crowded cores → frontiers (Thulven, deep
  Murunga). Migrations can **found new settlements** or **destabilize** targets.

### H. Resolve pending wars
- Wars declared in earlier ticks resolve here using army size, tech, terrain, supply,
  leadership, and seeded RNG. Outcomes: territory changes, casualties, treaties,
  collapses → all become **events** and new **pressures**.

**Phase 1 output = a fresh, true world state + a list of `pressures` per polity** (e.g.
`FAMINE_IN_OKSUS`, `KHORR_RAID_THREAT`, `TREASURY_LOW`, `TECH_BEHIND_NEIGHBOR`,
`SUCCESSION_CRISIS`).

---

## Phase 2 · The agents (this is where the repo's personas come in)

Each polity has a **leader agent** — an LLM persona that role-plays its ruler. **We reuse
the agent personalities already in this repo** as the behavioral backbone:

| Xos role | Built from repo persona(s) | Why |
|----------|----------------------------|-----|
| The Consul (Aurelia) | `strategy/` strategist + `marketing/` persuader | Faction politics & rhetoric |
| The Emperor (Zhang) | `strategy/` + `project-management/` planner | Order, bureaucracy, long horizon |
| The Khan (Khorr) | `strategy/` opportunist | Raid-or-trade calculus |
| The Jarl (Skelgard) | `game-development/narrative-designer` | Saga-driven, bold |
| The God-King (Kessar) | `strategy/` + tradition framing | Prestige, caution |
| The Priest-King (Altun) | `game-development/narrative-designer` | Ritual, cyclical worldview |
| War-Chief / Council | `strategy/` + persona flavor | Honor / rivalry |

> Practically: each Xos leader = a **system prompt** that fuses (a) the polity's stats
> and worldview from `03`, with (b) a personality lifted from an existing repo agent.
> This is the literal payoff of building Xos *inside* the agency repo.

### The brief → decision contract

Each tick, every leader agent receives a compact **BRIEF** (never the whole world — just
what its ruler would plausibly know):

```jsonc
{
  "you_are": "The Consul of the Aurelian League",
  "year": "59 BC",
  "your_state": { "treasury": 1200, "stability": 5, "military": 8, "regions": [...] },
  "pressures": ["NORVANIC_RAIDS_RISING", "GENERAL_AMBITIOUS"],
  "known_world": [ /* neighbors & contacts only, fogged */ ],
  "recent_news": [ "Skelgard raiders struck the Ambercoast", "Zhang silk price up" ],
  "options_menu": ["DECLARE_WAR","MAKE_PEACE","FORM_ALLIANCE","BUILD","REFORM",
                   "RAISE_ARMY","TRADE_DEAL","SEND_ENVOY","DO_NOTHING"]
}
```

The agent returns **structured actions + a one-paragraph in-character note**:

```jsonc
{
  "actions": [
    { "type": "RAISE_ARMY", "target": "Norvane", "size": 20000 },
    { "type": "SEND_ENVOY", "target": "Zhang Empire", "offer": "trade_pact" }
  ],
  "narration": "Rome — Auria — does not bleed at its edges and call it peace..."
}
```

### Guardrails (agents can't cheat)
- Actions are **validated against the rules**: can't spend money you don't have, can't
  move an army faster than terrain allows, can't declare war on someone you can't reach.
- Invalid actions are **rejected with a reason** and the agent may get one retry, else the
  turn defaults to `DO_NOTHING`.
- The agent's narration is **flavor only** — it never changes facts. Only validated
  structured actions touch the world.

### Cost control (because this is the expensive part)
- Only **active polities** get full LLM turns. Dormant/tribal regions use cheap rule-based
  behavior.
- **Quiet years are batched**: if no pressures cross a threshold, the agent turn is
  skipped and a rules-based default applies. LLM calls happen when history is interesting.
- Model tiering: routine turns on a small fast model; pivotal moments (wars, successions,
  first contact) escalate to a stronger model. Configurable per run.

---

## Phase 3 · Actions resolve

All validated actions from all agents are collected and resolved **deterministically and
simultaneously** (so no agent gets an unfair turn-order advantage):

- Diplomacy (alliances, pacts, marriages) updates relationship graph.
- War **declarations** are queued for next-tick resolution in Phase 1.H (gives the target
  a tick to react — and the chronicle a sense of escalation).
- Buildings, reforms, army-raising deduct cost now, deliver effects over 1–N ticks.
- Conflicting actions (two polities claim the same region) resolve by rule.

---

## Phase 4 · The Chronicle (the "record" half of the brief)

Everything is written to an **append-only** history. Three layers, so the website can
zoom from headline to detail:

| Layer | Granularity | Example |
|-------|-------------|---------|
| **Annals** | One line per year per polity | *"59 BC — Aurelia raised 20,000 troops on the Norvanic frontier."* |
| **Events** | Discrete happenings, typed & geolocated | `WAR_DECLARED`, `PLAGUE`, `CITY_FOUNDED`, `RULER_DIED`, `TECH_DISCOVERED`, `FIRST_CONTACT` |
| **Sagas** | Auto-stitched multi-year narratives | *"The Norvanic Wars (59–46 BC)"* — generated when a chain of related events closes |

Each event stores: `tick`, `year`, `type`, `location (region)`, `actors (polities)`,
`magnitude`, `causes (links to prior events)`, and optional `narration`. That causal
linking is what lets the site show **"why did this happen?"** trails.

> **The Chronicle is the product.** The map and stats show the *now*; the Chronicle is the
> living history the user came to watch. It is never overwritten — only appended.

---

## Tuning levers (the "sandbox" knobs)

Exposed so the user can shape — but not script — history:

- **Speed:** how many ticks/day the cron advances (1 year/day? 10?/manual step).
- **Chaos:** RNG variance — calm history vs. dramatic swings.
- **Agent autonomy:** fully autonomous ↔ user can issue "nudges" as fate/events.
- **Determinism:** fixed seed (replayable) vs. live temperature (one-of-a-kind timeline).
- **Detail:** how often LLM narration fires vs. terse rules-only annals (cost vs. color).

---

## What "good" looks like (success criteria)

A healthy Xos run should, **without scripting**, produce things like:
- Aurelia's republic cracking into empire after a victorious general overreaches.
- A plague riding the silk route from Zhang-Lu to Kessara and gutting both.
- Skelgard raiders founding a coastal kingdom in northern Aurelia.
- Zhang's dynastic cycle: golden age → corruption → rebellion → new dynasty.
- Centuries later: someone crosses the Pelagine and **discovers Itzalan** — first contact.
- Thulven slowly settled as a frontier when southern populations overflow.

If the engine generates surprises like these on its own and records *why* they happened,
it works.

---

**Next:** how we actually build and host it → [`05-architecture.md`](./05-architecture.md)
