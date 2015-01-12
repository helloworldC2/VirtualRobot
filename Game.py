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

def createCanvas() :
        pygame.init()
        canvas = pygame.display.set_mode((800,600))
        menu1(canvas)
        return


def menu1(canvas):

        Robo = ["robot.png","LF_0.png","GFront.png","robotj.png"]
        startButton = pygame.image.load("buttons/start.png").convert_alpha()
        leftArrow = pygame.image.load("buttons/larrow.png").convert_alpha()
        rightArrow = pygame.image.load("buttons/rarrow.png").convert_alpha()
        creditButton = pygame.image.load("buttons/credits.png").convert_alpha()
        leaderboardButton = pygame.image.load("buttons/credits.png").convert_alpha()
        closeButton = pygame.image.load("buttons/exit.png").convert_alpha()

        helloWorld = pygame.image.load("VR.png").convert_alpha()
        robot = pygame.image.load("robot.png").convert_alpha()
        robot = pygame.transform.scale(robot,(300,300))

        robot = pygame.transform.scale(robot,(200,200))

        bg = pygame.image.load("wallpaper.jpg")

        soundDisabled = pygame.image.load("buttons/soundoff.png").convert_alpha()
        soundDisabled = pygame.transform.scale(soundDisabled,(35,50))
        soundEnabled = pygame.image.load("buttons/soundon.png").convert_alpha()
        soundEnabled = pygame.transform.scale(soundEnabled,(60,50))

        leftX = 10
        leftY = 300
        rightX = 100
        rightY = 300
        sX = 720
        sY = 540
        rX = 75
        rY = 200

        cX = 440
        cY = 400
        startX = 450
        startY = 200
        lX = 400
        lY = 300
        eX = 500
        eY = 500

        canvas.fill((0,0,0))
        canvas.blit(bg, (0,0))
        canvas.blit(leftArrow, (leftX,leftY))
        canvas.blit(rightArrow, (rightY,rightY))
        canvas.blit(soundDisabled,(sX,sY))
        canvas.blit(robot,(rX,rY))
        canvas.blit(leaderboardButton,(lX,lY))
        canvas.blit(creditButton,(cX,cY))
        canvas.blit(helloWorld,(0,0))
        canvas.blit(startButton,(startX,startY))
        canvas.blit(closeButton,(eX,eY))


        r = startButton.get_rect()
        #print (r.width,r.height,r.x)

        sound = 0
        skin = 0
        ran = ""

        while True:
                for event in pygame.event.get():
                        if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                        if event.type == KEYDOWN :
                            if event.key == K_ESCAPE :
                                pygame.quit()
                                sys.exit()
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                            if collide(startX,startY,startButton,pos) == 1 :
                                pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)
                                gui.start(canvas)
                                #Play.playMenu(canvas)

                            elif collide(eX,eY,closeButton,pos) :
                                pygame.quit()
                                sys.exit()

                            elif sound == 0 and collide(sX,sY,soundDisabled,pos) == 1 :
                                sound = 1
                                canvas.blit(bg, (0,0))
                                canvas.blit(leftArrow, (leftX,leftY))
                                canvas.blit(rightArrow, (rightY,rightY))
                                canvas.blit(soundDisabled,(sX,sY))
                                canvas.blit(soundEnabled,(sX,sY))
                                canvas.blit(robot,(rX,rY))
                                canvas.blit(creditButton,(cX,cY))
                                canvas.blit(leaderboardButton,(lX,lY))
                                canvas.blit(helloWorld,(0,0))
                                canvas.blit(startButton,(startX,startY))
                                canvas.blit(closeButton,(eX,eY))
                                ran = Sound.random_sound()
                                print ran
                                Sound.pygame.mixer.music.load(ran)
                                pygame.mixer.music.play()
                                break

                            elif sound == 1 and collide(sX,sY,soundEnabled,pos) == 1 :
                                pygame.mixer.music.stop()
                                pygame.mixer.init(44100, -16,2,2048)
                                sound = 0
                                canvas.blit(bg, (0,0))
                                canvas.blit(leftArrow, (leftX,leftY))
                                canvas.blit(rightArrow, (rightY,rightY))
                                canvas.blit(soundDisabled,(sX,sY))
                                canvas.blit(robot,(rX,rY))
                                canvas.blit(creditButton,(cX,cY))
                                canvas.blit(leaderboardButton,(lX,lY))
                                canvas.blit(helloWorld,(0,0))
                                canvas.blit(startButton,(startX,startY))
                                canvas.blit(closeButton,(eX,eY))
                                break

                            elif collide(leftX,leftY,leftArrow,pos):
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
                                    canvas.blit(robot,(rX,rY))

                                    canvas.blit(bg, (0,0))
                                    canvas.blit(leftArrow, (leftX,leftY))
                                    canvas.blit(rightArrow, (rightY,rightY))
                                    canvas.blit(soundDisabled,(sX,sY))
                                    canvas.blit(soundEnabled,(sX,sY))
                                    canvas.blit(robot,(rX,rY))
                                    canvas.blit(creditButton,(cX,cY))
                                    canvas.blit(helloWorld,(0,0))
                                    canvas.blit(startButton,(startX,startY))
                                    canvas.blit(closeButton,(eX,eY))


                            elif collide(rightY,rightY,rightArrow,pos):
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
                                    canvas.blit(robot,(rX,rY))

                                    canvas.blit(bg, (0,0))
                                    canvas.blit(leftArrow, (leftX,leftY))
                                    canvas.blit(rightArrow, (rightY,rightY))
                                    canvas.blit(soundDisabled,(sX,sY))
                                    canvas.blit(soundEnabled,(sX,sY))
                                    canvas.blit(robot,(rX,rY))
                                    canvas.blit(creditButton,(cX,cY))
                                    canvas.blit(leaderboardButton,(lX,lY))
                                    canvas.blit(helloWorld,(0,0))
                                    canvas.blit(startButton,(startX,startY))
                                    canvas.blit(closeButton,(eX,eY))
                            elif collide(cX,cY,creditButton,pos) :
                                    pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)
                                    credit.creditMenu(canvas)
                            elif collide(lX,lY,leaderboardButton,pos) :
                                    pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)
                                    leaderboardMenu.leaderboardMenu(canvas)


                        if collide(startX,startY,startButton,pos) == 1 or collide(lX,lY,leaderboardButton,pos) == 1or collide(cX,cY,creditButton,pos) == 1 or collide(sX,sY,soundDisabled,pos) or collide(eX,eY,closeButton,pos)or collide(leftX,leftY,leftArrow,pos) or collide(rightY,rightY,rightArrow,pos) :
                                pygame.mouse.set_cursor(*cursor.HAND_CURSOR)
                        else :
                                pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)
                        #rX += 1
                        #canvas.blit(robot,(rX,rY))
                pygame.display.update()
        return

if __name__ == "__main__" :
        createCanvas()
