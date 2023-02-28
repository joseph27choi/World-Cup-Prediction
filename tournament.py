# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    # TODO: Read teams into memory from file
    # open file
    with open(sys.argv[1]) as file:

        # read as dictionary
        reader = csv.DictReader(file)

        # have teams[] store each country info
        for index, row in enumerate(reader):
            # update the team rating from string to int
            row['rating'] = int(row['rating'])
            # append it to teams
            teams.append(row)

    counts = {}
    # TODO: Simulate N tournaments and keep track of win counts
    for simulation in range(N):
        # simulate tournament and get the champion
        champ_name = simulate_tournament(teams)

        # add the champion to the count
        counts.setdefault(champ_name, 0)

        if champ_name in counts:
            # add one win
            counts[champ_name] += 1


    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    '''
    :team1: first team
    :type: str
    :team2: second team
    :type: str
    :returns: true if team1 wins, false if otherwise
    :rtype: bool
    '''

    # take the rating of both teams
    rating1 = team1["rating"]
    rating2 = team2["rating"]

    # find probability of team 1 winning
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))

    # return boolean
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    '''
    :teams: a list with all participating team names
    :type: list[str]
    :returns: name of winning team
    :rtype: str
    '''
    # TODO

    # copy array by value
    contenders = teams
    num_contenders = len(contenders)
    # simulate rounds until only one winner
    while (True):
        contenders = simulate_round(contenders)
        num_teams = len(contenders)

        if (num_teams == 1):
            break

    winner = contenders[0]

    return winner['team']


if __name__ == "__main__":
    main()
