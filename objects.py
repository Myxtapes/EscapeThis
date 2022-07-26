from EscapeThis import *
import time
import os, subprocess
import random
import rich
from rich.console import Console

start = False

console = Console(width=80)
console = Console(style = "bold green")

console.print(

'\n\n###################################################\n\n\n\n                    ESCAPE THIS!          \n\n                THE WONDER EDITION        \n\n\n\n\n                  by Myxtapes 2022        \n\n\n###################################################')     

time.sleep(2)

console.print('\n')

yourName = input("Please input your name: ")

console.print("\nWelcome to Escape This! The Wonder Edition. Your task is to escape from the room. To play, simply type in the commands you would like to execute, followed by the object you would like to interact with. Possible commands are: \n\nlook\nsearch\nwalk\nmove\nopen\nunlock\ntake\nread\npush/pull\nplay\nuse\n\nAt anytime, you can check this list of commands by typing 'commands'.\n\nIf you would like to check the current state of your inventory, type 'inventory'.\n")

while start == False:
     go = input("\nWhen you are ready to begin, type 'start': ")
     if 'start' in go:
        start = True
        continue
        
console.print("\nYou are in what looks to be some kind of study, comfortably furnished with a desk, a couch, bookshelves and other study-like furniture. You take particular note of the floor, less due to its rich, enviable hardwood, and more due to the rug that lies upon it. The rug, you notice, was designed in the style of a large compass.\n\nYou decide it would be wise to use the compass on the rug as a means to orient and navigate yourself around the room. In so doing, you see that you are standing in the north end of the room. If you would like to learn more specifically about the room, just say which direction you would like to look, using the compass as your guide. For example, if you would like to look at the north end of the room, type, 'look north', or, 'look at the north wall'.") 

playerLoc = ['north']
modelInventory = []
inventory = []
#inventory = [[modelInventory]]
failQuotes = ["\n\nThat didn't seem to work", "\n\nHmm...That didn't seem to accomplish anything.", "\n\nSurprisingly, nothing happens.", "\n\nNothing happens.", "\n\nNothing of note occurs.", "\n\nBupkis."]
bookmarkOne = 0
bookmarkTwo = 0
bookItems = ['a large, old-fashioned iron key']
boxItems = ['a box of matches', 'a medium sized steel key']
deskItems = ['Post-It notes of various colours', 'a laptop computer']
drawerItems = ['a small brass key', 'a small model of the Great Wall']
cabinetItems = ['a small model of Stonehenge']
safeItems = ['a small model of Chichen Itza']
hatchItems = ['a small model of Petra']
couchItems = ['a small model of the Eiffel Tower']
guessItItems = ['a small model of Machu Picchu']
shapesPuzzleItems = ['a small model of the Taj Mahal']
statueItems = ['a small model of the Great Pyramid']
recordCollection = ['Wish You were Here, by Pink Floyd', 'So Long and Thanks for All the Shoes, by NoFX', 'Greatest Hits, by Sonny and Cher', 'Radio, by L.L. Cool J', 'Play, by Moby', 'The 9th Symphony, by Ludwig van Beethoven']
globeSeen = ['true']
deskSeen = ['true']
pianoPlayed = ['false']
bookshelfOneItems = ['Famous Prison Cakes', 'The Music of Moby by R. Melville Hall', 'Scrambled Eggs for Breakfast, Lunch and Dinner']
bookshelfTwoItems = ['The Clock Echoes', 'Wonders of the World: Volume One', 'Wonders of the World: Volume Two']

def fail():
    console.print(random.choice(failQuotes))
    
#########################################################################################################
"""ITEM CLASSES"""
#########################################################################################################     

class Item():
    """base class for game items"""
    def __init__(self, name, desc, state, loc):
        self.name = name
        self.desc = desc
        self.state = state
        self.loc = loc

#########################################################################################################
"""ITEMS: WONDERS"""
#########################################################################################################         
class GreatWall(Item):
    def __init__(self):
        super().__init__(name = 'Great Wall model',
                         desc = "a small model of the Great Wall. Underneath the model, you notice a small black square has been attached.",
                         state = 'lost',
                         loc = 'southwest')
    def look(self):
        if self.state != 'lost':
            console.print('\nIt is ' + str(self.desc))
        else:
            fail() 

    def Take(self):
        global playerLoc
        if playerLoc == desk.loc and self.state == 'found' and 'a small model of the Great Wall' in drawerItems:
          console.print('\nYou take the model of the Great Wall')
          modelInventory.append('a small model of the Great Wall')
          drawerItems.remove('a small model of the Great Wall')
          self.state = 'owned'
        elif playerLoc != desk.loc and self.state == 'found' and 'a small model of the Great Wall' in drawerItems:
          console.print('\nYou walk to the desk and take the model of the Great Wall from the drawer')
          modelInventory.append('a small model of the Great Wall')
          drawerItems.remove('a small model of the Great Wall')
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail()             

class Stonehenge(Item):
    def __init__(self):
        super().__init__(name = 'Stonehenge model',
                         desc = "'a small model of Stonehenge. Underneath the model, you notice a small black square has been attached.",
                         state = 'lost',
                         loc = 'southwest')
    def look(self):
        if self.state != 'lost':
            console.print('\nIt is ' + str(self.desc))
        else:
            fail()   

    def Take(self):
        global playerLoc
        if playerLoc == filingCabinet.loc and self.state == 'found' and 'a small model of Stonehenge' in cabinetItems:
          console.print('\nYou take the model of Stonehenge')
          modelInventory.append('a small model of Stonehenge')
          cabinetItems.remove('a small model of Stonehenge')
          self.state = 'owned'
        elif playerLoc != filingCabinet.loc and self.state == 'found' and 'a small model of Stonehenge' in cabinetItems:
          console.print('\nYou walk to the filing cabinet and take the model of Stonehenge')
          modelInventory.append('a small model of Stonehenge')
          cabinetItems.remove('a small model of Stonehenge')
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail() 

class ChichenItza(Item):
    def __init__(self):
        super().__init__(name = 'Chichen Itza model',
                         desc = "'a small model of Chichen Itza. Underneath the model, you notice a small black square has been attached.",
                         state = 'lost',
                         loc = 'southwest')
    def look(self):
        if self.state != 'lost':
            console.print('/nIt is ' + str(self.desc))
        else:
            fail() 

    def Take(self):
        global playerLoc
        if playerLoc == wallSafe.loc and self.state == 'found' and 'a small model of Chichen Itza' in safeItems:
          console.print('\nYou take the model of Chichen Itza')
          modelInventory.append('a small model of Chichen Itza')
          safeItems.remove('a small model of Chichen Itza')
          self.state = 'owned'
        elif playerLoc != wallSafe.loc and self.state == 'found' and 'a small model of Chichen Itza' in safeItems:
          console.print('\nYou walk to the safe and take the model of Chichen Itza')
          modelInventory.append('a small model of Chichen Itza')
          safeItems.remove('a small model of Chichen Itza')
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail()                

class MachuPicchu(Item):
    def __init__(self):
        super().__init__(name = 'Machu Picchu model',
                         desc = "'a small model of Machu Picchu. Underneath the model, you notice a small black square has been attached.",
                         state = 'lost',
                         loc = 'west')
    def look(self):
        if self.state != 'lost':
            console.print('\nIt is ' + str(self.desc))
        else:
            fail()

    def Take(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'found' and 'a small model of Machu Picchu' in guessItItems:
          console.print('\nYou take the model of Machu Picchu')
          modelInventory.append('a small model of Machu Picchu')
          guessItItems.remove('a small model of Machu Picchu')
          self.state = 'owned'
        elif playerLoc != self.loc and self.state == 'found' and 'a small model of Machu Picchu' in guessItItems:
          console.print('\nYou walk to the painting of Saint Basils and take the model of Machu Picchu')
          modelInventory.append('a small model of Machu Picchu')
          guessItItems.remove('a small model of Machu Picchu')
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail()              

class TajMahal(Item):
    def __init__(self):
        super().__init__(name = 'Taj Mahal model',
                         desc = "'a small model of the Taj Mahal. Underneath the model, you notice a small black square has been attached.",
                         state = 'lost',
                         loc = 'north')
    def look(self):
        if self.state != 'lost':
            console.print('\nIt is ' + str(self.desc))
        else:
            fail()   

    def Take(self):
        global playerLoc
        if playerLoc == shapesPuzzle.loc and self.state == 'found' and 'a small model of the Taj Mahal' in shapesPuzzleItems:
          console.print('\nYou take the model of the Taj Mahal')
          modelInventory.append('a small model of the Taj Mahal')
          shapesPuzzleItems.remove('a small model of the Taj Mahal')
          self.state = 'owned'
        elif playerLoc != shapesPuzzle.loc and self.state == 'found' and 'a small model of the Taj Mahal' in shapesPuzzleItems:
          console.print('\nYou walk to the strange panel and take the model of the Taj Mahal')
          modelInventory.append('a small model of the Taj Mahal')
          shapesPuzzleItems.remove('a small model of the Taj Mahal')
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail()                                                            

class GreatPyramid(Item):
    def __init__(self):
        super().__init__(name = 'Great Pyramid model',
                         desc = "a small model of the Great Pyramid. Underneath the model, you notice a small black square has been attached",
                         state = 'lost',
                         loc = 'north')
    def look(self):
        if self.state != 'lost':
            console.print('\nIt is ' + str(self.desc))
        else:
            fail()   

    def Take(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'found' and 'a small model of the Great Pyramid' in statueItems:
          console.print('\nYou take the model of the Great Pyramid of Giza')
          modelInventory.append('a small model of the Great Pyramid')
          statueItems.remove('a small model of the Great Pyramid')
          self.state = 'owned'
        elif playerLoc != statue.loc and self.state == 'found' and 'a model of the Great Pyramid' in statueItems:
          console.print('\nYou walk to the statue and take the model of the Great Pyramid of Giza')
          modelInventory.append('a small model of the Great Pyramid')
          statueItems.remove('a small model of the Great Pyramid')
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail()                                                            

class EiffelTower(Item):
    def __init__(self):
        super().__init__(name = 'Eiffel Tower model',
                         desc = "a small model of the Eiffel Tower. Underneath the model, you notice a small black square has been attached.",
                         state = 'lost',
                         loc = 'northeast')
    def look(self):
        if self.state != 'lost':
            console.print('\nIt is ' + str(self.desc))
        else:
            fail()  

    def Take(self):
        global playerLoc
        if playerLoc == couch.loc and self.state == 'found' and 'a small model of the Eiffel Tower' in couchItems:
          console.print('\nYou take the model of the Eiffel Tower')
          modelInventory.append('a small model of the Eiffel Tower')
          couchItems.remove('a small model of the Eiffel Tower')
          self.state = 'owned'
        elif playerLoc != couch.loc and self.state == 'found' and 'a small model of the Eiffel Tower' in couchItems:
          console.print('\nYou walk to the couch and take the model of the Eiffel Tower')
          modelInventory.append('a small model of the Eiffel Tower')
          couchItems.remove('a small model of the Eiffel Tower')
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail()                                                           

class Petra(Item):
    def __init__(self):
        super().__init__(name = 'Petra model',
                         desc = "'a small model of Petra.",
                         state = 'lost',
                         loc = 'center')
    def look(self):
        if self.state != 'lost':
            console.print('\nIt is ' + str(self.desc))
        else:
            fail()  

    def Take(self):
        global playerLoc
        if playerLoc == hatch.loc and self.state == 'found' and 'a small model of Petra' in hatchItems:
          console.print('\nYou take the model of Petra')
          modelInventory.append('a small model of Petra')
          hatchItems.remove('a small model of Petra')
          self.state = 'owned'
        elif playerLoc != hatch.loc and self.state == 'found' and 'a small model of Petra' in hatchItems:
          console.print('\nYou walk to the hatch and take the model of Petra')
          modelInventory.append('a small model of Petra')
          hatchItems.remove('a small model of Petra')
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail()   

#########################################################################################################
"""ITEMS: DESK"""
######################################################################################################### 

class Pink_Post_Its(Item):
    def __init__(self):
        super().__init__(name = '4 pink Post-It notes',
                         desc = "4 pink Post-It notes with the letters, R and D written on one, S and S written on another, P and A written on the third, and W and O written on the fourth.",
                         state = 'found',
                         loc = 'southwest')
    def look(self):
      global playerLoc
      if playerLoc == self.loc and self.state == 'found':
          console.print('\nYou see: ' + str(self.desc))
      elif playerLoc == self.loc and self.state == 'owned':
          console.print('\nYou see: ' + str(self.desc)) 
      elif playerLoc != self.loc and self.state == 'found':
          console.print('\nYou walk over to the desk to get a better look at the Post-It notes. You see: ' + str(self.desc))                       
      else:
          fail()   

    def Take(self):
        if self.state == 'found' and self.name in deskItems:
          console.print('\nYou take the ' + str(self.name) + ' from the desk')
          inventory.append(self.name)
          deskItems.remove(self.name)
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail()                    
            
class Blue_Post_Its(Item):
    def __init__(self):
        super().__init__(name = '4 blue Post-It notes',
                         desc = "4 blue Post-It notes with the letters O and N written on one, Q and U written on another, T and I written on the third, and E and S written on the fourth.",
                         state = 'found',
                         loc = 'southwest')
    def look(self):
      global playerLoc
      if playerLoc == self.loc and self.state == 'found':
          console.print('\nYou see: ' + str(self.desc))
      elif playerLoc == self.loc and self.state == 'owned':
          console.print('\nYou see: ' + str(self.desc)) 
      elif playerLoc != self.loc and self.state == 'found':
          console.print('\nYou walk over to the desk to get a better look at the Post-It notes. you see: ' + str(self.desc))                       
      else:
          fail() 

    def Take(self):
        if self.state == 'found' and self.name in deskItems:
          console.print('\nYou take the ' + str(self.name) + ' from the desk')
          inventory.append(self.name)
          deskItems.remove(self.name)
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail()           

class Green_Post_Its(Item):
    def __init__(self):
        super().__init__(name = '1 green Post-It note',
                         desc = "a green Post-It note with the letters I and S written on it.",
                         state = 'found',
                         loc = 'southwest')
    def look(self):
      global playerLoc
      if playerLoc == self.loc and self.state == 'found':
          console.print('\nYou see: ' + str(self.desc))
      elif playerLoc == self.loc and self.state == 'owned':
          console.print('\nYou see: ' + str(self.desc)) 
      elif playerLoc != self.loc and self.state == 'found':
          console.print('\nYou walk over to the desk to get a better look at the Post-It notes. you see: ' + str(self.desc))                       
      else:
          fail() 

    def Take(self):
        if self.state == 'found' and self.name in deskItems:
          console.print('\nYou take the ' + str(self.name) + ' from the desk')
          inventory.append(self.name)
          deskItems.remove(self.name)
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail()            

class White_Post_Its(Item):
    def __init__(self):
        super().__init__(name = '1 white Post-It note',
                         desc = "a white Post-It note with the letters T, H and E written on it.",
                         state = 'found',
                         loc = 'southwest')
    def look(self):
      global playerLoc
      if playerLoc == self.loc and self.state == 'found':
          console.print('\nYou see: ' + str(self.desc))
      elif playerLoc == self.loc and self.state == 'owned':
          console.print('\nYou see: ' + str(self.desc)) 
      elif playerLoc != self.loc and self.state == 'found':
          console.print('\nYou walk over to the desk to get a better look at the post-it notes. you see: ' + str(self.desc))                       
      else:
          fail()

    def Take(self):
        if self.state == 'found' and self.name in deskItems:
          console.print('\nYou take the ' + str(self.name) + ' from the desk')
          inventory.append(self.name)
          deskItems.remove(self.name)
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail()             

class Paper_Clip(Item):
    def __init__(self):
        super().__init__(name = 'paper clips',
                         desc = "three paper clips",
                         state = 'lost',
                         loc = 'southwest')
    def look(self):
        if self.state != 'lost':
            console.print('you see ' + str(self.desc))
        else:
            fail()    

    def Take(self):
        if self.state == 'found' and self.name in deskItems:
          console.print('you take the ' + str(self.name) + ' from the desk')
          inventory.append(self.name)
          deskItems.remove(self.name)
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail()                                   

class Pencil(Item):
    def __init__(self):
        super().__init__(name = 'pencil and paper',
                         desc = 'a pencil and a few pages of blank white paper',
                         state = 'lost',
                         loc = 'southwest')
    def look(self):
        if self.state != 'lost':
            console.print('it is ' + str(self.desc))
        else:
            fail() 

    def Take(self):
        if self.state == 'found' and self.name in deskItems:
          console.print('you take the ' + str(self.name) + ' from the desk')
          inventory.append(self.name)
          deskItems.remove(self.name)
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail()   

class Computer(Item):
    def __init__(self):
        super().__init__(name = 'computer',
                         desc = "An old computer. On the screen you see the word 'Password: ' and an area in which, it seems, you are supposed to write a password.",
                         state = 'locked',
                         loc = 'southwest')
    def look(self):
        if playerLoc == self.loc and self.state == 'locked':
            console.print('\nIt is ' + str(self.desc))
        elif playerLoc != self.loc and self.state == 'locked':
            console.print('\nYou go to the desk to get a better look at the computer. it is ' + str(self.desc))
        elif playerLoc == self.loc and self.state == 'unlocked':
            console.print('\nThe computer screen is showing three two-digit numbers, each separated by a dash. The numbers are: 15, 25, and 35.')
        elif playerLoc != self.loc and self.state == 'unlocked':
            console.print('\nYou go to the desk to get a better look at the computer. The computer screen is showing three two-digit numbers, each separated by a dash. The numbers are: 15, 25, and 35.')
        else:
            fail() 

    def PasswordRight(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'locked':
            console.print("\nYou enter the word 'question' into the password box, hit enter, and to your delight, the screen refreshes to reveal three two-digit numbers, each separated by a dash. The numbers it reveals are: 15, 25, and 35.")
            self.state = 'unlocked'
        elif playerLoc != self.loc and self.state == 'locked': 
            console.print("\nYou walk to the computer and enter the word 'question', into the password box, hit enter, and to your delight, the screen refreshes to reveal three two-digit numbers, each separated by a dash. The numbers it reveals are: 15, 25, and 35.")
            self.state = 'unlocked'
            playerLoc = self.loc
        else:
            fail()                     

    def PasswordWrong(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'locked':
            console.print("\nYou enter your attempt, into the password box, hit enter, and to your disappointment, a message pops up on the screen that reads: 'Password incorrect. Please try again.'")
        elif playerLoc != self.loc and self.state == 'locked':
            console.print("\nYou enter your attempt into the password box, hit enter, and to your disappointment, a message pops up on the screen that reads: 'Password incorrect. Please try again.'") 
            playerLoc = self.loc 
        else:
            fail()  

    def Take(self):
        global playerLoc
        if playerLoc == self.loc:
            console.print('\nYou attempt to move the computer, but decide against it. Redecorating has never been your strong suit.')
        elif playerLoc != self.loc:
            console.print('\nYou walk to the desk to move the computer, but then decide against it. Redecorating has never been your strong suit.') 
            playerLoc = self.loc 
        else:
            fail()                 

#########################################################################################################
"""ITEMS: KEYS"""
#########################################################################################################                          
class SteelKey(Item):
    def __init__(self):
        super().__init__(name = 'steel key',
                         desc = "a medium sized steel key, with a hexagon on one side of the key head, and the number 1 on the other",
                         state = 'lost',
                         loc = 'northeast')
    def look(self):
        if self.state != 'lost':
            console.print('\nIt is ' + str(self.desc))
        else:
            fail() 

    def Take(self):
        if self.state == 'found':
          console.print('\nYou take the ' + str(self.name) + ' from the box')
          inventory.append('a medium sized steel key')
          boxItems.remove('a medium sized steel key')
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail()                

class SmallKey(Item):
    def __init__(self):
        super().__init__(name = 'small brass key',
                         desc = 'a small brass key, with a circle on one side of the key head, and the number 3 on the other',
                         state = 'lost',
                         loc = 'southwest')
    def look(self):
        if self.state != 'lost':
            console.print('\nIt is ' + str(self.desc))
        else:
            fail() 

    def Take(self):
        if self.state == 'found':
          console.print('\nYou take the ' + str(self.name) + ' from the desk drawer')
          inventory.append('a small brass key')
          drawerItems.remove('a small brass key')
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail()            

class IronKey(Item):
    def __init__(self):
        super().__init__(name = 'iron key',
                         desc = 'a large, old-fashioned, iron key, with a trapezoid wrought into one side of the key head, and the number 4 wrought into the other',
                         state = 'lost',
                         loc = 'east')
    def look(self):
        if self.state != 'lost':
            console.print('\nIt is ' + str(self.desc))
        else:
            fail()  

    def Take(self):
        if self.state == 'found':
          console.print('\nYou take the ' + str(self.name) + ' from the book')
          inventory.append('a large, old fashioned iron key')
          bookItems.remove('a large, old-fashioned iron key')
          self.state = 'owned'
        else:
          fail()



#########################################################################################################
"""ITEMS: BOOKS"""
######################################################################################################### 

class PrisonCakes(Item):
    def __init__(self):
        super().__init__(name = 'Famous Prison Cakes',
                         desc = 'Famous Prison Cakes showcases some of the most ingenious cakes made for some of the most notorious criminals in prisons from around the world. With full colour console.prints of each cake mentioned in the book, the reader will be left salivating at both the deliciousness and deviousness with which useful items have been smuggled into prisons throughout modern history.',
                         state = 'lost',
                         loc = 'east')
    def look(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'found':
            console.print('\nYou remove the book from the shelf, and note it is a heavy, hardbound book, well-used, with many scratches and dents. A portion from the back of the book reads: ' + str(self.desc))
        elif playerLoc != self.loc and self.state == 'found':
            console.print('\nYou walk to the bookshelf and remove Famous Prison Cakes from the shelf. You note it is a heavy, hardbound book, well-used, with many scratches and dents. A portion from the back of the book reads: ' + str(self.desc)) 
            playerLoc = self.loc  
        elif self.state == 'owned':
            console.print('\nFamous Prison Cakes is a heavy, hardbound book, well-used, with many scratches and dents. A portion from the back of the book reads: ' + str(self.desc))
        else:
            fail() 

    def Read(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'found':
            console.print('\nYou remove Famous Prison Cakes from the shelf, and open it up. To your surprise, you find that all of the pages have a large, roughly key-shaped hole cut out of their center, and inside the hole you find a large, old-fashioned iron key.')
            ironKey.state = 'found'
        elif playerLoc != self.loc and self.state == 'found':
            console.print('\nYou walk to the bookshelf, remove Famous Prison Cakes from the shelf, and open it up. To your surprise, you find that all of the pages have a large, roughly key-shaped hole cut out of their center, and inside the hole you find a large, old-fashioned iron key.') 
            playerLoc = self.loc  
            ironKey.state = 'found'
        elif self.state == 'owned':
            console.print('\nYou take out Famous Prison Cakes and open it up. To your surprise, you find that all of the pages have a large, roughly key-shaped hole cut out of their center, and inside the hole you find a large, old-fashioned iron key.')
            ironKey.state = 'found'
        elif ironKey.state == 'owned':
            console.print('\nYou take out Famous Prison Cakes and open it up. You see an empty key-shaped hole cut out of the pages in the book.')            
        else:
            fail()

    def Take(self):
        global playerLoc
        global bookshelfOneItems
        if playerLoc == self.loc and self.name in bookshelfOneItems and self.state == 'found':
          console.print('\nYou take ' + str(self.name))
          inventory.append(self.name)
          for self.name in list(bookshelfOneItems):
              bookshelfOneItems.remove(self.name)
          self.state = 'owned'
        elif playerLoc != self.loc and self.name in bookshelfOneItems and self.state == 'found':
          console.print('\nYou take ' + str(self.name) + ' from the bookshelf.')
          inventory.append(self.name)
          bookshelfOneItems.remove('Famous Prison Cakes')
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail()       

class Moby(Item):
    def __init__(self):
        super().__init__(name = "'The Music of Moby, by R. Melville Hall'",
                         desc = "'A detailed analysis of the methods and genius of one of the late 20th Century's greatest pop-music composers - Richard Mellville Hall - better known to the world as Moby.'",
                         state = 'lost',
                         loc = 'east')
    def look(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'found':
            console.print('\nYou remove the book from the shelf, and note it is a thin, paperback book in almost pristine condition - as if it has never been read before. A portion from the back of the book reads: ' + str(self.desc))
        elif playerLoc != self.loc and self.state == 'found':
            console.print('\nYou walk to the bookshelf and remove The Music of Moby from the shelf. You find it is a thin, paperback book in almost pristine condition - as if it has never been read before. A portion from the back of the book reads: ' + str(self.desc)) 
            playerLoc = self.loc  
        elif self.state == 'owned':
            console.print('\nThe Music of Moby is a thin, paperback book in almost pristine condition - as if it has never been read before. A portion from the back of the book reads: ' + str(self.desc))
        else:
            fail() 

    def Read(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'found':
            console.print("\nYou remove 'The Music of Moby' from the shelf and take a quick glance through its pages, noting the sasfying 'crack' of a book being opened for the first time. You learn that Moby's fifth album, entitled, 'Play' was his best selling record, and become curious to hear it for yourself.")
        elif playerLoc != self.loc and self.state == 'found':
            console.print("\nYou walk to the bookshelf, remove 'The Music of Moby' from the shelf and take a quick glance through its pages, noting the sasfying 'crack' of a book being opened for the first time. You learn that Moby's fifth album, entitled, 'Play' was his best selling record, and become curious to hear it for yourself.") 
            playerLoc = self.loc  
        elif self.state == 'owned':
            console.print("\nYou take out 'The Music of Moby' and take a quick glance through its pages, noting the sasfying 'crack' of a book being opened for the first time. You learn that Moby's fifth album, entitled, 'Play' was his best selling record, and become curious to hear it for yourself.")
        else:
            fail()

    def Take(self):
        global playerLoc
        if playerLoc == self.loc and self.name in bookshelfOneItems and self.state == 'found':
          console.print('\nYou take ' + str(self.name))
          inventory.append(str(self.name))
          bookshelfOneItems.remove(str(self.name))
          self.state = 'owned'
        elif playerLoc != self.loc and self.name in bookshelfOneItems and self.state == 'found':
          console.print('\nYou take ' + str(self.name) + ' from the bookshelf')
          inventory.append(str(self.name))
          bookshelfOneItems.remove(str(self.name))
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail()                  

class Eggs(Item):
    def __init__(self):
        super().__init__(name = "'Scrambled eggs for breakfast, lunch and dinner'",
                         desc = "'Scrambled Eggs for Breakfast, Lunch and Dinner is a huge leap forward in the evolution of the cookbook. In this book you will find the key to successfully including scrambled eggs as a side dish - or even a main course - in every conceivable meal, from every conceivable cusine, including scrambled eggs and fish, scrambled eggs and cereal and scrambled eggs and ice-cream.",
                         state = 'lost',
                         loc = 'east')
    def look(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'found':
            console.print("\nYou remove 'Scrambled Eggs for Breakfast, Lunch and Dinner' from the shelf, and note its impressive veneer and immaculate production value. Everything about the book screams quality. A portion from the back of the book reads: " + str(self.desc))
        elif playerLoc != self.loc and self.state == 'found':
            console.print("\nYou walk to the bookshelf, remove 'Scrambled Eggs for Breakfast, Lunch and Dinner' from the shelf, and note its impressive veneer and immaculate production value. Everything about the book screams quality. A portion from the back of the book reads: " + str(self.desc)) 
            playerLoc = self.loc  
        elif self.state == 'owned':
            console.print("\n'Scrambled eggs for Breakfast, Lunch and Dinner' is impressive with its veneer and immaculate production value. Everything about the book screams quality. A portion from the back of the book reads: " + str(self.desc))
        else:
            fail() 

    def Read(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'found':
            console.print("\nYou remove 'Scrambled Eggs for Breakfast, Lunch and Dinner' from the shelf and flip casually through its pages. You are amazed by the variety of ways scrambled eggs can be combined with seemingly every imaginable food, and are overcome with a desire to run to the grocery store, buy some eggs, and get scrambling. It is a real shame, you realize, that you are trapped inside this room.")
        elif playerLoc != self.loc and self.state == 'found':
            console.print("\nYou walk to the bookshelf, remove 'Scrambled Eggs for Breakfast, Lunch and Dinner' from the shelf and flip casually through its pages. You are amazed by the variety of ways scrambled eggs can be combined with seemingly every imaginable food, and are overcome with a desire to run to the grocery store, buy some eggs, and get scrambling. It is a real shame, you realize, that you are trapped inside this room.") 
            playerLoc = self.loc  
        elif self.state == 'owned':
            console.print("\nYou take out 'Scrambled Eggs for Breakfast, Lunch and Dinner' and flip casually through its pages. You are amazed by the variety of ways scrambled eggs can be combined with seemingly every imaginable food, and are overcome with a desire to run to the grocery store, buy some eggs, and get scrambling. It is a real shame, you realize, that you are trapped inside this room.")
        else:
            fail()

    def Take(self):
        global playerLoc
        if playerLoc == self.loc and self.name in bookshelfOneItems and self.state == 'found':
          console.print('\nYou take ' + str(self.name))
          inventory.append(str(self.name))
          bookshelfOneItems.remove(str(self.name))
          self.state = 'owned'
        elif playerLoc != self.loc and self.name in bookshelfOneItems and self.state == 'found':
          console.print('\nYou take ' + str(self.name) + ' from the bookshelf.')
          inventory.append(str(self.name))
          bookshelfOneItems.remove(str(self.name))
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail()   

class WondersOne(Item):
    def __init__(self):
        super().__init__(name = 'Wonders of the World, Volume One',
                         desc = "Wonders of the World is a two-volume, alphabetized catalogue of some of the great monuments and wonders from around the world. Volume One covers the wonders from A to M.",
                         state = 'lost',
                         loc = 'east')
    def look(self):
        global playerLoc
        global bookmarkOne
        if playerLoc == self.loc and self.state == 'found':
            console.print("\nYou remove the book from the shelf, and note it is a big, heavy, hardcover book. A portion from the back of the book reads: " + str(self.desc) + ". You also notice 5 bookmarks sticking out from 5 different pages in the book.")
            bookmarkOne = 1
        elif playerLoc != self.loc and self.state == 'found':
            console.print("\nYou walk to the bookshelf and remove 'Wonders of the World: Volume One', from the shelf. You find it is a big, heavy, hardcover book. A portion from the back of the book reads: " + str(self.desc) + '. You also notice 5 bookmarks sticking out from 5 different pages in the book.') 
            playerLoc = self.loc
            bookmarkOne = 1
        elif self.state == 'owned':
            console.print("\n'Wonders of the World: Volume One' is a big, heavy, hardcover book. A portion from the back of the book reads: " + str(self.desc) + ". You also notice 5 bookmarks sticking out from 5 different pages in the book.")
            bookmarkOne = 1
        else:
            fail() 

    def Read(self):
        global playerLoc
        global bookmarkOne
        if playerLoc == self.loc and self.state == 'found':
            console.print("\nYou remove 'Wonders of the World: Volume One' from the shelf, and open it up. You are amazed by the beauty and grandeur of some of humanity's greatest works of art and architecture. Marveling at the scale and design of some of the monuments, you promise yourself that, if you ever get out of this room, you will one day take a trip to visit some of them. You also notice 5 bookmarks have been placed in 5 different pages the book.")
            bookmarkOne = 1
        elif playerLoc != self.loc and self.state == 'found':
            console.print("\nYou walk to the bookshelf, remove 'Wonders of the World: Volume One', and take a quick glance through the pages. You are amazed by the beauty and grandeur of some of humanity's greatest works of art and architecture. Marveling at the scale and design of some of the monuments, you promise yourself that, if you ever get out of this room, you will one day take a trip to visit some of them. You also notice 5 bookmarks have been placed in 5 different pages the book.") 
            playerLoc = self.loc
            bookmarkOne = 1
        elif self.state == 'owned':
            console.print("\nYou take out 'Wonders of the World: Volume One', and take a quick glance through the pages. You are amazed by the beauty and grandeur of some of humanity's greatest works of art and architecture. Marveling at the scale and design of some of the monuments, you promise yourself that, if you ever get out of this room, you will one day take a trip to visit some of them. You also notice 5 bookmarks have been placed in 5 different pages the book.")
            bookmarkOne = 1
        else:
            fail()

    def Bookmark(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'found':
            console.print("\nYou remove 'Wonders of the World: Volume One' from the shelf, and look at the pages marked by the bookmarks. The wonders identified by the bookmarks are: Chichen Itza, located in Mexico; the Eiffel Tower, located in France; The Great Pyramid, located in Egypt; the Great Wall, located in China, and Machu Picchu, located in Peru.")
        elif playerLoc != self.loc and self.state == 'found':
            console.print("\nYou walk to the bookshelf, remove 'Wonders of the World: Volume One', and look at the pages marked by the bookmarks. The wonders identified by the bookmarks are: Chichen Itza, located in Mexico; the Eiffel Tower, located in France; The Great Pyramid, located in Egypt; the Great Wall, located in China, and Machu Picchu, located in Peru.") 
            playerLoc = self.loc  
        elif self.state == 'owned':
            console.print("\nYou take out 'Wonders of the World: Volume One', and look at the pages marked by the bookmarks. The wonders identified by the bookmarks are: Chichen Itza, located in Mexico; the Eiffel Tower, located in France; The Great Pyramid, located in Egypt; the Great Wall, located in China, and Machu Picchu, located in Peru.")
        else:
            fail()
            
    def BookmarkCheck(self):
        global playerLoc
        if bookmarkOne == 1 and bookmarkTwo == 0:
            console.print("\nYou take out 'Wonders of the World: Volume One', and look at the pages marked by the bookmarks. The wonders identified by the bookmarks are: Chichen Itza, located in Mexico; the Eiffel Tower, located in France; The Great Pyramid, located in Egypt; the Great Wall, located in China, and Machu Picchu, located in Peru.")
        elif bookmarkOne == 0 and bookmarkTwo == 1:
            console.print("\nYou take out 'Wonders of the World: Volume Two', and look at the pages marked by the bookmarks. The wonders identified by the bookmarks are: Petra, located in Jordan; Stonehenge, located in England, and the Taj Mahal, located in India.")
        elif bookmarkOne == 1 and bookmarkTwo == 1:
            console.print("\nYou take out 'Wonders of the World: Volume One', and look at the pages marked by the bookmarks. The wonders identified by the bookmarks are: Chichen Itza, located in Mexico; the Eiffel Tower, located in France; The Great Pyramid, located in Egypt; the Great Wall, located in China, and Machu Picchu, located in Peru.")
            console.print("\nNext, you take out 'Wonders of the World: Volume Two', and look at the pages marked by the bookmarks. The wonders identified by the bookmarks are: Petra, located in Jordan; Stonehenge, located in England, and the Taj Mahal, located in India.")
        else:
            fail()

    def Take(self):
        global playerLoc
        if playerLoc == self.loc and self.name in bookshelfTwoItems and self.state == 'found':
          console.print('\nYou take ' + str(self.name))
          inventory.append(str(self.name))
          bookshelfTwoItems.remove(str(self.name))
          self.state = 'owned'
        elif playerLoc != self.loc and self.name in bookshelfTwoItems and self.state == 'found':
          console.print('\nYou take ' + str(self.name) + ' from the bookshelf.')
          inventory.append(str(self.name))
          bookshelfTwoItems.remove(str(self.name))
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail() 

class WondersTwo(Item):
    def __init__(self):
        super().__init__(name = "'Wonders of the World, Volume Two'",
                         desc = "Wonders of the World is a two-volume, alphabetized catalogue of some of the great monuments and wonders from around the world. Volume Two covers the wonders from N to Z.",
                         state = 'lost',
                         loc = 'east')
    def look(self):
        global playerLoc
        global bookmarkTwo
        if playerLoc == self.loc and self.state == 'found':
            console.print('\nYou remove the book from the shelf, and note it is a big, heavy, hardcover book. A portion from the back of the book reads: ' + str(self.desc) + '. You also notice 3 bookmarks sticking out from 3 different pages in the book.')
            bookmarkTwo = 1
        elif playerLoc != self.loc and self.state == 'found':
            console.print("\nYou walk to the bookshelf and remove 'Wonders of the World: Volume Two', from the shelf. You find it is a big, heavy, hardcover book. A portion from the back of the book reads: " + str(self.desc) + '. You also notice 3 bookmarks sticking out from 3 different pages in the book.') 
            playerLoc = self.loc
            bookmarkTwo = 1
        elif self.state == 'owned':
            console.print("'Wonders of the World: Volume Two' is a big, heavy, hardcover book. A portion from the back of the book reads: " + str(self.desc) + '. You also notice 3 bookmarks sticking out from 3 different pages in the book.')
            bookmarkTwo = 1
        else:
            fail() 

    def Read(self):
        global playerLoc
        global bookmarkTwo
        if playerLoc == self.loc and self.state == 'found' and paper.state == 'lost':
            console.print("\nYou remove 'Wonders of the World: Volume Two' from the shelf, and open it up. You are amazed by the beauty and grandeur of some of humanity's greatest works of art and architecture. Marveling at the scale and design of some of the monuments, you promise yourself that, if you ever get out of this room, you will one day take a trip to visit some of them. You also notice 3 bookmarks have been placed in 3 different pages in the book.")
            bookmarkTwo = 1
            console.print('\nAs you read through the pages, a small slip of paper falls out and drops to the floor.')
            paper.state = 'found'
        elif playerLoc == self.loc and self.state == 'found':
            console.print("\nYou remove 'Wonders of the World: Volume Two' from the shelf, and open it up. You are amazed by the beauty and grandeur of some of humanity's greatest works of art and architecture. Marveling at the scale and design of some of the monuments, you promise yourself that, if you ever get out of this room, you will one day take a trip to visit some of them. You also notice 3 bookmarks have been placed in 3 different pages in the book.")
            bookmarkTwo = 1
          
        elif playerLoc != self.loc and self.state == 'found' and paper.state == 'lost':
            console.print("\nYou walk to the bookshelf, remove 'Wonders of the World: Volume Two', and take a quick glance through the pages. You are amazed by the beauty and grandeur of some of humanity's greatest works of art and architecture. Marveling at the scale and design of some of the monuments, you promise yourself that, if you ever get out of this room, you will one day take a trip to visit some of them. You also notice 3 bookmarks have been placed in 3 different pages in the book.") 
            playerLoc = self.loc
            bookmarkTwo = 1
            console.print('\nAs you read through the pages, a small slip of paper falls out and drops to the floor.')
            paper.state = 'found'

        elif playerLoc != self.loc and self.state == 'found':
            console.print("\nYou walk to the bookshelf, remove 'Wonders of the World: Volume Two', and take a quick glance through the pages. You are amazed by the beauty and grandeur of some of humanity's greatest works of art and architecture. Marveling at the scale and design of some of the monuments, you promise yourself that, if you ever get out of this room, you will one day take a trip to visit some of them. You also notice 3 bookmarks have been placed in 3 different pages in the book.") 
            playerLoc = self.loc
            bookmarkTwo = 1

        elif self.state == 'owned' and paper.state == 'lost':
            console.print("\nYou take out 'Wonders of the World: Volume Two', and take a quick glance through the pages. You are amazed by the beauty and grandeur of some of humanity's greatest works of art and architecture. Marveling at the scale and design of some of the monuments, you promise yourself that, if you ever get out of this room, you will one day take a trip to visit some of them. You also notice 3 bookmarks have been placed in 3 different pages in the book.")
            bookmarkTwo = 1
            console.print('\nAs you read through the pages, a small slip of paper falls out and drops to the floor.')
            paper.state = 'found'

        elif self.state == 'owned':
            console.print("\nYou take out 'Wonders of the World: Volume Two', and take a quick glance through the pages. You are amazed by the beauty and grandeur of some of humanity's greatest works of art and architecture. Marveling at the scale and design of some of the monuments, you promise yourself that, if you ever get out of this room, you will one day take a trip to visit some of them. You also notice 3 bookmarks have been placed in 3 different pages in the book.")
            bookmarkTwo = 1
        else:
            fail()     

    def Bookmark(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'found' and paper.state == 'lost':
          console.print("\nYou remove 'Wonders of the World: Volume Two' from the shelf, and look at the pages marked by the bookmarks. The wonders identified by the bookmarks are: Petra, located in Jordan; Stonehenge, located in England, and the Taj Mahal, located in India.")
          console.print('\nAs you flip through the pages, moving from bookmark to bookmark, a small slip of paper falls out and drops to the floor.')
          paper.state = 'found'

        elif playerLoc == self.loc and self.state == 'found':
          console.print("\nYou remove 'Wonders of the World: Volume Two' from the shelf, and look at the pages marked by the bookmarks. The wonders identified by the bookmarks are: Petra, located in Jordan; Stonehenge, located in England, and the Taj Mahal, located in India.")
            
        elif playerLoc != self.loc and self.state == 'found' and paper.state == 'lost':
          console.print("\nYou walk to the bookshelf, remove 'Wonders of the World: Volume Two', and look at the pages marked by the bookmarks. The wonders identified by the bookmarks are: Petra, located in Jordan; Stonehenge, located in England, and the Taj Mahal, located in India.") 
          playerLoc = self.loc
          console.print('\nAs you flip through the pages, moving from bookmark to bookmark, a small slip of paper falls out and drops to the floor.')
          paper.state = 'found'

        elif playerLoc != self.loc and self.state == 'found':
          console.print("\nYou walk to the bookshelf, remove 'Wonders of the World: Volume Two', and look at the pages marked by the bookmarks. The wonders identified by the bookmarks are: Petra, located in Jordan; Stonehenge, located in England, and the Taj Mahal, located in India.") 
          playerLoc = self.loc
            
        elif self.state == 'owned' and paper.state == 'lost':
          console.print("\nYou take out 'Wonders of the World: Volume Two', and look at the pages marked by the bookmarks. The wonders identified by the bookmarks are: Petra, located in Jordan; Stonehenge, located in England, and the Taj Mahal, located in India.")
          console.print('\nAs you flip through the pages, moving from bookmark to bookmark, a small slip of paper falls out and drops to the floor.')
          paper.state = 'found'

        elif self.state == 'owned':
          console.print("\nYou take out 'Wonders of the World: Volume Two', and look at the pages marked by the bookmarks. The wonders identified by the bookmarks are: Petra, located in Jordan; Stonehenge, located in England, and the Taj Mahal, located in India.")

        else:
            fail()                    

    def Take(self):
        global playerLoc
        if playerLoc == self.loc and self.name in bookshelfTwoItems and self.state == 'found':
          console.print('\nYou take ' + str(self.name))
          inventory.append(str(self.name))
          bookshelfTwoItems.remove(str(self.name))
          self.state = 'owned'
        elif playerLoc != self.loc and self.name in bookshelfTwoItems and self.state == 'found':
          console.print('\nYou take ' + str(self.name) + ' from the bookshelf.')
          inventory.append(str(self.name))
          bookshelfTwoItems.remove(str(self.name))
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail()
          
    def BookmarkCheck(self):
        global playerLoc
        if bookmarkOne == 1 and bookmarkTwo == 0:
            console.print("\nYou take out 'Wonders of the World: Volume One', and look at the pages marked by the bookmarks. The wonders identified by the bookmarks are: Chichen Itza, located in Mexico; the Eiffel Tower, located in France; The Great Pyramid, located in Egypt; the Great Wall, located in China, and Machu Picchu, located in Peru.")
        elif bookmarkOne == 0 and bookmarkTwo == 1 and paper.state == 'lost':
          console.print("\nYou take out 'Wonders of the World: Volume Two', and look at the pages marked by the bookmarks. The wonders identified by the bookmarks are: Petra, located in Jordan; Stonehenge, located in England, and the Taj Mahal, located in India.")
          console.print('\nAs you flip through the pages, moving from bookmark to bookmark, a small slip of paper falls out and drops to the floor.')
          paper.state = 'found'
        elif bookmarkOne == 0 and bookmarkTwo == 1:
          console.print("\nYou take out 'Wonders of the World: Volume Two', and look at the pages marked by the bookmarks. The wonders identified by the bookmarks are: Petra, located in Jordan; Stonehenge, located in England, and the Taj Mahal, located in India.")

        elif bookmarkOne == 1 and bookmarkTwo == 1 and paper.state == 'lost':
          console.print("\nYou take out 'Wonders of the World: Volume One', and look at the pages marked by the bookmarks. The wonders identified by the bookmarks are: Chichen Itza, located in Mexico; the Eiffel Tower, located in France; The Great Pyramid, located in Egypt; the Great Wall, located in China, and Machu Picchu, located in Peru.")
          console.print("\nNext, you take out 'Wonders of the World: Volume Two', and look at the pages marked by the bookmarks. The wonders identified by the bookmarks are: Petra, located in Jordan; Stonehenge, located in England, and the Taj Mahal, located in India.")
          console.print('\nAs you flip through the pages, moving from bookmark to bookmark, a small slip of paper falls out and drops to the floor.')
          paper.state = 'found'
        elif bookmarkOne == 1 and bookmarkTwo == 1:
          console.print("\nYou take out 'Wonders of the World: Volume One', and look at the pages marked by the bookmarks. The wonders identified by the bookmarks are: Chichen Itza, located in Mexico; the Eiffel Tower, located in France; The Great Pyramid, located in Egypt; the Great Wall, located in China, and Machu Picchu, located in Peru.")
          console.print("\nNext, you take out 'Wonders of the World: Volume Two', and look at the pages marked by the bookmarks. The wonders identified by the bookmarks are: Petra, located in Jordan; Stonehenge, located in England, and the Taj Mahal, located in India.")
        else:
            fail()

class Clocks(Item):
    def __init__(self):
        super().__init__(name = "'The Clock Echoes'",
                         desc = "A ponderous, thoughful, and reflective tome on the epic machinery of the expansive influence of time across the great surface of the universal ocean we call life.",
                         state = 'lost',
                         loc = 'east')
    def look(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'found':
            console.print('\nYou remove the book from the shelf, and note the fancy cursive writing overtop a photo of The Thinker on the cover. A portion from the back of the book reads: ' + str(self.desc))
        elif playerLoc != self.loc and self.state == 'found':
            console.print("\nYou walk to the bookshelf and remove 'The Clock Echoes' from the shelf. You note the fancy cursive writing overtop a photo of The Thinker on the cover. A portion from the back of the book reads: " + str(self.desc)) 
            playerLoc = self.loc  
        elif self.state == 'owned':
            console.print("\nYou take out 'The Clock Echoes', and note the fancy cursive writing overtop a photo of The Thinker. A portion from the back of the book reads: " + str(self.desc))
        else:
            fail() 

    def Read(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'found':
            midTime = time.perf_counter()
            elapsedTime = (int(midTime) - int(startTime))
            console.print("\nYou try to read 'The Clock Echoes' and note that it opens up to only a single page. Upon this single page, you see just a single sentence. It reads, 'You have spent " + str(elapsedTime) + " seconds trapped, alone, in this room.' A cold chill runs down your spine.")
        elif playerLoc != self.loc and self.state == 'found':
            console.print("\nYou walk to the bookshelf, and take out 'The Clock Echoes' from its shelves. You note that it opens up to only a single page. Upon this single page, you see just a single sentence. It reads, 'You have spent" +  str(elapsedTime) + " seconds trapped, alone, in this room.' A cold chill runs down your spine.")
            playerLoc = self.loc  
        elif self.state == 'owned':
            console.print("\nYou try to read 'The Clock Echoes' and note that it opens up to only a single page. Upon this single page, you see just a single sentence. It reads, 'You have spent " + str(elapsedTime) + " seconds trapped, alone, in this room.' A cold chill runs down your spine.")
        else:
            fail()              
           
    def Take(self):
        global playerLoc
        if playerLoc == self.loc and self.name in bookshelfTwoItems and self.state == 'found':
          console.print('\nYou take ' + str(self.name))
          inventory.append(str(self.name))
          bookshelfTwoItems.remove(str(self.name))
          self.state = 'owned'
        elif playerLoc != self.loc and self.name in bookshelfTwoItems and self.state == 'found':
          console.print('\nYou take ' + str(self.name) + ' from the bookshelf.')
          inventory.append(str(self.name))
          bookshelfTwoItems.remove(str(self.name))
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail()   

#########################################################################################################
"""ITEMS: MISC"""
#########################################################################################################                                            
class Matches(Item):
    def __init__(self):
        super().__init__(name = 'matchbox',
                         desc = 'a box of matches',
                         state = 'lost',
                         loc = 'northeast')
    def look(self):
        if self.state != 'lost':
            console.print('\nIt is ' + str(self.desc))
        else:
            fail()   

    def Light(self):
        if self.state == 'owned':
            console.print('\nYou remove a match from the box, and run it along the strike pad. The match ignites, casting a nice glow and a gentle warmth, before extingushing.')
        elif self.state == 'found':
            console.print('\nYou do not have any matches.')
        else:
          fail() 

    def Take(self):
        global playerLoc
        if playerLoc == self.loc and self.desc in boxItems and self.state == 'found':
          console.print('\nYou take the box of matches.')
          inventory.append(str(self.desc))
          boxItems.remove(str(self.desc))
          self.state = 'owned'
        elif playerLoc != self.loc and self.name in boxItems and self.state == 'found':
          console.print('\nYou take box of matches from the small table.')
          inventory.append(str(self.desc))
          boxItems.remove(str(self.desc))
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail()               

class Records(Item):
    def __init__(self):
        super().__init__(name = 'records',
                         desc = 'a small collection of records, on a shelf next to a record player. The following records are in the collection: ' + str(recordCollection)[1:-1],
                         state = 'found',
                         loc = 'west')
    def look(self):
        console.print('\nIt is ' + str(self.desc))

    def Take(self):
        console.print("\nYou think about maybe taking one of the records, but ultimately decide against it, reasoning it makes sense to keep them by the record player. Deep down, though, you know the real reason is because you left your big backpack at home and have nowhere else to keep an object this size.") 

    def Walk(self):
      global playerLoc
      if playerLoc == self.loc:
        console.print('\nYou are already by the ' + str(self.name))         
      elif playerLoc != self.loc:
        console.print('\nYou walk to the ' + str(self.name))        
                                          

class LightBulb(Item):
    def __init__(self):
        super().__init__(name = 'a light bulb',
                         desc = 'an old, incandescent light bulb',
                         state = 'lost',
                         loc = 'southeast')
    def look(self):
        if self.state != 'lost':
            console.print('\nIt is ' + str(self.desc))
        else:
            fail() 

    def Take(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'found':
          console.print('\nYou take the ' + str(self.name))
          inventory.append(str(self.desc))
          #globeItems.remove(str(self.desc))
          self.state = 'owned'
        elif playerLoc != self.loc and self.state == 'found':
          console.print('\nYou take the light bulb from the globe.')
          inventory.append(str(self.desc))
          #globeItems.remove(str(self.desc))
          self.state = 'owned'
          playerLoc = self.loc
        else:
          fail()  

    def Use(self):
        global playerLoc
        if playerLoc == table.loc and self.state == 'owned':
          console.print("\nYou take out the light bulb and screw it into the table lamp. With the bulb now in, you turn the lamp on, which reveals a hidden message upon the table. The message revealed by the lamp begins with a music note, and is followed by the phrase, 'A cage aced'.")
          inventory.remove(str(self.desc)) 
          lamp.state = 'bulbIn'
          lamp.move = 'on'
        elif playerLoc != table.loc and self.state == 'owned':
          console.print("\nYou walk over to the small table by the couch, take out the light bulb and screw it into the table lamp. The light from the lamp reveals a hidden message upon the table. The message revealed by the lamp begins with a music note, and is followed by the phrase, 'A cage aced'.")
          inventory.remove(str(self.desc)) 
          lamp.state = 'bulbIn'
          lamp.move = 'on'
          playerLoc = self.loc
        else:
          fail()  

class GoldToken(Item):
    def __init__(self):
        super().__init__(name = 'a gold token',
                         desc = "a small gold token. On one side of the token, you see, from top to bottom, a triangle, a square, and a pentagon. On the other side of the token, you see, from top to bottom, the numbers 0, 5, and 2.",
                         state = 'lost',
                         loc = 'west')
    def look(self):
        if self.state != 'lost':
            console.print('\nIt is ' + str(self.desc))
        else:
            fail() 

    def Take(self):
        global playerLoc
        if self.state == 'found':
          console.print('\nYou take ' + str(self.name))
          inventory.append(str(self.name))
          self.state = 'owned'
        else:
          fail()   

class Paper(Item):
    def __init__(self):
        super().__init__(name = 'a small slip of paper',
                         desc = "a small slip of paper. On the paper you see several small drawings, organized in a row from top to bottom. In order, the drawings are: a pair of wings, a bow and arrow, a tombstone, a flower, a giant, fire and a triangle.",
                         state = 'lost',
                         loc = 'east')
    def look(self):
        if self.state != 'lost':
            console.print('\nIt is ' + str(self.desc))
        else:
            fail() 

    def Take(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'found':
          console.print('\nYou take the ' + str(self.name))
          inventory.append(str(self.name))
          self.state = 'owned'
        else:
          fail()  

          
#########################################################################################################
"""RECORD CLASS"""
#########################################################################################################     

class Record():
    """base class for game items"""
    def __init__(self, name, loc):
        self.name = name
        self.loc = loc 

    def look(self):
      global playerLoc
      if playerLoc == self.loc:
        console.print('\nIt is ' + str(self.name))
      elif playerLoc != self.loc:
        console.print('\nYou walk over to the shelf, and look at the record. It is the album ' + str(self.name) + '. You wish you were a better artist, you think to yourself. If you were, perhaps YOU would be the one designing cool artwork for famous musicians. You are not, however, and instead are trapped alone inside this room.')
        playerLoc = self.loc

    def Take(self):
        console.print('\nYou think about taking the record, but decide it would be easier for everyone to just leave it on the shelf.')

    def Play(self):
      global playerLoc
      if playerLoc == self.loc:
        console.print('\nYou pull out a record from the shelf, and enjoy its fine melodies and rhythms. Your spirits uplifted, you return to your efforts to escape from the room with renewed determination and confidence.')
      elif playerLoc != self.loc:
        console.print('\nYou pull out a record from the shelf, and enjoy its fine melody and rhythm. Your spirits uplifted, you return to your efforts to escape from the room with renewed determination and confidence.')
        playerLoc = self.loc        
            

pinkFloyd = Record('Wish You Were Here, by Pink Floyd', 'west')
noFX = Record('So Long and Thanks for All the Shoes, by NoFX', 'west')
sonnyCher = Record('Greatest Hits, by Sonny and Cher', 'west')
coolJ = Record('Radio, by L.L. Cool J', 'west')
ludwigVan = Record('The 9th Symphony', 'west')

petra = Petra()
eiffelTower = EiffelTower()
greatPyramid = GreatPyramid()
tajMahal = TajMahal()                        
machuPicchu = MachuPicchu()
chichenItza = ChichenItza()
stonehenge = Stonehenge()                                                         
greatWall = GreatWall()

steelKey = SteelKey()
smallKey = SmallKey()
ironKey = IronKey()

token = GoldToken()
matches = Matches()
lightBulb = LightBulb()
records = Records()

prisonCakes = PrisonCakes()
moby = Moby()
eggs = Eggs()
clocks = Clocks()
wondersOne = WondersOne()
wondersTwo = WondersTwo()

pinkPostIts = Pink_Post_Its()
bluePostIts = Blue_Post_Its()
whitePostIts = White_Post_Its()
greenPostIts = Green_Post_Its()
paperClip = Paper_Clip()
pencil = Pencil()
computer = Computer() 
paper = Paper()

#########################################################################################################
"""OBJECT CLASSES"""
######################################################################################################### 

class Object():
    """base class for game objects"""
    def __init__(self, name, desc, touch, state, loc, move):
        self.name = name
        self.desc = desc
        self.touch = touch
        self.state = state
        self.loc = loc
        self.move = move

class Door(Object):
    def __init__(self):
        super().__init__(name = 'door',
                         desc = "a big, heavy, old wooden door. It is the only door in the room, and, thus, the only thing standing between you and freedom. Ominously, you notice, there is no lock or handle of any kind.",
                         touch = '\nYou give the door a thorough examination in an attempt to discover something new about how to get it to open. You poke every corner, you tap on every square inch. You kick, punch, and scream at the door in an attempt to get it to open. In all of your efforts, however, you fail.',
                         state = 'locked',
                         loc = 'north',
                         move = 'false')

    def look(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'locked':
          console.print ('\nIt is ' + str(self.desc))  
        elif playerLoc != self.loc and self.state == 'locked':
          console.print ('\nYou move to the door to get a better look. It is ' + str(self.desc))  
        else:
          console.print("\nThe door is now open, beckoning you to walk through it. Perhaps you lack the courage, though. Perhaps you have come to love your time being imprisoned, alone, in this room and fear what is outside. Perhaps you decide NOT to walk through the door, that you SHOULD NOT walk through the door, now that it is open. That would almost be too easy...")          

    def Touch(self):
        global playerLoc
        if playerLoc == self.loc:  
          console.print(str(self.touch)) 
        elif playerLoc != self.loc:
          console.print('nYou get closer to the door. ' + str(self.touch))
          playerloc = self.loc
        elif self.state == 'unlocked':
          console.print("\nYou hesitate before the door, running your hand along the menace that once kept you trapped in the room, reminiscing about your failures and successes, and whisper, quietly, 'So long old friend.' You wipe your eyes on your sleeve.")

    def Open(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'locked':  
          console.print('\nYou try to open the door, but cannot even see where to begin.') 
        elif playerLoc != self.loc and self.state == 'locked':
          console.print('\nYou get closer to the door and try to open the door, but cannot even see where to begin.')
          playerloc = self.loc
        elif self.state == 'unlocked':
            console.print('\nThe door is already open. How did you make it THIS far without realizing this?')
          
    def Walk(self):
        global playerLoc
        midTime = time.perf_counter()
        elapsedTime = (int(midTime) - int(startTime))        
        if playerLoc == self.loc and self.state == 'locked':  
          console.print('\nYou are already in front of the ' + str(self.name)) 
        elif playerLoc != self.loc and self.state == 'locked':
          console.print('\nYou walk to the ' + str(self.name))
          playerloc = self.loc
        elif self.state == 'unlocked':
            console.print('\nAfter having been trapped, alone, in this room for ' + str(elapsedTime) + ' seconds, you walk at last through the only door in the room, now open and inviting you through. You have escaped! Thank you for playing Escape This! The Wonder Edition. Stay tuned for more rooms!')         
          
         

class Rug(Object):
    def __init__(self):
        super().__init__(name = 'rug',
                         desc = "a large rug covering most of the floor in the room. On the rug is a console.print of a giant compass, with North pointing toward the room's only door.",
                         touch = '\nThe rug has a low-pile, and seems well worn. With some further exploration, you notice the center of the rug is raised slightly, in a roughly square shape.',
                         state = 'found',
                         loc = 'center',
                         move = 'true')

    def look(self):
        console.print ('\nIt is ' + str(self.desc))    

    def Touch(self):
        console.print(str(self.touch)) 

    def Move(self):
        console.print('\nYou lift the rug and discover a square hatch in the floor.')
        hatch.state = 'found'

    def Walk(self):
      global playerLoc
      if playerLoc == self.loc:
        console.print('\nYou are already by the ' + str(self.name))         
      elif playerLoc != self.loc:
        console.print('\nYou walk to the ' + str(self.name))         

class Hatch(Object):
    def __init__(self):
        super().__init__(name = 'hatch',
                         desc = "a square hatch, with three old hinges on one side. The hatch has a large, old-fashioned iron keyhole.",
                         touch = "\nThe hatch, like the rest of the floor, is made from some kind of hardwood. Beech wood, you think to yourself. Maybe ash. Or oak. It couldn't be cedar, though. Or could it?? You learn, in the end, nothing new about the hatch that you could confidently tell another person that were here in the room with you, which there isn't.",
                         state = 'lost',
                         loc = 'center',
                         move = 'locked')

    def look(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'found':
          console.print ('\nIt is ' + str(self.desc))  
        elif playerLoc != self.loc and self.state == 'found':
          console.print ('\nYou move to the hatch to get a better look. It is ' + str(self.desc))  
        else:
          fail()          

    def Touch(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'found':  
          console.print(str(self.touch)) 
        elif playerLoc != self.loc and self.state == 'found':
          console.print('\nYou get closer to the hatch in order to carry out a proper investigation. ' + str(self.touch))
        else:
          fail()

    def Open(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'found':  
          console.print('\nThe hatch is locked') 
        elif playerLoc != self.loc and self.state == 'found':
          console.print('\nThe hatch is locked')
          playerLoc = self.loc
        else:
          fail()          

    def Unlock(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'found' and self.move == 'locked' and ironKey.state == 'owned':
          console.print('\nYou insert the large, old-fashioned iron key into the large, old-fashioned iron keyhole in the hatch, and with some extra wiggling and a little bit of force, you manage to unlock the old lock, and open the hatch. Inside the hatch you find a model of the ancient city of Petra.') 
          self.move = 'unlocked'
          petra.state = 'found'
        elif playerLoc != self.loc and self.state == 'found' and self.move == 'locked' and ironKey.state == 'owned':
          console.print('\nYou go to the hatch in the floor. Inserting the large, old-fashioned iron key into the large, old-fashioned iron keyhole in the hatch, and with some extra wiggling and a little bit of force, you manage to unlock the old lock, and open the hatch. Inside the hatch you find a model of the ancient city of Petra.') 
          playerLoc = self.loc
          self.move = 'unlocked'
          petra.state = 'found'
        elif self.move == 'unlocked':
          console.print('\nThe hatch is already unlocked.')
        else:
          fail()     

    def Walk(self):
      global playerLoc
      if playerLoc == self.loc:
        console.print('\nYou are already by the ' + str(self.name))         
      elif playerLoc != self.loc:
        console.print('\nYou walk to the ' + str(self.name))                

class Statue(Object):
    def __init__(self):
        super().__init__(name = 'statue',
                         desc = "a meticulous reproduction of the Statue of Liberty, on a pedestal to the right of the door. The first thing you notice about the statue is its colour: made fully of new copper that, unlike the copper in the original Statue of Liberty, has not oxidized into pale green, but stands, gloriously, in glorious copper-gold glory. It is, you estimate, about 7 feet tall from crown to torch, and immensely impressive.",
                         touch = "Devoting your full investigory attention onto the statue, you use your hands to search every little nook and cranny of Lady Liberty, leaving oily hand prints all over the previously immaculate piece of art. Working from bottom to top, you make your way, eventually, to the torch at the end of the statue's outstretched right arm. On the torch, you notice a small hole, inside of which you discover a wick and the smell of kerosene.",
                         state = 'unlit',
                         loc = 'north',
                         move = 'false')

    def look(self):
        global playerLoc
        if playerLoc == self.loc:
          console.print ('\nIt is ' + str(self.desc))  
        elif playerLoc != self.loc:
          console.print ('\nYou move to the statue to get a better look. It is ' + str(self.desc))  
          playerLoc = self.Loc
        else:
          fail()          

    def Touch(self):
        global playerLoc
        if playerLoc == self.loc:  
          console.print(str(self.touch)) 
        elif playerLoc != self.loc:
          console.print('\nYou walk to the statue to conduct a proper investigation. ' + str(self.touch))
        else:
          fail()

    def Light(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'unlit' and matches.state == 'owned':
          console.print('\nYou remove a match from the box, light it, and bring it to the torch, which ignites and casts a brilliant orange glow upon the statue, making this impressive statue remarkably more impressive. You hear a click from inside the pedestal at the base, and notice a hidden door along its front has opened. Inside the door you find a small model of the Great Pyramid of Giza.') 
          self.state = 'lit'
          greatPyramid.state = 'found'
        elif playerLoc != self.loc and self.state == 'unlit' and matches.state == 'owned':
          console.print('\nYou go to the statue, remove a match from the box, and light it. You bring it to the torch, which ignites and casts an orange glow upon the statue, making this impressive statue remarkably more impressive. You hear a click from inside the pedestal at the base, and notice a hidden door along its front has opened. Inside the door you find a small model of the Great Pyramid of Giza.') 
          playerLoc = self.loc
          self.state = 'lit'
          greatPyramid.state = 'found'
        elif self.state == 'lit':
          console.print('\nThe torch is already lit.')
        else:
          fail() 

    def Walk(self):
      global playerLoc
      if playerLoc == self.loc:
        console.print('\nYou are already by the ' + str(self.name))         
      elif playerLoc != self.loc:
        console.print('\nYou walk to the ' + str(self.name))           

class ShapesPuzzle(Object):
    def __init__(self):
      super().__init__(name = 'strange panel',
                       desc = 'a strange panel attached to the north wall to the left of the door. On the panel you see 6 different shapes: a circle, a triangle, a square, a trapezoid, a pentagon, and a hexagon. Within each shape, you notice a small dial, with each dial displaying the number 0. You quickly fiddle with the numbers in the dials, and learn they all range from 0 to 5.',
                       touch = '\nYou explore the strange panel with your hands, and are reminded that each of the dials rotate through the numbers zero through five.',
                       state = 'closed',
                       loc = 'north',
                       move = 'lost') 

    def look(self):
        global playerLoc
        if playerLoc == self.loc:
          console.print ('\nIt is ' + str(self.desc))
          self.move = 'found'
        elif playerLoc != self.loc:
          console.print ('\nYou walk to the north wall to get a better look at the panel. You see ' + str(self.desc))
          playerLoc = self.loc
          self.move = 'found'         
          

    def Touch(self):
        global playerLoc
        if playerLoc == self.loc:
          console.print (str(self.touch))  
        elif playerLoc != self.loc:
          console.print ('\nYou walk to the north wall to get a better look at the panel. ' + str(self.touch))
          playerLoc = self.loc       

    def Solve(self):
          console.print('\nAs you finish adjusting the last dial, you hear the whir of a mechanism within the interior of the panel. The panel recedes into the wall, and then moves to the side, removing itself from your view. In its place you see a hollow in the wall, and in that hollow you find a small model of the Taj Mahal.')
          tajMahal.state = 'found'
          self.state = 'open'

    def Walk(self):
      global playerLoc
      if playerLoc == self.loc:
        console.print('\nYou are already by the ' + str(self.name))         
      elif playerLoc != self.loc:
        console.print('\nYou walk to the ' + str(self.name))           
                                         

class Couch(Object):
      def __init__(self):
        super().__init__(name = 'couch',
                         desc = 'a comfortable looking couch.',
                         touch = 'The fabric is soft, and the cushioning is supple. You note there is something hard and pointy inside the couch cushion.',
                         state = 'closed',
                         loc = 'northeast',
                         move = 'false')

      def look(self):
        global playerLoc
        if playerLoc == self.loc:
          console.print ('\nIt is ' + str(self.desc))  
        elif playerLoc != self.loc:
          console.print ('\nIt is ' + str(self.desc))
          playerLoc = self.loc  
        else:
          fail()          

      def Touch(self):
        global playerLoc
        if playerLoc == self.loc:  
          console.print(str(self.touch)) 
        elif playerLoc != self.loc:
          console.print('\nYou walk to get a better feel of the couch. ' + str(self.touch))
          playerLoc = self.loc
        else:
          fail()

      def Sit(self):
        global playerLoc
        if 'a small model of the Eiffel Tower' in couchItems:
          console.print('\nYou make a move to sit on the couch. With your full weight pressed against the cushion, you notice something hard and pointy poking your bum, making what would otherwise be a comfortable sitting experience decidedly uncomfortable.')
          playerLoc = self.loc
        else:
          console.print('\nYou take a break from puzzle solving and room-escaping to relax on the now quite comfortable couch.')
          playerLoc = self.loc

      def Open(self):
        global playerLoc
        if 'a small model of the Eiffel Tower' in couchItems:
          console.print('\nYou take the cushions off the couch, and unzip the covers. Inside one of the cushions, you find a small model of the Eiffel Tower.')
          eiffelTower.state = 'found'
        else:
          console.print('\nYou think about opening up the couch cushions once again, but decide not to waste your time on such a pointless activity.')

      def Move(self):
        global playerLoc
        console.print('\nGetting a good position behind the couch, you struggle to move it out of position. Finding nothing of interest in the area beneath the couch, you again struggle to return the couch to its original place. You are now just a little bit sweaty.')
        playerLoc = self.loc   

      def Walk(self):
          global playerLoc
          if playerLoc == self.loc:
            console.print('\nYou are already by the ' + str(self.name))         
          elif playerLoc != self.loc:
            console.print('\nYou walk to the ' + str(self.name))            

class Table(Object):
    def __init__(self):
        super().__init__(name = 'small table',
                         desc = 'a small side table next to the couch. On the top of the table, there is a lamp.',
                         touch = 'You make a quick study of the small table. Feeling around it, on top of it, and underneath it for anything unusual, you discover a small box that has been attached to the bottom of the table.',
                         state = 'found',
                         loc = 'northeast',
                         move = 'true')   
     
    def look(self):
        global playerLoc
        
        if playerLoc == self.loc and lamp.move == 'off':
          console.print ('\nIt is ' + str(self.desc))
        if lamp.move == 'on':
          console.print ("\nThe message revealed by the lamp begins with a music note, and is followed by the phrase, 'A cage aced.")            
        elif playerLoc != self.loc and lamp.move == 'off':
          console.print ('It is ' + str(self.desc))
          playerLoc = self.loc           

    def Touch(self):
        global playerLoc
        if playerLoc == self.loc:  
          console.print('You make a quick study of the small table. Feeling around it, on top of it, and underneath it for anything unusual, you discover a small box that has been attached to its bottom.') 
          box.state = 'found'
        elif playerLoc != self.loc:
          console.print('\n' + str(self.touch))
          box.state = 'found'
          playerLoc = self.loc   

    def Move(self):
        global playerLoc
        if playerLoc == self.loc:  
          console.print('\nDeciding the table is light enough, you pick it up and move it out of the way. Looking around the area underneath the table, you find nothing of interest. Moving the table back into position, however, your hand feels something attached to the bottom of the table. Investigating further, you discover the object to be a small box.') 
          box.state = 'found'
        elif playerLoc != self.loc:
          console.print('\nDeciding the table is light enough, you move to pick it up and put it aside. Looking around the area underneath the table, you find nothing of interest. Moving the table back into position, however, your hand feels something attached to the bottom of the table. Investigating further, you discover the object to be a small box.')
          box.state = 'found'
          playerLoc = self.loc 

    def Walk(self):
      global playerLoc
      if playerLoc == self.loc:
        console.print('\nYou are already by the ' + str(self.name))         
      elif playerLoc != self.loc:
        console.print('\nYou walk to the ' + str(self.name))             

class Box(Object):
    def __init__(self):
        super().__init__(name = 'box',
                         desc = 'a small white box.',
                         touch = '\nYou open the box, and discover the following items: ' + str(boxItems)[1:-1],
                         state = 'lost',
                         loc = 'northeast',
                         move = 'closed') 

    def look(self):
        global playerLoc
        if playerLoc == self.loc and box.state == 'found':
          console.print ('\nIt is ' + str(self.desc))  
        elif playerLoc != self.loc and self.state == 'found':
          console.print ('\It is ' + str(self.desc))
          playerLoc = self.loc    
        if self.state == 'owned':
          console.print (str(self.touch))
          inventory.append('a box of matches')
          inventory.append('a medium sized steel key')          
          
          inventory.remove('a small box')
          self.state = 'lost'
          matches.state = 'owned'
          steelKey.state = 'owned'
        else:
          fail()             

    def Take(self):
        global playerLoc
        if self.state == 'found':  
          console.print('\nYou take the small box from the underside of the table, and feel clever for having found it.') 
          box.state = 'owned'
          playerLoc = self.loc
          inventory.append('a small box')
        elif self.state == 'owned':  
          console.print('\nThe box is already in your possession')

    def Open(self):
        global playerLoc
        if self.state == 'found':  
          console.print('\nYou do not have the box in your possession') 
          playerLoc = self.loc
        elif self.state == 'owned':  
          console.print('\nYou open the box, and discover the following items: ' + str(boxItems)[1:-1]) 
          inventory.append('a box of matches')
          inventory.append('a medium sized steel key')  
          inventory.remove('a small box')
#          boxItems.remove('a box of matches',  'a medium sized steel key')
          self.state = 'lost'
          matches.state = 'owned'
          steelKey.state = 'owned'
        else:
          fail()  


class Lamp(Object):
    def __init__(self):    
      super().__init__(name = 'table lamp',
                     desc = 'a small, ornate table lamp. Quite lovely, actually. Taking a closer look, you notice it is missing its light bulb',
                     touch = '\nExploring the table lamp, you notice it is heavier than you expected, reinforcing its impressive quality. The other thing you notice is that it is missing a light bulb',
                     state = 'bulbOut',
                     loc = 'northeast',
                     move = 'off')       

    def look(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'bulbOut':
          console.print ('\nIt is ' + str(self.desc))  
        elif playerLoc != self.loc and self.state == 'bulbOut':
          console.print ('\nIt is ' + str(self.desc))
          playerLoc = self.loc           
        elif playerLoc == self.loc and self.move == 'on':
          console.print ("\nThe message revealed by the lamp begins with a music note, and is followed by the phrase, 'A cage aced.'")  
        elif playerLoc != self.loc and self.move == 'on':
          console.print ("\nThe message revealed by the lamp begins with a music note, and is followed by the phrase, 'A cage aced.'") 
          playerLoc = self.loc  
          
    def Touch(self):
        global playerLoc
        if playerLoc == self.loc:  
          console.print(str(self.touch)) 
        elif playerLoc != self.loc:
          console.print('\nYou walk to the table beside the couch. ' + str(self.touch))
          playerLoc = self.loc   

    def Move(self):
        global playerLoc
        if playerLoc == self.loc:  
          console.print('\nYou pick up the lamp, hoping to find something useful hidden under it. Alas, you fail in your endeavour, and return the lamp to its rightful position upon the table. You notice, when putting the lamp down, that it is missing a light bulb.') 
        elif playerLoc != self.loc:
          console.print('\nYou walk up to the lamp and pick it up, hoping to find something useful hidden under it. Alas, you fail in your endeavour, and return the lamp to its rightful position upon the table. You notice, when putting it down, that the lamp is missing a light bulb.')
          playerLoc = self.loc  

    def On(self):
        global playerLoc
        if self.state == 'bulbIn' and self.move == 'off':
          console.print("\nWith the light bulb now in place, you turn on the lamp and see a hidden message revealved on the table by the now glowing bulb. The message revealed by the lamp begins with a music note, and is followed by the phrase, 'A cage aced.'")  
          self.move == 'on'       

    def Off(self):
        global playerLoc
        if self.move == 'on':
          console.print('\nYou turn off the lamp') 
          self.move == 'off'

    def Walk(self):
      global playerLoc
      if playerLoc == self.loc:
        console.print('\nYou are already by the ' + str(self.name))         
      elif playerLoc != self.loc:
        console.print('\nYou walk to the ' + str(self.name))                                                                

class Book_Shelf_One(Object):
    def __init__(self):
        super().__init__(name = 'bookshelf',
                         desc = 'a large bookshelf made of heavy dark brown wood. Among the books on its shelves you notice such titles as: ' + str(bookshelfOneItems)[1:-1],
                         touch = 'like a quality old bookshelf',
                         state = 'found',
                         loc = 'east',
                         move = 'false')
    def look(self):
        global playerLoc
        global bookshelfOneItems
        if playerLoc == self.loc:
            console.print('\nIt is ' + str(self.desc))
            prisonCakes.state = 'found'
            moby.state = 'found'
            eggs.state = 'found'
        else:
            console.print('\nYou move to get a better look at the ' + str(self.name))
            playerLoc = self.loc
            console.print('\nYou see it is ' + str(self.desc))
            prisonCakes.state = 'found'
            moby.state = 'found'
            eggs.state = 'found'            
            
    def Touch(self):
        global playerLoc
        if playerLoc == self.loc:
            console.print("\nThe bookshelves are made of a very smooth wood and you catch yourself saying, 'nice,' to yourself as you run your hands along them. You pull some of the books, hoping to engage some sort of secret door or rotating platform. Alas, nothing happens, which is too bad, because that would have been a very cool thing to have happened.")
        else:
            console.print("\nYou move to get a better sense of the bookshelves. They are made of a very smooth wood and you catch yourself saying, 'nice,' to yourself as you run your hands along them. You pull some of the books, hoping to engage some sort of secret door or rotating platform. Alas, nothing happens, which is too bad, because that would have been a very cool thing to have happened.")
            playerLoc = self.loc
            console.print('and note that it feels ' + str(self.touch))       
                                    
    def Move(self):
        global playerLoc
        if playerLoc == self.loc:
            console.print('\nThe bookshelves are too heavy for you to move')         
            playerLoc = self.loc
        elif playerLoc != self.loc and self.move == 'true':
            console.print('\nYou walk to the bookshelf to try to move them out of the way. To your dismay, they are far, far too heavy for you to move.')
            playerLoc = self.loc

    def Walk(self):
      global playerLoc
      if playerLoc == self.loc:
        console.print('\nYou are already by the ' + str(self.name))         
      elif playerLoc != self.loc:
        console.print('\nYou walk to the ' + str(self.name))             
                        
            
class Book_Shelf_Two(Object):
    def __init__(self):
        super().__init__(name = 'bookshelf',
                         desc = 'a large bookshelf made of heavy dark brown wood. Among the books on its shelves you notice such titles as, ' + str(bookshelfTwoItems)[1:-1],
                         touch = 'like a quality old bookshelf',
                         state = 'found',
                         loc = 'east',
                         move = 'false')
    def look(self):
        global playerLoc
        if playerLoc == self.loc:
            console.print('\nIt is ' + str(self.desc))
            clocks.state = 'found'
            wondersOne.state = 'found'
            wondersTwo.state = 'found'
        else:
            console.print('\nYou move to get a better look at the ' + str(self.name))
            playerLoc = self.loc
            console.print('\nYou see it is ' + str(self.desc))
            clocks.state = 'found'
            wondersOne.state = 'found'
            wondersTwo.state = 'found'
            
    def Touch(self):
        global playerLoc
        if playerLoc == self.loc:
            console.print("\nThe bookshelves are made of a very smooth wood and you catch yourself saying, 'nice,' to yourself as you run your hands along them. You pull some of the books, hoping to engage some sort of secret door or rotating platform. Alas, nothing happens, which is too bad, because that would have been a very cool thing to have happened.")
        else:
            console.print("\nYou move to get a better sense of the bookshelves. They are made of a very smooth wood and you catch yourself saying, 'nice,' to yourself as you run your hands along them. You pull some of the books, hoping to engage some sort of secret door or rotating platform. Alas, nothing happens, which is too bad, because that would have been a very cool thing to have experienced.")
            playerLoc = self.loc    
                                    
    def Move(self):
        global playerLoc
        if playerLoc == self.loc:
            console.print('\nThe bookshelves are too heavy for you to move')         
            playerLoc = self.loc
        elif playerLoc != self.loc and self.move == 'true':
            console.print('\nYou walk to the bookshelves to try to move them out of the way. To your dismay, they are far, far too heavy for you to move.')
            playerLoc = self.loc

    def Walk(self):
      global playerLoc
      if playerLoc == self.loc:
        console.print('\nYou are already by the ' + str(self.name))         
      elif playerLoc != self.loc:
        console.print('\nYou walk to the ' + str(self.name))            
            
class Painting(Object):
    def __init__(self):
        super().__init__(name = 'painting',
                         desc = 'an oil painting of the Spiral Minaret. You catch a faint smell of turpentine, indicating the painting must have been finished very recently.',
                         touch = '\nYou reach out and touch the painting, smearing some of the paint around, and hope no one notices. You then clean the excess paint from your hands by wiping them along the wall beside the painting. As you do so, you notice there is a larger than expected gap between the frame of the painting and the wall.',
                         state = 'found',
                         loc = 'southeast',
                         move = 'true')
    def look(self):
        global playerLoc
        if playerLoc == self.loc:
            console.print('\nIt is ' + str(self.desc))
        else:
            console.print('\nYou move toward the ' + str(self.name))
            playerLoc = self.loc
            console.print('\nYou see it is ' + str(self.desc))
            
    def Touch(self):
        global playerLoc
        if playerLoc == self.loc:
            console.print(str(self.touch))
        else:
            console.print('\nYou move toward the ' + str(self.name))
            playerLoc = self.loc
            console.print(str(self.touch))          
                                    
    def Move(self):
        global playerLoc
        if playerLoc == self.loc and self.move == 'false':
            console.print('\nIt is too heavy for you to move')
        elif playerLoc == self.loc and self.move == 'true':
            console.print('\nYou remove the painting from its hook and find a safe hidden in the wall behind it.')
            self.state = 'moved'
        elif playerLoc != self.loc and self.move == 'false':
            console.print('\nYou walk to the ' + str(self.name) + ' and attempt to move it but it is too heavy.')           
            playerLoc = self.loc
        elif playerLoc != self.loc and self.move == 'true':
            console.print('\nYou move to get to into a better position.')
            console.print('\nAs you remove the painting from its hook you find a safe hidden in the wall behind it.')
            self.state = 'moved'            
            playerLoc = self.loc

    def Walk(self):
      global playerLoc
      if playerLoc == self.loc:
        console.print('\You are already by the ' + str(self.name))         
      elif playerLoc != self.loc:
        console.print('\nYou walk to the ' + str(self.name))             

class WallSafe(Object):
    def __init__(self):
      super().__init__(name = 'wall safe',
                     desc = 'a steel safe, built into the wall. On the front of the safe there is a large dial, with numbers around it reading from 1 to 60.',
                     touch = '\nYou move your hands around the safe, looking for ways to open it, and find it firmly locked tight. The dial spins smoothly as you turn it left and right. This is no doubt the only means to open the safe. If only you had the combination...',
                     state = 'locked',
                     loc = 'southeast',
                     move = 'false')

    def look(self):
        global playerLoc
        if playerLoc == self.loc and painting.state == 'moved':
            console.print('\nIt is ' + str(self.desc))
        elif playerLoc != self.loc and painting.state == 'moved':
            console.print('\nYou move to get a better look at the ' + str(self.name))
            playerLoc = self.loc
            console.print('\nYou see it is ' + str(self.desc))
        elif playerLoc == self.loc and self.state == 'unlocked' and 'a model of Chichen Itza' in inventory:
            console.print('\nYou look into the wall safe, but see it is empty')
        elif playerLoc != self.loc and self.state == 'unlocked' and 'a model of Chichen Itza' in inventory:
            console.print('\nYou look into the wall safe, but see it is empty')  
            playerLoc = self.loc 
        elif playerLoc == self.loc and self.state == 'unlocked' and 'a small model of Chichen Itza' in safeItems:
            console.print('\nLooking into the safe, you see a small model of Chichen Itza')
        elif playerLoc != self.loc and self.state == 'unlocked' and 'a small model of Chichen Itza' in safeItems:
            console.print('\nYou walk to the wall safe, and see a small model of Chichen Itza')  
            playerLoc = self.loc                         
        else:
          fail()
            
    def Touch(self):
        global playerLoc
        if playerLoc == self.loc and painting.state == 'moved':
            console.print(str(self.touch))
        elif playerLoc != self.loc and painting.state == 'moved':
            console.print('\nYou move closer to get a better sense of the ' + str(self.name))
            playerLoc = self.loc
            console.print(str(self.touch)) 
        else:
          fail()      
                                    
    def Open(self):
        global playerLoc
        if playerLoc == self.loc and painting.state == 'moved' and self.state == 'locked':
          console.print('\nThe safe is locked and will not open')
        if playerLoc != self.loc and painting.state == 'moved' and self.state == 'locked':
          console.print('\nYou walk to the safe and try to open it, but it is locked')
          playerLoc = self.loc          
        elif playerLoc == self.loc and painting.state == 'moved' and self.state == 'unlocked':
          console.print('\nYou open the safe and find a small model of Chichen Itza within it.')  
        elif playerLoc != self.loc and painting.state == 'moved' and self.state == 'unlocked': 
          console.print('\nYou walk towards the safe and open it, revealing a small model of Chichen Itza.')
          playerLoc = self.loc
        else:
          fail()
    
    def Unlock(self):
        global playerLoc
        if playerLoc == self.loc and painting.state == 'moved' and self.state == 'locked':
          console.print('\nYou spin the dial clockwise to the number 15, then reverse the dial all the way around to the number 25, spin it clockwise once more to the number 35, and give the door a gentle pull. To your immense satisfaction, the wall safe opens. Inside the safe you find a small model of Chichen Itza.')
          self.state = 'unlocked'  
          chichenItza.state = 'found'
        elif playerLoc != self.loc and painting.state == 'moved' and self.state == 'locked':
          console.print('nYou spin the dial clockwise to the number 15, then reverse the dial all the way around to the number 25, spin it clockwise once more to the number 35, and give the door a gentle pull. To your immense satisfaction, the wall safe opens. Inside the safe, you find a small model of Chichen Itza')
          self.state = 'unlocked'
          chichenItza.state = 'found'   
          playerLoc = self.loc 

    def Walk(self):
      global playerLoc
      if playerLoc == self.loc:
        console.print('\nYou are already by the ' + str(self.name))         
      elif playerLoc != self.loc:
        console.print('\nYou walk to the ' + str(self.name))                                                       
            
class Globe(Object):
    def __init__(self):
        super().__init__(name = 'globe',
                         desc = 'a large globe. Upon close inspection, you notice there are eight small black squares on the globe, each located in a different country, spread around the world.',
                         touch = '\nYou turn the globe slowly with your hands. Examining the squares, you get the sense they are likely magnets.',
                         state = 'found',
                         loc = 'southeast',
                         move = 'false')
    def look(self):
        global playerLoc
        global globeSeen
        if self.state == 'unlocked':
            console.print('\nLooking inside the now opened globe, you find an old, incandescent light bulb.')
            lightBulb.state = 'found'        
        elif playerLoc == self.loc and globeSeen == ['false']:
            console.print('\nIt is ' + str(self.desc))
            globeSeen = ['true']
        elif playerLoc != self.loc and globeSeen == ['false']:
            console.print('\nYou move toward the ' + str(self.name))
            playerLoc = self.loc
            console.print('\nYou see it is ' + str(self.desc))
            globeSeen = ['true']
        elif playerLoc == self.loc and globeSeen == ['true']:
            console.print('\nInvestigating the globe further, you notice the eight black squares are located in the following countries: Peru, Mexico, England, France, Egypt, Jordan, India, and China.')
        elif playerLoc != self.loc and globeSeen == ['true']:
            console.print('\nYou move toward the ' + str(self.name))
            playerLoc = self.loc
            console.print('\nInvestigating the globe further, you notice the eight black squares are located in the following countries: Peru, Mexico, England, France, Egypt, Jordan, India, and China.')       
            
    def Touch(self):
        global playerLoc
        if playerLoc == self.loc:
            console.print(str(self.touch))
        else:
            console.print('\nYou move toward the ' + str(self.name))
            playerLoc = self.loc
            console.print(str(self.touch))          
                                    
    def Move(self):
        global playerLoc
        if playerLoc == self.loc and self.move == 'false':
            console.print('Strangely, the globe is bolted to the floor. It is a shame, because you would really like to move it. Some things, it appears, are just not meant to be.')
        elif playerLoc == self.loc and self.move == 'true':
            console.print('you remove the painting from its hook and find a safe hidden in the wall behind it.')
            #wallSafe = 'found'
        elif playerLoc != self.loc and self.move == 'false':
            console.print('\nYou walk to the ' + str(self.name) + ' and attempt to move it. Strangely, the globe is bolted to the floor. It is a shame, because you would really like to move it. Some things, it appears, are just not meant to be.')           
            playerLoc = self.loc
        elif playerLoc != self.loc and self.move == 'true':
            console.print('you move to get to into a better position.')
            console.print('you walk to the ' + str(self.name) + ' move it to the side, and look around the newly revealed area beneath. Finding nothing of interest, you return the ' + str(self.name) + 'to its original position.')
            #wallSafe = 'found'            
            playerLoc = self.loc

    def Walk(self):
      global playerLoc
      if playerLoc == self.loc:
        console.print('\nYou are already by the ' + str(self.name))         
      elif playerLoc != self.loc:
        console.print('\nYou walk to the ' + str(self.name))
        
    def Unlock(self):
      global playerLoc
      console.print('\nAs you plaYou hear a small click, and the globe gently pops open along the equator. Inside the globe, you find an old, incandescent light bulb.')        
      lightBulb.state = 'found'
      self.state = 'unlocked'

             
        
            
class Window(Object):
    def __init__(self):
        super().__init__(name = 'window',
                         desc = 'a small window, looking down onto a darkened city landscape, dotted with building lights and the distant glow of passing cars.',
                         touch = "\nYou touch the window, noticing a slight chill to the glass. You gently breathe on it, and write '" + (yourName) + " was here!' in the condensation. You feel affirmed! Then you watch as this proof of your unique existence fades to nothingness, as if you had never, in fact, been here at all.",
                         state = 'found',
                         loc = 'south',
                         move = 'false')
    def look(self):
        global playerLoc
        if playerLoc == self.loc:
            console.print('\nIt is ' + str(self.desc))
        else:
            console.print('\nYou move toward the ' + str(self.name))
            playerLoc = self.loc
            console.print('\nYou see it is ' + str(self.desc))
            
    def Touch(self):
        global playerLoc
        if playerLoc == self.loc:
            console.print(str(self.touch))
        else:
            console.print('\nYou move toward the ' + str(self.name))
            playerLoc = self.loc
            console.print(str(self.touch))          
                                    
    def Move(self):
        global playerLoc
        if playerLoc == self.loc and self.move == 'false':
            console.print('\nMoving the window is not something you really have the tools to do.')
        elif playerLoc != self.loc and self.move == 'false':
            console.print('\nYou walk to the ' + str(self.name) + ' and attempt to move it. It is only then that you realize that moving a window is a weird thing to do on a whim. Besides, you have not the tools to accomplish this task in the first place.')           
            playerLoc = self.loc
            
    def Open(self):
        global playerLoc
        if playerLoc == self.loc:
            console.print("\nYou give your mightiest effort in an attempt to open the window but it does not budge. It is either locked, or, it was never designed to be opened in the first place.")
        else:
            console.print('\You move toward the ' + str(self.name))
            playerLoc = self.loc
            console.print("\nYou give your mightiest effort in an attempt to open the window but it does not budge. It is either locked, or, it was never designed to be opened in the first place.")
            
    def Close(self):
            console.print("\nIt is already closed.")

    def Walk(self):
      global playerLoc
      if playerLoc == self.loc:
        console.print('\nYou are already by the ' + str(self.name))         
      elif playerLoc != self.loc:
        console.print('\nYou walk to the ' + str(self.name))             

class Filing_Cabinet(Object):
    def __init__(self):
        super().__init__(name = 'filing cabinet',
                         desc = 'a small, grey steel filing cabinet. There is a small lock visible next to the handle',
                         touch = "\nYou touch the cabinet, running your fingers slowly along its top, dreaming of maybe one day owning a small, steel grey filing cabinet. You then look behind it, and all around it too, but discover nothing else unusual about it. 'It has one job, and it does it well,' you think to yourself. 'One day...' You hand lingers for just a moment before you return again to the problem of escaping this room.",
                         state = 'locked',
                         loc = 'southwest',
                         move = 'false')
    def look(self):
        global playerLoc
        if playerLoc == self.loc:
            console.print('\nIt is ' + str(self.desc))
            
        else:
            console.print('\nYou move toward the ' + str(self.name))
            time.sleep(1)
            playerLoc = self.loc
            console.print('\nYou see it is ' + str(self.desc))
            
    def Touch(self):
        global playerLoc
        if playerLoc == self.loc:
            console.print(str(self.touch))
        else:
            console.print('\nYou move toward the ' + str(self.name))
            playerLoc = self.loc
            console.print(str(self.touch))          
                                    
    def Move(self):
        global playerLoc
        if playerLoc == self.loc and self.move == 'false':
            console.print('\nYou carefully lift the filing cabinet and peek underneath it. Unfortunately, your search reveals nothing new.')
        elif playerLoc != self.loc and self.move == 'false':
            console.print('\nYou walk to the ' + str(self.name) + '. You then carefully lift it and peek underneath. Unfortunately, your search reveals nothing new.')           
            playerLoc = self.loc

    def Open(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'locked':
          console.print('\nThe cabinet is locked')
        elif playerLoc != self.loc and self.state == 'locked':
          console.print('\nYou move towards the filing cabinet and attempt to open it, but it is locked.')
          playerLoc = self.loc
        elif playerLoc == self.loc and self.state == 'unlocked':
          console.print('\nLooking inside the filing cabinet, you see ' + str(cabinetItems)[1:-1])
          stonehenge.state = 'found'
        elif playerLoc != self.loc and self.state == 'unlocked':
          console.print('\nYou move towards the filing cabinet. Looking inside the cabinet, you see a small model of Stonehenge.')
          stonehenge.state = 'found'
          playerLoc = self.loc   

    def Unlock(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'locked' and smallKey.state == 'owned':
          console.print('\nYou insert the small key into the filing cabinet lock, and the lock turns with ease. Inside the cabinet, you see a small model of Stonehenge.')
          self.state = 'unlocked'
          stonehenge.state = 'found'
        elif playerLoc != self.loc and self.state == 'locked' and smallKey.state == 'owned':
          console.print('\nYou walk to the filing cabinet, insert the small brass key into the lock, and unlock it. Inside the cabinet, you find a small model of Stonehenge.')
          self.state = 'unlocked'  
          stonehenge.state = 'found'
          playerLoc = self.loc
        elif playerLoc == self.loc and self.state == 'unlocked' and smallKey.state == 'owned':
          console.print('\nIt is already unlocked')
        elif playerLoc != self.loc and self.state == 'unlocked' and smallKey.state == 'owned':
          console.print('\nYou walk to the filing cabinet and attempt to unlock it, and then realize it is already unlocked') 
        else:
          fail()   

    def Walk(self):
      global playerLoc
      if playerLoc == self.loc:
        console.print('\nYou are already by the ' + str(self.name))         
      elif playerLoc != self.loc:
        console.print('\nYou walk to the ' + str(self.name))                                          
            
class Desk(Object):
    def __init__(self):
        super().__init__(name = 'desk',
                         desc = 'a desk with one drawer under the desktop. On the desktop, you see an old computer and various post-it notes.',
                         touch = '\nYou search around the desk, giving it little pushes and leans, and decide it is sturdy enough, with very little wobble. Other than the Post-It notes, the computer and the drawer, there is nothing else of note about the desk.',
                         state = 'locked',
                         loc = 'southwest',
                         move = 'false')
    def look(self):
        global deskSeen
        global playerLoc
        if playerLoc == self.loc:
            console.print('\nYou see ' + str(self.desc))
            deskSeen = ['true']
            pencil.state = 'found'
            paperClip.state = 'found'
            #postIts.state = 'found'
            pinkPostIts.state = 'found'
            bluePostIts.state = 'found'
            greenPostIts.state = 'found'
            whitePostIts.state = 'found'                                    
        else:
            console.print('\nYou move to get a better look at the desk, and see ' + str(self.desc))
            deskSeen = ['true']
            pencil.state = 'found'
            paperClip.state = 'found'
            pinkPostIts.state = 'found'
            bluePostIts.state = 'found'
            greenPostIts.state = 'found'
            whitePostIts.state = 'found'             
            playerLoc = self.loc
            
    def Touch(self):
        global playerLoc
        if playerLoc == self.loc:
            console.print(str(self.touch))
        else:
            console.print('\nYou move toward the ' + str(self.name))
            playerLoc = self.loc
            console.print(str(self.touch))
            
    def Walk(self):
      global playerLoc
      if playerLoc == self.loc:
        console.print('\nYou are already by the ' + str(self.name))         
      elif playerLoc != self.loc:
        console.print('\nYou walk to the ' + str(self.name))             
            
    def Unlock(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'locked' and 'a medium sized steel key' in inventory:
          console.print('\nYou insert the steel key into the desk drawer lock, and the lock turns with a click. Inside the drawer you find a small brass key and a small model of the Great Wall of China.')
          self.state = 'unlocked'
          greatWall.state = 'found'
          smallKey.state = 'found'
        elif playerLoc != self.loc and self.state == 'locked' and 'a medium sized steel key' in inventory:
          console.print('\nYou walk to the desk, insert the steel key into the lock in the drawer, and the lock turns with a click. Inside the drawer you find a small brass key and a small model of the Great Wall of China.')
          self.state = 'unlocked'  
          greatWall.state = 'found'
          smallKey.state = 'found'
          playerLoc = self.loc
        elif playerLoc == self.loc and self.state == 'unlocked' and 'a medium sized steel key' in inventory:
          console.print('\nIt is already unlocked.')
        elif playerLoc != self.loc and self.state == 'unlocked' and 'a medium sized steel key' in inventory:
          console.print('\nYou walk to the desk and attempt to unlock its drawer, and then realize it is already unlocked.') 
          playerLoc = self.loc
        else:
          fail() 

    def Move(self):
        global playerLoc
        if playerLoc == self.loc and self.move == 'false':
            console.print('\nYou relocate the desk so that it sits under the window, leaving an ugly, empty space in the room where the desk once was. Realizing how terrible this end of the room now looks, you quickly return the desk to its original spot.')
        elif playerLoc != self.loc and self.move == 'false':
            console.print('\nYou relocate the desk so that it sits under the window, leaving an ugly, empty space in the room where the desk once was. Realizing how terrible this end of the room now looks, you quickly return the desk to its original spot.')           
            playerLoc = self.loc

    def lookPostIts(self):
        global playerLoc
        if playerLoc == self.loc and deskSeen == ['true']:
          console.print('\nYou take a closer look at the Post-It notes on the desk.')
          console.print('\nYou see that each Post-It note except one has two letters written on it, the other note having three letters written on it. As well, there are a variety of different colours of notes. Taking a moment to count them up, you see that there are 4 blue notes, 4 pink notes, 1 white note and 1 green note.')
        elif playerLoc != self.loc and deskSeen == ['true']:
          console.print('\nYou walk to the desk to take a closer look at the Post-It notes.')
          playerLoc = self.loc
          console.print('\nYou see that each Post-It note except one has two letters written on it, the other note having three letters written on it. As well, there are a variety of different colours of notes. Taking a moment to count them up, you see that there are 4 blue notes, 4 pink notes, 1 white note and 1 green note.')
        else:
            fail()

    def TakePostIts(self):
        global playerLoc
        if playerLoc == self.loc and 'post-it notes of various colours' in deskItems and deskSeen == ['true']:
          console.print('\nYou take the Post-It notes.')
          inventory.append['4 pink post-it notes', '4 blue post-it notes', '1 white post-it note', '1 green post-it note']
          deskItems.remove['post-it notes of various colours']
          pinkPostIts.state = 'owned'
          bluePostIts.state = 'owned'
          whitePostIts.state = 'owned'
          greenPostIts.state = 'owned'
        elif playerLoc != self.loc and 'post-it notes of various colours' in deskItems and deskSeen == ['true']:
          console.print('\nYou take the Post-It notes from the desk in the corner.')
          inventory.append['4 pink post-it notes', '4 blue post-it notes', '1 white post-it note', '1 green post-it note']
          deskItems.remove['post-it notes of various colours']
          pinkPostIts.state = 'owned'
          bluePostIts.state = 'owned'
          whitePostIts.state = 'owned'
          greenPostIts.state = 'owned'
          playerLoc = self.loc
        else:
          fail()      

    def lookDrawer(self):
        global playerLoc
        if playerLoc == self.loc and self.state == 'locked':
          console.print('\nThe drawer is locked.')
        elif playerLoc != self.loc and self.state == 'locked':
          console.print('\nYou move towards the desk and attempt to open its drawer, but it is locked.')
          playerLoc = self.loc
        if playerLoc == self.loc and self.state == 'unlocked':
          console.print('\nLooking inside the desk drawer, you see ' + str(drawerItems)[1:-1])
          greatWall.state = 'found'
          smallKey.state = 'found'
        elif playerLoc != self.loc and self.state == 'unlocked':
          console.print('\nYou move towards the desk. looking inside the drawer, you see ' + str(drawerItems)[1:-1])
          greatWall.state = 'found'
          smallKey.state = 'found'
          playerLoc = self.loc      

class Basil_Left(Object):
    def __init__(self):
        super().__init__(name = 'st basils cathedral',
                         desc = "Looking closer at the framed picture, you see that it is actually two nearly identical photographs of Saint Basil's Cathedral, placed side by side.",
                         touch = 'you search around the picture, hoping to accomplish...something, but nothing happens',
                         state = 'lost',
                         loc = 'west',
                         move = 'false')
    def look(self):
        global playerLoc
        if playerLoc == self.loc: 
          console.print (str(self.desc) + '. Please look at the screen for a more detailed look at the picture.')
          showImage = subprocess.Popen(["python3", "-m", "wand.display", "/home/pi/Robot_Files/Escape!/media/StBasils.jpg"])          
          #time.sleep(15)
          #showImage.kill()          
        elif playerLoc != self.loc:
          console.print('you walk towards the picture. ' + str(self.desc) + '. Please look at the screen for a more detailed look at the picture.')
          showImage = subprocess.Popen(["python3", "-m", "wand.display", "/home/pi/Robot_Files/Escape!/media/StBasils.jpg"])         
          #time.sleep(15)
          #showImage.kill()          
          playerLoc = self.loc

    def Sign(self):
        global playerLoc
        if playerLoc == self.loc: 
          console.print ('\nYou place the last of the sketches upon the shelves within the display, and take a step back. After a brief moment of intense anticipation....You head a gentle clunking sound coming from the bottom of the display. Looking closer at the sound, you see that a trap door has opened up in the display base, and inside that trap door you find a small model of Machu Picchu.') 
          machuPicchu.state = 'found'
        elif playerLoc != self.loc:
          console.print('\nYou place the last of the sketches upon the shelves within the display, and take a step back. After a brief moment of intense anticipation....You head a gentle clunking sound coming from the bottom of the display. Looking closer at the sound, you see that a trap door has opened up in the display base, and inside that trap door you find a small model of Machu Picchu.')     
          playerLoc = self.loc
          machuPicchu.state = 'found'

    def Window(self):
        global playerLoc
        if playerLoc == self.loc: 
          console.print ('you press firmly the on window in one of the towers in the picture of Saint Basils Cathedral. A faint hum emerges from somewhere behind the picture, and the picture itself begins to roll up into its frame, revealing a hidden space in the wall behind. In the space you find a small model of Machu Picchu.') 
        elif playerLoc != self.loc:
          console.print('you walk towards the picture of Saint Basils Cathedral, and press firmly on the window you see in one of the towers. A faint hum emerges from somewhere behind the picture, and the picture begins to roll up into the frame itself, revealing a hidden space in the wall behind. In the space you find a small model of Machu Picchu.')
          playerLoc = self.loc

    def Opening(self):
        global playerLoc
        if playerLoc == self.loc: 
          console.print ('you press the opening in one of the towers on the picture of Saint Basils Cathedral. A faint hum emerges from somewhere behind the picture, and the picture itself begins to roll up into its frame, revealing a hidden space in the wall behind. In the space you find a model of Machu Picchu.') 
          machuPicchu.state = 'found'
        elif playerLoc != self.loc:
          console.print('you walk towards the picture of Saint Basils Cathedral, and press firmly on the opening you see in one of the towers. A faint hum emerges from somewhere behind the picture, and the picture begins to roll up into the frame itself, revealing a hidden space in the wall behind. In the space you find a model of Machu Picchu.')
          playerLoc = self.loc
          machuPicchu.state = 'found'

    def Dome(self):
        global playerLoc
        if playerLoc == self.loc: 
          console.print ('you press firmly on the dome of the left tower in the picture of Saint Basils Cathedral. A faint hum emerges from somewhere behind the picture, and the picture itself begins to roll up into its frame, revealing a hidden space in the wall behind. In the space you find a model of Machu Picchu.') 
          machuPicchu.state = 'found'
        elif playerLoc != self.loc:
          console.print('you walk towards the picture of Saint Basils Cathedral, and press firmly on the dome of the left tower. A faint hum emerges from somewhere behind the picture, and the picture begins to roll up into the frame itself, revealing a hidden space in the wall behind. In the space you find a model of Machu Picchu.')     
          playerLoc = self.loc
          machuPicchu.state = 'found'

    def Touch(self):
        global playerLoc
        if playerLoc == self.loc: 
          console.print (str(self.touch)) 
        elif playerLoc != self.loc:
          console.print('you walk towards the photograph of Saint Basils. ' + (self.touch))   
          playerLoc = self.loc   

    def Walk(self):
      global playerLoc
      if playerLoc == self.loc:
        console.print('you are already by the ' + str(self.name))         
      elif playerLoc != self.loc:
        console.print('you walk to the ' + str(self.name))                      

class Basil_Right(Object):
    def __init__(self):
        super().__init__(name = 'st basils cathedral',
                         desc = "a photograph of Saint Basils Cathedral at night",
                         touch = 'you feel around the picture, hoping to accomplish...something, but nothing happens',
                         state = 'lost',
                         loc = 'west',
                         move = 'false')
    def look(self):
        global playerLoc
        if playerLoc == self.loc: 
          console.print ('it is ' + str(self.desc) + '. Please look at the screen for a more detailed look at the picture.')
          showImage = subprocess.Popen(["python3", "-m", "wand.display", "/home/pi/Robot_Files/Escape!/media/StBasils_Right.jpg"])
          time.sleep(15)
          showImage.kill()          
        elif playerLoc != self.loc:
          console.print('you walk towards the picture. You see it is ' + str(self.desc) + '. Please look at the screen for a more detailed look at the picture.')
          showImage = subprocess.Popen(["python3", "-m", "wand.display", "/home/pi/Robot_Files/Escape!/media/StBasils_Right.jpg"])
          time.sleep(15)
          showImage.kill()          
          playerLoc = self.loc

    def Touch(self):
        global playerLoc
        if playerLoc == self.loc: 
          console.print (str(self.touch)) 
        elif playerLoc != self.loc:
          console.print('you walk towards the photograph of Saint Basils. ' + (self.touch))   
          playerLoc = self.loc

class RecordPlayer(Object):
    def __init__(self):
        super().__init__(name = 'record player',
                         desc = "an antique phonographic record player, with a large acoustic horn spiraling out of the top. On a shelf beside the record player you see a collection of records.",
                         touch = '\nThe record player feels very well made, and is remarkably free of dents and scratches given its age. You wish things were made this well nowadays.',
                         state = 'found',
                         loc = 'west',
                         move = 'false')

    def look(self):
        global playerLoc
        if playerLoc == self.loc: 
          console.print ('it is ' + str(self.desc)) 
          records.state = 'found'
        elif playerLoc != self.loc:
          console.print('\nMoving closer to the ' + str(self.name) + ' you notice it is ' + str(self.desc))  
          playerLoc = self.loc    

    def Touch(self):
        global playerLoc
        if playerLoc == self.loc: 
          console.print(str(self.touch)) 
        elif playerLoc != self.loc:
          console.print('\nYou walk towards the ' + str(self.name) + '. ' + (self.touch))    
          playerLoc = self.loc 

    def Play(self):
        global playerLoc
        if playerLoc == self.loc:
          console.print('\nYou pull out a record at random from the cabinet, and enjoy its fine melodies and rhythms. Your spirits uplifted, you return to your efforts to escape from the room with renewed determination and confidence.') 
        elif playerLoc != self.loc:
          console.print('\nYou pull out a record at random from the cabinet, and enjoy its fine melodies and rhythms. Your spirits uplifted, you return to your efforts to escape from the room with renewed determination and confidence.')
          playerLoc = self.loc   

    def PlayMoby(self):
        global playerLoc
        if playerLoc == self.loc:
          console.print('\nYou take the Moby album Play from the collection, and pull the record out. As you do, a small, gold token falls out of the sleeve and drops to the floor.')
          token.state = 'found'      
        elif playerLoc != self.loc:
          console.print('\nYou walk to the record collection, take the Moby album Play from the collection, and pull the record out. As you do, a small, gold token falls out of the sleeve and drops to the floor.')
          token.state = 'found'
          playerLoc = self.loc

    def Walk(self):
      global playerLoc
      if playerLoc == self.loc:
        console.print('\nYou are already by the ' + str(self.name))         
      elif playerLoc != self.loc:
        console.print('\nYou walk to the ' + str(self.name))           

class Piano(Object):
    def __init__(self):
        super().__init__(name = 'piano',
                         desc = 'an apartment sized upright piano',
                         touch =  "\nYou search all over the piano for clues. You play each key and push each pedal. You open the lid and peek inside, and marvel at the complex engineering of the instrument's actions. Your search for clues, however, comes up empty.",
                         state = 'unplayed',
                         loc = 'west',
                         move = 'false')

    def look(self):
        global playerLoc
        if playerLoc == self.loc: 
          console.print('\nIt is ' + str(self.desc)) 
        elif playerLoc != self.loc:
          console.print('\nIt is ' + str(self.desc))  
          playerLoc = self.loc    

    def Move(self):
        global playerLoc
        if playerLoc == self.loc: 
          console.print('\The piano is far too heavy for you to move.') 
        elif playerLoc != self.loc:
          console.print('\nYou walk over to try and move the piano, and find yourself hopelessly incapable of budging it, even an inch.')  
          playerLoc = self.loc           

    def Touch(self):
        global playerLoc
        if playerLoc == self.loc: 
          console.print("\nYou search all over the piano for clues. You play each key and push each pedal. You open the lid and peek inside, and marvel at the complex engineering of the instrument's actions. Your search for clues, however, comes up empty.") 
        elif playerLoc != self.loc:
          console.print("\nYou search all over the piano for clues. You play each key and push each pedal. You open the lid and peek inside, and marvel at the complex engineering of the instrument's actions. Your search for clues, however, comes up empty.")    
          playerLoc = self.loc    

    def Play(self):
        global playerLoc
        if playerLoc == self.loc and lamp.state == 'bulbOut' and self.state == 'unplayed': 
          console.print("\nYou play a few pieces that you know from memory, including the best rendition of the theme song to 'Jeopardy!' you have ever played. You wish there was an audience to have witnessed such excellence, alas, you are still trapped in this room, alone.") 
          self.state = 'played'
        elif playerLoc != self.loc and lamp.state == 'bulbOut' and self.state == 'unplayed':
          console.print("\nYou walk over to the piano and play a few pieces that you know from memory, including the best rendition of the theme song to 'Jeopardy!' you have ever played. You wish there was an audience to have witnessed such excellence, alas, you are still trapped in this room, alone.")    
          playerLoc = self.loc
          self.state = 'played'
        elif lamp.state == 'bulbIn' and self.state == 'played':
          console.print('\nYou sit down at the piano, with a renewed determination to solve the riddle of its presence in the room. What notes would you like to play?')
          solution = input('Notes: ').lower()
          if 'a cage aced' in solution or 'acageaced' in solution:
              console.print('\nYou play the notes revealed by the lamp on the table. After a brief pause, you hear a sound of the lifting of some kind of latch coming from your right, followed by a gentle creaking noise. You turn to look at the source of the sounds, and see that the only door in the room has opened up.') 
              door.state = 'unlocked'                              
          else:
              console.print('\nYou play your chosen notes, and, while you appreciate the tonal quality of the piano, that is all that happens. The piano still mocks you with its presence.')    

        elif lamp.state == 'bulbIn' and self.state == 'unplayed':
          console.print('\nYou sit down at the piano, your fingers ready on the keys. What notes would you like to play?')
          solution = input('Notes: ').lower()
          if 'a cage aced' in solution or 'acageaced' in solution:
              console.print('\nYou play the notes revealed by the lamp on the table. After a brief pause, you hear a sound of the lifting of some kind of latch coming from your right, followed by a gentle creaking noise. You turn to look at the source of the sounds, and see that the only door in the room has opened up.') 
              door.state = 'unlocked'                              
          else:
              console.print('\nYou play your chosen notes, and, while you appreciate the tonal quality of the piano, that is all that happens. The piano still mocks you with its presence.') 

    def Walk(self):
      global playerLoc
      if playerLoc == self.loc:
        console.print('you are already by the ' + str(self.name))         
      elif playerLoc != self.loc:
        console.print('you walk to the ' + str(self.name))                                

door = Door()
statue = Statue()
shapesPuzzle = ShapesPuzzle()

couch = Couch()
table = Table()
lamp = Lamp()
box = Box()

bookShelfOne = Book_Shelf_One()
bookShelfTwo = Book_Shelf_Two()
painting = Painting()
wallSafe = WallSafe()

globe = Globe()
window = Window()
filingCabinet = Filing_Cabinet()
desk = Desk()

basilLeft = Basil_Left()
basilRight = Basil_Right()
recordPlayer = RecordPlayer()
piano = Piano()

rug = Rug()
hatch = Hatch()



