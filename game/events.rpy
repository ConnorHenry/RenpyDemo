init python:
    import json
    import math
    
    x =  '{ "name":"John", "age":30, "city":"New York"}'
    y = json.loads(x)
    print(y["age"])

    item = None
    class Player(object):
        def __init__(self, name, anxious, maxAnxious=10):
            self.name = name
            self.anxious = anxious

        def handleAnxious(self, incomingAnxious):
            if self.anxious + incomingAnxious > 10:
                self.anxious = 10
            elif self.anxious + incomingAnxious < 0:
                self.anxious = 0
            else:
                self.anxious += incomingAnxious

    class NoteBook(object):
        def __init__(self, name, notes, newNote):
            self.name = name
            self.notes = []
            self.newNote = newNote

        def addNote(self, note): 
            self.items.notes(note)


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
        def __init__(self, name, image=""):
            self.name = name
            self.image = image 

    class Inventory(store.object):
        def __init__(self, money=10, itemNumber=0, maxSpace=5):
            self.itemNumber = itemNumber
            self.money = money
            self.items = []
            self.maxSpace = maxSpace
        def add(self, item): 
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

    class Room(object):
        def __init__(self, name, locked, background=""):
            self.name = name
            self.locked = locked

        def unlock(self):
            self.locked = False

    class Question():
        def __init__(self, id, question, possibleAnswers, correctAnswer):
            self.id = id
            self.question = question
            self.possibleAnswers = possibleAnswers
            self.correctAnswer = correctAnswer

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

    class Shaker(object):
    
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }
    
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child
            
        def __call__(self, t, sizes):
            # Float to integer... turns floating point numbers to
            # integers.                
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor
            
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

            return (int(nx), int(ny), 0, 0)
    
    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)
    
        return renpy.display.layout.Motion(move,
                        time,
                        child,
                        add_sizes=True,
                        **properties)

    Shake = renpy.curry(_Shake)

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
