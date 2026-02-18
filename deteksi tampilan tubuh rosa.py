import cv2
import mediapipe as mp
mpose = mp.solutions.pose
pose = mpose.Pose()
cap = cv2.VideoCapture(0)

while True:
    succes, img = cap.read()
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hasil = pose.process(imgrgb)
    if hasil.pose_landmarks:
        print ("terdeteksi")
    else:
        print ("tidak terdeteksi")
    cv2.imshow("webcam",img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()