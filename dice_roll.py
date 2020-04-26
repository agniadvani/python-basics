import random
def main():
    dice_sides = int(input("Enter sides of a dice: "))
    random_dice = lis_of_dice_rolled(dice_sides)
    print(random_dice)


def lis_of_dice_rolled(n):
    dice = []
    for sides in range(n):
        ran_dig = random.randint(1,n)
        dice.append(ran_dig)
    return dice

main()



