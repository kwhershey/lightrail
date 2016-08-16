import threading
import time
import RPi.GPIO as GPIO
import cmdline

global cath1
global cath2
cath1=[]
cath2=[]
# setup all the outputs
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.output(3,False)
GPIO.output(5,False)
GPIO.output(7,True)
GPIO.output(8,True)
GPIO.output(10,True)
GPIO.output(11,True)
GPIO.output(12,True)
GPIO.output(13,True)
GPIO.output(15,True)
GPIO.output(16,True)
GPIO.output(18,True)
GPIO.output(19,True)
GPIO.output(21,True)
GPIO.output(23,True)

# figure out what pins need to be on
def newDigits():
    global west
    global east
    global cath1
    global cath2
    d=[]
    d.append(west//10)
    d.append(west%10)
    d.append(east//10)
    d.append(east%10)
    print(d)
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
        if i[0]==3:
            cath1.append(i[1])
        elif i[0]==5:
            cath2.append(i[1])
    
    return cath1, cath2    
        

#pin map
pins=[{},{},{},{}]
pins[0]['lb']=(-1,-1) #NA
pins[0]['lt']=(-1,-1) #NA
pins[0]['mb']=(-1,-1) #NA
pins[0]['mm']=(-1,-1) #NA
pins[0]['mt']=(-1,-1) #NA
pins[0]['rb']=(5,7)
pins[0]['rt']=(3,7)
pins[1]['lb']=(5,8)
pins[1]['lt']=(3,8)
pins[1]['mb']=(5,12)
pins[1]['mm']=(5,11)
pins[1]['mt']=(3,12)
pins[1]['rb']=(5,10)
pins[1]['rt']=(3,10)
pins[2]['lb']=(5,13)
pins[2]['lt']=(3,13)
pins[2]['mb']=(5,16)
pins[2]['mm']=(6,18)
pins[2]['mt']=(3,16)
pins[2]['rb']=(5,15)
pins[2]['rt']=(3,15)
pins[3]['lb']=(5,19)
pins[3]['lt']=(3,19)
pins[3]['mb']=(5,23)
pins[3]['mm']=(3,13)
pins[3]['mt']=(3,22)
pins[3]['rb']=(5,21)
pins[3]['rt']=(3,21)

def updateDisplay():
    global cath1
    global cath2
    while(1):
        lcath1=cath1[:]
        lcath2=cath2[:]
        for t in range(50):
            # turn on cathode 1
            GPIO.output(3,True)
            # light up bottoms
            for i in lcath1:
                GPIO.output(i, False)
            for i in lcath1:
                GPIO.output(i, True)
            # turn off cathode 1
            GPIO.output(3,False)
            # turn on cathode 2
            GPIO.output(5,True)
            # light up tops
            for i in lcath2:
                GPIO.output(i, False)
            for i in lcath2:
                GPIO.output(i, True)
            # turn off cathode 2
            GPIO.output(5,False)

def updateTimes():
    global west
    global east
    cath1=[]
    cath2=[]
    while(1):
        west,east= cmdline.return_next('RAST')
        print(west)
        print( east )
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
