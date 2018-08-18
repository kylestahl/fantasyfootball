import sqlalchemy
import pandas as pd


## SQLAlchemy and Pandas
conn = sqlalchemy.create_engine('postgresql://nfldb:131718@localhost:5432/nfldb')
game = pd.read_sql("SELECT * FROM game", conn)
play = pd.read_sql("SELECT * FROM play", conn)
drive = pd.read_sql("SELECT * FROM drive", conn)
player = pd.read_sql("SELECT * FROM player", conn)
team = pd.read_sql("SELECT * FROM team", conn)
agg_play =  pd.read_sql("SELECT * FROM agg_play", conn)
play_player =  pd.read_sql("SELECT * FROM play_player", conn)