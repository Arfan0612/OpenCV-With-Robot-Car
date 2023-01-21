import cv2 as cv
import numpy as np
import RPi.GPIO as GPIO
import time

#cap= cv.VideoCapture('track/track6.mp4')
cap = cv.VideoCapture(0)
cap.set(3, 160)  # set video width
cap.set(4, 120)  # set video height

in1 = 24
in2 = 23
enA = 25

in3 = 22
in4 = 27
enB = 17

GPIO.setmode(GPIO.BCM)

#setup motor A
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)

#setup motor B
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)

#set intial state of motors
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

#set PWM for motor A
p1=GPIO.PWM(enA,1000)
p1.start(0)#left tire 

#set PWM for motor B
p2=GPIO.PWM(enB,1000)
p2.start(0)#right tire 

def forward():
    p1.ChangeDutyCycle(38)
    p2.ChangeDutyCycle(46) #p2 must be higher by at least 6
    
    #left tire 
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    #right tire 
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

def right1():
    p1.ChangeDutyCycle(38)#left
    p2.ChangeDutyCycle(0)#right

    #opposite turning
    #left tire
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    #right tire
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)


def left1():
    p1.ChangeDutyCycle(0)#left
    p2.ChangeDutyCycle(46)#right

    #opposite turning
    #left tire
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    #right tire 
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)


while True:
    ret, img = cap.read()
    img = cv.flip(img,-1)
    crop = img[40:160, 0:120]
    
    gray = cv.cvtColor(crop, cv.COLOR_RGB2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)

    ret, th2 = cv.threshold(blur, 60, 255, cv.THRESH_BINARY_INV)
    opening = cv.morphologyEx(th2, cv.MORPH_OPEN, None)
    
    im, contours, hierarchy = cv.findContours(opening, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(img, contours, -1, (0, 255, 0), 3)
    
    if len(contours)>0:
        c=max(contours, key=cv.contourArea)
        
        M = cv.moments(c)
        
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        
        print("CX : " + str(cx) + "  CY : " + str(cy))
        
        center=(int(cx),int(cy))
        cv.circle(img, center, 1, (0, 0, 255), 2)
                    
        if cx>=48 and cx<105:
            print('going forward')
            forward()
        
        elif cx<=48:
            print('turn left1')
            left1()
                       
        elif cx>=105:
            print('turn right1')
            right1()
        
    else:
        stop()
                
    
    cv.imshow("Frame", img)
    cv.imshow("Pre",opening)

    if cv.waitKey(30) & 0xFF == ord('q'):  # press 'ESC' to quit
        break

#set final state of motors
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

GPIO.cleanup()
cap.release()
cv.destroyAllWindows()
