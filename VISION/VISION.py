# ***********************************VISION************************************
from tkinter import *
import RPi.GPIO as GPIO
import time
import cv2
import numpy as np




# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):
    GPIO.setmode(GPIO.BOARD)

    # Initializing the GPIO pins
    # PIN 11 and PIN 13 for front motor used to control
    # direction of the CAR that is Left or Right
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    # PIN 35 and 37 are used for back motor direction control
    # which controls the FORWARD and BACKWARD motion of the car
    GPIO.setup(35, GPIO.OUT)
    GPIO.setup(37, GPIO.OUT)
    

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()
        #self.Vision_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        quitButton = Button(self, text="Exit",command=self.client_exit)
        leftButton = Button(self, text="Left", command=self.moveLeft)
        rightButton = Button(self, text="Right", command=self.moveRight)
        forwardButton = Button(self, text="Forward", command=self.moveForward)
        backwardButton = Button(self, text="Back", command=self.moveBackward)
        stopButton = Button(self, text="Stop", command=self.stopMotion)
        newButton = Button(self, text= 'Vision', command=self.Vision)
        autoPilotButton = Button(self, text= "Auto-Pilot", command=self.autoPilot)
        #visionButton = Button(self, text="Vision", command=self.Vision)
        
        # placing the button on my window
        quitButton.grid(row=5, column=0)
        leftButton.grid(row=2, column=4)
        rightButton.grid(row=2, column=6)
        backwardButton.grid(row=3, column=5)
        forwardButton.grid(row=1, column=5)
        stopButton.grid(row=5, column= 6)
        newButton.grid(row=6, column= 6)
        autoPilotButton.grid(row= 7, column=7)
        #visionButton.grid(row=2, column= 8)
	
    """def Vision_window(self):
        self.master.title("Vision")
        self.pack(fill=BOTH, expand=1)

        visionButton = Button(self, text="Vision", command=self.Vision)
        visionButton.grid(row=2, column= 8)"""
       

    def client_exit(self):
        GPIO.cleanup()
        exit()
    def moveLeft(self):
        print("calling this moveleft")
        GPIO.output(35, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(37, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(13, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(11, GPIO.LOW)
        time.sleep(0.2)
        #GPIO.cleanup()

    def moveRight(self):
        print("called moveRight")
        GPIO.output(35, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(37, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(13, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(11, GPIO.LOW)
        time.sleep(0.2)
        #GPIO.cleanup()

    def moveForward(self):
        print("calling moveForward")
        GPIO.output(35, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(37, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(13, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(11, GPIO.LOW)
        time.sleep(0.2)
        #GPIO.cleanup()
        

    def moveBackward(self):
        print("calling moveBackward")
        GPIO.output(35, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(37, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(13, GPIO.LOW)
        time.sleep(0.2)
        #GPIO.cleanup()

    def stopMotion(self):
        print("calling Stop Motion")
        GPIO.output(13, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(11, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(35, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(37, GPIO.LOW)
        time.sleep(0.2)
        #GPIO.cleanup()
    def Vision(self):
        self.VisionWindow = Toplevel(self.master)
        self.app = VisionEye(self.VisionWindow)
    def autoPilot(self):
        self.auto = Toplevel(self.master)
        self.app = AutoPilot(self.auto)

class VisionEye:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.quitButton = Button(self.frame, text = 'Quit', width = 25, command = self.exitVision)
        self.eyeButton = Button(self.frame, text = 'Open Eye', width = 25, command = self.Eye)
        self.quitButton.pack()
        self.eyeButton.pack()
        self.frame.pack()
        
    def exitVision(self):
        self.destroy()


    def Eye(self):
        cap = cv2.VideoCapture(0)
        cap.set(4, 360)
        cap.set(3, 240)
        cap.set(1, 0.1)
        cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
        print(cap.get(cv2.CAP_PROP_EXPOSURE))
        while True:
                _, frame = cap.read()
                #img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.imshow('gray', frame)
                k = cv2.waitKey(5) & 0xFF
                if k ==27:
                        break

        cv2.destroyAllWindows()
        cap.release()
class AutoPilot:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.quitButton = Button(self.frame, text = 'Quit', width = 25, command = self.exitAuto)
        #self.eyeButton = Button(self.frame, text = 'Open Eye', width = 25, command = self.Eye)
        self.quitButton.pack()
        #self.eyeButton.pack()
        self.frame.pack()
    def exitAuto(self):
        self.destroy()
    
# root window created. Here, that would be the only window, but
# you can later have windows within windows.
def main():
    
    root = Tk()

    root.geometry("400x300")
    '''while True:
        vision()'''

    #creation of an instance
    app = Window(root)

    #mainloop 
    root.mainloop()

    #GPIO.cleanup()
if __name__=='__main__':
    main()
