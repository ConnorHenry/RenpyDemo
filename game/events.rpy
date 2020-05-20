init python:
    item = None
    class Player(object):
        def __init__(self, name, max_hp=0, max_mp=0, element=None):
            self.name=name
            self.max_hp=max_hp
            self.hp=max_hp
            self.max_mp=max_mp
            self.mp=max_mp
            self.element=element

    class NPC(object):
        def __init__(self, name, trust, image="", maxTrust=100):
            self.name = name
            self.trust = trust
            self.image = image
            self.maxTrust = maxTrust

        def handleTrust(self, incomingTrust):
            if self.trust + incomingTrust > 100:
                self.trust = 100
            elif self.trust + incomingTrust < 0:
                self.trust = 0
            else:
                self.trust += incomingTrust


    class Item(object):
        def __init__(self, name, player=None, hp=0, mp=0, element="", image="", cost=0):
            self.name = name
            self.player = player # which character can use this item?e
            self.hp = hp # does this item restore hp?
            self.mp = mp # does this item restore mp?
            self.element = element # does this item change elemental damage?
            self.image = image # image file to use for this item
            self.cost = cost # how much does it cost in shops?
        def use(self): #here we define what should happen when we use the item
            if self.hp>0: #healing item
                player.hp = player.hp+self.hp
                if player.hp > player.max_hp: # can't heal beyond max HP
                    player.hp = player.max_hp
                inventory.drop(self) # consumable item - drop after use
            elif self.mp>0: #mp restore item
                player.mp = player.mp+self.mp
                if player.mp > player.max_mp: # can't increase MP beyond max MP
                    player.mp = player.max_mp
                inventory.drop(self) # consumable item - drop after use
            else:
                player.element = self.element #item to change elemental damage; we don't drop it, since it's not a consumable item

    class Inventory(store.object):
        def __init__(self, money=10, itemNumber=0, maxSpace=5):
            self.itemNumber = itemNumber
            self.money = money
            self.items = []
            self.maxSpace = maxSpace
        def add(self, item): # a simple method that adds an item; we could also add conditions here (like check if there is space in the inventory)
            if self.itemNumber<self.maxSpace:
                self.itemNumber+=1
                self.items.append(item)
        def drop(self, item):
            self.itemNumber-=1
            self.items.remove(item)
        def buy(self, item):
            if self.money >= item.cost:
                self.items.append(item)
                self.money -= item.cost

    def item_use():
        item.use()

    def isFriendly(character):
        if character.trust<30:
            return False
        elif character.trust>70:
            return True

    #Tooltips:
    style.tips_top = Style(style.default)
    #style.title.font="gui/arial.ttf"
    style.tips_top.size=14
    style.tips_top.color="fff"
    style.tips_top.outlines=[(3, "6b7eef", 0,0)]
    style.tips_top.kerning = 5

    style.tips_bottom = Style(style.tips_top)
    style.tips_top.size=20
    style.tips_bottom.outlines=[(0, "6b7eef", 1, 1), (0, "6b7eef", 2, 2)]
    style.tips_bottom.kerning = 2

    style.button.background=Frame("gui/frame.png",25,25)
    style.button.yminimum=52
    style.button.xminimum=52
    style.button_text.color="000"


    showitems = True #turn True to debug the inventory
    # def display_items_overlay():
    #     if showitems:
    #         inventory_show = "Money:" + str(inventory.money) + " HP: " + str(player.hp) + " bullets: " + str(player.mp) + " element: " + str(player.element) + "\nInventory: "
    #         for i in range(0, len(inventory.items)):
    #             item_name = inventory.items[i].name
    #             if i > 0:
    #                 inventory_show += ", "
    #             inventory_show += item_name
    #
    #         ui.frame()
    #         ui.text(inventory_show, color="#000")
    # config.overlay_functions.append(display_items_overlay)
