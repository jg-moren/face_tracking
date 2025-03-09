import cv2

# frame resolution to tracking
IA_FRAME_SIZE = (400, 200)

class OpenCVTR:

    def __init__(self):
        self.classifier = cv2.CascadeClassifier("./models/haarcascade_frontalface_default.xml")

    def face_points(self, frame):

        # scale frame reduction
        scale_x = float(frame.shape[1] / IA_FRAME_SIZE[0]) 
        scale_y = float(frame.shape[0] / IA_FRAME_SIZE[1])        
        
        # resize frame 
        frame_gray = cv2.resize(frame, (IA_FRAME_SIZE), interpolation=cv2.INTER_LANCZOS4)

        # convert frame to gray scale 
        frame_gray = cv2.cvtColor(frame_gray, cv2.COLOR_BGR2GRAY)

        # detect face
        faces = self.classifier.detectMultiScale(frame_gray, 1.05, 5 )

        # order the coordinates with the largest area h * w
        faces = sorted(faces, key=lambda x: ( x[2] * x[3] ))

        # resize points to original frame scale
        faces = [ [ int(x*scale_x), int(y*scale_y) ,int(w*scale_x), int(h*scale_y) ] for [x,y,w,h] in faces ]

        # draw rectangles
        for [x,y,w,h] in faces[0:1]:
           
            frame = frame[y:y+h,x:x+w]
            return frame
            #cv2.rectangle( frame_gray, (x,y), (x+w,y+h), (255,0,0), 2)
            #cv2.rectangle( frame, (x,y), (x+w,y+h), (255,0,0), 2)

        
        
        

        return frame



