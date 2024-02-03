import cv2
import imutils
import numpy as np
import argparse

def detect(frame):
    bounding_box_cordinates, weights =  HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=0.5)
    
    person = 1
    for x, y, w, h in bounding_box_cordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        person += 1
    
    cv2.putText(frame, 'Status : Detecting ', (40, 40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.putText(frame, f'Total Persons : {person-1}', (40, 70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.imshow('output', frame)

    return frame

def detectByURL(url, writer):
    video = cv2.VideoCapture(url)
    print('Detecting people...')

    while True:
        check, frame = video.read()

        frame = detect(frame)
        if writer is not None:
            writer.write(frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

def argsParser():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-o", "--output", type=str, help="Path to optional output video file")
    args = vars(arg_parse.parse_args())

    return args

if __name__ == "__main__":
    HOGCV = cv2.HOGDescriptor()
    HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    args = argsParser()
    detectByURL('http://192.168.40.111:8080/video', args["output"])
