screen cameraOptions:
    imagemap:
        ground "images/camera.png" align (.60,.99)
        #hotspot (501, 110, 68, 53) clicked Show("inventory_screen")

screen inventory_button:
    textbutton "Show Inventory" action [ Show("inventory_screen"), Hide("inventory_button")] align (.95,.04)

screen map_button:
    textbutton "Show Map" action [ Show("map_screen"), Hide("map_button")] align (.95,.15)

screen inventory_screen:
    modal True

    hbox align (.95,.04) spacing 20:
        textbutton "Close Inventory" action [ Show("inventory_button"), Hide("inventory_screen")]
    $ x = 515 # coordinates of the top left item position
    $ y = 25
    $ i = 0

    for item in inventory.items:
        $ pic = item.image
        $ my_tooltip = "tooltip_inventory_" + pic.replace("gui/inv_", "").replace(".png", "") # we use tooltips to describe what the item does.
        imagebutton idle pic hover pic xpos x ypos y action [Hide("gui_tooltip"), Show("inventory_button"), SetVariable("item", item), Hide("inventory_screen"), item_use] hovered Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=693) unhovered [Hide("gui_tooltip")]
    $ i += 1
    if len(inventory.items)>9:
        textbutton _("Next Page") action [SetVariable('inv_page', next_inv_page), Show("inventory_screen")] xpos .475 ypos .83

screen gui_tooltip (my_picture="", my_tt_xpos=58, my_tt_ypos=687):
    add my_picture xpos my_tt_xpos ypos my_tt_ypos

screen map_screen:
    modal True

    hbox align (.95,.15) spacing 20:
        textbutton "Close Map" action [ Show("map_button"), Hide("map_screen")]

    #add im.FactorScale("gui/HouseMap.png", 0.4)

    imagemap:
        ground "images/house_map.png"
        hotspot (36, 24, 522, 239) clicked [ Hide("map_screen"), Show("map_button"), Show("office_screen") ]
        hotspot (562, 25, 274, 143) clicked [ Show("bathroom_screen"), Hide("map_screen"), Show("map_button") ]
        hotspot (845, 24, 275, 412) clicked [ Show("living_screen"), Hide("map_screen"), Show("map_button") ]
        hotspot (841, 440, 280, 159) clicked [ Show("security_screen"), Hide("map_screen"), Show("map_button") ]
        hotspot (36, 269, 805, 330) clicked [ Show("main_screen"), Hide("map_screen"), Show("map_button") ]

    # imagebutton:
    #     idle "gui/bedroom.png" 
    #     hover "gui/bedroom_hovered.png" action Show("room_tooltip", my_picture="Bedroom") unhovered [Hide("room_tooltip")]
    #     clicked Jump("bedroom")

    # imagebutton:
    #     align (.95,.15)
    #     idle "gui/bedroom.png" 
    #     hover "gui/bedroom_hovered.png" action Show("room_tooltip", my_picture="Bedroom") unhovered [Hide("room_tooltip")]
    #     clicked Jump("bedroom")

screen room_tooltip (my_picture="", my_tt_xpos=58, my_tt_ypos=687):
    text my_picture xpos my_tt_xpos ypos my_tt_ypos

screen office_screen:
    if office.locked == False:
        add "images/office_screen.jpg"
        text "This is the office"
    elif office.locked == True and officeKey in inventory.items:
        text "You unlocked the door"
        add "images/office_screen.jpg"
        #inventory.drop(officeKey)
    else:
        text "Locked"
