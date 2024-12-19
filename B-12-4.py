import pyxel

pyxel.init(200, 200)
pyxel.cls(7)


class Ball():
    speed=2
    def __init__(self):
        Ball.restart(self)
        
    def move(self):
        self.x += self.vx * Ball.speed
        self.y += self.vy * Ball.speed
        if self.x>=200 or self.x<0:
            self.vx*=-1

    def restart(self):
        Ball.speed+=1
        self.x=pyxel.rndi(1,199)
        self.y=0
        angle=pyxel.rndi(10, 170)
        self.vx=pyxel.cos(angle)
        self.vy=pyxel.sin(angle)

class Pad():
    def __init__(self):
        self.x = pyxel.mouse_x

    def catch(self,ball):
        if ball.y>=195 and self.x-20<=ball.x<=self.x+20:
                return True
        else:
            return False


class App:
    balls=[Ball()]
    score=0
    miss=0
    GameOver=False
    pad=Pad()
    def __init__(self):
        pyxel.run(self.update,self.draw)

    def update(self):
            if App.GameOver:
                return
            App.pad=Pad()
            for ball in App.balls:
                ball.move()
                if Pad.catch(App.pad,ball):
                    ball.restart()
                    App.score+=1
                    if App.score>=int(len(App.balls))*10:
                        App.balls.append(Ball())
                        Ball.speed=3
                if ball.y>200:
                    ball.restart()
                    App.miss+=1
                    if App.miss>=10:
                        App.GameOver=True

    def draw(self):
            if App.GameOver:
                pyxel.text(20,80,'GAME OVER',0)
                return
            pyxel.cls(7)
            for ball in App.balls:
                pyxel.circ(ball.x,ball.y,10,5)
                pyxel.rect(App.pad.x-20, 195, 40, 5, 14)
                pyxel.text(20,20,"score="+str(App.score),0)
                pyxel.text(20,40,"miss="+str(App.miss),0)

App()
