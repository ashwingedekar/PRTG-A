import cv2

# IP Webcam URL (replace with your mobile device's IP and port)
url = 'http://192.168.40.111:8080/video'

# Open video stream
cap = cv2.VideoCapture(url)

while True:
    # Read frame from the video stream
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow('IP Webcam Stream', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video stream and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
