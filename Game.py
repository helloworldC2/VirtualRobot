import cursor
from cursor import *
import pygame
from pygame.locals import *
import sys
import gui
import Play
import credit
import leaderboardMenu
import Robot_Skin_selector
import random
import Config
import Image
from Image import *
import Button
from Button import *
import TickBox
import textfield
import Sounds

#if the script was run directly, this fnction will run
def createCanvas() :
        pygame.init()
        Config.loadConfig()
        #,pygame.FULLSCREEN|pygame.HWSURFACE,32
        canvas = pygame.display.set_mode((800,600))
        menu1(canvas)
        return


def menu1(canvas):
        #setting up the coordinates for the images and buttons
        
        #left arrow
        leftX = 10
        leftY = 300
        #right arrow
        rightX = 280
        rightY = 300
        #sound
        sX = 720
        sY = 530
        #robot
        rX = 65
        rY = 200
        #credit button
        cX = 402
        cY = 350
        #start button
        startX = 400
        startY = 170
        #leaderboard button
        lX = 406
        lY = 440
        #close button
        eX = 400
        eY = 510
        #settings
        setX = 402
        setY = 260

#loading all images, buttons
        robot = image(canvas,rX,rY,"robots/robot.png")
        robot.scale(300,300)
        robot.scale(200,200)
        transp = image(canvas,10,140,"menu/transparrent.png")
        helloW = image(canvas,0,0,"menu/VR.png")
        bgpart = image(canvas,0,0,"menu/bgpart.png")
        background  = image(canvas,0,0,"menu/wallpaper.jpg")
        startB = button(canvas,startX,startY,"buttons/start.png")
        leftB = button(canvas,leftX,leftY,"buttons/larrow.png")
        rightB = button(canvas,rightX,rightY,"buttons/rarrow.png")
        soundOffB = button(canvas,sX,sY,"buttons/soundoff.png")
        soundOffB.scale(35,50)
        soundOnB = button(canvas,sX,sY,"buttons/soundon.png")
        soundOnB.scale(60,50)
        creditB = button(canvas,cX,cY,"buttons/credits.png")
        leaderboardB = button(canvas,lX,lY,"buttons/Leaderboard.png")
        closeB = button(canvas,eX,eY,"buttons/exit.png")
        single = button(canvas,20,200,"buttons/Single-Player.png")
        multi = button(canvas,20,260,"buttons/Multiplayer.png")
        ai = button(canvas,20,320,"buttons/AI.png")
        settingsB = button(canvas,setX,setY,"buttons/Settings.png")

        font = pygame.font.SysFont("calibri",25)
        font.set_bold(1)
        text = font.render("Recieve emails",1,(250,250,250))
        text1 = font.render("Enter Email:",1,(250,250,250))
        text2 = font.render("Enter Name:",1,(250,250,250))

                                

#blitting everything    
        canvas.fill((0,0,0))
        
        background.blit()
        transp.blit()
        #leftB.blit()
        #rightB.blit()
        
        leaderboardB.blit()
        creditB.blit()
        helloW.blit()
        closeB.blit()
        robot.blit()
        startB.blit()
        soundOffB.blit()
        #soundOnB.blit()
        settingsB.blit()

#initializing the tickbox and textfields
        emailTickBox = TickBox.tickBox(canvas,230,370,"email")
        emailTextField = textfield.textField(canvas,20,310,280,30,"",20)
        nameTextField = textfield.textField(canvas,20,210,280,30,"",20)

#no when the game run, this var will be set to 1 if the sound button clicked
        sound = 0
        ran = ""
#this variable is for checking if the start button was clicked
        inStart= 0
#if the settings button was clicked
        inSettings= 0

        if sound == 1:
                soundOnB.blit()

        while True:
                for event in pygame.event.get():
                        #if user hits x button, window closes
                        if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                                
                        #if the user presses a key
                        if event.type == KEYDOWN :
                            #if esc key pressed, window closes
                            if event.key == K_ESCAPE :
                                pygame.quit()
                                sys.exit()

                        #if we are in the settings menu
                            if inSettings== 1:
                                #if the email textfield was clicked, user will write in it
                                    if emailTextField.isSelected():
                                            emailTextField.handle(event)
                                #if the name textfield was clicked
                                    elif nameTextField.isSelected():
                                            nameTextField.handle(event)
                                            
                        #getting position of the mouse
                        pos = pygame.mouse.get_pos()

                        #if user pressed the left mouse button
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                            #play click sound
                            Sounds.Plysound(False,False,True,False,False)
                            #if we are in the startmenu
                            if inStart== 1:
                                    #if singleplayer button was clicked, start in single player mode
                                    if single.clicked():
                                            gui.start(canvas,False,False,False,0,0)
                                    #if ai button was clicked, start in ai mode
                                    elif ai.clicked():
                                            gui.start(canvas,False,False,True,1,4)
                            #if we are in the settings menu
                            if inSettings== 1:
                                #if the email tickbox was clicked, untick/tick it
                                emailTickBox.clicked()

                            #if email textfield was clicked, select it and unselect the other one
                            if emailTextField.clicked():
                                    emailTextField.select()
                                    nameTextField.off()
                            #if name textfield clicked
                            if nameTextField.clicked():
                                    nameTextField.select()
                                    emailTextField.off()

                            #if the start button was clicked
                            if startB.clicked() == 1 :
                                pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)
                                #we are in startmenu
                                inStart= 1
                                #not in settings menu
                                inSettings= 0

                                #reblit everything with the game mode buttons
                                background.blit()
                                transp.blit()
                                leaderboardB.blit()
                                creditB.blit()
                                helloW.blit()
                                closeB.blit()
                                startB.blit()
                                soundOffB.blit()
                                if sound == 1:
                                        soundOnB.blit()
                                settingsB.blit()
                                single.blit()
                                multi.blit()
                                ai.blit()

                            #if settings button clicked    
                            if settingsB.collide(pos):
                                pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)

                                inStart= 0
                                inSettings= 1
                                background.blit()
                                transp.blit()
                                leaderboardB.blit()
                                creditB.blit()
                                helloW.blit()
                                closeB.blit()
                                startB.blit()
                                soundOffB.blit()
                                if sound == 1:
                                        soundOnB.blit()
                                settingsB.blit()
                                
                                canvas.blit(text,(30,380))
                                canvas.blit(text1,(30,280))
                                canvas.blit(text2,(30,180))
                                emailTextField.blit()
                                nameTextField.blit()
                                
                                emailTickBox.blit()
                                
                        #if close button was clicked, window closes
                            elif closeB.collide(pos) :
                                pygame.quit()
                                sys.exit()
                        #if sound button was clicked and it was off
                            elif sound == 0 and soundOffB.collide(pos) == 1 :
                                pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)
                                inStart= 0
                                sound = 1
                                bgpart.blit()
                                soundOffB.blit()
                                soundOnB.blit()
                                Sounds.playMusic()
                                
                                break
                        #if it was on
                            elif sound == 1 and soundOnB.collide(pos) == 1 :
                                inStart= 0
                                pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)
                                pygame.mixer.music.stop()
                                pygame.mixer.init(44100, -16,2,2048)
                                sound = 0
                                bgpart.blit()
                                soundOffB.blit()
                                
                        
                            #if credit button clicked        
                            elif creditB.clicked() :
                                    pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)
                                    credit.creditMenu(canvas)

                            #if leaderboard button was clicked    
                            elif leaderboardB.clicked():
                                    pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)
                                    leaderboardMenu.leaderboardMenu(canvas)

                        #if we are in start menu
                        if inStart== 1:
                                #if collision with the game mode buttons, use hand cursor
                                if single.collide(pos) or multi.collide(pos) or ai.collide(pos):
                                        pygame.mouse.set_cursor(*cursor.HAND_CURSOR)
                                #else use arrow
                                else :
                                        pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)
                        #if collision with buttons, use hand cursor              
                        if (settingsB.collide(pos) == 1 or
                        startB.collide(pos) == 1 or
                        leaderboardB.collide(pos) == 1 or
                        creditB.collide(pos) == 1 or
                        soundOffB.collide(pos) or
                        closeB.collide(pos)):
                                pygame.mouse.set_cursor(*cursor.HAND_CURSOR)
                        else :
                                pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)
               
                        #print emailTickBox.getStatus(
                pygame.display.update()
        return

#if the script was run directly, run createCanvas function
if __name__ == "__main__" :
        createCanvas()
