#!/usr/bin/env python3

import time
import os, subprocess
import random
#from colorama import Fore
#from colorama import Back
import rich
from rich.console import Console
#console.print(Fore.GREEN)
#console.print(Back.BLACK)

console = Console(width=80)
console = Console(style = "bold green")

console.print('\n\n###################################################\n\n\n\n                    ESCAPE THIS!          \n\n                THE WONDER EDITION        \n\n\n\n\n                  by Myxtapes 2022        \n\n\n###################################################')     

console.print('\n')
time.sleep(2)

yourName = input("Please input your name: ")

console.print("\nWelcome to Escape This! The Wonder Edition. Your goal is to escape from your starting room. To play, simply type in the commands you would like to execute, followed by the object you would like to interact with. Possible commands are: \n\nlook\nsearch\ntake\nuse\n\nput\nwalk\nmove\nopen\nunlock\nread\nplay\n\nAt anytime, you can check this list of commands by typing 'commands'.\n\nIf you would like to check the current state of your inventory, type 'inventory'.\n")
print("\nWhen you are ready to begin, press 'Enter'.")
input("")

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
failQuotes = ["\nThat didn't seem to work", "\nHmm...That didn't seem to accomplish anything.", "\nSurprisingly, nothing happens.", "\nNothing happens.", "\nNothing of note occurs.", "\nBupkis.", "\nNada parece haber pasado."]
  
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
          console.print('n\You get closer to the door. ' + str(self.touch))
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
          console.print ('\nYou place the last of the sketches upon the shelves within the display, and take a step back. After a brief moment of intense anticipation...You hear a gentle clunking sound coming from the bottom of the display. Looking closer at the sound, you see that a trap door has opened up in the display base, and inside that trap door you find a small model of Machu Picchu.') 
          machuPicchu.state = 'found'
        elif playerLoc != self.loc:
          console.print('\nYou place the last of the sketches upon the shelves within the display, and take a step back. After a brief moment of intense anticipation...You hear a gentle clunking sound coming from the bottom of the display. Looking closer at the sound, you see that a trap door has opened up in the display base, and inside that trap door you find a small model of Machu Picchu.')     
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
        if playerLoc == self.loc and token.state == 'lost':
          console.print('\nYou take the Moby album Play from the collection, and pull the record out. As you do, a small, gold token falls out of the sleeve and drops to the floor.')
          token.state = 'found'
        elif playerLoc == self.loc and token.state != 'lost':
          console.print('\nYou take the Moby album Play from the collection, and pull the record out. You look inside the sleeve for more gold tokens, alas, there are no more to be found.') 
        elif playerLoc != self.loc and token.state == 'lost':
          console.print('\nYou walk to the record collection, take the Moby album Play from the collection, and pull the record out. As you do, a small, gold token falls out of the sleeve and drops to the floor.')
          token.state = 'found'
          playerLoc = self.loc
        elif playerLoc != self.loc and token.state != 'lost':
          console.print('\nYou walk to the record collection, take the Moby album Play from the collection, and pull the record out. You look inside the sleeve for more gold tokens, alas, there are no more to be found.')
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


#INITIALIZE GAME 
  
def main(): 

  """PUZZLE STATES"""
  score = 0 
  playerLoc = 'north' 
  playerOrient = 'south' 
  global countries 
  countries = ['Peru', 'Mexico', 'England', 'France', 'Egypt', 'Jordan', 'India', 'China'] 
  wonderModels = ['a small model of the Great Pyramid', 'a small model of the Taj Mahal', 'a small model of the Great Wall', 'a small model of the Eiffel Tower', 'a small model of Petra', 'a small model of Stonehenge', 'a small model of Machu Picchu', 'a small model of Chichen Itza'] 
  countryList = ['Peru', 'Mexico', 'England', 'France', 'Egypt', 'Jordan', 'India', 'China'] 
  global modelInventory 
  Trial = {} 
  mahalModelX = 0 
  gizaModelX = 0 
  eiffelModelX = 0 
  wallModelX = 0 
  petraModelX = 0 
  stonehengeModelX = 0 
  machuModelX = 0 
  chichenModelX = 0 
    
  shapesSolution = {'circle':'3', 'triangle':'0', 'square':'5', 'trapezoid':'4', 'pentagon':'2', 'hexagon':'1'} 
  shapesState = {'circle':'5', 'triangle':'2', 'square':'4', 'trapezoid':'1', 'pentagon':'3', 'hexagon':'0'} 
  shapesRange = ['0', '1', '2', '3', '4', '5'] 
  circleX = '5' 
  triangleX = '2' 
  squareX = '4' 
  trapezoidX = '1' 
  pentagonX = '3' 
  hexagonX = '0' 

  ancientWonders = ['statue', 'temple', 'mausoleum', 'garden', 'colossus', 'lighthouse', 'pyramid']
  ancientSolution = []
  sketch = 'askew'
  sketchSolve = True
  display = 'unsolved'
  modelKeys = ['the Great Wall', 'the Great Pyramid', 'the Eiffel Tower', 'Petra', 'Machu Picchu', 'Chichen Itza', 'Stonehenge', 'the Taj Mahal']
  modelAttempt = []
  peruX = 0
  mexicoX = 0
  englandX = 0
  franceX = 0
  egyptX = 0
  jordanX = 0
  indiaX = 0
  chinaX = 0
  startTime = time.perf_counter()



  """CORE GAME / INPUT LOOPS"""
  
  while True:

    text = input("\nCommand: ").lower()
    
    """SYNONYMS / COMMAND REPLACE"""
    text = text.replace ('touch','search')
    text = text.replace('put','use')

    """GAME INPUT AND RESPONSE LOGIC"""
    
    if 'commands' in text:
      console.print("\nPossible commands are: \n\nlook\nsearch\nwalk\nmove\nopen\nunlock\ntake\nread\npush/pull\nplay\nuse\n")
      
    elif 'inventory' in text:
      if len(inventory) == 0 and len(modelInventory) == 0:
        console.print("\nYou are not carrying anything.")
      
      else:
        console.print("\nYou are carrying:\n")
        if len(modelInventory) != 0:
          for x in modelInventory:
            console.print(str(x))
        if len(inventory) != 0:
          for y in inventory:
            console.print(str(y))
        #console.print(str(inventory)[3:-1])

    #ORIENTATION inputs
      
    elif 'listen' in text: 
      console.print('\nYou listen carefully to the room, ready to take note of any unusual sound. You hear nothing out of the ordinary, however. Nothing at all, actually, except the sound of your own heartbeat.') 
      
    elif 'where am I' in text or 'look around' in text or 'look' in text and 'room' in text or 'what do I see' in text: 
      console.print("\nYou are in what looks to be some kind of study, comfortably furnished with bookshelves and other study-like furniture, a piano, a record player, paintings and pictures upon the wall, and various other neat objects. The ceiling is high, and the floor is made of hardwood, with a large rug upon it. You take particular note of the rug, upon which you notice the design of a large compass. You decide it would be wise to use the compass as a means to orient and navigate yourself around the room.")

    elif text == 'look':
      console.print("\nYou are in what looks to be some kind of study, comfortably furnished with bookshelves and other study-like furniture, a piano, a record player, paintings and pictures upon the wall, and various other neat objects. The ceiling is high, and the floor is made of hardwood, with a large rug upon it. You take particular note of the rug, upon which you notice the design of a large compass. You decide it would be wise to use the compass as a means to orient and navigate yourself around the room.")
      
    elif 'look' in text and 'north' in text: 
      console.print('\nLooking at the North wall, you see the only door in the room, which must be your way out. On the wall to the left of the door, you see a strange panel with shapes on it. On the floor to the right of the door, you see a reproduction of the Statue of Liberty. In the Northeast corner, to the right of the statue, there is a couch and small table.') 
    elif 'look' in text and 'east' in text: 
      console.print('\nLooking to the East wall, you see two large bookshelves, both filled with many books. To the left of the bookshelves, you see a couch and small table. On the wall to the right of the bookshelves, there is a painting. In the Southeast corner, to the right of the painting, there is a large globe.') 
    elif 'look' in text and 'south' in text: 
      console.print('\nLooking to the South wall, you see a window looking out into a city. To the left of the window you see a large globe, and to the right of the window you see a small cabinet. In the Southwest corner, to the right of the cabinet, there is a desk.') 
    elif 'look' in text and 'west' in text: 
      console.print('\nLooking to the West wall, you see a piano, and beside the piano to the left you see a record player. On the North end of the wall, to the right of the piano, you see a large display case.') 

    elif 'look' in text and 'ceiling' in text: 
      console.print('\nAs far as your limited knowlegde of ceilings goes, it looks like a nice ceiling.') 
    elif 'look' in text and 'floor' in text: 
      rug.look() 

    #wallCHOICE inputs
    
    elif 'look' in text and 'wall' in text: 
      wallChoice = input('\nWhich wall would you like to look at: the North, the East, the South, or the West wall?\n\nWall choice: ')
      if 'north' in wallChoice:
        console.print('\nLooking at the North wall, you see the only door in the room, which must be your way out. On the wall to the left of the door, you see a strange panel with shapes on it. On the floor to the right of the door, you see a reproduction of the Statue of Liberty. In the Northeast corner, to the right of the statue, there is a couch and small table.')
        continue
      elif 'south' in wallChoice:
        console.print('\nLooking to the South wall, you see a window looking out into a city. To the left of the window you see a large globe, and to the right of the window you see a small cabinet. In the Southwest corner, to the right of the cabinet, there is a desk.') 
        continue
      elif 'east' in wallChoice:
        console.print('\nLooking to the East wall, you see two large bookshelves, both filled with many books. To the left of the bookshelves, you see a couch and small table. On the wall to the right of the bookshelves, there is a painting. In the Southeast corner, to the right of the painting, there is a large globe.') 
        continue
      elif 'west' in wallChoice:
        console.print('\nLooking to the West wall, you see a piano, and beside the piano to the left you see a record player. On the North end of the wall, to the right of the piano, you see a large framed picture.') 
        continue
      else:
        console.print("\nYou return your efforts to the room at large.")
        continue

    #WALK inputs

    elif 'walk' in text and 'north' in text: 
      console.print('\nYou walk over to the north side of the room') 
      playerLoc = 'north' 
    elif 'walk' in text and 'east' in text: 
      console.print('\nYou walk over to the east side of the room') 
      playerLoc = 'east' 
    elif 'walk' in text and 'south' in text: 
      console.print('\nYou walk over to the south side of the room') 
      playerLoc = 'south' 
    elif 'walk' in text and 'west' in text:  
      console.print('\nYou walk over to the west side of the room') 
      playerLoc = 'west' 

    #wONDER MODEL inputs
    
    elif 'take' in text and 'machu' in text or 'take' in text and 'picchu' in text: 
       machuPicchu.Take()             
    elif 'take' in text and 'chichen' in text or 'take' in text and 'itza' in text: 
       chichenItza.Take()  
    elif 'take' in text and 'stonehenge' in text: 
       stonehenge.Take()  
    elif 'take' in text and 'eiffel' in text or 'take' in text and 'tower' in text: 
       eiffelTower.Take() 
    elif 'take' in text and 'pyramid' in text or 'take' in text and 'giza' in text: 
       greatPyramid.Take()  
    elif 'take' in text and 'petra' in text: 
       petra.Take()  
    elif 'take' in text and 'mahal' in text or 'take' in text and 'taj' in text: 
       tajMahal.Take()  
    elif 'take' in text and 'wall' in text: 
       greatWall.Take() 

    elif 'look' in text and 'pyramid' in text: 
      greatPyramid.look() 
    elif 'look' in text and 'petra' in text: 
      petra.look() 
    elif 'look' in text and 'stonehenge' in text: 
      stonehenge.look() 
    elif 'look' in text and 'great wall' in text: 
      greatWall.look() 
    elif 'look' in text and 'chichen' in text or 'look' in text and 'itza' in text: 
      chichenItza.look() 
    elif 'look' in text and 'machu' in text or 'look' in text and 'picchu' in text: 
      machuPicchu.look() 
    elif 'look' in text and 'taj' in text or 'look' in text and 'mahal' in text: 
      tajMahal.look()
    elif 'look' in text and 'eiffel' in text or 'look' in text and 'tower' in text: 
      eiffelTower.look() 
      
    elif 'search' in text and 'pyramid' in text: 
      greatPyramid.look() 
    elif 'search' in text and 'petra' in text: 
      petra.look() 
    elif 'search' in text and 'stonehenge' in text: 
      stonehenge.look() 
    elif 'search' in text and 'great wall' in text: 
      greatWall.look() 
    elif 'search' in text and 'chichen' in text or 'search' in text and 'itza' in text: 
      chichenItza.look() 
    elif 'search' in text and 'machu' in text or 'search' in text and 'picchu' in text: 
      machuPicchu.look() 
    elif 'search' in text and 'taj' in text or 'search' in text and 'mahal' in text: 
      tajMahal.look() 
    elif 'search' in text and 'eiffel' in text or 'search' in text and 'tower' in text: 
      eiffelTower.look() 

    #KEY inputs
      
    elif 'look' in text and 'key' in text and 'iron' in text or 'look' in text and 'large' in text and 'key' in text: 
      ironKey.look() 
    elif 'take' in text and 'key' in text and 'iron' in text or 'take' in text and 'large' in text and 'key' in text: 
      ironKey.Take() 
    elif 'look' in text and 'key' in text and 'steel' in text or 'look' in text and 'medium ' in text and 'key' in text: 
      steelKey.look()              
    elif 'take' in text and 'key' in text and 'steel' in text or 'take' in text and 'medium ' in text and 'key' in text: 
      steelKey.Take() 
    elif 'look' in text and 'key' in text and 'brass' in text or 'look' in text and 'small' in text and 'key' in text: 
      smallKey.look()              
    elif 'take' in text and 'key' in text and 'brass' in text or 'take' in text and 'small' in text and 'key' in text: 
      smallKey.Take() 
    elif 'take' in text and 'key' in text:
      if ironKey.state == "found" or steelKey.state == "found" or smallKey.state == "found":
        console.print('\nWhich key would you like to take?')
        keyInput = input("\nKey: ")
        if 'iron' in keyInput or 'fashioned' in keyInput or 'large' in keyInput:
          ironKey.Take()
          continue
        elif 'brass' in keyInput or 'small' in keyInput:
          smallKey.Take()
          continue
        elif 'steel' in keyInput or 'medium' in keyInput:
          steelKey.Take()
          continue
      else:
        console.print(random.choice(failQuotes))
        
    elif 'look' in text and 'key' in text:
      if ironKey.state == "found" or steelKey.state == "found" or smallKey.state == "found":
        console.print('\nWhich key would you like to look at?')
        keyInput = input("\nKey: ")
        if 'iron' in keyInput or 'fashioned' in keyInput or 'large' in keyInput:
          ironKey.look()
          continue
        elif 'brass' in keyInput or 'small' in keyInput:
          smallKey.look()
          continue
        elif 'steel' in keyInput or 'medium' in keyInput:
          steelKey.look()
          continue
    
      elif ironKey.state == "owned" or steelKey.state == "owned" or smallKey.state == "owned":
        console.print('\nWhich key would you like to look at?')
        keyInput = input("\nKey: ")
        if 'iron' in keyInput or 'fashioned' in keyInput or 'large' in keyInput:
          ironKey.look()
          continue
        elif 'brass' in keyInput or 'small' in keyInput:
          smallKey.look()
          continue
        elif 'steel' in keyInput or 'medium' in keyInput:
          steelKey.look()
          continue
      else:
        console.print(random.choice(failQuotes))
        

    #NORTH WALL inputs

    elif 'look' in text and 'door' in text: 
      door.look() 
    elif 'open' in text and 'door' in text: 
      door.Open() 
    elif 'touch' in text and 'door' in text: 
      door.Touch() 
    elif 'walk' in text and 'door' in text and door.state == 'unlocked':
        midTime = time.perf_counter()
        elapsedTime = (int(midTime) - int(startTime))  
        console.print('\nAfter having been trapped, alone, in this room for ' + str(elapsedTime) + ' seconds, you walk at last through the only door in the room, now open and inviting you through. You have escaped! Thank you for playing Escape This! The Wonder Edition. Stay tuned for more rooms!')
    elif 'walk' in text and 'door' in text: 
      door.Walk()                    

    elif 'move' in text and 'rug' in text or 'under' in text and 'rug' in text: 
      rug.Move() 
    elif 'look' in text and 'rug' in text: 
      rug.look() 
    elif 'touch' in text and 'rug' in text: 
      rug.Touch()   
    elif 'walk' in text and 'rug' in text: 
      rug.Walk()                          
          
    elif 'look' in text and 'hatch' in text: 
      hatch.look() 
    elif 'unlock' in text and 'hatch' in text or 'iron key' in text and 'hatch' in text: 
      hatch.Unlock() 
    elif 'touch' in text and 'hatch' in text: 
      hatch.Touch()  
    elif 'open' in text and 'hatch' in text: 
      hatch.Open()  
    elif 'walk' in text and 'hatch' in text: 
      hatch.Walk()                

    elif 'look' in text and 'statue' in text: 
      statue.look() 
    elif 'search' in text and 'statue' in text: 
      statue.Touch() 
    elif 'light' in text and 'statue' in text or 'light' in text and 'wick' in text: 
      statue.Light() 
    elif 'light' in text and 'torch' in text: 
      statue.Light()   
    elif 'look' in text and 'torch' in text or 'search' in text and 'torch' in text or 'touch' in text and 'torch' in text: 
      console.print('\nYou investigate the torch on the statue more closely. Like the rest of the statue, it is made of metal. You also notice a faint smell of kerosene coming from it. If you brought a flame to the wick in the torch, it would no doubt ignite excellently.') 
    elif 'look' in text and 'pedestal' in text or 'search' in text and 'pedestal' in text: 
      console.print('\nYou focus your attention on the statues pedestal. It is a large, rectangular block of marble. You tap gently around the pedestal, and, based on the sound of your tapping, you note it is likely hollow')                                      
    elif 'walk' in text and 'statue' in text: 
      statue.Walk()                

    elif 'open' in text and 'couch' in text or 'open' in text and 'cushion' in text or 'search' in text and 'cushion' in text: 
      couch.Open() 
    elif 'look' in text and 'couch' in text: 
      couch.look() 
    elif 'search' in text and 'couch' in text: 
      couch.Touch() 
    elif 'move' in text and 'couch' in text: 
      couch.Move() 
    elif 'sit' in text and 'couch' in text: 
      couch.Sit()  
    elif 'walk' in text and 'couch' in text: 
      couch.Walk()  

    #TABLE ITEM inputs

    elif 'look' in text and 'table' in text: 
      table.look() 
    elif 'search' in text and 'table' in text: 
      table.Touch() 
    elif 'move' in text and 'table' in text: 
      table.Move() 
    elif 'walk' in text and 'table' in text: 
      table.Walk()                            

    elif 'look' in text and 'lamp' in text: 
      lamp.look() 
    elif 'search' in text and 'lamp' in text: 
      lamp.Touch() 
    elif 'move' in text and 'lamp' in text: 
      lamp.Move() 
    elif 'on' in text and 'lamp' in text: 
      lamp.On()  
    elif 'off' in text and 'lamp' in text: 
      lamp.Off()  
    elif 'walk' in text and 'lamp' in text: 
      lamp.Walk() 
    
    elif 'take' in text and 'box' in text: 
      box.Take() 
    elif 'open' in text and 'box' in text or 'search' in text and 'box' in text: 
      box.Open() 
    elif 'look' in text and 'box' in text: 
      box.look()  
      
    elif 'light' in text and 'match' in text or 'light' in text and 'matches' in text: 
      matches.Light()
    elif 'use' in text and 'match' in text or 'use' in text and 'matches' in text: 
      matches.Light()

    elif 'take' in text and 'bulb' in text: 
      lightBulb.Take() 
    elif 'look' in text and 'bulb' in text: 
      lightBulb.look() 
    elif 'use' in text and 'lamp' in text and 'bulb' in text or 'put' in text and 'lamp' in text and 'bulb' in text: 
      lightBulb.Use()

    #EAST WALL inputs

    elif 'look' in text and 'bookshelf' in text and 'left' in text: 
        bookShelfOne.look() 
    elif 'walk' in text and 'bookshelf' in text and 'left' in text: 
        bookShelfOne.Walk()                 
    elif 'look' in text and 'bookshelf' in text and 'right' in text: 
        bookShelfTwo.look() 
    elif 'walk' in text and 'bookshelf' in text and 'right' in text: 
        bookShelfTwo.Walk()                 
    elif 'search' in text and 'bookshelf' in text and 'left' in text: 
        bookShelfOne.Touch() 
    elif 'search' in text and 'bookshelf' in text and 'right' in text: 
        bookShelfTwo.Touch() 
    elif 'move' in text and 'bookshelf' in text and 'left' in text: 
        bookShelfOne.Move() 
    elif 'move' in text and 'bookshelf' in text and 'right' in text: 
        bookShelfTwo.Move()
    elif 'move' in text and 'bookshelves' in text:
        bookshelfOne.Move()
    elif 'search' in text and 'bookshelves' in text:
        bookshelfOne.Move()

    elif 'look' in text and 'bookshelf' in text or 'look' in text and 'bookshelves' in text: 
        bookShelfPrompt = input('\nWhich bookshelf would you like to look at? The one on the left or the one on the right? ').lower()             
        if 'left' in bookShelfPrompt: 
            bookShelfOne.look() 
            continue 
        elif 'right' in bookShelfPrompt: 
            bookShelfTwo.look() 
            continue                     
 
    elif 'look' in text and 'prison' in text: 
        prisonCakes.look() 
    elif 'take' in text and 'prison' in text: 
        prisonCakes.Take() 
    elif 'read' in text and 'prison' in text: 
        prisonCakes.Read() 
          
    elif 'look' in text and 'music of moby' in text: 
        moby.look() 
    elif 'take' in text and 'music of moby' in text: 
        moby.Take() 
    elif 'read' in text and 'music of moby' in text: 
        moby.Read() 
          
    elif 'look' in text and 'scrambled' in text: 
        eggs.look() 
    elif 'take' in text and 'scrambled' in text: 
        eggs.Take() 
    elif 'read' in text and 'scrambled' in text: 
        eggs.Read() 

    elif 'look' in text and 'clock' in text: 
        clocks.look() 
    elif 'take' in text and 'clock' in text: 
        clocks.Take() 
    elif 'read' in text and 'clock' in text: 
        midTime = time.perf_counter() 
        elapsedTime = (int(midTime) - int(startTime)) 
        console.print("\nYou try to read The Clock Echoes but note that it opens up to only a single page. Upon this single page, you see just a single sentence. It reads,\n\n'You have spent " + str(elapsedTime) + " seconds trapped, alone, in this room.'\n\nA cold chill runs down your spine.") 
    elif 'look' in text and 'echoes' in text: 
        clocks.look() 
    elif 'take' in text and 'echoes' in text: 
        clocks.Take() 
    elif 'read' in text and 'echoes' in text: 
        clocks.Read()                
          
    elif 'look' in text and 'one' in text and 'bookmark' in text: 
        wondersOne.Bookmark()  
    elif 'look' in text and 'wonders' in text and 'one' in text: 
        wondersOne.look() 
    elif 'take' in text and 'wonders' in text and 'one' in text: 
        wondersOne.Take() 
    elif 'read' in text and 'wonders' in text and 'one' in text: 
        wondersOne.Read() 
           
    elif 'look' in text and 'two' in text and 'bookmark' in text: 
        wondersTwo.Bookmark()                
    elif 'look' in text and 'wonders' in text and 'two' in text: 
        wondersTwo.look() 
    elif 'take' in text and 'wonders' in text and 'two' in text: 
        wondersTwo.Take() 
    elif 'read' in text and 'wonders' in text and 'two' in text: 
        wondersTwo.Read() 

    elif 'look' in text and 'bookmark' in text: 
        wondersTwo.BookmarkCheck() 

    elif 'look' in text and 'paper' in text:
        paper.look()
    elif 'take' in text and 'paper' in text:
        paper.Take()
    
    elif 'look' in text and 'behind' in text and 'painting' in text: 
        painting.Move() 
    elif 'look' in text and 'painting' in text: 
        painting.look() 
    elif 'search' in text and 'painting' in text: 
        painting.Touch() 
    elif 'move' in text and 'painting' in text: 
        painting.Move() 
    elif 'take' in text and 'painting' in text: 
        painting.Move()   
    elif 'walk' in text and 'painting' in text: 
        painting.Walk()                             
         
    elif 'walk' in text and 'safe' in text: 
        wallSafe.Walk() 
    elif 'look' in text and 'safe' in text: 
        wallSafe.look() 
    elif 'touch' in text and 'safe' in text: 
        wallSafe.Touch() 
    elif 'move' in text and 'safe' in text: 
        wallSafe.Move() 
    elif 'open' in text and 'safe' in text: 
        wallSafe.Open()  
    elif '15' in text and '25' in text and '35' in text and 'safe' in text: 
        wallSafe.Unlock()                               
    elif 'unlock' in text and 'safe' in text or 'combination' in text and 'safe' in text: 
        safeCombination = input('\nWhat combination would you like to try?\n\nCombination: ') 
        if '15' in safeCombination and '25' in safeCombination and '35' in safeCombination: 
            wallSafe.Unlock() 
            continue 
        else: 
            console.print('\nYou spin the dial to your chosen numbers, but the safe remains locked.') 
            continue 
         
    elif 'look' in text and 'globe' in text: 
        globe.look() 
    elif 'search' in text and 'globe' in text or 'look' in text and 'black squares' in text: 
        globe.Touch() 
    elif 'move' in text and 'globe' in text: 
        globe.Move() 
    elif 'walk' in text and 'globe' in text: 
        globe.Walk() 

    #GLOBE PUZZLE

    elif 'use' in text and 'globe' in text or 'model' in text and 'globe' in text or 'models' in text and 'globe' in text: 
        if len(modelInventory) == 0: 
          console.print('\nYou attempt to solve the riddle of the globe, but quickly realize you have no idea what to do or where to begin. With that in mind, you return your efforts to the rest of the room.') 
        elif len(modelInventory) < 8: 
          console.print('\nYou attempt to solve the riddle of the globe, but realize you still do not have all that you need. You remind yourself that there are 8 countries with black squares, and you have ' + str(len(modelInventory)) + ' models in your inventory.')                
        else: 
          solving = 1 
          console.print("\nIf at any time you would like to exit the globe puzzle, type 'exit'")
          time.sleep(2)
          while solving == 1:  
            while len(modelAttempt) < 8:
              if solving == 0:
                break
              for x in modelKeys:
                  if solving == 0:  
                    break
                  if x not in modelAttempt:
                    if solving == 0:
                      break
                    countryX = input('\nIn which country would you like to place ' + str(x) + '? ')
                    countryX = countryX.replace('france','France').replace('india','India').replace('china','China').replace('jordan','Jordan').replace('england','England').replace('peru','Peru').replace('mexico','Mexico').replace('egypt','Egypt')            
                    if 'exit' in countryX: 
                          console.print('\nDeciding to focus your efforts elsewhere for the time being, you gather up your models, and return to the room.') 
                          for x in wonderModels: 
                            if x not in modelInventory:
                              modelInventory.append(x) 
                          modelAttempt.clear()
                          mahalModelX = 0 
                          gizaModelX = 0 
                          eiffelModelX = 0 
                          wallModelX = 0 
                          petraModelX = 0 
                          stonehengeModelX = 0 
                          machuModelX = 0 
                          chichenModelX = 0 
                          solving = 0 
                          

                    elif countryX not in countries: 
                      console.print('\nThere does not seem to be a country with a black square by that name on the globe. You find yourself a little bit confused, however, and decide to come back to ' + str(x) + " later.") 
                      time.sleep(3)
                    
                    elif 'France' in countryX:
                      if franceX == 1:
                        if len(modelAttempt) == 7:
                          console.print('\nThere is already a model in ' + str(countryX) + ". Hmm...")
                        else:
                          console.print("\nThere is already a model in " + str(countryX) + ". Hmm... You decide to wait to place " + str(x) + " until the globe has been filled in a little more." )
                        time.sleep(3)
                      else:
                        franceX = 1   
                        console.print('\nYou place ' + str(x) + ' in ' + (countryX) + ".") 
                        modelAttempt.append(x)
                        time.sleep(3)
                    elif 'England' in countryX:
                      if englandX == 1:
                        if len(modelAttempt) == 7:
                          console.print('\nThere is already a model in ' + str(countryX) + ". Hmm...")
                        else:
                          console.print("\nThere is already a model in " + str(countryX) + ". Hmm... You decide to wait to place " + str(x) + " until the globe has been filled in a little more." )
                        time.sleep(3)
                      else:
                        englandX = 1   
                        console.print('\nYou place ' + str(x) + ' in ' + (countryX) + ".") 
                        modelAttempt.append(x)
                        time.sleep(3)
                    elif 'Peru' in countryX:
                      if peruX == 1:
                        if len(modelAttempt) == 7:
                          console.print('\nThere is already a model in ' + str(countryX) + ". Hmm...")
                        else:
                          console.print("\nThere is already a model in " + str(countryX) + ". Hmm... You decide to wait to place " + str(x) + " until the globe has been filled in a little more." )
                        time.sleep(3)
                      else:
                        peruX = 1   
                        console.print('\nYou place ' + str(x) + ' in ' + (countryX) + ".") 
                        modelAttempt.append(x)
                        time.sleep(3)
                    elif 'Mexico' in countryX:
                      if mexicoX == 1:
                        if len(modelAttempt) == 7:
                          console.print('\nThere is already a model in ' + str(countryX) + ". Hmm...")
                        else:
                          console.print("\nThere is already a model in " + str(countryX) + ". Hmm... You decide to wait to place " + str(x) + " until the globe has been filled in a little more." )
                        time.sleep(3)
                      else:
                        mexicoX = 1   
                        console.print('\nYou place ' + str(x) + ' in ' + (countryX) + ".") 
                        modelAttempt.append(x)
                        time.sleep(3)
                    elif 'Jordan' in countryX:
                      if jordanX == 1:
                        if len(modelAttempt) == 7:
                          console.print('\nThere is already a model in ' + str(countryX) + ". Hmm...")
                        else:
                          console.print("\nThere is already a model in " + str(countryX) + ". Hmm... You decide to wait to place " + str(x) + " until the globe has been filled in a little more." )
                        time.sleep(3)
                      else:
                        jordanX = 1   
                        console.print('\nYou place ' + str(x) + ' in ' + (countryX) + ".") 
                        modelAttempt.append(x)
                        time.sleep(3)
                    elif 'Egypt' in countryX:
                      if egyptX == 1:
                        if len(modelAttempt) == 7:
                          console.print('\nThere is already a model in ' + str(countryX) + ". Hmm...")
                        else:
                          console.print("\nThere is already a model in " + str(countryX) + ". Hmm... You decide to wait to place " + str(x) + " until the globe has been filled in a little more." )
                        time.sleep(3)
                      else:
                        egyptX = 1   
                        console.print('\nYou place ' + str(x) + ' in ' + (countryX) + ".") 
                        modelAttempt.append(x)
                        time.sleep(3)
                    elif 'China' in countryX:
                      if chinaX == 1:
                        if len(modelAttempt) == 7:
                          console.print('\nThere is already a model in ' + str(countryX) + ". Hmm...")
                        else:
                          console.print("\nThere is already a model in " + str(countryX) + ". Hmm... You decide to wait to place " + str(x) + " until the globe has been filled in a little more." )
                        time.sleep(3)
                      else:
                        chinaX = 1   
                        console.print('\nYou place ' + str(x) + ' in ' + (countryX) + ".") 
                        modelAttempt.append(x)
                        time.sleep(3)
                    elif 'India' in countryX:
                      if indiaX == 1:
                        if len(modelAttempt) == 7:
                          console.print('\nThere is already a model in ' + str(countryX) + ". Hmm...")
                        else:
                          console.print("\nThere is already a model in " + str(countryX) + ". Hmm... You decide to wait to place " + str(x) + " until the globe has been filled in a little more." )
                        time.sleep(3)
                      else:
                        indiaX = 1   
                        console.print('\nYou place ' + str(x) + ' in ' + (countryX) + ".") 
                        modelAttempt.append(x)
                        time.sleep(3)
                        
                    t = {countryX:x} 
                    Trial.update(t) 

                    if 'Pyramid' in x and 'Egypt' in countryX: 
                          gizaModelX = 1 
                    if 'Taj' in x and 'India' in countryX: 
                          mahalModelX = 1 
                    if 'Eiffel' in x and 'France' in countryX : 
                          eiffelModelX = 1   
                    if 'Wall' in x and 'China' in countryX: 
                          wallModelX = 1  
                    if 'Petra' in x and 'Jordan' in countryX: 
                          petraModelX = 1 
                    if 'Stonehenge' in x and 'England' in countryX: 
                          stonehengeModelX = 1 
                    if 'Machu' in x and 'Peru' in countryX: 
                          machuModelX = 1   
                    if 'Chichen' in x and 'Mexico' in countryX: 
                          chichenModelX = 1 

                    if mahalModelX == 1 and eiffelModelX == 1 and gizaModelX == 1 and wallModelX == 1 and petraModelX == 1 and stonehengeModelX == 1 and machuModelX == 1 and chichenModelX == 1: 
                      globe.Unlock() 
                      modelInventory.clear()
                      solving = 0
                       

                    elif len(modelAttempt) == 8:
                      console.print('\nYou have placed all the wonders on the globe, but, to your disappointment, nothing seems to have happened. Undeterred, you gather up your models, and prepare yourself for another attempt.')
                      solving = 0
                      break
      

      
                  #elif 
              
              
              
              

    #SOUTH WALL inputs

    elif 'look' in text and 'window' in text: 
        window.look() 
    elif 'search' in text and 'window' in text: 
        window.Touch() 
    elif 'move' in text and 'window' in text: 
        window.Move() 
    elif 'open' in text and 'window' in text: 
        window.Open() 
    elif 'close' in text and 'window' in text: 
        window.Close() 
    elif 'walk' in text and 'window' in text: 
        window.Walk()
    elif 'break' in text and 'window' in text or 'smash' in text and 'window' in text: 
        console.print("\nWorking yourself into a frothy rage, you ball your hands up into fists and cock them back, ready to smash the window before you into pieces in a desperate attempt to escape the room by any means necessary.\n\nMoments before your fists begin their descent towards the helpless window, some sense returns to you in a flash, and you find yourself thinking, 'No! There must be a better way!'\n\nYour sanity returns, and you stare confusingly at your still balled fists. You open them back up, take a minute to collect yourself, and return to solving the room, 'Without breaking things!' you say to yourself aloud.") 
         
    elif 'look' in text and 'cabinet' in text: 
        filingCabinet.look() 
    elif 'search' in text and 'cabinet' in text: 
        filingCabinet.Touch() 
    elif 'move' in text and 'cabinet' in text: 
        filingCabinet.Move()   
    elif 'open' in text and 'cabinet' in text: 
        filingCabinet.Open() 
    elif 'unlock' in text and 'cabinet' in text or 'brass key' in text and 'cabinet' in text: 
        filingCabinet.Unlock()  
    elif 'walk' in text and 'cabinet' in text: 
        filingCabinet.Walk() 

    elif 'look' in text and 'drawer' in text: 
        desk.lookDrawer()                
    elif 'look' in text and 'desk' in text: 
        desk.look() 
    elif 'search' in text and 'desk' in text: 
        desk.Touch() 
    elif 'move' in text and 'desk' in text: 
        desk.Move() 
    elif 'unlock' in text and 'desk' in text or 'unlock' in text and 'drawer' in text or 'steel key' in text and 'drawer' in text or 'steel key' in text and 'desk' in text:  
        desk.Unlock() 
    elif 'open' in text and 'drawer' in text: 
        desk.lookDrawer() 
    elif 'walk' in text and 'desk' in text: 
        desk.Walk()                
          
    elif 'look' in text and 'computer' in text: 
        computer.look() 
    elif 'move' in text and 'computer' in text: 
        computer.Take() 
    elif 'take' in text and 'computer' in text: 
        computer.Take()                 
    elif 'search' in text and 'computer' in text or 'use' in text and 'computer' in text or 'password' in text and 'computer' in text: 
        console.print('\nYou get yourself in front of the computer, ready to hack it like a champion.')
        password = input('\nPassword: ')
        if password == 'question': 
            computer.PasswordRight() 
            continue 
        else: 
            computer.PasswordWrong() 
            continue 

    elif "look" in text and "pink" in text: 
        pinkPostIts.look() 
    elif "take" in text and "pink" in text: 
        pinkPostIts.take() 
    elif "look" in text and "blue" in text: 
        bluePostIts.look() 
    elif "take" in text and "blue" in text: 
        bluePostIts.take() 
    elif "look" in text and "green" in text: 
        greenPostIts.look() 
    elif "take" in text and "green" in text: 
        greenPostIts.take() 
    elif "look" in text and "white" in text: 
        whitePostIts.look() 
    elif "take" in text and "white" in text: 
        whitePostIts.take() 
    elif 'look' in text and 'post' in text or 'look' in text and 'post' in text or 'look' in text and 'notes' in text: 
        desk.lookPostIts()                
    elif 'take' in text and 'post' in text: 
        whitePostIts.Take() 
        bluePostIts.Take() 
        greenPostIts.Take() 
        pinkPostIts.Take() 
              
    #RECORD inputs
      
    elif 'look' in text and 'record player' in text: 
      recordPlayer.look() 
    elif 'search' in text and 'record player' in text: 
      recordPlayer.Touch() 
    elif 'move' in text and 'record player' in text: 
      recordPlayer.Move() 
    elif 'walk' in text and 'record player' in text: 
      recordPlayer.Walk()  
    elif 'play' in text and 'record' in text or 'use' in text and 'record player' in text: 
      console.print("\nWhich record would you like to play?")
      recordChoice = input("\nRecord choice: ").lower()
      if "pink" in recordChoice or "floyd" in recordChoice or "wish" in recordChoice:
        pinkFloyd.Play()
        continue
      elif "nofx" in recordChoice or "thanks" in recordChoice or "shoes" in recordChoice or "long" in recordChoice:
        noFX.Play()
        continue
      elif "sonny" in recordChoice or "cher" in recordChoice or "greatest" in recordChoice or "hits" in recordChoice:
        sonnyCher.Play()
        continue
      elif "beethoven" in recordChoice or "9th" in recordChoice or "symphony" in recordChoice or "ninth" in recordChoice:
        ludwigVan.Play()
        continue
      elif "radio" in recordChoice or "cool" in recordChoice:
        sonnyCher.Play()
        continue
      elif "play" in recordChoice or "moby" in recordChoice:
        moby.Play()
        continue
      else:
        console.print("\nYou cannot seem to find that particular record.")
        continue

    elif 'play' in text and 'moby' in text or 'search' in text and 'moby' in text or 'search' in text and 'play' in text: 
      recordPlayer.PlayMoby() 

    elif 'take' in text and 'records' in text: 
      records.Take() 
    elif 'look' in text and 'records' in text: 
      records.look() 
    elif 'take' in text and 'token' in text: 
      token.Take()      
    elif 'look' in text and 'token' in text: 
      token.look()

    elif 'look' in text and 'shelf' in text: 
      records.look()    
    elif 'walk' in text and 'shelf' in text or 'walk' in text and 'records' in text: 
      records.Walk()

    elif 'look' in text and 'sonny & cher' in text or 'look' in text and 'sonny and cher' in text: 
      sonnyCher.look() 
      console.print('\nYou note this record is smaller than the others, most likely a single.')      
    elif 'take' in text and 'sonny & cher' in text or 'take' in text and 'sonny and cher' in text: 
      sonnyCher.Take()   
    elif 'play' in text and 'sonny & cher' in text or 'play' in text and 'sonny and cher' in text: 
      sonnyCher.Play() 
    elif 'search' in text and 'sonny & cher' in text or 'search' in text and 'sonny and cher' in text: 
      sonnyCher.Search()

    elif 'look' in text and 'pink floyd' in text or 'look' in text and 'wish you were here' in text: 
      pinkFloyd.look()  
    elif 'take' in text and 'pink floyd' in text or 'take' in text and 'wish you were here' in text: 
      pinkFloyd.Take()   
    elif 'play' in text and 'pink floyd' in text or 'play' in text and 'wish you were here' in text: 
      pinkFloyd.Play() 
    elif 'search' in text and 'pink floyd' in text or 'search' in text and 'wish you were here' in text: 
      pinkFloyd.Search() 

    elif 'look' in text and 'beethoven' in text or 'look' in text and 'symphony' in text: 
      ludwigVan.look()  
    elif 'take' in text and 'beethoven' in text or 'take' in text and 'symphony' in text: 
      ludwigVan.Take()   
    elif 'play' in text and 'beethoven' in text or 'play' in text and 'symphony' in text: 
      ludwigVan.Play()     
    elif 'search' in text and 'beethoven' in text or 'search' in text and 'symphony' in text: 
      ludwigVan.Search() 

    elif 'look' in text and 'radio' in text or 'look' in text and 'cool' in text: 
      coolJ.look()  
    elif 'take' in text and 'radio' in text or 'take' in text and 'cool' in text: 
      coolJ.Take()   
    elif 'play' in text and 'radio' in text or 'play' in text and 'cool' in text: 
      coolJ.Play()
    elif 'search' in text and 'radio' in text or 'search' in text and 'cool' in text: 
      coolJ.Search() 
        
    elif 'look' in text and 'nofx' in text or 'look' in text and 'shoes' in text: 
      noFX.look()  
    elif 'take' in text and 'nofx' in text or 'take' in text and 'shoes' in text: 
      noFX.Take()   
    elif 'play' in text and 'nofx' in text or 'play' in text and 'shoes' in text: 
      noFX.Play()
    elif 'search' in text and 'nofx' in text or 'search' in text and 'shoes' in text: 
      noFX.Search()

    elif 'look' in text and 'piano' in text: 
        piano.look() 
    elif 'search' in text and 'piano' in text: 
        piano.Touch() 
    elif 'move' in text and 'piano' in text: 
        piano.Move() 
    elif 'play' in text and 'piano' in text or 'sit' in text and 'piano' in text or 'use' in text and 'piano' in text or 'notes' in text and 'piano' in text: 
        piano.Play() 
    elif 'walk' in text and 'piano' in text: 
        piano.Walk()

    elif 'look' in text and 'panel' in text or 'look' in text and 'shapes' in text: 
      shapesPuzzle.look() 
    elif 'walk' in text and 'panel' in text or 'walk' in text and 'shapes' in text: 
      shapesPuzzle.Walk()               
    elif 'search' in text and 'panel' in text or 'search' in text and 'shapes' in text: 
      shapesPuzzle.Touch() 

    elif 'solve' in text and 'panel' in text or 'solve' in text and 'shapes' in text or 'use' in text and 'panel' in text or 'use' in text and 'shapes' in text or 'numbers' in text and 'panel' in text or 'numbers' in text and 'shapes' in text or 'combination' in text and 'panel' in text or 'combination' in text and 'shapes' in text or 'open' in text and 'panel' in text or 'unlock' in text and 'panel' in text: 
        console.print("\nConfident you have what it takes to open up the strange panel, you approach it with steady resolve.")

        circleTrial = input('\nWhich number would you like to set the circle to? ') 
        if circleTrial not in shapesRange: 
          console.print('\nYou are only able to input the numbers 0 through 5. It seems you perhaps overestimated your ability to solve this puzzle.') 
          continue 
        else: 
          shapesState['circle'] = circleTrial 

        triangleTrial = input('\nWhich number would you like to set the triangle to? ') 
        if triangleTrial not in shapesRange: 
          console.print('\nYou are only able to input the numbers 0 through 5. It seems you perhaps overestimated your ability to solve this puzzle.') 
          continue 
        else: 
          shapesState['triangle'] = triangleTrial 

        squareTrial = input('\nWhich number would you like to set the square to? ') 
        if squareTrial not in shapesRange: 
          console.print('\nYou are only able to input the numbers 0 through 5. It seems you perhaps overestimated your ability to solve this puzzle.') 
          continue 
        else: 
          shapesState['square'] = squareTrial 

        trapezoidTrial = input('\nWhich number would you like to set the trapezoid to? ') 
        if trapezoidTrial not in shapesRange: 
          console.print('\nYou are only able to input the numbers 0 through 5. It seems you perhaps overestimated your ability to solve this puzzle.') 
          continue 
        else: 
          shapesState['trapezoid'] = trapezoidTrial    

        pentagonTrial = input('\nWhich number would you like to set the pentagon to? ') 
        if pentagonTrial not in shapesRange: 
          console.print('\nYou are only able to input the numbers 0 through 5. It seems you perhaps overestimated your ability to solve this puzzle.') 
          continue 
        else: 
          shapesState['pentagon'] = pentagonTrial 

        hexagonTrial = input('\nWhich number would you like to set the hexagon to? ') 
        if hexagonTrial not in shapesRange: 
          console.print('\nYou are only able to input the numbers 0 through 5. It seems you perhaps overestimated your ability to solve this puzzle.') 
          continue 
        else: 
          shapesState['hexagon'] = hexagonTrial  
           
        if shapesState == shapesSolution: 
          shapesPuzzle.Solve()  
          continue 
        else: 
          console.print('\nAfter setting the dials under each shape on the panel, nothing appears to have happened. The confident smile you once wore fades, and you begin to question whether you were ever good at anything at all.')            
    elif 'look' in text and 'panel' in text: 
      panel.look() 
    elif 'search' in text and 'panel' in text: 
      panel.touch() 
    elif 'take' in text and 'panel' in text: 
      panel.Take()  

    elif 'look' in text and 'display' in text and display == 'unsolved':
      console.print("\nInside the display you see several drawings that appear to have fallen down, and that sit currently in a mess at the bottom of the display. On the display board itself, you see some small shelves. To the left of each shelf you see a number - beginning at the top shelf with 1 and ending at the bottom with 7.")
    elif 'look' in text and 'sketches' in text or 'look' in text and 'drawings' in text:
      console.print("\nLooking at the drawings, you see that they are sketches of the Seven Wonders of the Ancient World, with each wonder being identified with a label on the bottom of each sketch.\n\nThe ancient wonders that have been sketched are:\n\nThe Great Lighthouse of Alexandria\nThe Great Pyramid of Giza\nThe Statue of Zeus\nThe Mausoleum at Halicarnassus\nThe Temple of Artemis\nThe Hanging Gardens of Babylon\nThe Colossus of Rhodes.")
      sketchQuery = input("\nWould you like to take a closer look at the sketches? ")
      if "y" in sketchQuery:
        sketchLook = True
        while sketchLook == True:
          print("\nWhich sketch would you like to look at? If you are done looking, type 'exit'.")
          sketchQuery = input("\nSketch: ").lower()
          if "exit" in sketchQuery:
            console.print("\nDeciding that you have seen enough of these sketches for now, you return your efforts to solving the room.")
            sketchLook = False
            break
          elif "zeus" in sketchQuery or "statue" in sketchQuery:
            console.print('\nThe sketch of the Statue of Zeus in Olympia shows the Greek God Zeus sitting upon a throne. In his left hand he is holding a large sceptre, and in his right hand he is holding a statue of Nike, the winged god of victory.')
    
          elif "temple" in sketchQuery or "artemis" in sketchQuery:
            console.print('\nThe Temple of Artemis is a large columned temple, with many friezes on its facade depicting scenes from Greek mythology. Among the friezes, you identify what is most likely a depiction of the Greek God Artemis, identifiable due to a bow being carried in one hand, and several arrows being carried in the other.')

          elif "pyramid" in sketchQuery or "giza" in sketchQuery:
            console.print("\nThe sketch of the Great Pyramid of Giza shows the pyramid in its context within the larger Giza plateau and in its original state - with its smooth, white, triangular walls, and topped with a smaller gold pyramidal capstone. You also see the other two main pyramids within the complex, as well as the Sphynx, facing the setting constellation of Leo the Lion.")

          elif "mausoleum" in sketchQuery or "halicarnassus" in sketchQuery or "masoleum" in sketchQuery or "halicarnasus" in sketchQuery:
            console.print('\nThe Mausoleum at Halicarnassus is a many-levelled structure, topped with a temple in the classical Greek style. The temple itslef sits upon several large, flat vertical pedestals, each separated by smaller, intricately detailed friezes. Surprising yourself with your memory, you recall that the Mausoleum was built as a tomb for an ancient king named Mausolus and his wife Artemisia.')

          elif "hanging" in sketchQuery or "garden" in sketchQuery or "gardens" in sketchQuery or "babylon" in sketchQuery:
            console.print("\nThe sketch of the Hanging Gardens of Babylon shows a beautiful and luscious botanic structure, covered with flowing waterfalls, columns and innumerable exotic plants. You note many separate levels and walled off areas within the larger structure, each with its own garden. You think to yourself that it is one of the most wonderful buildings you have ever seen.")

          elif "lighthouse" in sketchQuery or "alexandria" in sketchQuery or 'ligthouse' in sketchQuery:
            console.print('\nThe Great Lighthouse stands on a small island in the sea, and towers above the magnificent ancient city of Alexandria, on the north coast of Egypt. Atop the lighthouse you spot a huge flame that lights up the port and that would no doubt have been visible for kilometers in the dark Mediterranean nights.')

          elif "colossus" in sketchQuery or "colosus" in sketchQuery or "rhodes" in sketchQuery or "rodes" in sketchQuery:
            console.print('\nThe sketch of the Colossus of Rhodes shows a monumentally large statue, standing astride the harbour entrance to the ancienct city of Rhodes. You look in disbelief at the enormity of the statue, and wonder how on Earth an object of that size, with such impressive life-like detail, could have been built in so distant an age.')

          else:
              console.print('\nThere is no sketch that you can see that matches that title.')


      
    elif 'use' in text and 'display' in text and display == 'unsolved' or 'picture' in text and 'display' in text and display == 'unsolved' or 'sketches' in text and 'display' in text  and display == 'unsolved' or 'solve' in text and 'display' in text and display == 'unsolved':
        console.print('\nYou move to the display, pick up the sketches, and attempt to place them in their rightful spots.')
        sketchSolve = True
        while sketchSolve == True:
          for x in range (1,8):
              if sketchSolve == False:
                break
              wonderTry = input("\nWhich sketch would you like to place on shelf number " + str(x) + "? ").lower()
              if 'exit' in wonderTry:
                sketchSolve = False
                console.print('\nYou decide to you no longer wish to continue reorganizing the display, place the sketches back down where you found them, and refocus your efforts elsewhere.')
                break
              elif "zeus" in wonderTry or "statue" in wonderTry:
                wonderTry = "statue"
              elif "temple" in wonderTry or "artemis" in wonderTry:
                wonderTry = "temple"
              elif "pyramid" in wonderTry or "giza" in wonderTry:
                wonderTry = "pyramid"
              elif "mausoleum" in wonderTry or "halicarnassus" in wonderTry or "masoleum" in wonderTry or "halicarnasus" in wonderTry:
                wonderTry = "mausoleum"
              elif "hanging" in wonderTry or "garden" in wonderTry or "gardens" in wonderTry or "babylon" in wonderTry:
                wonderTry = "garden"
              elif "lighthouse" in wonderTry or "alexandria" in wonderTry or 'ligthouse' in wonderTry:
                wonderTry = "lighthouse"
              elif "colossus" in wonderTry or "colosus" in wonderTry or "rhodes" in wonderTry or "rodes" in wonderTry:
                wonderTry = "colossus"
              ancientSolution.append(wonderTry)
          if len(ancientSolution) == 7 and ancientSolution == ancientWonders:
            basilLeft.Sign()
            display = 'solved'
            break
        
          elif len(ancientSolution) == 7 and ancientSolution != ancientWonders:
            console.print("\nAfter placing the last sketch upon the shelf, you stand back and wait. Suddenly, the shelves begin to slide into the wall, causing the sketches to fall back to the bottom of the display, where they lie once more in a disordered mess.\n\nAfter another moment, the shelves reveal themselves again. Nothing else happens that you can see or hear.\n\nYou did not, it seems, organize the sketches correctly.")
            ancientSolution.clear()
            break
          else:
            break

    elif 'look' in text and 'trap' in text and display == 'solved' and machuPicchu.state == 'found':
      console.print('\nYou peek again at the trap door. Inside the trap door is a small mode of Machu Picchu.')

    elif 'look' in text and 'trap' in text and display == 'solved' and machuPicchu.state == 'owned':
      console.print('\nYou peek again at the trap door. Neat.')

    elif 'look' in text and 'display' in text and display == 'solved' and sketch == 'askew':
      console.print('\nYou take a good look at the now organized display, proudly presenting the sketches of the Seven Wonders of the Ancient World in exquisite order. You notice one of the sketches is slightly askew, and nudge it into symmetric harmony.')
      sketch = 'correct'

    elif 'look' in text and 'display' in text and display == 'solved' and sketch == 'correct':
      console.print('\nYou take a good look at the now organized display, proudly presenting the sketches of the Seven Wonders of the Ancient World in exquisite order.')
      

    else:
      console.print(random.choice(failQuotes))



      
if __name__ == '__main__':
   main()   

