n = int(input())
tabl = {}
for i in range(n):
    team1, score1, team2, score2 = input().split(';')
    if team1 not in tabl:
        tabl[team1] = [0, 0, 0, 0, 0]
    if team2 not in tabl:
        tabl[team2] = [0, 0, 0, 0, 0]

    tabl[team1][0] += 1  # all games team 1
    tabl[team2][0] += 1  # all games team 2

    if int(score1) > int(score2):
        tabl[team1][1] += 1  # wins
        tabl[team1][4] += 3  # points
        tabl[team2][3] += 1  # loose team 2
    elif int(score1) < int(score2):
        tabl[team2][1] += 1  # wins team 2
        tabl[team2][4] += 3  # points team 2
        tabl[team1][3] += 1  # loose team 1
    else:
        tabl[team1][2] += 1  # draws team 1
        tabl[team2][2] += 1  # draws team 2
        tabl[team1][4] += 1  # points team 1
        tabl[team2][4] += 1  # points team 2

for team, tbl in tabl.items():
    print(team + ':', tbl[0], tbl[1], tbl[2], tbl[3], tbl[4])