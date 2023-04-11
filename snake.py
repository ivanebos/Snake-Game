import pygame

class Snake():

    def __init__(self,gap,size):

        self.growing = False
        
        self.gap = gap
        self.size = size

        self.headx = 5
        self.heady = 15
        self.chain = [(self.headx,self.heady)]
        self.direction = "still" 
        self.currentDir = "still"


    def move_up(self):
        if not self.currentDir == "down":
            self.direction = "up"
    def move_down(self):
        if not self.currentDir == "up":
            self.direction = "down"

    def move_right(self):
        if not self.currentDir == "left":
            self.direction = "right"

    def move_left(self):
        if not self.currentDir == "right":
            self.direction = "left"
    
    def grow(self):
        self.growing = True
        print("growing")

    def draw(self):
        rect = []

        for i in self.chain:
            rect.append(pygame.Rect(i[0]*self.gap+1, i[1]*self.gap+1, self.gap,self.gap))

        return rect
    
    def update(self):

        self.checkBounds()
        self.checkOverLap()

        if self.direction == "right":
            self.headx += 1
            self.chain.insert(0,(self.headx,self.heady))
            self.currentDir = "right"
        
        elif self.direction == "left":
            self.headx -= 1
            self.chain.insert(0,(self.headx,self.heady))

            self.currentDir = "left"


        elif self.direction == "up":
            self.heady -= 1
            self.chain.insert(0,(self.headx,self.heady))

            self.currentDir = "up"


        elif self.direction == "down":
            self.heady += 1
            self.chain.insert(0,(self.headx,self.heady))
            self.currentDir = "down"

  
        if not self.growing and self.direction != "still":
            self.chain.pop()
        
        
        elif self.growing: 
            self.growing = False

    def checkBounds(self):
        if self.headx <= -1 or self.headx >= self.size:
            pygame.quit() 

        if self.heady <= -1 or self.heady >= self.size:
            pygame.quit() 
    
    def checkOverLap(self):
        for i in range(1,len(self.chain)):
            if (self.headx,self.heady) == self.chain[i]:
                pygame.quit() 


        


    


