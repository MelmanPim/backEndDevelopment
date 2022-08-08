# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1

player_0 = "Ruud Gullit"
goal_0 = 32
player_1 = "Marco van Basten"
goal_1 = 54

scorers = f'{player_0} {goal_0}, {player_1} {goal_1}'
print(scorers)

report = f'{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute'
print(report)

# Part 2

player = "Frank Rijkaard"
first_name = player[:5]
last_name_len = len(player[6:])
print(last_name_len)
name_short = f'{player[0]}. {player[6:]}'
print(name_short)
chant = (first_name + "! ") * (len(first_name) - 1) + (first_name + "!")
print(chant)

good_chant = chant[-1] != " "
print(good_chant)
