# Data dictionary

All inputs and training records are synthetic. Fields are numeric; counts and cents must be integers.

- `enrollment_per_week` — Expected enrollment / week; valid range 1–150; real number.
- `kits_per_participant` — Kits per participant; valid range 1–12; integer.
- `on_hand_kits` — Available kits; valid range 0–10000; integer.
- `lead_time_days` — Replenishment lead time (days); valid range 1–60; integer.
- `expiry_days` — Days until kit expiry; valid range 1–365; integer.

`target`: weekly_kit_demand in kits per week.

Poisson enrollment times kits per participant, plus small Gaussian noise, generates weekly demand. Only enrollment and kits enter the ML model; inventory policy is calculated separately.
