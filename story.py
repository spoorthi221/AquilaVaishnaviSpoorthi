print("An enigma awaits you, one that defies explanation. Two paths lie before you, each shrouded in mystery. Choose wisely, for the adventure begins with your decision.")

response = input("Are you in for this adventure? Yes or No? ")

if response.lower() == "yes":
    choice = input("You have two options: 1) An abandoned cabin way or 2) An adventure park. Which way do you want to go? (Enter 1 or 2) ")

    if choice == "1":
        print("You decide to explore the abandoned cabin deep in the woods. As you enter, you notice the dilapidated furniture and cobwebs everywhere. Amidst the dusty shelves, you stumble upon an old, leather-bound book. It emanates an eerie aura.")
        decision = input("You hear a knock on the cabin door. Will you open the door (yes/no)? ").lower()
        if decision == "yes":
            print("You cautiously open the door.")
            print("As you open the door, you see someone hanging from the ceiling. It's a ghostly apparition!")
            print("Terrified, you quickly shut the door.")
            
            # Add code here for what happens when you see the ghost
            
            print("You decide to explore the cabin further. In one corner, you find a large wardrobe.")
            open_wardrobe = input("Do you want to open the wardrobe? Yes or No? ").lower()
            if open_wardrobe == "yes":
                print("You open the wardrobe and find a dusty, old book inside.")
                print("You open the book and discover a glowing mantra that says, 'Its me, Hi! I am the problem its me.'")
                print("The words shimmer and stay imprinted in your mind. You close the book.")
                print("Suddenly, you hear thundering and shattering noises, along with distant screams echoing through the cabin.")
                print("You sense an ominous presence. What do you do?")
                
                # User must type the mantra correctly to proceed
                enchant_mantra = input("Type the mantra to enchant it: ")
                if enchant_mantra.lower() == "its me, hi! i am the problem its me":
                    print("As you chant the mantra, the disturbances in the cabin subside.")
                    print("A divine voice echoes, 'You are worthy.' The door before you opens, revealing a new path.")
                else:
                    print("Your attempt to chant the mantra goes awry. The disturbances intensify.")
                    print("You must try again or face the consequences.")
            else:
                print("You decide not to open the wardrobe and continue exploring the cabin, hearing more thundering and shattering.")
                print("The ghostly presence seems to grow stronger.")
        else:
            print("You decide not to open the door and stay inside.")
            print("Suddenly, the lights start flickering, casting eerie shadows in the cabin.")
            print("You feel an ominous presence in the room. What do you do?")
            
            # User must type the mantra correctly to proceed
            enchant_mantra = input("Type the mantra to enchant it: ")
            if enchant_mantra.lower() == "its me, hi! i am the problem its me":
                print("As you chant the mantra, the disturbances in the cabin subside.")
                print("A divine voice echoes, 'You are worthy.' The door before you opens, revealing a new path.")
            else:
                print("Your attempt to chant the mantra goes awry. The disturbances intensify.")
                print("You must try again or face the consequences.")
        
    elif choice == "2":
        print("You choose to visit the adventure park, a place known for its thrilling rides and hidden surprises. As you wander through the park, you come across a peculiar statue of a mythical creature. At its feet, there's a small, dusty tome.")
        
        open_book = input("Do you want to open the book? Yes or No? ")
        
        if open_book.lower() == "yes":
            print("You open the dusty tome and find that it contains riddles and challenges that lead to a hidden treasure within the park. The adventure has only just begun...")
        else:
            print("You decide not to open the book and continue exploring the park's attractions, wondering if there are more secrets to uncover.")

    else:
        print("You didn't choose a valid option. The adventure ends here.")
else:
    print("The enigma remains unsolved as you choose not to embark on this mysterious journey. Perhaps another time...")
