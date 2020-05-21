
define e = Character("Hero")

image character1 = im.FactorScale("images/character.jpg", 0.5)
image scene1 = "images/interrogation_room_background.jpg"
image bedroomScene = "gui/bedroomBackground.jpg"

label start:
    python:
        player = Player("Derp", 100, 50)
        npc1 = NPC("Friendly", 80, image="images/character.jpg")
        player.hp = 50
        player.mp = 10
        chocolate = Item("Chocolate", hp=40, image="gui/window_icon.png")
        banana = Item("Banana", mp=20, image="gui/window_icon.png")
        gun = Item("Gun", element="bullets", image="gui/window_icon.png", cost=7)
        laser = Item("Laser Gun", element="laser", image="gui/window_icon.png")
        inventory = Inventory()
        #add items to the initial inventory:
        inventory.add(chocolate)
        inventory.add(chocolate)
        inventory.add(banana)

    scene scene1 with dissolve
    show screen inventory_button
    show screen map_button
    show screen cameraOptions

    # # play music "audio/ES_Pyramid.mp3"
    show character1 at left
    pause
    
    e "Hellooo."
    e "I am currently your friend"
    e "My trust value to you is [npc1.trust]"
   
    menu:
        "Do something suspicious":
            $ npc1.handleTrust(-60)
            jump option1
        "Do something casual":
            $ npc1.handleTrust(10)
            jump option2

    label option1:
        "Hmmmm odd.."
        jump nextScreen
    label option2:
        "Nothing unusual here.."
        jump nextScreen

    label nextScreen:
        e "My trust value to you is [npc1.trust]"
        e "Are we friends?"
        if isFriendly(npc1) == True:
            e "Yes"
        elif isFriendly(npc1) == False:
            e "No"
        
    label bedroom:
        scene bedroomScene
        "This is the bedroom"

    return
