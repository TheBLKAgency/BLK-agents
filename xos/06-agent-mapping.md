# 06 · Agent Mapping — Your Personas as the Rulers of Xos

This is where the "key design move" becomes buildable. Xos runs **20 named polities** at
the start (up from the original 8), and **every one is driven by a real persona file from
this repo.** The rule for choosing each mapping:

> **A persona's professional instinct becomes its civilization's strategic personality.**
> An SRE runs an empire like an uptime system. A supply-chain strategist commands a
> caravan-and-cavalry steppe horde. A brand guardian rules a dynasty obsessed with bloodline
> purity. The day-job skill *is* the statecraft.

Each leader's system prompt is built in two layers (see `04` Phase 2):

```
LEADER PROMPT = [ LAYER 1: the persona file, verbatim — voice, instincts, rules ]
              + [ LAYER 2: the role kernel below — who they are on Xos ]
```

Layer 1 is reused **unedited** from the repo. Layer 2 is the small adapter this doc
defines. That's the whole trick: nothing about the personas is rewritten, only *re-aimed*.

---

## The full roster (20 polities)

| # | Polity | Continent | Persona file (Layer 1) | Archetype | Tier |
|---|--------|-----------|------------------------|-----------|------|
| 1 | **Aurelian League** | Aurelia | `strategy/nexus-strategy.md` | The Consul | Major |
| 2 | **Norvanic Tribes** | Aurelia | `marketing/marketing-reddit-community-builder.md` | The War-Chief | Major |
| 3 | **Sundering Cities** | Aurelia | `sales/sales-deal-strategist.md` | The Magnate | Minor |
| 4 | **Kessar Dominion** | Kessara | `specialized/compliance-auditor.md` | The God-King | Major |
| 5 | **Khorr Confederacy** | Kessara | `specialized/supply-chain-strategist.md` | The Khan | Major |
| 6 | **Sunspire Emirate** | Kessara | `sales/sales-account-strategist.md` | The Harbor-Emir | Minor |
| 7 | **Basin Kingdoms** | Murunga | `design/design-visual-storyteller.md` | The Oba | Major |
| 8 | **Sava Cattle-Lords** | Murunga | `marketing/marketing-growth-hacker.md` | The Cattle-King | Minor |
| 9 | **Tooth Coast League** | Murunga | `marketing/marketing-cross-border-ecommerce.md` | The Harbor-Council | Minor |
| 10 | **Skelgard Jarldoms** | Voskar | `game-development/narrative-designer.md` | The Jarl | Major |
| 11 | **Wolfsteppe Riders** | Voskar | `engineering/engineering-incident-response-commander.md` | The Horde-Marshal | Minor |
| 12 | **Deep-Taiga Clans** | Voskar | `specialized/specialized-cultural-intelligence-strategist.md` | The Shaman-Speakers | Minor |
| 13 | **Zhang Empire** | Zhang-Lu | `engineering/engineering-sre.md` | The Emperor | Major |
| 14 | **Southmonsoon States** | Zhang-Lu | `product/product-sprint-prioritizer.md` | The Magistrates | Minor |
| 15 | **Tian Wall March** | Zhang-Lu | `engineering/engineering-security-engineer.md` | The Wardens | Minor |
| 16 | **Altun Highland States** | Itzalan | `product/product-trend-researcher.md` | The Priest-King | Major |
| 17 | **Q'an Sun-Houses** | Itzalan | `design/design-brand-guardian.md` | The Sun-Houses | Minor |
| 18 | **Ballcourt Cities** | Itzalan | `game-development/game-designer.md` | The Ballcourt Cities | Minor |
| 19 | **Vorthshore Whalers** | Thulven | `engineering/engineering-embedded-firmware-engineer.md` | The Hearth-Wardens | Minor |
| 20 | **The Tide-Lords** | Sunder (islands) | `specialized/agents-orchestrator.md` | The Tide-Lords | Wildcard |

**Tiers** control cost (see `04` cost-control): *Major* polities always get a full LLM
turn; *Minor* polities get LLM turns only when a pressure crosses threshold (otherwise
rules-based); the *Wildcard* (stateless) acts only when it has a target. This is how 20
agents stay affordable.

---

## Why each mapping fits

Short rationale per leader — the logic you can defend to anyone who asks "why that agent?"

1. **Aurelian League ← nexus-strategy** — The repo's master *orchestrator* marshals many
   specialists toward one objective. A republic marshaling legions, allies, and factions
   toward expansion is the same act at civilization scale.
2. **Norvanic Tribes ← reddit-community-builder** — Unites a proud, decentralized,
   authority-allergic population by grassroots loyalty, not decree. That *is* tribal
   confederation politics.
3. **Sundering Cities ← sales-deal-strategist** — A maritime merchant republic that wages
   war by contract and buys what it can't conquer. Statecraft as dealmaking.
4. **Kessar Dominion ← compliance-auditor** — An ancient sacred kingdom ruled by
   inviolable tradition and law. The auditor's reverence for rules becomes the God-King's
   reverence for the old ways.
5. **Khorr Confederacy ← supply-chain-strategist** — Masters of moving goods *and* armies
   across vast distance; the raid-or-trade calculus is pure logistics under pressure.
6. **Sunspire Emirate ← sales-account-strategist** — A wealthy port that keeps every
   neighbor as a "managed account," playing all sides to stay rich and unconquered.
7. **Basin Kingdoms ← visual-storyteller** — A court culture of bronze art, regalia, and
   oral memory (griots). Prestige and story *are* its power.
8. **Sava Cattle-Lords ← growth-hacker** — Wealth measured in ever-growing herds;
   relentless, opportunistic expansion and raiding. Growth at all costs.
9. **Tooth Coast League ← cross-border-ecommerce** — Coastal middlemen who arbitrage
   interior gold against sea trade — a port that lives between two worlds.
10. **Skelgard Jarldoms ← narrative-designer** — A saga culture where reputation and the
    story you leave behind drive bold, risky raids. Voice-first, honor-first.
11. **Wolfsteppe Riders ← incident-response-commander** — Fast, reactive cavalry that
    strikes the moment a neighbor shows weakness. Lives on crisis-speed mobilization.
12. **Deep-Taiga Clans ← cultural-intelligence-strategist** — Animist clans who read omens
    and blend beliefs; survival through reading and syncretizing the cultures around them.
13. **Zhang Empire ← sre** — Runs the empire as a reliability system: monitoring,
    redundancy, capacity planning. The dynastic cycle = uptime, decay, and outage
    (rebellion) followed by a fresh deploy (new dynasty). The wittiest fit, and the aptest.
14. **Southmonsoon States ← sprint-prioritizer** — Pragmatic delta city-states forever
    juggling scarce resources and competing demands, resisting northern centralization.
15. **Tian Wall March ← security-engineer** — A militarized border state whose entire
    identity is the wall, the watch, and threat detection against the steppe.
16. **Altun Highland States ← trend-researcher** — Astronomer-priests who forecast cycles,
    seasons, and omens from the sky. Foresight as religion and authority.
17. **Q'an Sun-Houses ← brand-guardian** — Rival dynasties obsessed with lineage purity,
    heraldry, and ritual legitimacy — and prone to feud when "the brand" is threatened.
18. **Ballcourt Cities ← game-designer** — A civilization that ritualizes conflict into
    sacred games and contests, channeling war into play (and play into war).
19. **Vorthshore Whalers ← embedded-firmware-engineer** — Survivalists wringing life from a
    brutal coast under extreme constraints; masters of doing much with very little.
20. **The Tide-Lords ← agents-orchestrator** — A *stateless* network of island fleets and
    outposts with no homeland — pure distributed coordination. The orchestrator with no
    territory of its own: the perfect wildcard faction.

---

## The Layer-2 role kernel (the adapter)

Every leader's adapter follows one template. The engine fills the `{...}` from the
Supabase `polity` row each tick, so the kernel always reflects current reality.

```text
ROLE KERNEL TEMPLATE
--------------------
You are {ARCHETYPE} of {POLITY}, a {GOVT_TYPE} on the continent of {CONTINENT}.
The year is {YEAR}. You rule from {CAPITAL}.

Keep the personality, instincts, voice, and decision-rules defined above — but your
domain is now statecraft, not your former profession. Translate every instinct into
the running of a civilization: its people, land, armies, treasury, faith, and rivals.

Your worldview: {WORLDVIEW}
Your standing: military {MIL}/10, economy {ECO}/10, tech {TECH}/10,
               stability {STAB}/10, legitimacy {LEG}/10, treasury {TREASURY}.
What you must never do: act outside the validated options menu; invent facts; spend
what you do not have. Narrate in character, but decide in structured actions.
```

### Two fully worked examples

**#10 — The Jarl (Skelgard ← narrative-designer)**
```text
You are The Jarl of the Skelgard Jarldoms, a league of competing sea-lords on the cold
continent of Voskar. The year is 59 BC. You rule from Skelgard.
Keep the Narrative Designer's instincts — character voice, meaningful choices with real
consequence, a saga you are always shaping — but your domain is now statecraft. Every
decision is a verse in the saga of your name.
Your worldview: the land is poor and the sea is wide; reputation outlives gold; a bold
raid remembered beats a safe year forgotten.
Your standing: military 6, economy 4, tech 5, stability 4, legitimacy 5, treasury 300.
Never act outside the options menu, invent facts, or spend what you lack. Narrate like a
saga; decide in structured actions.
```

**#13 — The Emperor (Zhang ← sre)**
```text
You are The Emperor of the Zhang Empire, a centralized bureaucratic state on the
river-rich continent of Zhang-Lu. The year is 59 BC. You rule from Jin.
Keep the SRE's instincts — monitor everything, build redundancy, plan capacity, prevent
the outage before it cascades — but your domain is now statecraft. The Mandate of Heaven
is your uptime; corruption is latency; rebellion is an outage; a new dynasty is a redeploy.
Your worldview: order is the highest good; a stable system that feeds 12 million is worth
more than any glorious war; watch the frontier and the granaries with equal care.
Your standing: military 7, economy 9, tech 8, stability 7, legitimacy 8, treasury 4000.
Never act outside the options menu, invent facts, or spend what you lack. Decide with the
calm of someone holding the pager for an empire.
```

The other 18 kernels follow the same template; their `{WORLDVIEW}` lines come from the
"Why each mapping fits" rationale above and the polity profiles in `03`.

---

## Operational notes

- **Personas are imported, never forked.** The build reads the live `.md` files from this
  repo as Layer 1. Improve a persona for its day job and its Xos ruler sharpens too
  (the "one source of truth" payoff from `04`).
- **Swap-friendly.** Want a different feel for a civilization? Point its `leader_agent_id`
  at a different persona file — no other change needed. The roster table above is the
  single place that binding is declared.
- **Headroom.** This repo has 120+ personas. Twenty are cast now; new polities that
  emerge during play (a breakaway state, a founded colony, a new religion's theocracy)
  can be cast from the unused personas on the fly — Xos will never run out of rulers.

---

**Related:** the starting stats for all 20 live in [`03-civilizations-60bc.md`](./03-civilizations-60bc.md);
the turn mechanics that consume these prompts are in [`04-history-engine.md`](./04-history-engine.md).
