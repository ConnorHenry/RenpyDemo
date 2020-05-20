
define e = Character("Hero")
default i = 0

image character1 = im.FactorScale("images/character.jpg", 0.5)
image scene1 = im.FactorScale(im.Grayscale("images/interrogation_room_background.jpg"), 1.3)

label start:
    python:
        player = Player("Derp", 100, 50)
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

    # $ inventory = Inventory()
    # # show screen Inventory
    #
    scene scene1 with dissolve
    show screen inventory_button

    # # play music "audio/ES_Pyramid.mp3"
    show character1 at left
    # pause
    # # $ y = renpy.input("Who am i?")
    # # e "[coins]"
    pause
    #
    e "This is our first line."
    #
    # pause
    #
    # #e "[coins]"
    #
    # menu:
    #     "Shoot him":
    #         $ choice1 = "1"
    #         jump option1
    #     "Spare him":
    #         $ choice1 = "2"
    #         jump option2
    #
    # label option1:
    #     $ killed = True
    #     hide character
    #     "You monster"
    #     jump secondChoice
    # label option2:
    #     "You hero"
    #     jump secondChoice
    #
    # label secondChoice:
    #     if choice1 == "1":
    #         "Bad Ending"
    #     if choice1 == "2":
    #         "Good Ending"
    #
    # pause


    return
