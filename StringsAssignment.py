# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

goalscorer_0 = 'Ruud Gullit'
goalscorer_1 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = goalscorer_0 + " " +str(goal_0) + ', ' + goalscorer_1 + " " + str(goal_1)

report = goalscorer_0 + " scored in the " + str(goal_0)+'nd minute' '\n' + goalscorer_1 + " scored in the " + str(goal_1)+'th minute'
print(report)

player = "Wim Kieft"
first_name = player[0:3]

last_name_len = len(player[player.find("Kieft"):])
print(last_name_len)

name_short= player[0]+'. '+ player[4:9]

print(name_short)

chant_list =[]
name_length = len(player[0:3])

for i in range (name_length):
    chant_list.append(player[0:3] +"!")

#chant = (player[0:3]+"! ")* len(player[0:3]) #wrong chant
space = " "
chant = space.join(chant_list)

print(chant)

good_chant = chant[-1] != " "
print(good_chant)

