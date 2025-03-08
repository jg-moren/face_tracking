import cv2

# frame resolution to tracking
IA_FRAME_SIZE = (400, 300)

# exibcion frame resolution
#FRAME_SIZE = (640, 480)
#FRAME_SIZE = (320, 240)
FRAME_SIZE = (1280, 960)

# load and show camera info
def getCapture( source ):
    capture = cv2.VideoCapture( source )

    #capture.set(cv2.CAP_PROP_FPS, 30.0)
    #capture.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_SIZE[0])
    #capture.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_SIZE[1])

    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(capture.get(cv2.CAP_PROP_FPS))

    print(f"Source({source}), fps: {fps}, resolution: {width} x {height}")

    return capture


def main():

    cap = getCapture(2)

    while( cap.isOpened() ):
        
        _, frame = cap.read()
        cv2.imshow('img',frame)

        if ( cv2.waitKey(5) & 0xFF == ord('q') ):
            cap.release()
        





if __name__ == '__main__':
    main()

