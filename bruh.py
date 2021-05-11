def coins(one, two, five, goal):
    for x in range(0, one+1):
        for y in range(0, two+1):
            for z in range(0, five+1):
                print(x,y,z)
                if x + 2 * y + 5 * z == goal:
                    return True
    return False


print(coins(4,2,0,10))


