## Dataset checked
- File: data/raw/dataset_Cheat_Detection.csv (D1, Mendeley time-window dataset)
- Shape: 3584 rows, 18 columns
- Read with sep=";" and decimal=","

## Label columns
- es_trampa_max: general cheat indicator (1 = cheat)
- isAimbot_max, isVidaInfinita_max, isMunicionInfinita_max, isSuperVelocidad_max: specific cheat types

## Findings
- Class balance: 1851 legit (0) vs 1733 cheat (1), about 52% / 48%. This is unusually balanced for real gameplay.
- Missing values: 0 in all columns.
- Duplicate rows: 0.
- Consistency: es_trampa_max equals "any of the 4 specific labels" in all 3584 rows (no conflicts).
- No player or session ID column, only timestamp.

## Rules
- All 5 label columns must NOT be used as model features (label leakage).
- Target column: es_trampa_max (pending team decision).
- D1 cannot be joined with D2 or D3 (no shared identifier, different unit of observation).

## Open questions (not verified yet)
- How the labels were created and by whom (to check on the Mendeley page).
- Whether the data comes from PUBG or another game (the report says it is not established).
- Why the classes are so balanced.

# NNEEEWWWWWW 



## Source check (Mendeley description)
- Each row is a 2-second sliding window. Features are mean, max, min and sum of raw events. Values are normalized.
- Label meaning: es_trampa_max = 1 means a cheat was active in the window. The 4 specific labels mark aimbot, infinite health, infinite ammo and speed hack.
- Not stated by the source: the game name, how cheating was labeled, the number of players or sessions, and whether the data is real or synthetic.

## Risks to report to the team
- infinite_ammo_ratio and ammo_max may be strongly related to isMunicionInfinita_max. Check the correlation before using them as features.
- Timestamps cover 2026-01-16 to 2026-03-31 but only 7 distinct days (3583 unique timestamps for 3584 rows). Rows from the same day probably come from the same session or player, so they may be very similar. A random train/test split could leak information. Splitting by day should be considered (inference, not verified).
- timestamp is stored as text (UTC datetime), not as a number.