import sys;

from Data.Database import *
from Data.CSV import *;
from Data.WebScrape import *;

#This is the main script that will be run for now, in order to test or run our function. This will very likely become a GUI
#see Web folder for web files.

#Main features being displayed for the user to select.
userInput = int(input('''Please select which feature you would like to use? 
Enter 1, for single versus battle. One pokemon vs another pokemon. 
Enter 2, for team battle. You would build two pokemon teams and  simulations will be ran. 
Please enter your choice: '''))
#feature 1: single versus (1 v 1)
#So the user may choose to compare two pokemon and see who would win if they would fight, the program would then run
#multiple simulations do some ML stuff (which at this point is I'm not sure how to do). Either with a fixed moveset or
# a variable moveset (the machine chooses the moves)
if(userInput==1):
    #ask the user to select two pokemon
    p1,p2 = None
    #Ask user for the moveset

    #validate moveset - make sure the pokemon can learn the moves. For example bulbasaur can't learn flamethrower.

    #Use PokemonAPI.py functions to search for the pokemon on name and generate an object (defined in \Objects not the jsonfiles)

    #run simulations either with variable or given movesets

    #collect the data, and do more ML stuff here...
    pass

#feature 2: team versus
#pokemon team vs pokemon team
#so its esentially feature 1, but its a full on team battle (3 vs 3, six vs six)
else:
    #ask the user to list two pokemon teams
    team1,team2=list()

    #Search for the pokemon within the teams

    #Ask for the moveset for each pokemon (either can be given by the user, or the user may enter variable so then that
    #would be generated and tested.

    #Validate the movesets (if the moveset is variable, then don't worry about it)

    #run simulations with the two teams

    #collect data from the simulations and do more ML stuff here...
    pass



