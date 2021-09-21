# Server containing Tournament classes

class Tournament():
    def __init__(self, win=3, draw=1, loss=0):
        self.settings = {"win": int(win), "draw": int(draw), "loss": int(loss)}
        self.scores = {}


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

    # Function for handling content of a game file sent between active players
    def handleGameFile(self, filePath):
        # Extract the relevant content without altering the file
        fileContent = self.readGameFile(filePath)
        # If game is still active, return false (no action required)
        if fileContent['gamedone'] != True:
            return(False)
        # If game is over and final score is greater than zero, add one point to sending player's score
        if fileContent['gamescore'] > 0:
            self.scores[fileContent['fplayer']] += self.settings['win']
            self.scores[fileContent['tplayer']] += self.settings['loss']
        # If final score is lower than zero, add one point to receiving player's score
        elif fileContent['gamescore'] < 0:
            self.scores[fileContent['tplayer']] += self.settings['win']
            self.scores[fileContent['fplayer']] += self.settings['loss']
        elif fileContent['gamescore'] == 0:
            self.scores[fileContent['fplayer']] += self.settings['draw']
            self.scores[fileContent['tplayer']] += self.settings['draw']
        # Return true
        return(True)

def main():

    ## plan the color order of games to make sure everyone gets to play both colors

    ### prompt players to initiate game
    tournament = Tournament()
    tournament.handleGameFile('testGameFile.txt')
    # store the results in the tournament data in local variable
    # tournament_data += tournament
    # send out tournamnet data

if __name__ == '__main__':
    main()
