# Game Score Tracker to keep track of all players and their scores

# Features
# Add players
# Add names
# Add Scores
# Score History

#Extras
# - Dice Roll/Coin flip/Random number

PlayerScores = dict() #{"Name", Score]}
Commands = [("'e'", "Save and Exit the Game"),
            ("'h'", "Display Help Menu"),
            ("'a [playerName]'", "Add a Player"),
            ("'r [playerName]'", "Remove a Player"),
            ("'c [playerName] [playerName] [scoreChange]'", "Change Score"),
            ("'s'", "Scoreboard"),
            ("'n'", "New Game - set scores back to 0")]

ErrorMessages = {"InvalidCommand": "Invalid Command: '{p1}'.  Please try again or run 'h' for a list of Help Options",
                 "InvalidNumArgs": "Invalid Number of Arguments for command '{p1}'.  Expected {p2} and received {p3}",
                 "InvalidValue": "Invalid {p1} value: '{p2}'",
                 "PlayerAlreadyExists": "Cannot Add new Player '{p1}' because another player with this name already exists.",
                 "PlayerNotExists": "Cannot Remove Player '{p1}' because no Player exists with this name."}


def main():
    
    userInput = ""
    while (True):
        userInput = input("\nEnter a command: ")
        
        if(userInput == "e"):
            # End Game
            print("\nGame Ended")
            #TODO Add Saving Functionality
            break
        elif(userInput == "h"):
            # Help Options
            DisplayHelpOptions()
        elif(userInput.split(" ")[0] == "a"):
            # Add Player
            AddPlayer(userInput)
        elif(userInput.split(" ")[0] == "r"):
            # Remove Player
            RemovePlayer(userInput)
        elif(userInput.split(" ")[0] == "c"):
            # Change Score
            ChangeScore(userInput)
        elif(userInput == "s"):
            # Scoreboard
            DisplayScoreboard()
        elif(userInput == "n"):
            # New Game
            NewGame()
        else:
            ReturnError("InvalidCommand",[userInput])

def DisplayHelpOptions():
    print("\nHelp Options:")
    for c in Commands:
        print(c[0] + ": " + c[1])

def AddPlayer(commandInput):
    commandComponents = commandInput.split(" ")
    #Validations
    if(len(commandComponents) not in [2,3]):
        ReturnError("InvalidNumArgs", [commandComponents[0], "2 or 3", len(commandComponents)])
    elif(commandComponents[1] == ""):
        ReturnError("InvalidValue", ["Player Name", commandComponents[1]])
    elif(len(commandComponents) == 3 and not(commandComponents[2].isnumeric())):
        ReturnError("InvalidValue", ["Score", commandComponents[2]])
    elif(commandComponents[1] in PlayerScores):
        ReturnError("PlayerAlreadyExists", [commandComponents[1]])
    else:
        #Add Player
        score = 0
        if(len(commandComponents) == 3):
            score = int(commandComponents[2])

        PlayerScores[commandComponents[1]] = score
        print(f"Player '{commandComponents[1]}' has been added with a current score of {PlayerScores[commandComponents[1]]}!")

def RemovePlayer(commandInput):
    commandComponents = commandInput.split(" ")
    #Validations
    if(len(commandComponents) != 2):
        ReturnError("InvalidNumArgs", [commandComponents[0], 2, len(commandComponents)])
    elif(commandComponents[1] == ""):
        ReturnError("InvalidValue", ["Player Name", commandComponents[1]])
    elif(commandComponents[1] not in PlayerScores):
        ReturnError("PlayerNotExists", [commandComponents[1]])
    else:
        #Remove Player
        PlayerScores.pop(commandComponents[1])
        print(f"Player '{commandComponents[1]}' has been removed!")

def ChangeScore(commandInput):
    commandComponents = commandInput.split(" ")
    #Validations
    if(len(commandComponents) != 3):
        ReturnError("InvalidNumArgs", [commandComponents[0], 3, len(commandComponents)])
    elif(commandComponents[1] == ""):
        ReturnError("InvalidValue", ["Player Name", commandComponents[1]])
    elif(commandComponents[1] not in PlayerScores):
        ReturnError("PlayerNotExists", [commandComponents[1]])
    elif(not(commandComponents[2].isnumeric())):
        ReturnError("InvalidValue", ["Score", commandComponents[2]])
    else:
        #Change Points
        previousPoints = PlayerScores[commandComponents[1]]
        PlayerScores[commandComponents[1]] = previousPoints + int(commandComponents[2])
        print(f"Score for '{commandComponents[1]}' has been updated!  New score is {PlayerScores[commandComponents[1]]}")

def DisplayScoreboard():
    if(len(PlayerScores) == 0):
        print("\nNo scores exist")
        return 0
    
    print("\nSCOREBOARD")
    
    place = 0
    sorted_scores = sorted(PlayerScores.items(), key=lambda item: item[1], reverse=True)
    for s in range(len(sorted_scores)):
        if(s == 0 or sorted_scores[s][1] != sorted_scores[s-1][1]):
            place = s+1
        print(f"{place} - {sorted_scores[s][0]} ({sorted_scores[s][1]})")    

def NewGame():
    print("\n'New Game' has been selected")
    yn_NewGame = input("\nAre you sure?  Run 'y' to continue, otherwise press enter: ")
    if(yn_NewGame == "y"):
        print("\nNew Game Started!\nAll player scores have been reset to 0")
        for k in PlayerScores.keys():
            PlayerScores[k] = 0
    else:
        print("\nCommand skipped.  No changes have been made")
        return 0



def ReturnError(msgKey, parameters):
    if(msgKey not in ErrorMessages):
        print("\nInternal Error")
        raise Exception(f"No ErrorMessage exists with the key '{msgKey}'")
    elif(len(parameters) == 0):
        print(ErrorMessages[msgKey])
    else:
        parameterDict = {}
        for i in range(len(parameters)):
            k = "p" + str(i + 1)
            parameterDict[k] = parameters[i]

        print(ErrorMessages[msgKey].format_map(parameterDict))





main()