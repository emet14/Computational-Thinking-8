###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("winter")
q1=codesters.Square(100, 100, 200, 'blue')
q2=codesters.Square(-100, 100, 200, 'black')
q3=codesters.Square(-100, -100, 200, 'red')
q4=codesters.Square(100, -100, 200, 'white')

s1=codesters.Sprite("baseball", 100, 100)
s1.set_size(3)
s2=codesters.Sprite("snow", 100, -100)
s3=codesters.Sprite("angel",-100,-100)
s3.set_size(0.5)
s4=codesters.Sprite("kitten",-100,100)

message1=codesters.Text("My names Emmett",0,220,"black")
message2=codesters.Text("I snowboard",0,-220, "black")