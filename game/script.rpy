
define hero = Character("Hero")
define guard = Character("Guard")

image character1 = im.FactorScale("images/character.jpg", 0.5)
image scene1 = "images/interrogation_room_background.jpg"
image bedroomScene = "gui/bedroomBackground.jpg"
image officeScene = "images/office_screen.jpg"


# Text Tags
# alpha
# 
# 
# 
# 

init python:
    
    txt1 = ""
    txt2 = ""
    txt3 = ""
    
    def word_effect(txt, textTag):
        global txt1, txt2, txt3
        txt1 = txt
        txt2 = ""
        txt3 = ""
        i = 2
        for letter in txt:
            i += 1
            if i % 2 == 0:
                txt2 += letter
                txt3 += "{"+textTag+"=-" + str(player.anxious) + "}" + letter + "{/"+textTag+"}"
            else:
                txt2 += "{"+textTag+"=-" + str(player.anxious) + "}" + letter + "{/"+textTag+"}"
                txt3 += letter    

    def word_effect2(txt, textTag):
        global txt4, txt5, txt6
        txt4 = txt
        txt5 = ""
        txt6 = ""
        i = 2
        for letter in txt:
            i += 1
            if i % 2 == 0:
                txt5 += letter
                txt6 += "{"+textTag+"=-" + str(player.anxious) + "}" + letter + "{/"+textTag+"}"
            else:
                txt5 += "{"+textTag+"=-" + str(player.anxious) + "}" + letter + "{/"+textTag+"}"
                txt6 += letter

image word_effect:
    ui.text("[txt2]")
    pause .2
    ui.text("[txt3]")
    pause .2
    repeat

image word_effect2:
    Text("[txt5]")
    pause .2
    Text("[txt6]")
    pause .2
    repeat

label start:
    python:
        player = Player("Derp", 8)
        npc1 = NPC("Friendly", 80, image="images/character.jpg")
        officeKey = Item("officeKey", image="gui/key.jpg")
        inventory = Inventory()
        inventory.add(officeKey)
        office = Room("Office", True)

        timeout = player.anxious

    scene scene1 with dissolve
    show screen inventory_button
    show screen map_button
    show screen notebook_button

    # # play music "audio/ES_Pyramid.mp3"
    show character1 at left

    pause

    guard "Where was it you studied?"

    $ timeout_label = "question2"
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
        $ word_effect("time did", "size")
        $ word_effect2("get here", "i")
        guard "What {image=word_effect} you {image=word_effect2}?"


    #$ povname = renpy.input("What is your name?")
    #$ player.name = povname.strip()

    $ timeout_label = "nextScreen"   
    menu:
        "Do something suspicious":
            $ npc1.handleTrust(-60)
            jump option1
        "Do something casual":
            $ npc1.handleTrust(10)
            jump option2
    
    guard "Hello, i need to make {image=word_effect}, can you help me?"

    label option1:    
        $ word_effect("Odd...", "size")
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
