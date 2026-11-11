import pandas as pd

#makes a datafram from the csv file
football_info = pd.read_csv("HW\\cfb.csv")

#Starts a loop that while the condition is true it will keep running
#In this case it will keep running until the user inputs a valid season
#Otherwise it will keep asking for a valid season
while True:
    try:
        season = int(input("Enter a season to analyze: "))
    except ValueError:
        print("Invalid input. Enter a whole-number season, such as 2020.")
        continue
    if season in football_info["Season"].values:
        break
    print(f"Season {season} was not found. Please try again.")

#allows for the filtering of the data based on the season that the user inputs
season_teams = football_info.query("Season == @season")

#Creates a dictionary that will hold the different categories of wins
#and the teams that fall into those categories
win_categories = {
    "10 or more wins": [],
    "8-9 wins": [],
    "6-7 wins": [],
    "Less than 6 wins": [],
}

#Creates a for loop that will go through each row of the data frame and check
#the number of wins for each team and add them to the appropriate category
#in the dictionary
for index, team in season_teams.iterrows():
    wins = team["Win"]
    if wins >= 10:
        win_categories["10 or more wins"].append(team["Team"])
    elif wins >= 8:
        win_categories["8-9 wins"].append(team["Team"])
    elif wins >= 6:
        win_categories["6-7 wins"].append(team["Team"])
    else:
        win_categories["Less than 6 wins"].append(team["Team"])

#Prints out the results in a formatted way that shows the season at the top
# and the teams in each category of wins.
print(f"\nCollege Football Results for {season}")
for category, teams in win_categories.items():
    print(f"\n{category}:")
    for team in teams:
        print(team)
