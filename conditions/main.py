# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line


def farm_action(weather, time, do_need_milking, location, season, is_slurrytank_full, is_grass_long):
    if time == "night" and weather == "rainy" and location != "cowshed" or do_need_milking == True and location == "pasture":
        print('take cows to cowshed')
        return True
    elif do_need_milking == True:
        print('milk cows')
        return True
    elif do_need_milking == True and location == "pasture":
        print('take cows back to pasture')
        return True
    elif is_slurrytank_full == True and location == "cowshed" and (weather != "sunny" or weather != "windy"):
        print('fertilize pasture')
        return True
    elif is_grass_long == True and season == "spring" and weather == "sunny" and location != "pasture":
        print('mow grass')
        return True
    else:
        print('wait')
        return False


# print

print(farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True))
'fertilize pasture'

print(farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))
'wait'

print(farm_action('windy', 'night', True, 'cowshed', 'winter', True, True))
'milk cows'

print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))
# take cows to cowshed, milk cows, take cows back to pasture""")
