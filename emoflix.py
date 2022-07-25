from tkinter import *   
from tkinter.ttk import *
import cv2
from cv2 import LINE_4
from deepface import DeepFace
import webbrowser

def emod():

    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot Open Webcam")

    while True:
        ret,frame = cap.read()
        result = DeepFace.analyze(frame, actions = ['emotion'])


        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray,1.1,4)

        for(x, y, w, h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

        font = cv2.FONT_HERSHEY_PLAIN

        cv2.putText(frame,
                    result['dominant_emotion'],
                    (x-5,y-10),
                    font, 1,
                    (0, 255, 0),
                    2,
                    cv2.LINE_4)
        cv2.imshow('Demo Video',frame)
    
        if result['dominant_emotion']=='neutral':
            webbrowser.open('http://127.0.0.1:5500/Emoflix/neutral.html')
            break  

        if result['dominant_emotion']=='happy':
            webbrowser.open('http://127.0.0.1:5500/Emoflix/happy.html')
            break

        if result['dominant_emotion']=='sad':
            webbrowser.open('http://127.0.0.1:5500/Emoflix/sad.html')
            break    

        if result['dominant_emotion']=='angry':
            webbrowser.open('http://127.0.0.1:5500/Emoflix/angry.html')
            break  
            
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break

        
    cap.release()
    cv2.destroyAllWindows()
 
# create a tkinter window
root = Tk()             
 
# Open window having dimension 100x100
root.geometry('1280x720')
 
# Create a Button
btn = Button(root, text = 'Click me !',
                command = emod)
 
# Set the position of button on the top of window.  
btn.pack()   
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
 
root.mainloop()