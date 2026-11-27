Raw Dataset Collection Report
Project: PUBG Cheater Detection — Machine Learning
Stage: Data Collection
Prepared by: Mohtady
Last updated: 2026-11-25
Directory: data/raw/
1. Purpose and scope
This directory contains (or will contain, once downloaded) the original, unmodified datasets selected as potential inputs for the PUBG Cheater Detection project. The aim of this stage is to locate useful sources, preserve their raw files, and document what they contain and what they cannot establish.

This report is based on the linked dataset descriptions and repository documentation. The exact downloaded files, schemas, row counts, checksums, and label quality have not yet been audited locally. No cleaning, feature engineering, relabeling, or merging is performed at the collection stage.
2. Dataset inventory
ID	Source	Data type	Approximate size	Confirmed cheating ground truth?	Intended use
D1	Mendeley — Time-Window Normalized Dataset for Video Game Cheat Detection using Neural Networks	Short-window gameplay telemetry and cheat indicators	3,584 instances (source description)	Cheat-status labels provided; labeling methodology still requires validation	Primary candidate for supervised cheat classification
D2	GitHub — JunjieCheng/PUBG-hack-detection	PUBG player-level aggregate statistics	Repository describes ~85,000 records in an upstream Kaggle source; exact file size to verify	No verified cheater/legit ground truth in the documented approach	PUBG-specific statistics, EDA and potential features
D3	Kaggle — PUBG Finish Placement Prediction	PUBG player-match, post-game statistics	~4.45 million training rows, 29 columns in the commonly used train_V2.csv version (reported by public analyses; verify download)	No	PUBG-specific behavioral statistics and optional anomaly analysis


3. Source details
D1 — Video Game Cheat Detection Dataset (Mendeley)
- Source: Mendeley Data
- Official title: Time-Window Normalized Dataset for Video Game Cheat Detection using Neural Networks
- URL: https://data.mendeley.com/datasets/bx3y8ktrsf/1
- Published: 14 July 2026 (Version 1)
- DOI: 10.17632/bx3y8ktrsf.1
- License listed by source: CC BY 4.0
- Size reported by source: 3,584 instances
- Granularity: Gameplay telemetry aggregated into two-second sliding windows
Example input metrics: angle_error_mean, angle_error_max, speed_mean, speed_max, is_shot_sum, is_hit_sum, is_received_damage_sum, health_mean, ammo_left_min, ammo_max, accuracy_rate, and infinite_ammo_ratio.

Label columns documented by the source:
- es_trampa_max — general binary cheat-active indicator.
- isAimbot_max — aimbot indicator.
- isVidaInfinita_max — infinite-health / god-mode indicator.
- isMunicionInfinita_max — infinite-ammunition indicator.
- isSuperVelocidad_max — speed-hack indicator.
Important limitations:
- The source does not establish that these are PUBG gameplay records.
- The original telemetry collection and labeling methodology should be checked before choosing it as the final supervised-learning dataset.
- Cheat-status columns must not accidentally be used as model input features when predicting cheating. Potential label leakage through derived fields should also be reviewed later.
- The downloaded file appears to use semicolon-separated columns and comma decimal notation in the sample inspected visually; confirm the format from the raw file, rather than modifying it during collection.
D2 — PUBG Player Statistics (GitHub)
- Source: JunjieCheng/PUBG-hack-detection
- Repository: https://github.com/JunjieCheng/PUBG-hack-detection
- Referenced upstream Kaggle dataset: https://www.kaggle.com/lazyjustin/pubgplayerstats
- Repository file to inspect: PUBG_Player_Statistics.csv (plus regional source spreadsheets, if included)
- Size: The repository README references approximately 85,000 records from its original Kaggle source, as well as 500 highly ranked players from five servers. Do not assume that every local file has exactly that row count.
Description: A PUBG-specific player-statistics source. The reference project discusses win ratio, kill/death ratio, headshot ratio, and top-10 placement ratio, and uses K-Means clustering to group player behavior.

Important limitations:
- The project's proposed clusters (e.g., aimbot or waller) are algorithmic interpretations, not independently verified cheating labels.
- High performance or statistical outliers do not prove a player cheated.
- Confirm the raw file schema, number of observations, duplicates, and any license/reuse conditions before downstream use.
D3 — PUBG Finish Placement Prediction (Kaggle)
- Source: Kaggle competition
- URL: https://www.kaggle.com/competitions/pubg-finish-placement-prediction/data
- Common training filename: train_V2.csv (verify after download)
- Approximate training size: 4,446,966 rows and 29 columns, as reported in public analyses of this competition dataset
- Original task: Predict a player's final placement in a match, not cheat detection
Examples of available statistics: kills, headshotKills, damageDealt, longestKill, walkDistance, weaponsAcquired, matchId, groupId, and matchType.

Original competition target: winPlacePerc, a normalized match finishing-placement measure. This is not a cheating label.

Important limitations:
- No verified cheater-versus-legitimate target is provided for the intended supervised task.
- A suspicious value such as an unusually high kill count should not be converted into a "cheater" label without external evidence.
- Review Kaggle's applicable competition/data terms before redistribution or committing downloaded raw files to a public repository.
4. Dataset compatibility and risks
These are different datasets with different units of observation:
- D1: short temporal windows from a general video-game cheat-detection setting.
- D2: aggregated PUBG player statistics.
- D3: PUBG player-match post-game records.
They must not be concatenated or joined solely because they share concepts such as kills, accuracy, or speed. There is no confirmed shared player/session identifier linking D1, D2, and D3. Keeping them separate is the default until the team establishes a scientifically justified integration method.

Primary selection decision still open: whether the project will use D1 for supervised general game cheat detection, or instead prioritize PUBG-only records with a different detection strategy or newly verified labels.
5. Suggested raw folder structure
data/
└── raw/
    ├── README.md
    ├── mendeley_cheat_detection/
    │   └── <original downloaded file(s)>
    ├── pubg_player_statistics/
    │   └── <original downloaded file(s)>
    └── pubg_finish_placement/
        └── <original downloaded file(s)>
Place downloads under the relevant source folder without editing their contents or filenames. Preserve original archives if possible. Record exact downloaded filenames, source version, file sizes, and retrieval dates once the files are available.
6. Handoff and next steps
Mohtady — Data Collection:
- Identify sources and download the original datasets.
- Keep source files unchanged and document source URLs, rough contents, and label availability.
- Hand over the raw files and this report to the team.
Rakha — Labeling and Integration / Dataset Validation:
- Verify label provenance and whether a defensible cheating target exists.
- Review compatibility and document whether any integration is justified.
- Report data suitability concerns before training.
Mohtady + Yahia — Later Preprocessing and Feature Engineering:
- Start only after the data sources and label strategy have been agreed upon.
- Perform cleaning, preprocessing, and feature engineering in separate stages, not inside data/raw/.
7. Collection verification checklist
- [ ] Download D1 and record exact filename, size, row count, and column count.
- [ ] Download D2 and verify the CSV's actual number of records.
- [ ] Download D3 and verify Kaggle filenames, size, and terms.
- [ ] Confirm D1 delimiter/decimal conventions from its raw file.
- [ ] Record retrieval dates and whether source licenses permit repository redistribution.
- [ ] Share the files and source report with Rakha for the next stage.
Repository note: The Kaggle dataset is large. Avoid committing large binaries directly to normal Git if they exceed hosting limits; use an approved shared storage location or Git LFS when appropriate. This README.md can be committed independently as a reproducible source manifest.