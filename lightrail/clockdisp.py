import threading
import time
import RPi.GPIO as GPIO

# setup all the outputs
GPIO.setup(18, GPIO.OUT)

# figure out what pins need to be on
def newDigits():
    global west
    global east
    d=[]
    d.append(west/10)
    d.append(west%10)
    d.append(east/10)
    d.append(east%10)
    active=[]
    for i in range(4):
        if(d[i]==1):
            active.append(pins[i]['rb'])
            active.append(pins[i]['rt'])
        elif(d[i]==2):
            active.append(pins[i]['mt'])
            active.append(pins[i]['rt']) 
            active.append(pins[i]['mm'])
            active.append(pins[i]['lb'])
            active.append(pins[i]['mb'])
        elif(d[i]==3):
            active.append(pins[i]['mt'])
            active.append(pins[i]['rt']) 
            active.append(pins[i]['mm'])
            active.append(pins[i]['rb'])
            active.append(pins[i]['mb'])  
        elif(d[i]==4):
            active.append(pins[i]['lt'])
            active.append(pins[i]['rt']) 
            active.append(pins[i]['mm'])
            active.append(pins[i]['rb'])
        elif(d[i]==5):
            active.append(pins[i]['mt'])
            active.append(pins[i]['lt']) 
            active.append(pins[i]['mm'])
            active.append(pins[i]['rb'])
            active.append(pins[i]['mb'])
        elif(d[i]==6):
            active.append(pins[i]['lt']) 
            active.append(pins[i]['mm'])
            active.append(pins[i]['rb'])
            active.append(pins[i]['lb'])
            active.append(pins[i]['mb']) 
        elif(d[i]==7):
            active.append(pins[i]['mt'])
            active.append(pins[i]['rt']) 
            active.append(pins[i]['rb'])
        elif(d[i]==8):
            active.append(pins[i]['mt'])
            active.append(pins[i]['lt'])
            active.append(pins[i]['rt']) 
            active.append(pins[i]['mm'])
            active.append(pins[i]['rb'])
            active.append(pins[i]['lb'])
            active.append(pins[i]['mb'])
        elif(d[i]==9):
            active.append(pins[i]['mt'])
            active.append(pins[i]['lt'])
            active.append(pins[i]['rt']) 
            active.append(pins[i]['mm'])
            active.append(pins[i]['rb'])
        elif(d[i]==0):
            if(i==1 or i==3):
                active.append(pins[i]['mt'])
                active.append(pins[i]['lt'])
                active.append(pins[i]['rt']) 
                active.append(pins[i]['rb'])
                active.append(pins[i]['lb'])
                active.append(pins[i]['mb'])
    
    cath1=[]
    cath2=[]
    for i in active:
        if i[0]==1:
            cath1.append(i[1])
        elif i[0]==2:
            cath2.append(i[1])
    
    return cath1, cath2    
        

#pin map
pins=[{},{},{},{}]
pins[0]['lb']=(-1,-1) #NA
pins[0]['lt']=(-1,-1) #NA
pins[0]['mb']=(-1,-1) #NA
pins[0]['mm']=(-1,-1) #NA
pins[0]['mt']=(-1,-1) #NA
pins[0]['rb']=(1,3)
pins[0]['rt']=(1,3)
pins[1]['lb']=(1,3)
pins[1]['lt']=(1,3)
pins[1]['mb']=(1,3)
pins[1]['mm']=(1,3)
pins[1]['mt']=(1,3)
pins[1]['rb']=(1,3)
pins[1]['rt']=(1,3)
pins[2]['lb']=(1,3)
pins[2]['lt']=(1,3)
pins[2]['mb']=(1,3)
pins[2]['mm']=(1,3)
pins[2]['mt']=(1,3)
pins[2]['rb']=(1,3)
pins[2]['rt']=(1,3)
pins[3]['lb']=(1,3)
pins[3]['lt']=(1,3)
pins[3]['mb']=(1,3)
pins[3]['mm']=(1,3)
pins[3]['mt']=(1,3)
pins[3]['rb']=(1,3)
pins[3]['rt']=(1,3)

def updateDisplay():
    while(1):
        # turn on cathode 1
        # light up bottoms
        for i in cath1:
            GPIO.output(i, True)
        for i in cath1:
            GPIO.output(i, False)
        # turn off cathode 1
        # turn on cathode 2
        # light up tops
        for i in cath2:
            GPIO.output(i, True)
        for i in cath2:
            GPIO.output(i, False)
        # turn off cathode 2

def updateTimes():
    global west
    global east
    cath1=[]
    cath2=[]
    while(1):
        west,east=#fetch from kevin
        cath1,cath2=newDigits()
        time.sleep(15)



        
global west
global east
west=0
east=0

t1 = threading.Thread(target=updateTimes)
t2 = threading.Thread(target=updateDisplay)

t1.start()
t2.start()