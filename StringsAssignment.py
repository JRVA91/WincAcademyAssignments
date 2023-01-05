# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

goalscorer_0 = 'Ruud Gullit'
goalscorer_1 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = goalscorer_0 + " " +str(goal_0) + ', ' + goalscorer_1 + " " + str(goal_1)


report = f"{goalscorer_0} scored in the {str(goal_0)}nd minute \n{goalscorer_1} scored in the {str(goal_1)}th minute "
print(report)

player = "Wim Kieft"
first_name = player[:player.find(" ")]
print(first_name)
last_name = player[player.find(" ")+1:]
last_name_len = len(last_name)
print(last_name)
print(last_name_len)

name_short= player[0]+'. '+ last_name

print(name_short)

chant = (f'{first_name}! '*len(first_name)).strip()

print(chant)
good_chant = chant[-1] != " "
print(good_chant)
