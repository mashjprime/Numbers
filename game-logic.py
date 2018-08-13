    import random
    num = random.randint(1,101)
    gs = [0]

    while True:
        g = int(input('Please enter a number between 1 and 100: '))

        if g<1 or g>100:
            print("Out of bounds!!")
            continue

        if g == num:
            print(f'Yay, you guessed it in {len(gs)} guesses :)')
            break

        gs.append(g)

        if gs[-2]:
            if abs(num-g) < abs(num-gs[-2]):
                print("Warmer")
            else:
                print("Colder")
        else:
            if abs(num-g) <= 10:
                print("Warm")
            else:
                print("Cold")
