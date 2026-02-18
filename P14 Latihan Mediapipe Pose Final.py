import cv2
import mediapipe as mp

mpose = mp.solutions.pose
pose = mpose.Pose()
mdraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    succes, img = cap.read()
    if not succes:
        break

    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hasil = pose.process(imgrgb)

    if hasil.pose_landmarks:
        mdraw.draw_landmarks(img,
                             hasil.pose_landmarks,
                             mpose.POSE_CONNECTIONS,
                             mdraw.DrawingSpec(color=(0, 225, 0), thickness=3, circle_radius=3),
                             mdraw.DrawingSpec(color=(225, 0, 0), thickness=3))

    lm = hasil.pose_landmarks.landmark

    if lm[mpose.PoseLandmark.RIGHT_WRIST.value].y < lm[mpose.PoseLandmark.RIGHT_SHOULDER.value].y:
          cv2.putText(img, "Tangan Kanan Terangkat", (10, 40),
                      cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    if lm[mpose.PoseLandmark.LEFT_WRIST.value].y < lm[mpose.PoseLandmark.LEFT_SHOULDER.value].y:
            cv2.putText(img, "Tangan Kiri Terangkat", (10, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Deteksi Pose", img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()