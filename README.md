# GroupF
Repository for Group F. Game server.
This is a test.

## Conventions

### Players
- Player names can't contain blankspaces

## Game file key words:
FPLAYER: Id of sending player
FPCOLOUR: Colour of sending player
TPLAYER: Id of receiving player
TPCOLOUR: Colour of receiving player. W = white, B = black
GAMEDONE: Boolean telling if the game is finished (0/1)
GAMESCORE: The point difference between players. >0 -> FPLAYER is in lead, <0 -> TPLAYER is in lead.

## Tournament file key words:
GAMESPLAYED: Number of games played
PLAYERSCORE: Follows by a player name and player score. Is printed in ascending order.
NEXTPLAYERS: Follows by names of the next players and their color. Format -> "Player1:W Player2:B"
