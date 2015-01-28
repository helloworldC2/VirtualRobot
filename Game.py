import cursor
from cursor import *
import pygame
from pygame.locals import *
import sys
import gui
import Play
import credit
import leaderboardMenu
import Sound
import Robot_Skin_selector
import random
import Config
import Image
from Image import *
import Button
from Button import *
import TickBox
import textfield

def createCanvas() :
        pygame.init()
        Config.loadConfig()
        #,pygame.FULLSCREEN|pygame.HWSURFACE,32
        canvas = pygame.display.set_mode((800,600))
        menu1(canvas)
        return


def menu1(canvas):

        Robo = ["robots/robot.png","robots/LF_0.png","robots/GFront.png","robots/robotj.png"]

        robot = pygame.image.load("robots/robot.png").convert_alpha()
        robot = pygame.transform.scale(robot,(300,300))

        robot = pygame.transform.scale(robot,(200,200))
        
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

        transp = image(canvas,10,140,"menu/transparrent.png")
        helloW = image(canvas,0,0,"menu/VR.png")
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
             
        canvas.fill((0,0,0))
        
        background.blit()
        transp.blit()
        #leftB.blit()
        #rightB.blit()
        
        leaderboardB.blit()
        creditB.blit()
        helloW.blit()
        closeB.blit()
        canvas.blit(robot,(rX,rY))
        startB.blit()
        soundOffB.blit()
        soundOnB.blit()
        settingsB.blit()

        box1 = TickBox.tickBox(canvas,230,370,"email")
        txfld = textfield.textField(canvas,20,310,280,30,"",20)
        txfld1 = textfield.textField(canvas,20,210,280,30,"",20)
        sound = 1
        skin = 0
        ran = ""
        st = 0
        sett=0

        while True:
                #print sett, st
                for event in pygame.event.get():
                        if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                        if event.type == KEYDOWN :
                            if event.key == K_ESCAPE :
                                pygame.quit()
                                sys.exit()

                            if sett == 1:
                                    if txfld.isSelected():
                                            txfld.handle(event)
                                    elif txfld1.isSelected():
                                            txfld1.handle(event)
                        pos = pygame.mouse.get_pos()
                        
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                            if st == 1:
                                    if single.clicked():
                                            gui.start(canvas,False,False,False,0,0)
                                    elif ai.clicked():
                                            gui.start(canvas,False,False,True,1,4)
                            if sett == 1:
                                box1.clicked()


                            if txfld.clicked():
                                    txfld.select()
                                    txfld1.off()
                                    
                            if txfld1.clicked():
                                    txfld1.select()
                                    txfld.off()
                        
                            if startB.collide(pos) == 1 :
                                pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)
                                st = 1
                                sett = 0
                                background.blit()
                                transp.blit()
                                leaderboardB.blit()
                                creditB.blit()
                                helloW.blit()
                                closeB.blit()
                                startB.blit()
                                soundOffB.blit()
                                soundOnB.blit()
                                settingsB.blit()
                                single.blit()
                                multi.blit()
                                ai.blit()   
                            if settingsB.collide(pos):
                                pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)
                                st = 0
                                sett = 1
                                background.blit()
                                transp.blit()
                                leaderboardB.blit()
                                creditB.blit()
                                helloW.blit()
                                closeB.blit()
                                startB.blit()
                                soundOffB.blit()
                                soundOnB.blit()
                                settingsB.blit()

                                font = pygame.font.SysFont("calibri",25)
                                font.set_bold(1)
                                text = font.render("Recieve emails",1,(250,250,250))
                                text1 = font.render("Enter Email:",1,(250,250,250))
                                text2 = font.render("Enter Name:",1,(250,250,250))

                                
                                canvas.blit(text,(30,380))
                                canvas.blit(text1,(30,280))
                                canvas.blit(text2,(30,180))
                                txfld.blit()
                                txfld1.blit()
                                
                                box1.blit()
                            elif closeB.collide(pos) :
                                pygame.quit()
                                sys.exit()

                            elif sound == 0 and soundOffB.collide(pos) == 1 :
                                pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)
                                st = 0
                                sound = 1
                                background.blit()
                                transp.blit()
                                soundOffB.blit()
                                soundOnB.blit()
                                leaderboardB.blit()
                                helloW.blit()
                                startB.blit()
                                closeB.blit()
                                creditB.blit()
                                canvas.blit(robot,(rX,rY))
                                settingsB.blit()
                                
                                ran = Sound.random_sound()
                                print ran
                                Sound.pygame.mixer.music.load(ran)
                                pygame.mixer.music.play()
                                break

                            elif sound == 1 and soundOnB.collide(pos) == 1 :
                                st = 0
                                pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)
                                pygame.mixer.music.stop()
                                pygame.mixer.init(44100, -16,2,2048)
                                sound = 0

                                background.blit()
                                transp.blit()
                                soundOffB.blit()
                                canvas.blit(robot,(rX,rY))

                                creditB.blit()
                                leaderboardB.blit()
                                helloW.blit()
                                startB.blit()
                                closeB.blit()
                                settingsB.blit()
                                break

                            elif leftB.collide(pos):
                                    st = 0
                                    sett = 0
                                    pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)
                                    skin = skin + 1

                                    if skin == 0:
                                            cRBskin= Robo[0]
                                    elif skin == 1:
                                            cRBskin= Robo[1]
                                    if skin == 2:
                                            cRBskin= Robo[2]
                                    elif skin == 3:
                                            cRBskin= Robo[3]


                                    robot = pygame.image.load(cRBskin).convert_alpha()
                                    robot = pygame.transform.scale(robot,(300,300))
                                    robot = pygame.transform.scale(robot,(200,200))
                                    

                                    background.blit()
                                    helloW.blit()
                                    transp.blit()
                                    soundOffB.blit()
                                    if sound == 1:
                                            soundOnB.blit()
                                    canvas.blit(robot,(rX,rY))
                                    creditB.blit()
                                    startB.blit()
                                    closeB.blit()
                                    leaderboardB.blit()
                                    settingsB.blit()


                            elif rightB.clicked():
                                    st = 0
                                    sett = 0
                                    pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)
                                    skin = skin - 1
                                    if skin == 3:
                                            cRBskin= Robo[0]
                                    elif skin == 2:
                                            cRBskin= Robo[1]
                                    if skin == 1:
                                            cRBskin= Robo[2]
                                    elif skin == 0:
                                            cRBskin= Robo[3]

                                    robot = pygame.image.load(cRBskin).convert_alpha()
                                    robot = pygame.transform.scale(robot,(300,300))
                                    robot = pygame.transform.scale(robot,(200,200))

                                    background.blit()
                                    helloW.blit()
                                    transp.blit()
                                    soundOffB.blit()
                                    if sound == 1:
                                            soundOnB.blit()
                                    canvas.blit(robot,(rX,rY))
                                    creditB.blit()
                                    startB.blit()
                                    closeB.blit()
                                    leaderboardB.blit()
                                    settingsB.blit()
                                    
                            elif creditB.clicked() :
                                    pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)
                                    credit.creditMenu(canvas)
                            elif leaderboardB.clicked():
                                    pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)
                                    leaderboardMenu.leaderboardMenu(canvas)


                        if st == 1:
                                if single.collide(pos) or multi.collide(pos) or ai.collide(pos):
                                        pygame.mouse.set_cursor(*cursor.HAND_CURSOR)
                                else :
                                        pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)
                                        
                        elif (settingsB.collide(pos) == 1 or
                        startB.collide(pos) == 1 or
                        leaderboardB.collide(pos) == 1 or
                        creditB.collide(pos) == 1 or
                        soundOffB.collide(pos) or
                        closeB.collide(pos)or
                        leftB.collide(pos) or
                        rightB.collide(pos) ):
                                pygame.mouse.set_cursor(*cursor.HAND_CURSOR)
                        else :
                                pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)
               
                        #print box1.getStatus(
                pygame.display.update()
        return

if __name__ == "__main__" :
        createCanvas()
