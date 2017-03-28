from gamelib import *

game = Game(800,600,"mario vs bowser 2")
bk = Image("mario\\castle.jpg",game)
mario = Image("mario\\mariowalk.png",game)
button = Image("mario\\button.png",game)
while not game.over:
     game.processInput()
     bk.draw()
     mario.draw()
     mario.resizeTo(50,25)
     mario.move to (-90,0)
     
     button.draw()
     
     


     if keys.Pressed[K_LEFT] and mario.left > game.left:
        mario.moveX(-4)
     elif keys.Pressed[K_RIGHT] and mario.right < game.right:
        mario.moveX(4)




      game.update()
      game.quit()
