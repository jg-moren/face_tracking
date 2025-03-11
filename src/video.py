import cv2
#import opencv_tr as tr
#import dlib_tr as tr
import mediapipe_tr as tr

# exibcion frame resolution
FRAME_SIZE = (640, 480)
#FRAME_SIZE = (320, 240)
#FRAME_SIZE = (800, 800)

# load and show camera info
def getCapture( source ):
    capture = cv2.VideoCapture( source )

    capture.set(cv2.CAP_PROP_FPS, 30.0)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_SIZE[0])
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_SIZE[1])

    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(capture.get(cv2.CAP_PROP_FPS))

    print(f"Source({source}), fps: {fps}, resolution: {width} x {height}")

    return capture

def getFrame( cap ):
    ok, frame = cap.read()
    frame = cv2.resize(frame, (FRAME_SIZE), interpolation=cv2.INTER_LANCZOS4)
    return frame    


def showFrame( frame ):
    frame = cv2.resize(frame, (FRAME_SIZE), interpolation=cv2.INTER_LANCZOS4)
    cv2.imshow('img',frame)


def main():

    #cap = getCapture("temp/examaple.mp4")
    cap = getCapture(2)
    
    #track = tr.DlibTr()
    #track = tr.OpenCVTR()
    track = tr.MediaPipeTr()

    while( cap.isOpened() ):
        
        frame = getFrame(cap)

        

        frame = track.face_points(frame)

        showFrame(frame)

        if ( cv2.waitKey(5) & 0xFF == ord('q') ):
            cap.release()
        


if __name__ == '__main__':
    main()

