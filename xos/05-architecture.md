# 05 · Technical Architecture — Next.js + Supabase + Vercel

How Xos becomes a thing you can put on your website. This is the **build plan** that flows
from the design docs. Nothing here changes the world's design (`01`–`03`) or the engine's
logic (`04`) — it's the machinery that runs them.

---

## Stack at a glance

| Layer | Choice | Why |
|-------|--------|-----|
| **Database / state** | **Supabase** (Postgres + Row Level Security + Realtime) | Persistent world state that survives between visits and *accumulates*; Realtime pushes live updates to the map |
| **App / UI / API** | **Next.js** (App Router) | Map view, timeline, chronicle reader; server routes for the engine |
| **Tick engine** | **Supabase Edge Function** (or Next.js route) invoked by cron | Advances the world one year per run |
| **Scheduler** | **Vercel Cron** | "Time passes" automatically — e.g. one year per day |
| **Agents** | **Claude API** (Anthropic) via the engine | Leader-agent decisions + narration (see `04` Phase 2) |
| **Hosting** | **Vercel** | One-click deploy of the Next.js app; serverless functions; cron |

> All three platforms (Supabase, Vercel, and the GitHub repo) are reachable from this
> session via MCP, so the build can be largely automated when you give the word.

---

## Data model (Supabase / Postgres)

The schema mirrors the design docs one-to-one.

```sql
-- The world itself (supports multiple sandboxes / re-rolls)
world            (id, name, master_seed, current_tick, current_year,
                  speed, chaos, determinism_mode, created_at)

-- Fixed geography (seeded from 01 & 02, never mutated by the sim)
continent        (id, world_id, name, hemisphere, climate_band, analog)
region           (id, world_id, continent_id, name, climate_band,
                  base_carrying_capacity, terrain, coast bool, resources jsonb)

-- Mutable world state (the sim writes these every tick)
polity           (id, world_id, name, govt_type, capital_region_id,
                  treasury, stats jsonb,        -- mil/eco/tech/stability/...
                  religion_id, leader_agent_id, alive bool)
region_control   (region_id, polity_id, population, since_tick)  -- who holds what now
tech             (id, world_id, polity_id, tech_key, level, acquired_tick)
religion         (id, world_id, name, type, origin_region_id, founded_tick)
trade_route      (id, world_id, from_region_id, to_region_id, kind, active bool)
relationship     (world_id, polity_a, polity_b, status, value)   -- ally/war/...
pending_action   (id, world_id, tick, polity_id, type, payload jsonb, resolves_tick)

-- The history (append-only — the product)
annal            (id, world_id, tick, year, polity_id, line)
event            (id, world_id, tick, year, type, region_id,
                  actors jsonb, magnitude, causes jsonb, narration text)
saga             (id, world_id, title, start_tick, end_tick, event_ids jsonb, summary)

-- Reproducibility / audit
agent_log        (id, world_id, tick, polity_id, prompt jsonb, response jsonb, model)
```

Design rules:
- `continent` / `region` base columns are **write-once** (the fixed contract from `01`§6).
  Everything mutable lives in `region_control`, `polity`, etc.
- `event` and `annal` are **append-only** (enforced by RLS / no UPDATE/DELETE policy).
- `agent_log` makes any run **replayable** (`04` determinism contract).

---

## The tick loop, as code paths

```
Vercel Cron  ──(POST /api/tick, secured)──►  Tick Engine
                                                │
   1. load world_state from Supabase            │
   2. run SYSTEMS (Phase 1) ───────────────────► pure TS modules, seeded RNG
   3. build BRIEFs, call Claude per active polity (Phase 2)
   4. validate + resolve ACTIONS (Phase 3)
   5. write events / annals / sagas (Phase 4)
   6. UPDATE world.current_tick (+1), persist new state
   7. Supabase Realtime ──► connected browsers update live
```

- The engine is **idempotent per tick**: it checks `current_tick` so a retried cron run
  can't double-advance the year.
- One tick = one DB transaction where possible, so a crash leaves the world consistent.
- Manual stepping is the same endpoint, called from an admin button (the "press play /
  step one year" control in the sandbox).

---

## The website (Next.js)

Pages the user actually sees on their site:

| Route | What it shows |
|-------|---------------|
| `/` | **The living map of Xos** — continents, borders, cities; current year; play/pause/step; Realtime updates |
| `/chronicle` | The **Chronicle** — annals → events → sagas, filterable by polity, region, era, type |
| `/event/[id]` | A single event with its **causal trail** ("why did this happen?") |
| `/polity/[id]` | A civilization's dashboard: stats over time, territory history, rulers, its sagas |
| `/timeline` | Scrubbable timeline of the whole history; jump to any year |
| `/admin` | (private) seed/reset world, tune knobs (`04` levers), step manually, view `agent_log` |

UI building blocks:
- **Map:** SVG/Canvas of the 7 continents and ~49 regions (geometry digitized from `02`);
  region fill = controlling polity; hover = stats; Realtime re-color on tick.
- **Chronicle reader:** infinite-scroll annals with expand-to-event; sagas as featured
  story cards.
- **Time scrubber:** drag to replay borders/population shifting across centuries (powered
  by `region_control.since_tick` history).

---

## Build milestones (suggested order)

1. **Schema + seed.** Create the Supabase project; migrate the schema above; seed
   geography from `01`/`02` and the tick-0 state from `03`. *(Deliverable: the world
   exists in the DB, frozen at 60 BC.)*
2. **Systems engine (no AI yet).** Implement Phase 1 + 3 + 4 deterministic systems; run
   ticks; confirm history accumulates as annals/events. *(Deliverable: a pure-rules Xos
   that already makes plausible history.)*
3. **Map + Chronicle UI.** Next.js read-only views over the DB; deploy to Vercel.
   *(Deliverable: you can watch Xos on the web.)*
4. **Agents.** Add Phase 2 — Claude leader-agents built from repo personas (`04` table),
   with guardrails and cost controls. *(Deliverable: history gains character.)*
5. **Cron + live.** Vercel Cron advances time on a schedule; Supabase Realtime makes the
   map update live. *(Deliverable: the sandbox runs on its own, forever.)*
6. **Admin + knobs.** Tuning levers, manual step, replay/reset. *(Deliverable: it's a
   sandbox you control.)*

Each milestone is independently demoable, so Xos is "real" after step 3 and only gets
richer.

---

## Operational notes

- **Secrets:** Claude API key, Supabase service key, and a cron auth secret live in Vercel
  env vars — never in the repo.
- **Cost:** the dominant cost is agent LLM calls; the `04` cost-control rules (skip quiet
  years, tier models, batch tribal regions) keep a self-running world affordable.
- **Backups:** the Chronicle is the irreplaceable artifact — schedule Supabase backups;
  consider periodically exporting the chronicle to Markdown/JSON into this repo as a
  durable, versioned record of the history Xos made.
- **Reproducibility:** keep `master_seed` + `agent_log` and any run can be replayed or
  forked into an alternate timeline.

---

## How this ties back to the repo

Xos isn't a random side project bolted onto `blk-agents` — it's a **showcase of the
agency's own agents** doing something nobody scripted: running civilizations across a
thousand years and writing the history themselves. The personas in `strategy/`,
`game-development/`, `marketing/`, and `project-management/` become the Consuls, Khans,
and Emperors of a living world (`04` Phase 2). That's the throughline that makes Xos
belong here.

---

**Back to start:** [`README.md`](./README.md) · **The world:** [`01`](./01-planet.md)
[`02`](./02-continents.md) [`03`](./03-civilizations-60bc.md) · **The engine:**
[`04`](./04-history-engine.md)
