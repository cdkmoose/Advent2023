max = {"red": 12, "green": 13, "blue": 14}

sum = 0

file1 = open('./data/cubes.txt', 'r')
lines = file1.readlines()

#lines = {
#"Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
#}

for l in  lines:
    games = l.split(':')
    gameid = int(games[0].split()[1])

    pulls = games[1].split(';')

    for pull in pulls:
        cubes = pull.split(',')

        for cube in cubes:
            selection = tuple(cube.split())
            print(selection)

            if int(selection[0]) > max[selection[1]]:        
                gameid = 0


    sum = sum + gameid

print(sum)

