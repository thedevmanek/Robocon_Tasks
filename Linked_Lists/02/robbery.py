houses = [6, 7, 1, 3, 8, 2, 4]


def houseRobberRecursive(house_value):
    def stealFromHouse(index):
        if(index >= len(house_value)):
            return 0

        return max(house_value[index] + stealFromHouse(index + 2), stealFromHouse(index + 1))

    return stealFromHouse(0)

print(houseRobberRecursive(houses))
