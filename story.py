def intro():
    print("You wake up in a dark forest. You can go left, right, or center.")
    choice = input("Which direction do you choose? (left/right/center): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    elif choice == "center":
        center_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")
    print("Its whispers tempt you with power… you accept, and feel corruption spreading.")

def center_path():
    print("You walk straight ahead and discover a peaceful meadow with a sparkling stream.")

if __name__ == "__main__":
    intro()
