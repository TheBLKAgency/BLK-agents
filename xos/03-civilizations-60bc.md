# 03 · The Starting State — Xos in 60 BC (Tick 0)

This is the **seed**. When the simulation presses play, this is exactly what exists. Every
later year of history grows out of these starting conditions. Numbers are deliberately
round and "Iron Age plausible" — they're the engine's initial values, not census truth.

> **Tech baseline:** the world is broadly **Iron Age / Classical Antiquity.** Iron tools
> and weapons, writing in the advanced cultures, organized armies, sailing ships,
> wheeled transport (except isolated Itzalan), coined or weighed money, early empires
> alongside tribal confederations.

---

## The eight starting powers

Seven continents, but history clusters — eight named polities carry the opening, with
the rest of the map as tribal/uncontrolled regions the sim fills in.

| # | Polity | Continent | Type | Pop. (est.) | Vibe |
|---|--------|-----------|------|-------------|------|
| 1 | **The Aurelian League** | Aurelia | Expanding republic→empire | 6.0 M | Rome at the republic's edge |
| 2 | **Norvanic Tribes** | Aurelia (north) | Tribal confederation | 1.5 M | Gauls/Germans on the frontier |
| 3 | **Kessar Dominion** | Kessara | Old river kingdom | 5.0 M | Egypt-meets-Persia, ancient & wealthy |
| 4 | **Khorr Confederacy** | Kessara (steppe) | Nomad horse-clans | 0.8 M | Steppe raiders, caravan masters |
| 5 | **Zhang Empire** | Zhang-Lu | Centralized bureaucratic empire | **12.0 M** | The Han-analog superpower |
| 6 | **Skelgard Jarldoms** | Voskar | Seafaring raider-traders | 1.2 M | Norse-analog, rising |
| 7 | **Altun Highland States** | Itzalan | Highland city-states | 3.0 M | Andean/Maya-analog, isolated |
| 8 | **Murunga Kingdoms** | Murunga | Fragmented forest kingdoms | 4.0 M | Rich, populous, disunited |

**Unsettled / tribal at start:** most of Thulven, deep Murunga, far Voskar, deep Kessaran
desert, Itzalan lowlands. These regions hold scattered peoples the sim can grow, absorb,
or leave wild.

Approx. **world population at tick 0: ~40–45 million** (Earth ~60 BC was ~200M; Xos
starts lighter on purpose, leaving room to grow over the simulated centuries).

---

## Power profiles

Each polity gets a starting **stat block** the engine reads on tick 0. Stats are 1–10
unless noted.

### 1. The Aurelian League (Aurelia)
- **Government:** Oligarchic republic, expansionist, beginning to strain toward empire.
- **Capital:** Auria (region: Auria).
- **Territory:** Auria, Glasswater, Sundering Coast, Old Aurel (4 regions).
- **Stats:** Military 8 · Economy 7 · Tech 7 · Stability 5 · Legitimacy 6 · Culture 8.
- **Strengths:** Disciplined infantry, roads, law, naval power on the Glass Sea.
- **Tensions:** Republic vs. ambitious generals (built-in civil-war risk), restless
  Norvanic frontier.
- **Leader agent role:** *The Consul* — pragmatic, rhetoric-driven, plays factions.

### 2. Norvanic Tribes (northern Aurelia)
- **Government:** Loose confederation of chieftains.
- **Territory:** Norvane, Veld Marches, Tarn Highlands (3 regions).
- **Stats:** Military 6 · Economy 3 · Tech 4 · Stability 4 · Legitimacy 5 · Culture 5.
- **Strengths:** Fierce warriors, mobility, hard terrain.
- **Tensions:** Disunity; pressure from Aurelian expansion and Voskari raids.
- **Leader agent role:** *The War-Chief* — honor-bound, volatile, alliance-hungry.

### 3. Kessar Dominion (Kessara)
- **Government:** Sacred monarchy, ancient bureaucracy, priesthood-heavy.
- **Capital:** Kessar (Oksus Delta).
- **Territory:** Oksus Delta, Kessar, Sunspire Coast, The Reach of Salt (4 regions).
- **Stats:** Military 6 · Economy 8 · Tech 7 · Stability 6 · Legitimacy 8 · Culture 9.
- **Strengths:** Immense grain wealth, deep traditions, monumental works, sea+caravan trade.
- **Tensions:** Old and rigid; vulnerable to steppe raids and ambitious neighbors.
- **Leader agent role:** *The God-King* — tradition-bound, prestige-obsessed, cautious.

### 4. Khorr Confederacy (Kessaran steppe)
- **Government:** Nomadic clan confederation under a war-khan.
- **Territory:** Khorr Steppe, Caravan Gates (2 regions, mobile).
- **Stats:** Military 7 · Economy 4 · Tech 5 · Stability 3 · Legitimacy 4 · Culture 5.
- **Strengths:** Horse archers, speed, control of caravan routes (toll wealth).
- **Tensions:** Fragile unity; one strong khan from exploding outward, one weak khan from
  collapse.
- **Leader agent role:** *The Khan* — opportunistic, raid-or-trade calculus, charismatic.

### 5. Zhang Empire (Zhang-Lu)
- **Government:** Centralized bureaucratic empire, mandate-of-heaven legitimacy.
- **Capital:** Jin (Jin Valley).
- **Territory:** Jin Valley, Lo Valley, The Terraces, Jade Hills, Eastreach (5 regions).
- **Stats:** Military 7 · Economy 9 · Tech 8 · Stability 7 · Legitimacy 8 · Culture 9.
- **Strengths:** Largest population + economy on Xos, civil service, crossbows, ironworks,
  silk monopoly.
- **Tensions:** Steppe frontier beyond the Tian Wall; dynastic cycle (corruption →
  rebellion built into its long-run behavior).
- **Leader agent role:** *The Emperor* — order-obsessed, bureaucratic, long-horizon.

### 6. Skelgard Jarldoms (Voskar)
- **Government:** Competing jarls; raiding-and-trading economy.
- **Territory:** Skelgard, The Fjordlands, Ambercoast (3 regions).
- **Stats:** Military 6 · Economy 4 · Tech 5 · Stability 4 · Legitimacy 5 · Culture 6.
- **Strengths:** Superb ships, fearless raiders, amber/fur trade, coastal mobility.
- **Tensions:** Cold, poor land at home → pressure to expand by sea (the engine's main
  "raider migration" driver against the wealthy south).
- **Leader agent role:** *The Jarl* — bold, reputation-driven, expansionist.

### 7. Altun Highland States (Itzalan)
- **Government:** Loose league of highland city-states, priest-king led.
- **Capital:** Altun (Altun Plateau).
- **Territory:** Altun Plateau, Q'an Cordillera, Cloudvale (3 regions).
- **Stats:** Military 5 · Economy 6 · Tech 6 · Stability 6 · Legitimacy 7 · Culture 8.
- **Strengths:** Astronomy, monumental architecture, terraced agriculture, road networks,
  isolation (safe from the rest of Xos).
- **Tensions:** No wheel, no large draft animals, no iron-equivalent yet (obsidian/bronze);
  geographically locked away → develops on its own clock.
- **Leader agent role:** *The Priest-King* — ritual-driven, cyclical worldview, insular.
- **Note:** Effectively isolated until ocean-crossing tech (a deliberate "discovery"
  flashpoint many centuries in).

### 8. Murunga Kingdoms (Murunga)
- **Government:** Several independent forest/savanna kingdoms (modeled as one polity with
  low internal cohesion, splittable later).
- **Territory:** Murunga Basin, Tooth Coast, Sava North, Sava South, The Highveld (5 regions).
- **Stats:** Military 5 · Economy 6 · Tech 5 · Stability 4 · Legitimacy 5 · Culture 7.
- **Strengths:** Large population, gold and ivory, fertile land, river trade.
- **Tensions:** Disunity + jungle disease load → expansion is slow and costly; the engine
  models a malaria-analog that historically protected and isolated the interior.
- **Leader agent role:** *The Council of Kings* — rivalrous, trade-savvy, slow to unite.

---

## Starting technologies (shared baseline + spreads)

| Tech | Who has it at tick 0 |
|------|----------------------|
| Iron metallurgy | Aurelia, Kessara, Zhang-Lu, Voskar, Murunga (Itzalan: bronze/obsidian) |
| Writing | Aurelia, Kessara, Zhang-Lu, Altun (others: oral/proto) |
| Coined money | Aurelia, Kessara, Zhang-Lu |
| Cavalry / horse warfare | Khorr, Aurelia, Voskar, Kessara, Zhang-Lu (not Itzalan/Murunga) |
| Ocean-capable ships | Aurelia, Kessara, Skelgard (coastal); deep-ocean = nobody yet |
| The wheel | Everyone except Itzalan |
| Monumental architecture | Kessara, Zhang-Lu, Altun |
| Bureaucratic state | Zhang-Lu, Kessara |

Tech spreads by **trade, conquest, and proximity** as the sim runs (see `04`).

---

## Starting religions (broad strokes)

- **Aurelia:** Civic polytheism — gods of state, hearth, war; temple-and-augury culture.
- **Kessara:** Solar/river god-king cult; powerful priesthood; afterlife-focused.
- **Zhang-Lu:** Ancestor veneration + heaven-mandate philosophy; ritual bureaucracy.
- **Voskar:** Warrior pantheon; sea and storm gods; oath culture.
- **Itzalan:** Astronomical sky-and-sun religion; cyclical time; sacrifice.
- **Murunga:** Ancestral + nature spirits; secret societies; localized.
- **Khorr:** Sky-father + shamanism; mobile, syncretic.

Religions are simulation objects: they can spread, reform, schism, fuse, and birth new
faiths. A future-founded universal/missionary religion is an intended emergent event.

---

## The opening tensions (history's seeds)

The sim doesn't need a script — these built-in pressures generate the first centuries on
their own:

1. **Aurelia vs. Norvanic frontier** — expansion meets resistance (and triggers
   Aurelia's republic-to-empire crisis).
2. **Skelgard sea-pressure** — cold poor north pushes raiders toward rich southern coasts.
3. **Khorr vs. Kessar** — steppe nomads against an old, rich, rigid kingdom.
4. **Zhang dynastic cycle** — the superpower's internal corruption/rebellion clock.
5. **Murunga's slow unification** — a giant trying to wake up against disease and disunity.
6. **Itzalan in isolation** — a high civilization on its own timeline, awaiting contact.
7. **Thulven empty** — a whole continent waiting to be found.

---

**Next:** how all of this turns into a living, recorded history → [`04-history-engine.md`](./04-history-engine.md)
