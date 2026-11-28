# Task Report: Rakha (Labeling and Integration / Dataset Validation)

## Summary
I checked the three raw datasets (D1, D2, D3), verified which one has cheat labels, built a clean version of D1, and wrote automatic quality tests. Result: only D1 has cheat labels, and the three datasets should not be merged.

## What was done
1. Read data/raw/CollectingDataReport.md.
2. Checked D1 (dataset_Cheat_Detection.csv): 3584 rows, 18 columns, no missing values, no duplicate rows. It must be read with sep=";" and decimal=",".
3. Checked D2 (PUBG_Player_Statistics.csv, 152 columns) and D3 (train_V2.csv, 29 columns). Only the first 1000 rows were read, so their row counts are not verified.
4. Checked the labels in D1: es_trampa_max equals "any of the 4 specific labels" in all rows.
5. Checked the Mendeley description of D1.
6. Wrote docs/labeling_policy.md and docs/data_dictionary.md.
7. Wrote src/data/integrate.py. It reads D1, converts timestamp to datetime, makes labels integers, adds source_id, checks that features are between 0 and 1, and saves data/interim/d1_labeled.csv (3584 rows, 19 columns).
8. Wrote tests/test_data_quality.py (6 tests, all pass).

## Findings
- Only D1 has cheat labels. D2 and D3 have none. D3's winPlacePerc is finish placement, not cheating.
- D1 label counts: es_trampa_max 1733 cheat vs 1851 legit (about 48% / 52%). Specific labels: aimbot 1415, infinite health 1234, infinite ammo 869, speed hack 553. Their sum is above 1733, so several cheats can be active in the same window.
- All numeric features in D1 are min-max normalized to [0, 1]. Raw units are unknown, so columns cannot be compared with each other or with real PUBG numbers.
- timestamp is stored as text. It covers 2026-01-16 to 2026-03-31 but only 7 distinct days.
- D1, D2 and D3 have different row meanings (2-second window, player lifetime, player in one match) and no shared ID. They are not merged.

## Decisions made in my part
- The 5 label columns are never used as features (label leakage).
- No merge between D1, D2 and D3.
- Raw files in data/raw are not modified.

## Open issues for the team and the TA
1. How D1 labels were created is not stated by the source.
2. The source does not name the game, so D1 is not proven to be PUBG data.
3. The classes are very balanced (about 52/48). It is unclear if this is natural or intended.
4. Rows come from only 7 days, so rows from the same day may be similar. A random train/test split could leak information. Splitting by day should be considered (not verified).
5. Final target column (es_trampa_max or the 4 specific labels) needs a team decision.
6. Team decision needed: use D1 only, or a PUBG-only approach with a different label strategy.
7. Spec conflict: the table puts me on feature/data-cleaning, the branching section says member-rakha. Coordinator should confirm.
8. data/ is git-ignored, so how the data files are shared with the team needs to be agreed.

## Files
- docs/labeling_policy.md
- docs/data_dictionary.md
- src/data/integrate.py
- tests/test_data_quality.py
- data/interim/d1_labeled.csv (generated, not committed)

## How to reproduce
- python src/data/integrate.py
- python -m pytest tests/ -q