#!/usr/bin/env python3

import time
import random
import objects 
from objects import * 
#from colorama import Fore
#from colorama import Back
import rich
from rich.console import Console
#console.print(Fore.GREEN)
#console.print(Back.BLACK)


console = Console(width=80)
console = Console(style = "bold green")


failQuotes = ["\nThat didn't seem to work", "\nHmm...That didn't seem to accomplish anything.", "\nSurprisingly, nothing happens.", "\nNothing happens.", "\nNothing of note occurs.", "\nBupkis.", "\nNada parece haber pasado."]

def fail(): 
   console.print("\nThat didn't seem to work.")


  
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


  """CORE GAME / INPUT LOOPS"""
  
  while True:
    startTime = time.perf_counter() 
    text = input("\nCommand: ").lower()

    """SYNONYMS / COMMAND REPLACE"""
    text = text.replace ('hello','start')

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

    elif 'solve' in text and 'panel' in text or 'solve' in text and 'shapes' in text or 'use' in text and 'panel' in text or 'use' in text and 'shapes' in text or 'numbers' in text and 'panel' in text or 'numbers' in text and 'shapes' in text or 'combination' in text and 'panel' in text or 'combination' in text and 'shapes' in text: 
        console.print("\Confident you have what it takes to open up the strange panel, you approach it with steady resolve.")

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
    elif 'open' in text and 'panel' in text: 
      panel.Open() 
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
          console.print("\nWhich sketch would you like to look at? If you are done looking, type 'exit'.")
          sketchQuery = input("\nSketch: ").lower()
          if "exit" in sketchQuery:
            console.print("\nDeciding that you have seen enough of these sketches for now, you return your efforts to solving the room.")
            sketchLook = False
            break
          elif "zeus" in sketchQuery or "statue" in sketchQuery:
            console.print('\nThe sketch of the Statue of Zeus in Olympia shows the Greek God Zeus sitting upon a throne. In his left hand he is holding a large sceptre, and in his right hand he is holding a statue of Nike, the winged god of victory.')
            time.sleep(5)
          elif "temple" in sketchQuery or "artemis" in sketchQuery:
            console.print('\nThe Temple of Artemis is a large columned temple, with many friezes on its facade depicting scenes from Greek mythology. Among the friezes, you identify what is most likely a depiction of the Greek God Artemis, identifiable due to a bow being carried in one hand, and several arrows being carried in the other.')
            time.sleep(5) 
          elif "pyramid" in sketchQuery or "giza" in sketchQuery:
            console.print("\nThe sketch of the Great Pyramid of Giza shows the pyramid in its context within the larger Giza plateu and in its original state - with its smooth, white, triangular walls, and topped with a smaller gold pyramidal capstone. You also see the other two main pyramids within the complex, as well as the Sphynx, facing the setting constellation of Leo the Lion.")
            time.sleep(5)
          elif "mausoleum" in sketchQuery or "halicarnassus" in sketchQuery or "masoleum" in sketchQuery or "halicarnasus" in sketchQuery:
            console.print('\nThe Mausoleum at Halicarnassus is a many-levelled structure, topped with a temple in the classical Greek style. The temple itslef sits upon several large, flat vertical pedestals, each separated by smaller, intricately detailed friezes. Surprising yourself with your memory, you recall that the Mausoleum was built as a tomb for an ancient king named Mausolus and his wife Artemisia.')
            time.sleep(5)
          elif "hanging" in sketchQuery or "garden" in sketchQuery or "gardens" in sketchQuery or "babylon" in sketchQuery:
            console.print("\nThe sketch of the Hanging Gardens of Babylon shows a beautiful and luscious botanic structure, covered with flowing waterfalls, columns and innumerable exotic plants. You note many separate levels and walled off areas within the larger structure, each with its own garden. You think to yourself that it is one of the most wonderful buildings you have ever seen.")
            time.sleep(5)
          elif "lighthouse" in sketchQuery or "alexandria" in sketchQuery or 'ligthouse' in sketchQuery:
            console.print('\nThe Great Lighthouse stands on a small island in the sea, and towers above the magnificent ancient city of Alexandria, on the north coast of Egypt. Atop the lighthouse you spot a huge flame that lights up the port and that would no doubt have been visible for kilometers in the dark Mediterranean nights.')
            time.sleep(5)
          elif "colossus" in sketchQuery or "colosus" in sketchQuery or "rhodes" in sketchQuery or "rodes" in sketchQuery:
            console.print('\nThe sketch of the Colossus of Rhodes shows a monumentally large statue, standing astride the harbour entrance to the ancienct city of Rhodes. You look in disbelief at the enormity of the statue, and wonder how on Earth an object of that size, with such impressive life-like detail, could have been built in so distant an age.')
            time.sleep(5)
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
            continue
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
