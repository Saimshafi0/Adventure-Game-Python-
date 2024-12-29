name = input("Type your name: ")
print(f"Welcome, {name}, to the Mystic Adventure!")

answer = input(
    "You find yourself at the entrance of an ancient forest. You can either explore the 'forest' or follow the 'trail' leading to the mountains. Which do you choose? ")

if answer == "forest":
    answer = input(
        "As you venture deeper into the forest, you find a magical tree glowing faintly. Do you 'approach' the tree or 'ignore' it and move on? ")
    if answer == "approach":
        print("The tree grants you magical powers to control elements. You use them to protect the realm and become a hero. You win!")
    elif answer == "ignore":
        print("You wander further and encounter a pack of wolves. Without any defense, you become their dinner. You lose.")
    else:
        print("Not a valid option. You lose.")

elif answer == "trail":
    answer = input(
        "You follow the trail and come across an old, rickety cabin. Do you 'enter' the cabin or 'continue' up the trail? ")
    if answer == "enter":
        answer = input(
            "Inside the cabin, you find a mysterious book. Do you 'open' the book or 'leave' it alone? ")
        if answer == "open":
            print("The book contains ancient spells that summon a friendly dragon to aid you. You ride the dragon and win!")
        elif answer == "leave":
            print("You leave the book and exit the cabin, but a storm forces you to take shelter. Lightning strikes the cabin and it collapses. You lose.")
        else:
            print("Not a valid option. You lose.")
    elif answer == "continue":
        print("You climb higher but run out of supplies and energy, unable to continue. You lose.")
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print(f"Thankyou {name} for playing the Mystic Adventure!")