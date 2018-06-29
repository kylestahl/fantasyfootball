# Fantasy Football

The goal of this repo is to build off the prior work I did in `Draft-Kings-Optimization`. At the end of that project I showed that based on a solid estimate of (fantasy) points scored, you could use `PuLP` to optimize your fantasy line-up given the constraints imposed by the game (number of players, cost, etc). 


It was found that picking players that generally do well is not the best strategy for daily fantasy sports (though I may use it for other leagues). For daily fantasy it would be best to predict who, at each position, is most likely going to preform exceptionally well, a.k.a. who is going to be the best preformer in each position. The idea will to be predicting either raw points or the probabiltiy that a player scores exceptionally well (this would have to be mathematically defined later). And then use at as input into the optimization. 

The current step is to write a function that can calculate the points score for any player/week given their stats using this wonderful NFLBD provided by https://github.com/BurntSushi/nfldb. Follow those instructions to get a SQL database of the results from every single NFL play for the past 7 years or something (I forgot the actual amount of years). 


