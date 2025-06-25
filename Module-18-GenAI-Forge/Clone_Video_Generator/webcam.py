import cv2

cap = cv2.VideoCapture(0)  # 0 is default webcam
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('input_video.mp4', fourcc, 20.0, (640, 480))

print("Recording... Press 'q' to stop.")

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        out.write(frame)
        cv2.imshow('Webcam - Recording', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
