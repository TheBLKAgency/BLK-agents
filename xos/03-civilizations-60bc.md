# 03 · The Starting State — Xos in 60 BC (Tick 0)

This is the **seed**. When the simulation presses play, this is exactly what exists. Every
later year of history grows out of these starting conditions. Numbers are deliberately
round and "Iron Age plausible" — they're the engine's initial values, not census truth.

> **Tech baseline:** the world is broadly **Iron Age / Classical Antiquity.** Iron tools
> and weapons, writing in the advanced cultures, organized armies, sailing ships,
> wheeled transport (except isolated Itzalan), coined or weighed money, early empires
> alongside tribal confederations.

---

## The twenty starting powers

Seven continents, twenty named polities. History still clusters around a handful of
**Major** powers, but each continent now carries rivals, frontier states, and a wildcard,
so the opening map is alive rather than empty. Every polity is driven by a real persona
from this repo — the bindings live in [`06-agent-mapping.md`](./06-agent-mapping.md).

| # | Polity | Continent | Type | Pop. | Tier | Vibe |
|---|--------|-----------|------|------|------|------|
| 1 | **Aurelian League** | Aurelia | Republic→empire | 6.0 M | Major | Rome at the republic's edge |
| 2 | **Norvanic Tribes** | Aurelia | Tribal confederation | 1.5 M | Major | Gauls/Germans on the frontier |
| 3 | **Sundering Cities** | Aurelia | Maritime merchant republic | 1.0 M | Minor | Venice/Carthage of the Glass Sea |
| 4 | **Kessar Dominion** | Kessara | Sacred river kingdom | 5.0 M | Major | Egypt-meets-Persia, ancient |
| 5 | **Khorr Confederacy** | Kessara | Nomad horse-clans | 0.8 M | Major | Steppe raiders, caravan masters |
| 6 | **Sunspire Emirate** | Kessara | Coastal trade port | 0.7 M | Minor | Wealthy neutral middleman |
| 7 | **Basin Kingdoms** | Murunga | Forest river kingdom | 2.2 M | Major | Benin-analog, bronze & griots |
| 8 | **Sava Cattle-Lords** | Murunga | Savanna herders | 1.0 M | Minor | Cattle-wealth expansionists |
| 9 | **Tooth Coast League** | Murunga | Coastal trade cities | 0.8 M | Minor | Swahili-coast middlemen |
| 10 | **Skelgard Jarldoms** | Voskar | Seafaring raiders | 1.2 M | Major | Norse-analog, rising |
| 11 | **Wolfsteppe Riders** | Voskar | Cold-steppe cavalry | 0.6 M | Minor | Fast reactive horse-clans |
| 12 | **Deep-Taiga Clans** | Voskar | Forest animists | 0.5 M | Minor | Shamanic fur peoples |
| 13 | **Zhang Empire** | Zhang-Lu | Bureaucratic empire | **12.0 M** | Major | Han-analog superpower |
| 14 | **Southmonsoon States** | Zhang-Lu | River delta city-states | 3.0 M | Minor | Pragmatic southern rivals |
| 15 | **Tian Wall March** | Zhang-Lu | Militarized frontier state | 1.2 M | Minor | The watch on the steppe |
| 16 | **Altun Highland States** | Itzalan | Astronomer priest-kings | 3.0 M | Major | Andean/Maya, isolated |
| 17 | **Q'an Sun-Houses** | Itzalan | Feuding highland dynasties | 1.4 M | Minor | Lineage-obsessed rivals |
| 18 | **Ballcourt Cities** | Itzalan | Lowland ritual-game culture | 1.2 M | Minor | Conflict ritualized as sport |
| 19 | **Vorthshore Whalers** | Thulven | Sub-antarctic survivalists | 0.2 M | Minor | The only settled Thulven folk |
| 20 | **The Tide-Lords** | Sunder isles | Stateless pirate-traders | 0.3 M | Wildcard | Homeless sea-network |

**Unsettled / tribal at start:** most of Thulven, the Deep Green of Murunga, Frostmarch
and far Voskar, Deep Khorr desert, and Itzalan's Far Terraces. These regions hold
scattered peoples the sim can grow, absorb, or leave wild.

**Tiers** (from `06`) govern simulation cost: *Major* powers take a full AI turn every
year; *Minor* powers act on rules until a real pressure forces a decision; the *Wildcard*
acts only when it has prey. This is how twenty agents stay affordable.

Approx. **world population at tick 0: ~45–50 million** (Earth ~60 BC was ~200M; Xos
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

### 8. Basin Kingdoms (Murunga)
- **Government:** Forest river kingdom — a powerful court culture of art, regalia, and oral
  memory (the largest of Murunga's several kingdoms).
- **Capital:** Oba's seat (Murunga Basin).
- **Territory:** Murunga Basin, Deep Green fringe (2 regions).
- **Stats:** Military 5 · Economy 6 · Tech 5 · Stability 5 · Legitimacy 7 · Culture 9.
- **Strengths:** Large population, gold and ivory, bronze artistry, river trade, prestige.
- **Tensions:** Jungle disease load (malaria-analog) makes expansion slow and costly;
  rivalry with the Sava savanna kingdoms and Tooth Coast ports.
- **Leader agent role:** *The Oba* — prestige-driven, art-and-memory court, slow to war.

---

## The twelve further powers (Minor & Wildcard)

The remaining polities get the same stat blocks but run on the cheaper *Minor/Wildcard*
turn budget (`06` tiers). Stats: Mil · Eco · Tech · Stab · Leg · Culture.

| Polity (continent) | Stats | Territory | Defining tension / role |
|--------------------|-------|-----------|--------------------------|
| **Sundering Cities** (Aurelia) | 4·7·6·5·5·7 | Sundering Coast, Glasswater | Rich merchant republic squeezed between Aurelia and the sea; survives by deals, not armies |
| **Sunspire Emirate** (Kessara) | 4·7·6·6·6·7 | Sunspire Coast | Neutral trade port that plays every neighbor; first to feel any war over the Glass Sea |
| **Sava Cattle-Lords** (Murunga) | 5·5·4·4·5·6 | Sava North, Sava South, The Highveld | Herd-wealth expansionists; raid the Basin, pressured by drought |
| **Tooth Coast League** (Murunga) | 4·6·5·5·5·6 | Tooth Coast, Mangrove Marches | Coastal middlemen linking interior gold to the sea; vulnerable to raiders |
| **Wolfsteppe Riders** (Voskar) | 6·4·5·3·4·5 | Wolfsteppe | Fast reactive cavalry; strike settled lands at any sign of weakness |
| **Deep-Taiga Clans** (Voskar) | 4·3·4·4·5·6 | Deep Taiga, Frostmarch | Animist fur-clans; survive by reading omens and syncretizing neighbors |
| **Southmonsoon States** (Zhang-Lu) | 5·7·7·5·5·7 | Southmonsoon, Greater Zhang | Pragmatic delta city-states resisting Zhang centralization |
| **Tian Wall March** (Zhang-Lu) | 7·5·7·6·6·5 | Tian Wall | Militarized frontier whose whole identity is holding the steppe back |
| **Q'an Sun-Houses** (Itzalan) | 5·5·6·4·6·8 | Q'an Cordillera, Obsidian Valleys | Feuding dynasties obsessed with bloodline legitimacy |
| **Ballcourt Cities** (Itzalan) | 4·5·5·5·6·8 | Lowland Itzal, Cloudvale | Channel conflict into sacred games; rising lowland power |
| **Vorthshore Whalers** (Thulven) | 4·3·4·6·5·6 | Vorthshore, Glacier Coast | The only settled people of an empty continent; masters of scarcity |
| **The Tide-Lords** (Sunder isles) | 6·5·5·3·3·5 | Sunder island bases (no mainland) | Stateless pirate-trader network; the map's wildcard raider |

> **Why split Murunga and add rivals everywhere?** A single continent-spanning blob makes
> dull history. Splitting it into the **Basin / Sava / Tooth Coast** rivalry — and seeding
> every continent with a frontier state and a wildcard — means conflict and alliance can
> ignite *within* a continent, not just between them. More edges = more history.

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
