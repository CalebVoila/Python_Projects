import random

def start_game():
    print("Welcome to the Interactive Storytelling Game!")
    print("You find yourself in a mysterious forest. You must make decisions to find your way out.")
    play()

def play():
    while True:
        choice = input("What do you do? (1. Go left, 2. Go right): ")
        if choice == '1':
            explore_left()
            break
        elif choice == '2':
            explore_right()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

def explore_left():
    print("You decide to go left and encounter a locked door.")
    print("To unlock the door, you must solve a puzzle:")
    puzzle = "What has keys but can't open locks?"
    answer = "keyboard"
    player_answer = input("Puzzle: {}\nYour answer: ".format(puzzle))
    if player_answer.lower() == answer:
        print("The door unlocks, and you proceed.")
        next_step()
    else:
        print("The door remains locked. You must try again.")

def explore_right():
    outcome = random.choice(["animal", "chest"])
    if outcome == "animal":
        encounter_wild_animal()
    else:
        find_treasure_chest()

def encounter_wild_animal():
    print("You encounter a wild animal!")
    outcome = random.choice(["run", "fight"])
    if outcome == "run":
        print("You run away and find a hidden path.")
        next_step()
    else:
        print("You decide to fight the animal.")
        if random.random() < 0.5:  # 50% chance of winning the fight
            print("You defeat the animal and find a key.")
            next_step()
        else:
            print("The animal overwhelms you. Game over.")

def find_treasure_chest():
    print("You find a treasure chest!")
    outcome = random.choice(["map", "trap"])
    if outcome == "map":
        print("You open it and find a map.")
        next_step()
    else:
        print("As you open the chest, it triggers a trap. You narrowly avoid it and find a key inside.")
        next_step()

def next_step():
    while True:
        choice = input("What's your next move? (1. Follow the map, 2. Explore further): ")
        if choice == '1':
            follow_map()
            break
        elif choice == '2':
            explore_further()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

def follow_map():
    print("You follow the map and discover a secret exit from the forest.")
    print("Congratulations, you've won!")

def explore_further():
    print("You explore further and encounter a locked gate.")
    print("To unlock the gate, you must solve a riddle:")
    riddle = "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?"
    answer = "echo"
    player_answer = input("Riddle: {}\nYour answer: ".format(riddle))
    if player_answer.lower() == answer:
        print("The gate opens, and you proceed.")
        print("You find yourself in a clearing with the exit visible.")
        print("Congratulations, you've won!")
    else:
        print("The gate remains locked. You must try again.")

def main():
    start_game()
    while True:
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            start_game()
        else:
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
