



from bootstrap import *
from raspledstrip.animation import *

n = 48
numLED = 12
startnum = 0
endnum = startnum+numLED
led.fill(Color(0,255,0),0,numLED-1)
while (1>0):
        while (endnum < n-1): #going there
                endnum = startnum+numLED
                led.fill(Color(0,255,0),startnum,endnum)
                led.fill(Color(0,0,0),0,startnum-1)
                led.update()
                startnum = startnum +1
                print(startnum)
        while (startnum > 0): #going back
                endnum = startnum+numLED
                led.fill(Color(0,255,0),startnum-1,endnum)
                led.fill(Color(0,0,0),endnum+1,n)
                led.update()
                startnum = startnum-1
                print(startnum)



