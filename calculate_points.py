"""
Define Functions to calculate fantasy football points based on
Draft Kings rules.

https://www.draftkings.com/help/rules/nfl
"""

# Import Packages
import sqlalchemy
import pandas as pd
import numpy as np


# Create Database Connection
conn = sqlalchemy.create_engine('postgresql://nfldb:131718@localhost:5432/nfldb')



off_query = "SELECT  gsis_id, player_id, \
	passing_tds, passing_yds, passing_twoptm, \
	rushing_yds, rushing_tds, rushing_twoptm, \
	receiving_yds, receiving_tds, receiving_twoptm, receiving_rec,  \
	puntret_tds, kickret_tds, kicking_rec_tds, fumbles_rec_tds, \
	passing_int, fumbles_lost \
FROM play_player \
WHERE player_id IN (SELECT player_id FROM player \
                    WHERE player.position IN ('QB','RB','FB','WR','TE'));"

off_players = pd.read_sql(off_query, conn)
#off_players.set_index(['gsis_id','player_id'],inplace=True)
game_player = off_players.groupby(['gsis_id','player_id']).sum()


gameId, playerId = "2017123100","00-0027939"
def get_points(playerId,gameId):
    player = game_player.loc[(gameId,playerId),]
    points = 0
    points += 4 * player['passing_tds']
    points += 0.04 * player['passing_yds']
    points += int(player['passing_yds'] > 300) * 3
    points += -1 * player['passing_int']
    points += 6 * player['rushing_tds']
    points += 0.10 * player['rushing_yds']
    points += int(player['rushing_yds'] > 100) * 3
    points += 6 * player['receiving_tds']
    points += 0.10 * player['receiving_yds']
    points += int(player['receiving_yds'] > 100) * 3
    points += 6 * player['puntret_tds']
    points += 6 * player['kickret_tds']
    points += 6 * player['kicking_rec_tds']
    points += 6 * player['fumbles_rec_tds']
    points += -2 * player['fumbles_lost']
    points += 2 * player['passing_twoptm']
    points += 2 * player['rushing_twoptm']
    points += 2 * player['receiving_twoptm']
    return(points)

get_points(playerId,gameId)

total_points = []
for row in game_player.iterrows():
    total_points.append(get_points(row[0][1], row[0][0]))

game_player['total_points'] = total_points
player_ppg = game_player['total_points'].reset_index()

