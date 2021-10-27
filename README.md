# GroupF
This repository contains the necessary classes and functions for hosting a server and running a tournament of a general game. The server handles sending relevant game files, keeping track of matchups with player colours and keeping track of tournament scores.

The server sends out tournament files at the beginning and end of each game. It sends out an endfile once the last game is done. It reads and passes on gamefiles between each round in a game.

## Hosting
To host a server, initiate the Server class with port specified. If the server isn't to be hosted on localhost, change the address-variable in the class constructor.

To host a client/player, initiate the Client class with port specified. If the client isn't to be hosted the same address as the server, change the address-variable in the class constructor.

Both classes has functions distinguishing between the files sent and received. Where applicable to the communication platform, further functionality based on said files is included as well.

## Conventions

### Players
- Player names can't contain blankspaces.

## Game file key words:
Game files are files sent between two active players. The file should consist of all relevant game state data AND the following key word-value pairs:
GAMEFILE - the first word of the document.
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


## Endfile
The endfile is sent out once all games has been played, indicating that the tournament is over.
It only contains the ENDFILE keyword and the final scores.

###Licence
MIT License

Copyright (c) 2021 ChefKeff

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
