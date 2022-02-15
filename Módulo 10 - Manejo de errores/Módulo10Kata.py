def waterLeft(astronauts, waterLeft, daysLeft):
    dailyUsage = astronauts * 11
    totalUsage = dailyUsage * daysLeft
    totalWaterLeft = waterLeft - totalUsage
    return f"Total water left after {daysLeft} days is: {totalWaterLeft} liters"


def waterLeft2(astronauts, waterLeft, daysLeft):
    dailyUsage = astronauts * 11
    totalUsage = dailyUsage * daysLeft
    totalWaterLeft = waterLeft - totalUsage
    if totalWaterLeft < 0:
        raise RuntimeError(
            f"There is not enough water for {astronauts} astronauts after {daysLeft} days!")
    return f"Total water left after {daysLeft} days is: {totalWaterLeft} liters"


def waterLeft3(astronauts, waterLeft, daysLeft):
    for argument in [astronauts, waterLeft, daysLeft]:
        try:
            if argument / 10:
                argument = astronauts

        except TypeError:
            raise TypeError(
                f"All arguments must be of type int, but received: '{argument}'")

    dailyUsage = astronauts * 11
    totalUsage = dailyUsage * daysLeft
    totalWaterLeft = waterLeft - totalUsage
    if totalWaterLeft < 0:
        raise RuntimeError(
            f"There is not enough water for {astronauts} astronauts after {daysLeft} days!")

    return f"Total water left after {daysLeft} days is: {totalWaterLeft} liters"

def main():
    #print(waterLeft(5, 100, 2))

    #print(waterLeft2(5, 100, 2))

    #print(waterLeft2("3", "200", None))

    print(waterLeft3("3", "200", None))


if __name__ == '__main__':
    main()
