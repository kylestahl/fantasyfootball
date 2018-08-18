

SELECT  gsis_id, drive_id, play_id, player_id, team,
	passing_tds, passing_yds,
	passing_twoptm, fumbles_rec_tds,
	rushing_yds, rushing_tds, rushing_twoptm,
	receiving_rec, receiving_yds, receiving_tds,
	rushing_twoptm, puntret_tds, kickret_tds,
	passing_int, fumbles_lost, kicking_rec_tds
FROM play_player
WHERE player_id IN (SELECT player_id FROM player WHERE player.position IN ('QB','RB','FB','WR','TE'))
AND gsis_id IN (SELECT gsis_id FROM game WHERE season_year = 2017);