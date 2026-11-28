## 1. Overview

| ID | File | Row represents | Rows checked | Columns | Identifier | Cheat label? |
|----|------|----------------|--------------|---------|------------|--------------|
| D1 | dataset_Cheat_Detection.csv | 2-second gameplay window | 3584 | 18 | none (timestamp only) | Yes (es_trampa_max + 4 types) |
| D2 | PUBG_Player_Statistics.csv | One player, lifetime aggregate | not counted yet (read 1000) | 152 | player_name, tracker_id | No |
| D3 | train_V2.csv | One player in one match | not counted yet (read 1000) | 29 | Id, groupId, matchId | No |

## 2. D1 columns
- Features: timestamp, angle_error_mean, angle_error_max, speed_mean, speed_max, is_shot_sum, is_hit_sum, is_received_damage_sum, health_mean, ammo_left_min, ammo_max, accuracy_rate, infinite_ammo_ratio
- Labels: es_trampa_max, isAimbot_max, isVidaInfinita_max, isMunicionInfinita_max, isSuperVelocidad_max
- Format: sep=";" decimal=","

## 3. D2 columns
- Identity: player_name, tracker_id
- Stats for 3 modes, prefixes solo_, duo_, squad_ (about 50 columns each)
- Same metrics repeat in each mode (KillDeathRatio, WinRatio, HeadshotKillRatio, DamageDealt, MoveDistance, Rating, ...)
- No cheat label

## 4. D3 columns
- Identity: Id, groupId, matchId
- Match context: matchType, matchDuration, maxPlace, numGroups
- Player stats: assists, boosts, damageDealt, DBNOs, headshotKills, heals, killPlace, kills, killStreaks, longestKill, revives, rideDistance, roadKills, swimDistance, teamKills, vehicleDestroys, walkDistance, weaponsAcquired
- Ranking points: killPoints, rankPoints, winPoints
- Original target: winPlacePerc (finish placement, not cheating)
- No cheat label

## 5. Compatibility
D1, D2 and D3 differ in what one row means and share no identifier. They are not merged.