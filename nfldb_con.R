library(RPostgreSQL)
library(DBI)
library(dplyr)


drv <- dbDriver("PostgreSQL")
conn <- dbConnect(drv, dbname = "nfldb",
                 host = "localhost", port = 5432,
                 user = "nfldb", password = 131718)

team <- conn %>% tbl("team") %>% data.frame()
game <- conn %>% tbl("game") %>% data.frame()
drive <- conn %>% tbl("drive") %>% data.frame()
play <- conn %>% tbl("play") %>% data.frame()
player <- conn %>% tbl("player") %>% data.frame()
play_player <- conn %>% tbl("play_player") %>% data.frame()
agg_play <- conn %>% tbl("agg_play") %>% data.frame()

game %>% group_by(season_year) %>% summarise(cnt = n())
