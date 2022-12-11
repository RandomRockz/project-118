import cv2


# Create our body classifier
bc=cv2.CascadeClassifier("haarcascade_fullbody.xml")

# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()

    #Convert Each Frame into Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Pass frame to our body classifier
    b=bc.detectMultiScale(gray, 1.2 ,3)
    
    # Extract bounding boxes for any bodies identified
    for x,y,w,h in b:
         cv2.rectangle(img(x,y)((x+w),(y+h)),(255,0,255,3,1))
    cv2.imshow(b,'img')     
    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
