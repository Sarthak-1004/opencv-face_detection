import cv2

face_cascade = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")

camera = cv2.VideoCapture(0)

while True:
    res,frame = camera.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray,1.1,5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
    cv2.imshow("Face Detector",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break
    
camera.release()
cv2.destroyAllWindows()
    