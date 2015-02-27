import Keyboard

class void:
    def __init__(self,i):
        self.x = 0
        self.y = 0
        return

    def tick(self):
        if self.x>=0 and self.y>=0 and self.x<=32*32 - 800 and self.y<=32*32 - 600:
            if Keyboard.keys['w']:
			self.y-=2
	    if Keyboard.keys['s']:
			self.y+=2
	    if Keyboard.keys['a']:
			self.x-=2
	    if Keyboard.keys['d']:
			self.x+=2

	if self.x<0:
            self.x = 0
        if self.y<0:
            self.y=0
        if self.x>32*32 - 800:
            self.x=32*32 - 800
        if self.y>32*32 - 600:
            self.y=32*32 - 600
        
	    
        
