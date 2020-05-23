
define hero = Character("Hero")
define guard = Character("Guard")

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
        player = Player("Derp", 3)
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

    guard "Where was it you studied?"

    menu:
        "University of Moscow":
            jump moscow
        "Coleraine Tech":
            jump tech
        "Harvard":
            jump harvard

    label moscow:
        $ player.handleAnxious(+1)
        guard "Oh really? You dont sound Russian?"
        jump question2

    label tech:
        $ player.handleAnxious(-1)
        guard "Oh yeah my brother got his Level 2 BTEC from there"
        jump question2

    label harvard:
        $ player.handleAnxious(+1)
        guard "You...?"
        jump question2

    label question2:
        $ word_effect("time did")
        guard "What {image=word_effect} you get here?"


    #$ povname = renpy.input("What is your name?")
    #$ player.name = povname.strip()

    #e "Hellooo [player.name]."

    # show officeKey.image
    
    $ word_effect("Appointment")
    guard "Hello, i need to make {image=word_effect}, can you help me?"
   
    menu:
        "Do something suspicious":
            $ npc1.handleTrust(-60)
            jump option1
        "Do something casual":
            $ npc1.handleTrust(10)
            jump option2
    
    # e "{size=+10}Bigger{/size} {size=-10}Smaller{/size} {size=24}24 px{/size}."
    guard "Hello, i need to make {image=word_effect}, can you help me?"
    # $ the_word = "Really?"
    # e "{image=word_effect}"
    # e "Hellooo."

    label option1:    
        $ word_effect("Odd...")
        guard "{image=word_effect}"
        jump nextScreen
    label option2:
        guard "Nothing unusual here.."
        jump nextScreen

    label nextScreen:
        guard "My trust value to you is [npc1.trust]"
        guard "Are we friends?"
        if isFriendly(npc1) == True:
            guard "Yes"
        elif isFriendly(npc1) == False:
            guard "No"
        
    label office:
        if office.locked == False:
            add "images/office_screen.jpg"
            text "This is the office"
        elif office.locked == True and officeKey in inventory.items:
            $ inventory.drop(officeKey)
            guard "You unlocked the door"
        else:
            guard "Locked"

    return
