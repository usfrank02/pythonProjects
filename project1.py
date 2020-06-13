#! python
import sys
# Set up price variables
ps3_game = 20
ps4_game = 45

#Temporary discount on PS3 games
ps3_game -= 2 #$2 off

#Ask for number of each game to be purchased
num_ps3_games = int(input("How many PS3 games?: "))
num_ps4_games = int(input("How many PS4 games?: "))

#Calculate total for each type of game
ps3_total = num_ps3_games * ps3_game
ps4_total = num_ps4_games * ps4_game

#Calculate total cost
total_cost = ps3_total + ps4_total

#Apply 15% discount
total_cost *= 15/100

#Print out total order cost
print("You order costs: ${}".format(total_cost))


