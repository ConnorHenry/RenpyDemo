
define e = Character("Hero")

image character1 = im.FactorScale("images/character.jpg", 0.5)
image scene1 = "images/interrogation_room_background.jpg"
image bedroomScene = "gui/bedroomBackground.jpg"
image officeScene = "images/office_screen.jpg"

label start:
    python:
        player = Player("Derp", 0)
        npc1 = NPC("Friendly", 80, image="images/character.jpg")
        officeKey = Item("officeKey", image="gui/key.jpg")
        inventory = Inventory()
        inventory.add(officeKey)
        office = Room("Office", True)

    scene scene1 with dissolve
    show screen inventory_button
    show screen map_button

    # # play music "audio/ES_Pyramid.mp3"
    show character1 at left

    pause
    
    e "Hellooo."

    $ povname = renpy.input("What is your name?")
    $ player.name = povname.strip()

    e "Hellooo [player.name]."

    # show officeKey.image

    # e "I am currently your friend"
    # e "My trust value to you is [npc1.trust]"
   
    # menu:
    #     "Do something suspicious":
    #         $ npc1.handleTrust(-60)
    #         jump option1
    #     "Do something casual":
    #         $ npc1.handleTrust(10)
    #         jump option2

    # label option1:
    #     "Hmmmm odd.."
    #     jump nextScreen
    # label option2:
    #     "Nothing unusual here.."
    #     jump nextScreen

    # label nextScreen:
    #     e "My trust value to you is [npc1.trust]"
    #     e "Are we friends?"
    #     if isFriendly(npc1) == True:
    #         e "Yes"
    #     elif isFriendly(npc1) == False:
    #         e "No"
        
    label office:
        if office.locked == False:
            add "images/office_screen.jpg"
            text "This is the office"
        elif office.locked == True and officeKey in inventory.items:
            text "You unlocked the door"
            #inventory.drop(officeKey)
        else:
            e "Locked"

    return
