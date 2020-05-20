
screen inventory_button:
    textbutton "Show Inventory" action [ Show("inventory_screen"), Hide("inventory_button")] align (.95,.04)

screen inventory_screen:
    modal True

    hbox align (.95,.04) spacing 20:
        textbutton "Close Inventory" action [ Show("inventory_button"), Hide("inventory_screen")]
    $ x = 515 # coordinates of the top left item position
    $ y = 25
    $ i = 0
    text str(inventory.itemNumber)

    for item in inventory.items:
        $ pic = item.image
        $ my_tooltip = "tooltip_inventory_" + pic.replace("gui/inv_", "").replace(".png", "") # we use tooltips to describe what the item does.
        imagebutton idle pic hover pic xpos x ypos y action [Hide("gui_tooltip"), Show("inventory_button"), SetVariable("item", item), Hide("inventory_screen"), item_use] hovered Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=693) unhovered [Hide("gui_tooltip")]
        if player.element and (player.element==item.element): #indicate the selected gun
            add "gui/selected.png" xpos x ypos y anchor(.5,.5)
    $ i += 1
    if len(inventory.items)>9:
        textbutton _("Next Page") action [SetVariable('inv_page', next_inv_page), Show("inventory_screen")] xpos .475 ypos .83

screen gui_tooltip (my_picture="", my_tt_xpos=58, my_tt_ypos=687):
    add my_picture xpos my_tt_xpos ypos my_tt_ypos
