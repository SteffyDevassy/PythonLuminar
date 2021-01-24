from functools import *
isl=[
    {"teamname":"mumbaicity","mp":7,"win":5,"drawn":1,"loss":1,"gf":11,"ga":3,"pts":16},
    {"teamname":"atk","mp":7,"win":5,"drawn":1,"loss":1,"gf":8,"ga":3,"pts":16},
    {"teamname":"benguluru","mp":7,"win":3,"drawn":3,"loss":1,"gf":11,"ga":8,"pts":12},
    {"teamname":"northeast","mp":7,"win":2,"drawn":4,"loss":1,"gf":8,"ga":6,"pts":10},
    {"teamname":"jemshedh","mp":7,"win":2,"drawn":4,"loss":1,"gf":8,"ga":7,"pts":10}

]

#print all team names in uppercase
teams=list(map(lambda team:team["teamname"].upper(),isl))
print(teams)
print("\n")

#print highest point
high=reduce(lambda p1,p2:p1 if p1>p2 else p2,
            list(map(lambda team:team["pts"],isl)))
teams=list(filter(lambda team:team["pts"]==high,isl))
print(teams)
print("\n")

#print min points

low=reduce(lambda p1,p2:p1 if p1<p2 else p2,
           list(map(lambda team:team["pts"],isl)))
print(low)
print("\n")

#highest win team
winner=reduce(lambda p1,p2:p1 if p1>p2 else p2,
            list(map(lambda team:team["win"],isl)))
teams=list(filter(lambda team:team["win"]==winner,isl))
print(teams)


