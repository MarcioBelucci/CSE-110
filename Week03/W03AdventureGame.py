#I added 3 initial scenarios, each of which contains multiple choices and unique possible ends.
#I showed the game to my family, and they played and had fun. One point that they highlighted was the message for wrong writing. 
print("One rainy afternoon, you and your cousins are exploring Grandpa's attic when you discover a dusty wooden box hidden behind some old books.\nInside the box, there is a strange map showing several places around town with tiny drawings beside them: a bridge, a windmill, and a giant tree.")
print('A note attached to the map says:\n\n"Only the brave will find the treasure."\n\nExcited by the mystery, you decide to begin the adventure immediately.')

first_choice = input("\nNow you need to choose what is the next step. Which path: BRIDGE, WINDMILL or TREE ? ").lower()

#FIRST SCENARIO
if first_choice == "bridge":
    brigde_first = input("Under the bridge, you find a loose brick. Behind it is a tiny metal key tied to a blue ribbon. Aside of it, you see some muddy footprints. What is the next step: KEY or FOOTPRINTS? ").lower()
    #SECOND SCENARIO
    if brigde_first == "key":
        metal_key = input('You search around the bridge and discover a tiny locked wooden case hidden under the rocks. The key fits perfectly inside. Inside the wooden case, you discover a tiny music box that still works when opened. A small note inside says:\n\n"Follow the melody".\n\nYou can listen the music or visit the old music shop. Which is the next step: MUSIC or SHOP? ').lower()
        #THIRD SCENARIO
        if metal_key == "music":
            print("You listen closely to the melody and recognize it as Grandpa's favorite childhood song. Back at home, Grandpa smiles when he hears you humming it and reveals a hidden drawer filled with family souvenirs and funny stories from his childhood.\n\nTHE END")
        #THIRD SCENARIO
        elif metal_key == "shop":
            print('At the music shop, the owner recognizes the music box immediately and hands you a sealed envelope Grandpa left there many years ago.\nInside is a coupon for free ice cream for the whole family and a note:\n\n"Every adventure deserves a celebration."\n\nTHE END')
        else:
            print("ERROR: Please verify if you wrote correct! Try again.")

    #SECOND SCENARIO
    elif brigde_first == "footprints":
        footprints = input("You follow the muddy footprints along the riverbank. They lead to a small boat with another piece of the treasure map hidden under a seat. The extra piece of the map reveals a drawing of a red flag near the harbor. You can choose to go to the harbor or search the small boat more carefully. Which is the next step: HARBOR or BOAT? ").lower()
        #THIRD SCENARIO
        if footprints == "harbor":
            print("At the harbor, you spot a red flag waving beside an old fishing shack. Hidden inside is a wooden chest filled with board games, comic books, and snacks Grandpa saved for rainy days.\nYour cousins immediately start playing together by the water.\n\nTHE END")
        #THIRD SCENARIO
        elif footprints == "boat":
            print("You continue searching the small boat and discover a hidden compartment beneath the floorboards. Inside is an old camera containing photos of Grandpa's childhood adventures around town.\nOn the final photo, someone wrote:\n\n'The best adventures are shared.'\n\nThat night, your whole family gathers to look through the photographs together.\n\nTHE END")
        else:
            print("ERROR: Please verify if you wrote correct! Try again.")
    else:
        print("ERROR: Please verify if you wrote correct! Try again.")
#FIRST SCENARIO
elif first_choice == "windmill":
    windmill = input("The windmill creaks slowly as it turns in the breeze. Inside, you discover strange marks painted on the floor that seem to point somewhere else, also you noted that have something red on the top of the building. What is the next step: MARKS or CLIMB? ").lower()
    #SECOND SCENARIO
    if windmill == "marks":
        marks = input("You follow the strange painted marks across the floor. They form arrows leading toward a hidden trapdoor beneath a dusty carpet.\nInside the compartment, you discover a spinning wooden disc covered in symbols.\nYou can choose to spin the woodem disc or try to match the symbols with the map. Which is the next step: SPIN or MATCH? ").lower()
        #THIRD SCENARIO
        if marks == "spin":
            print('You spin the wooden disc carefully. When it stops, part of the windmill wall slides open, revealing a tiny room filled with colorful kites Grandpa used to fly as a child.\nAttached to one kite is a note:\n\n"The wind always carries adventure."\n\nYour family spends the afternoon flying kites together outside the windmill.\n\nTHE END')
        #THIRD SCENARIO
        elif marks == "match":
            print("You compare the symbols on the disc with the treasure map. One symbol matches a drawing near the center perfectly.\nPressing it causes a small drawer to pop open. Inside are Grandpa's old puzzle games and brain teasers wrapped neatly in cloth.\nYour cousins immediately begin trying to solve them together.\n\nTHE END")
        else:
            print("ERROR: Please verify if you wrote correct! Try again.")
    #SECOND SCENARIO
    elif windmill == "climb":
        climb = input("You carefully climb the narrow stairs to the top of the windmill. Tied near the turning blades is a bright red cloth waving in the wind.\nWrapped inside the cloth is a small brass tube containing a rolled message.\nYou can choose to open the brass tube immediately OR look around from the top of the windmill first. Which is the next step: OPEN or TOP? ").lower()
        #THIRD SCENARIO
        if climb == "open":
            print('You unroll the message carefully. It contains a hand-drawn "Adventure Certificate" signed by Grandpa for whoever completed the treasure hunt.\nAt the bottom, it says:\n\n"Official Explorer of the Family."\n\nEveryone cheers as you proudly show the certificate.\n\nTHE END')
        #THIRD SCENARIO
        elif climb == "top":
            print("From the top of the windmill, you notice colorful ribbons hanging from trees all across town, marking places Grandpa once visited as a child.\nYour family decides to spend the summer visiting every location together and creating brand-new memories.\n\nTHE END")
    else:
        print("ERROR: Please verify if you wrote correct! Try again.")
#FIRST SCENARIO
elif first_choice == "tree":
    tree  = input('When you reach the giant tree, you notice a small hole in the trunk glowing faintly inside. Reaching your hand carefully into the opening, you find an old golden coin with the same symbol drawn on the map.\nAs you inspect it, you realize the coin has letters carved around the edges:\n\n"Look where water meets stone." \n\nYou can clean the coin and reveal more hidden letter or symbols, or follow the clue. What is the next step: CLEAN or FOLLOW? ').lower()
    #SECOND SCENARIO
    if tree == "clean":
        clean = input("You carefully wipe the dirt from the golden coin. As the mud disappears, strange markings begin to appear around the edges.\nIn the center, a hidden message slowly becomes readable:\n\n“Turn the silent eye to reveal the path.”\n\nYou suddenly remember the old stone statue in the town square that everyone calls “The Silent Eye.”\n\nNow you can go to the statue or study more carrefully the coin. Which is the next step: STATUE or STUDY? ").lower()
        #THIRD SCENARIO
        if clean == "statue":
            print("You hurry to the town square and stand before “The Silent Eye” statue. After examining it closely, you notice the eye of the statue can actually rotate.\nAs you turn it, part of the statue's base slides open, revealing a tiny hidden compartment. Inside is Grandpa's final note:\n\n“Curiosity will always lead you to adventure.”\n\nBeneath the note, you find a small silver medal shaped like a compass.\n\nTHE END")

        #THIRD SCENARIO
        elif clean == "study":
            print("You continue examining the golden coin carefully. Holding it toward the light, you notice tiny holes forming a hidden pattern.\nThe pattern matches the map exactly and reveals an X marked behind Grandpa's bookshelf in the attic. Rushing back upstairs, you discover a hidden wooden box containing old family photos, rare coins, and a letter from Grandpa.\nThe letter says:\n\n“The greatest treasure is the memories we create together.”\n\nTHE END")
        else:
            print("ERROR: Please verify if you wrote correct! Try again.")

    #SECOND SCENARIO
    elif tree == "follow":
        follow = input("You leave the tree behind and head toward the river, searching for the place “where water meets stone.” After walking for several minutes, you discover a large black rock beside the flowing water.\nSomething shiny is stuck between the stones underneath it.\nYou can choose to dig the shiny thing or to look around before to interact with it. Which is the next step: DIG or LOOK? ").lower()
        #THIRD SCENARIO
        if follow == "dig":
            print("You dig carefully around the stones using a small stick. After a few minutes, you uncover a rusty metal box buried in the dirt.\nInside are dozens of old arcade tokens, a faded photo of Grandpa with his cousins, and a note that says:\n\n“Some treasures are memories waiting to be rediscovered.”\n\nThat evening, your family decides to visit the old arcade downtown together.\n\nTHE END")

        #THIRD SCENARIO
        elif follow == "look":
            print("You kneel beside the black rock and inspect the shiny object closely before touching it. It turns out to be a polished mirror reflecting sunlight toward the trees nearby.\nFollowing the reflection, you discover a hidden wooden bench with Grandpa's initials carved into it. Taped underneath is a small envelope filled with funny riddles and family challenges for everyone to play together.\nThe adventure turns into a night full of games and laughter.\n\nTHE END")
        else:
            print("ERROR: Please verify if you wrote correct! Try again.")

    else:
        print("ERROR: Please verify if you wrote correct! Try again.")
else:
    print("ERROR: Please verify if you wrote correct! Try again.")