# 01 · The Planet Xos — Geophysical Specification

Xos is built to be **Earth's twin in physics, its stranger in geography.** A human
dropped onto Xos would find the air breathable, the gravity barely heavier, the seasons
familiar, the night sky almost right — and not a single coastline they recognize.

These values are **fixed**. The simulation never changes them; it only plays out on top
of them.

---

## 1. Vital statistics

| Property | Xos | Earth | Note |
|----------|-----|-------|------|
| Mean radius | 6,580 km | 6,371 km | ~3% larger |
| Mass | 1.10 M⊕ | 1.0 M⊕ | denser-ish core |
| Surface gravity | 1.05 g | 1.0 g | barely noticeable; you'd feel slightly heavier |
| Surface area | 543 M km² | 510 M km² | |
| Water coverage | **71%** | 71% | deliberately Earth-like |
| Land coverage | 29% (≈157 M km²) | 29% | spread across 7 continents |
| Atmosphere | 77% N₂ / 21% O₂ / 1% Ar / 1% other | 78/21/1 | breathable, near-identical |
| Mean surface temp | 15.2 °C | 14 °C | a touch warmer; smaller ice caps |
| Magnetic field | Yes, dipole | Yes | shields surface, enables compasses |

**Design intent:** every difference is small enough to keep Earth's biology, weather,
and human-scale technology plausible, but the world is its own.

---

## 2. Orbit, time, and the calendar

Xos's calendar is intentionally **cleaner than Earth's** so the simulation's clock is
tidy.

| Property | Value |
|----------|-------|
| Day length | **26 hours** (slightly slower spin) |
| Year length | **364 days** |
| Axial tilt | **24.1°** (seasons slightly more pronounced than Earth's 23.4°) |
| Orbital shape | Low eccentricity (0.012) — mild, stable seasons |
| Star | **Sol-Xos**, a G-type yellow main-sequence star, ~Sun-like |

### The Xos calendar

- **13 months × 28 days = 364 days.** Every month is exactly four 7-day weeks.
- Months (working names): *Brume, Thaw, Seedfall, Bloom, Highsun, Goldwane, Harvest,
  Emberfall, Mistdusk, Frostgate, Longnight, Deepwinter, Yearturn.*
- One intercalary day — **"the Still Day"** — sits outside all months at the new year to
  keep the calendar aligned with the seasons. Cultures treat it as a day of rest, omen,
  or festival.

> **In the engine, 1 tick = 1 Xos year.** Months and days exist for flavor and dating
> events ("on the 3rd of Harvest"), not for stepping the simulation.

### Era system

- The sandbox starts at **60 BC** on a human-relatable timeline.
- Internally we also count **Anno Xos (AX)**: the start year is `0 AX`. So `60 BC = 0 AX`,
  `59 BC = 1 AX`, and the year `1 AD = 60 AX`. Use whichever reads better in the UI;
  store `tick_index` (an integer starting at 0) as the canonical truth.

---

## 3. Moons and tides

Xos has **two moons**, which gives it a tidal signature no Earth observer would expect.

| Moon | Size | Orbit | Effect |
|------|------|-------|--------|
| **Maren** | ~Luna-sized (large) | 27.8-day period | Dominant tides; lights the night; drives lunar calendars and myth |
| **Vex** | Small (captured asteroid, ~Phobos-class) | 4.1-day period, low orbit | Fast-moving "wandering star"; faint extra tide; omens and superstition |

When Maren and Vex align, Xos gets unusually strong **"twin tides"** roughly every few
months — a natural calendar event coastal cultures plan around (and mystics fear).

---

## 4. Oceans

Five named oceans wrap the seven continents. (Their boundaries and the continents that
border them are detailed in `02-continents.md`.)

| Ocean | Character |
|-------|-----------|
| **The Pelagine** | The largest ocean; vast, deep, separates the western and eastern hemispheres |
| **Sregister Sea / The Auran Ocean** | Temperate northern ocean ringed by the oldest civilizations |
| **The Vorth Deep** | Cold southern polar ocean; storms, whaling, hard sailing |
| **The Sunder** | Warm equatorial ocean dense with islands and trade routes |
| **The Glass Sea** | A nearly enclosed, calm inland-ish ocean; cradle of early sea trade |

Major currents form a two-gyre system per hemisphere (like Earth's), driving climate:
warm water poleward on western continental coasts, cold upwelling on eastern coasts.

---

## 5. Climate model (design-level)

Xos uses Earth's climate machinery, so worldbuilders and the sim can reason about it
with real intuition. Latitude bands:

| Band | Latitude | Climate | Analog |
|------|----------|---------|--------|
| Polar | 70–90° | Ice caps, tundra | Arctic/Antarctic |
| Boreal | 55–70° | Taiga, cold forest | Scandinavia/Canada |
| Temperate | 35–55° | Deciduous forest, grassland, 4 seasons | Europe/N. China |
| Subtropical | 23–35° | Mediterranean coasts, deserts on west interiors | Med, Sahara fringe |
| Tropical | 0–23° | Rainforest, savanna, monsoon | Amazon/Congo/SE Asia |

Modifiers the sim respects:
- **Rain shadows** behind major mountain ranges → deserts and steppe.
- **Monsoons** on tropical coasts with large continental interiors.
- **Maritime vs continental**: coasts mild, interiors extreme.
- Slightly warmer baseline than Earth → **smaller ice caps, higher tree line, more
  habitable high-latitude land.** This subtly favors northern civilizations.

### Climate as a simulation input
The history engine reads climate per region to set:
- **Carrying capacity** (how many people a region feeds),
- **Crop suitability** (what can be farmed → economy),
- **Disaster odds** (drought, flood, freeze → events).

See `04-history-engine.md` §"Climate & Agriculture system."

---

## 6. What stays fixed vs. what evolves

| Fixed forever (this doc) | Evolves each tick (the sim) |
|--------------------------|------------------------------|
| Size, gravity, orbit, tilt | Borders, populations |
| Calendar, moons, tides | Technologies, religions |
| Ocean basins, mountain ranges, coastlines | Cities, trade routes, wars |
| Climate _bands_ and currents | Local climate _events_ (droughts, plagues) |
| Continents' positions | Who rules each region |

This boundary is the contract that keeps a thousand simulated years internally
consistent.

---

**Next:** the land itself → [`02-continents.md`](./02-continents.md)
