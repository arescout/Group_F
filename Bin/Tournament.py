# Server containing Tournament classes

class Tournament():
    def __init__(self):
        self.scores = {'Player2': 0, "Player1": 5}


        ### read game history from server (such as last move made) from txt file

        ### let player make her/his move

        ### store the data for that players move and send to server

        ## if game finish ->
            # let host decide point format? (not sure what this is for)
            # let everyone know that game is over and the results
            # return
        return

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

    def handleGameFile(self, filePath):
        fileContent = self.readGameFile(filePath)
        if fileContent['gamedone'] != True:
            return(False)
        if fileContent['gamescore'] > 0:
            self.scores[fileContent['fplayer']] += 1
        elif fileContent['gamescore'] < 0:
            self.scores[fileContent['tplayer']] += 1
        return(True)

def main():

    ## plan the color order of games to make sure everyone gets to play both colors

    ### prompt players to initiate game
    tournament = Tournament()
    print(tournament.scores)
    tournament.handleGameFile('testGameFile.txt')
    print(tournament.scores)
    # store the results in the tournament data in local variable
    # tournament_data += tournament
    # send out tournamnet data

if __name__ == '__main__':
    main()
