
define e = Character("Hero")

image character1 = im.FactorScale("images/character.jpg", 0.5)
image scene1 = "images/interrogation_room_background.jpg"
image bedroomScene = "gui/bedroomBackground.jpg"
image officeScene = "images/office_screen.jpg"

init python:
    
    txt1 = ""
    txt2 = ""
    txt3 = ""
    
    def word_effect(txt):
        global txt1, txt2, txt3
        txt1 = txt
        txt2 = ""
        txt3 = ""
        i = 2
        for letter in txt:
            i += 1
            if i % 2 == 0:
                txt2 += letter
                txt3 += "{size=-" + str(player.anxious) + "}" + letter + "{/size}"
            else:
                txt2 += "{size=-" + str(player.anxious) + "}" + letter + "{/size}"
                txt3 += letter

image word_effect:
    Text("[txt2]")
    pause .2
    Text("[txt3]")
    pause .2
    repeat

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

    #$ povname = renpy.input("What is your name?")
    #$ player.name = povname.strip()

    #e "Hellooo [player.name]."

    # show officeKey.image

    e "I am currently your friend"
    e "My trust value to you is [npc1.trust]"
    
    $ word_effect("Appointment")
    e "Hello, i need to make {image=word_effect}, can you help me?"
   
    menu:
        "Do something suspicious":
            $ npc1.handleTrust(-60)
            jump option1
        "Do something casual":
            $ npc1.handleTrust(10)
            jump option2
    
    # e "{size=+10}Bigger{/size} {size=-10}Smaller{/size} {size=24}24 px{/size}."
    e "Hello, i need to make {image=word_effect}, can you help me?"
    # $ the_word = "Really?"
    # e "{image=word_effect}"
    # e "Hellooo."

    label option1:    
        $ word_effect("Odd...")
        e "{image=word_effect}"
        jump nextScreen
    label option2:
        e "Nothing unusual here.."
        jump nextScreen

    label nextScreen:
        e "My trust value to you is [npc1.trust]"
        e "Are we friends?"
        if isFriendly(npc1) == True:
            e "Yes"
        elif isFriendly(npc1) == False:
            e "No"
        
    label office:
        if office.locked == False:
            add "images/office_screen.jpg"
            text "This is the office"
        elif office.locked == True and officeKey in inventory.items:
            $ inventory.drop(officeKey)
            e "You unlocked the door"
        else:
            e "Locked"

    return
