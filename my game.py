import os
os.getcwd()
os.chdir('C:\\Users\\LG\\Desktop\\2d')

import random

from pico2d import *
        
import game_framework
import start_state



game_framework.run(start_state)		



open_canvas()

                
        


class Boy:
    def __init__(self):
        self.x,self.y =  random.randint(100, 700), 90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')
      
    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)
            
    def update(self):
        self.frame = (self.frame+1)%8
        self.x +=2  


team = [Boy() for i in range(11)]


              
class Grass:
	def __init__(self):
		self.image = load_image('grass.png')
	def draw(self):
		self.image.draw(400,30)




def handle_events():
        global running
        global x, y
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                running = False  
            elif event.type == SDL_MOUSEMOTION:
                x, y = event.x, 600 - event.y

            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_1:
                    team[1].x,team[1].y = x,y
                if event.key == SDLK_2:
                    team[2].x,team[2].y = x,y
                if event.key == SDLK_3:
                    team[3].x,team[3].y = x,y
                if event.key == SDLK_4:
                    team[4].x,team[4].y = x,y
                if event.key == SDLK_5:
                    team[5].x,team[5].y = x,y
                if event.key == SDLK_6:
                    team[6].x,team[6].y = x,y
                if event.key == SDLK_7:
                    team[7].x,team[7].y = x,y
                if event.key == SDLK_8:
                    team[8].x,team[8].y = x,y
                if event.key == SDLK_9:
                    team[9].x,team[9].y = x,y
                if event.key == SDLK_0:
                    team[0].x,team[0].y = x,y
             
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                running = False
                  



boy = Boy()
    
grass = Grass()

running = True;

while running:
    handle_events()
    clear_canvas()
    grass.draw()
    for boy in team:
      boy.draw()
    update_canvas()
    for boy in team:
     boy.update() 

    delay(0.05)
   

close_canvas()
