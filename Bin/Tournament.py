# Server containing Tournament classes

class Tournament():
    def __init__(self, win=3, draw=1, loss=0):
        # Dict for storing settings
        self.settings = {"win": int(win), "draw": int(draw), "loss": int(loss)}
        # Dict for storing player scores
        self.scores = {}
        # Dict for storing player names and addresses
        self.players = {}
        # Dict for keeping game history
        self.history = {}
        # Int for keeping track of number of games
        self.gamesPlayed = 0


        ### read game history from server (such as last move made) from txt file

        ### let player make her/his move

        ### store the data for that players move and send to server

        ## if game finish ->
            # let host decide point format? (not sure what this is for)
            # let everyone know that game is over and the results
            # return
        return

    # Function for adding a player to the tournament
    def addPlayer(self, playerName, playerAddress):
        # Check if player is new
        if playerAddress in self.players.values():
            # If not, print for logging and return False
            print(f'{playerAddress} already registered!')
            return(False)
        # Check if player name is already taken
        if playerName in self.players.keys():
            # If so, print for logging and give a new name
            print(f'{playerName} already taken, new name is {playerName + str(len(self.players))}')
            playerName = playerName + str(len(self.players))
        # If new, add player to dict
        self.players.update({playerName: playerAddress})
        self.scores.update({playerName: 0})
        return(True)

    # Function for reading a game file sent between players
    # Returns a dict with player names, gamescore and game status
    def readGameFile(self, filePath):
        # Define empty dict
        content = {
        'fplayer': "",
        'tplayer': "",
        "gamescore": "",
        "gamedone": ""}
        # Open gamefile (already received and stored locally)
        # Open with read only
        with open(filePath, 'r+') as f:
            # Split the file into lines
            lines = f.readlines()
            # Iterate over each line
            for line in lines:
                # Strip the line of trailing blankspaces
                line.rstrip()
                # Split the line into a list of words
                # Splitting is done on blanksplace as default
                line = line.split()
                # If line is empty, skip it
                if line == []:
                    continue
                # Check if line starts with tournament keyword
                # If so, add information to dict
                if line[0] == "FPLAYER:":
                    content['fplayer'] = line[1]
                if line[0] == 'TPLAYER:':
                    content['tplayer'] = line[1]
                if line[0] == 'GAMESCORE:':
                    content['gamescore'] = int(line[1])
                if line[0] == 'GAMEDONE:':
                    if line[1] == '1':
                        content['gamedone'] = True
                    else:
                        content['gamedone'] = False
            # When all lines are read, file is closed
        # Return dict
        return(content)

    # Function for handling content of a game file sent between active players
    def handleGameFile(self, filePath):
        # Extract the relevant content without altering the file
        fileContent = self.readGameFile(filePath)
        # If game is still active, return false (no action required)
        if fileContent['gamedone'] != True:
            return(False)
        # Add one to games played
        self.gamesPlayed += 1
        self.history.update({self.gamesPlayed: {
        "players": [fileContent['fplayer'], fileContent['tplayer']],
        "score": fileContent['gamescore']
        }})
        # If game is over and final score is greater than zero, add one point to sending player's score
        # Also update game history
        if fileContent['gamescore'] > 0:
            self.scores[fileContent['fplayer']] += self.settings['win']
            self.scores[fileContent['tplayer']] += self.settings['loss']

            self.history[self.gamesPlayed].update({'winner': fileContent['fplayer']})
        # If final score is lower than zero, add one point to receiving player's score
        elif fileContent['gamescore'] < 0:
            self.scores[fileContent['tplayer']] += self.settings['win']
            self.scores[fileContent['fplayer']] += self.settings['loss']

            self.history[self.gamesPlayed].update({'winner': fileContent['tplayer']})
        elif fileContent['gamescore'] == 0:
            self.scores[fileContent['fplayer']] += self.settings['draw']
            self.scores[fileContent['tplayer']] += self.settings['draw']

            self.history[self.gamesPlayed].update({'winner': 'draw'})

        # Return true
        return(True)

    def generateSortedScores(self):
        return(dict(sorted(self.scores.items(), key=lambda item: item[1])))

    def generateNextGameData(self):
        # This is just a placeholder
        nextGame = {'player1':'Player1', 'player1Colour': 'B', 'player2':'Player2', 'player2Colour': "W"}
        return(nextGame)

    def generateTournamentFile(self, filePath):
        sortedScores = self.generateSortedScores()
        nextGame = self.generateNextGameData()
        print(nextGame)
        with open(filePath, 'w+') as f:
            f.write(f'GAMESPLAYED: {self.gamesPlayed}\n')
            for player, score in sortedScores.items():
                f.write(f'PLAYERSCORE: {player} {score}\n')
            f.write('NEXTPLAYERS: ')
            for key, val  in nextGame.items():
                if 'Colour' in key:
                    f.write(val+' ')
                else:
                    f.write(val+':')
            f.write('\n')
        return(True)


def main():

    ## plan the color order of games to make sure everyone gets to play both colors

    ### prompt players to initiate game
    tournament = Tournament()
    tournament.addPlayer('Player1',1234)
    tournament.addPlayer('Player2', 1235)
    tournament.addPlayer('Player3', 1236)
    print(tournament.players)
    tournament.handleGameFile('testGameFile.txt')
    tournament.handleGameFile('testGameFile0.txt')
    print(tournament.scores)
    print(tournament.history)
    tournament.generateTournamentFile('testTournamentFile.txt')
    # store the results in the tournament data in local variable
    # tournament_data += tournament
    # send out tournamnet data

if __name__ == '__main__':
    main()
