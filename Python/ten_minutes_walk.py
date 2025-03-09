def is_valid_walk(walk):
    if len(walk) != 10:
        return False 
    north_south = walk.count('n') - walk.count('s')
    east_west = walk.count('e') - walk.count('w')
    return north_south == 0 and east_west == 0
