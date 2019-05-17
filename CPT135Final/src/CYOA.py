'''
Created on May 14, 2019

@author: Alex Birmingham
'''
from tkinter import PhotoImage, Label, RIGHT, LEFT, X
import tkinter as tk
from winsound import PlaySound, SND_ASYNC, SND_FILENAME, SND_LOOP


#Create Parent Frame called gameScreen
class gameScreen(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        #Sets initial value to initialized frame as None to distinguish from subsequent frames
        self._frame = None
        #call first frame class using switch_frame function of gameScreen 
        self.switch_frame(mainMenu)

#define function switch_frame function that replaces current slave class with switch_frame(new class name)
    def switch_frame(self, frame_class):
        #Destroy current frame and replace it with a new one.  
        next_episode = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
            
        #set new frame to the new frame_class
        self._frame = next_episode
        
        #used .pack() to utilize destroy functionality, https://effbot.org/tkinterbook/pack.htm
        self._frame.pack()
        
#define mainMenu screen
class mainMenu(tk.Frame):
    def __init__(self, master):
        #define variables & constants
        global windowTitle
        windowTitle = "Choose Your Own Adventure!"
        
        #create frame with dimension parameters
        tk.Frame.__init__(self, master, bg = 'light steel blue', padx=150, pady=50)
        self.master.title("%s" % windowTitle)
        
        #add image files to frame as header
        img = PhotoImage(file="../image/laurels.png") #../ goes up a folder from src
        self._imgLab = Label(self, image= img, text = 'Image Here')
        self._imgLab.image = img
        self._imgLab.pack()
        
        #add widgets for story selection and credits
        #widgets open new frame class and access txt files
        
        #first story widget
        tk.Button(self, text='Villager\'s Quest', bg = "deep sky blue", fg = 'midnight blue', command=lambda: (_story('s2','A'), master.switch_frame(mainGame))).pack(pady=10, fill=X)
        #second story widget
        tk.Button(self, text='Knight\'s Quest', bg = "purple1", fg = 'snow', command=lambda: (_story('s1','ep0d0'), master.switch_frame(mainGame))).pack(pady=10, fill=X)
        #credits widget
        tk.Button(self, text='Credits!', bg = 'chocolate1', command=lambda: (play_sound('creditsAudio'), master.switch_frame(cCredits))).pack(side = RIGHT)
        #quit widget
        tk.Button(self, text='Quit', bg = 'maroon', command=quit).pack()
    
#create frame class for main game
class mainGame(tk.Frame):
    def __init__(self, master):
        #declare variables and constants
        global option1, option2, windowTitle, mainBody
        #update storyList using newData() function
        #create frame with dimension parameters
        tk.Frame.__init__(self, master, bg = 'light steel blue', padx=150, pady=50)
        self.master.title("%s" % windowTitle)
        
        #Displays story text from body of text files
        tk.Label(self, text=mainBody, pady=20, padx=10).pack(side="top", fill="x")
        
        #add widgets for choice selection and returning to main menu frame
        #Option 1
        tk.Button(self, text = storyList[3], bg = 'blue', fg = 'white', command=lambda:(_story(folder,_option(2)), master.switch_frame(mainGame))).pack(side=LEFT, fill =X)
        #Option 2
        if storyList[2] != storyList[4]:
            tk.Button(self, text = storyList[5], bg = 'red', fg = 'white', command=lambda:(_story(folder,_option(4)), master.switch_frame(mainGame))).pack(side=RIGHT, fill=X)
        #Return to Main Menu frame
        tk.Button(self, text="Return to start page", bg = 'goldenrod', command=lambda: (master.switch_frame(mainMenu))).pack()

#create frame class for credits
class cCredits(tk.Frame):
    def __init__(self, master):
        #create frame with dimension parameters
        tk.Frame.__init__(self, master, bg= 'light steel blue', pady=50, padx=150)
        #Created By widget
        tk.Label(self, text="CREATED BY\nJohn B. \nJohn Scharbarker.\nKevin Schene", bg= 'light steel blue', fg='gray0').pack(side="top", pady=10)
        #Music credit widget
        tk.Label(self, text='Music:\n\'Pixel Squirrel\' -- https://www.premiumbeat.com/royalty-free-music-genre/games\n\'The Sledgehammer\' -- https://www.premiumbeat.com/royalty-free-music-genre/games',bg= 'light steel blue').pack(pady=10)
        #image credit widget
        tk.Label(self, text='Image from vectorstock.com',bg='light steel blue').pack(pady=10)
        #Return to Main Menu frame
        tk.Button(self, text="Return to Main Menu", command=lambda: (play_sound('gameAudio'), master.switch_frame(mainMenu))).pack(pady=10)

#create function to chosen first story
#update txt file vars after switching txt files
def _story(curFolder, story):
    #declare variables and constants
    global mainBody, windowTitle, storyList, folder
    folder = curFolder
    mainBody =''
    x = 0
    #open txt file
    currentScreen = open("../data/"+folder+'/'+story+".txt", "r")
    #separate first line of text, separate by commas and assign to list "storyList"
    #attach following lines to variable "main body"
    for line in currentScreen:
        if x<1:
            stuff = str(line)
            storyList = stuff.split(',')
            x += 1
        else:
            mainBody += str(line)   
    #change window title variable to list element from text file
    windowTitle = storyList[1]
    
    #close txt file
    currentScreen.close()
    
#create function to update storyList var from current txt file data
def _option(choice):
    global storyList
    storyList[0] = storyList[choice]
    return storyList[0]
    
#create function to start audio
def play_sound(choice):
    PlaySound('../audio/'+choice+'.wav', SND_FILENAME|SND_LOOP|SND_ASYNC)
    
#run all executable code in file from top to bottom
if __name__ =="__main__":
    #declare constants and variables
    windowTitle = ""
    mainBody = "There was an error and the text file did not open"
    folder = ''
    
    #start audio file loop
    play_sound('gameAudio')
    
    #Run gameScreen class as loop
    gameScreen().mainloop()