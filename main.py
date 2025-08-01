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
            ("'s [playerName] [playerName] [scoreChange]'", "Update Score"),
            ("'n'", "New Game")]

ErrorMessages = {"InvalidCommand": "Invalid Command: '{p1}'.  Please try again or run 'h' for a list of Help Options",
                 "InvalidNumArgs": "Invalid Number of Arguments for command '{p1}'.  Expected {p2} and received {p3}"}


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
            # Add User
            AddUser(userInput)
        else:
            ReturnError("InvalidCommand",[userInput])

def DisplayHelpOptions():
    print("\nHelp Options:")
    for c in Commands:
        print(c[0] + ": " + c[1])

def AddUser(commandInput):
    commandComponents = commandInput.split(" ")
    #Validations
    if(len(commandComponents) != 2):
        ReturnError("InvalidNumArgs", [commandComponents[0], 2, len(commandComponents)])


def ReturnError(msgKey, parameters):
    if(msgKey not in ErrorMessages):
        print("\nInternal error")
        raise Exception("No ErrorMessage exists with the key '{msgKey}'")
    elif(len(parameters) == 0):
        print(ErrorMessages[msgKey])
    else:
        parameterDict = {}
        for i in range(len(parameters)):
            k = "p" + str(i + 1)
            parameterDict[k] = parameters[i]

        print(ErrorMessages[msgKey].format_map(parameterDict))





main()