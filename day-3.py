from resources.day3.art import treasure_chest, game_over

play_game = True

print(treasure_chest)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

while play_game == True:

    obs_1 = input("You see two doors, which will you choose? Left or Right? ").lower()
    obs_1_choices = ['left', 'l', 'right', 'r']

    while obs_1 not in obs_1_choices:
            obs_1 = input("Choose left or right: ").lower()
    else:
        if obs_1 == 'l' or obs_1 == 'left':
            obs_2 = input("You arrived at the port, will you swim or wait?").lower()
            obs_2_choices = ['swim', 's', 'wait', 'w']

            while obs_2 not in obs_2_choices:
                obs_2 = input("Will you swim or wait? ").lower()
            else:
                if obs_2 == 'w' or obs_2 == 'wait':
                    print("A ship takes you to another room with 3 doors.")
                    obs_3 = input("Choose which one to open: Red, Yellow, or Blue: ").lower()
                    obs_3_choices = ['red', 'yellow', 'blue']

                    while obs_3 not in obs_3_choices:
                        obs_3 = input("Choose from ReRed, Yellow, or Blue: ").lower()
                    else:
                        if obs_3 == 'blue':
                            print("You found the treasure! Congratulations")

                        elif obs_3 == 'red':
                            print("You lose your head and lost your way in the fog.")
                            print(game_over)

                        elif obs_3 == 'yellow':
                            print("You turned to stone, forever sentient but never moving.")

                elif obs_2 == 's' or obs_2 == 'swim':
                    print("The Kraken pulled you to the deepest depths of the ocean.")

        elif obs_1 =='r' or obs_1 == 'right':
            print("You fell into the fiery pits of HELL!")

    print(game_over)
    play_again = input("Start game? ").lower()
    if play_again.startswith('n'):
        play_game = False

print("Goodbye")
