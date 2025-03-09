import dlib
import cv2

# frame resolution to tracking
IA_FRAME_SIZE = (300, 150)

class DlibTr:
    def __init__(self):
        self.classificador_dlib_68 = "models/shape_predictor_68_face_landmarks.dat"
        self.classificador_dlib = dlib.shape_predictor(self.classificador_dlib_68)
        self.detector_face = dlib.get_frontal_face_detector()

    def face_points(self, frame):

        # scale frame reduction
        scale_x = float(frame.shape[1] / IA_FRAME_SIZE[0]) 
        scale_y = float(frame.shape[0] / IA_FRAME_SIZE[1])        
        
        # resize frame 
        frame_gray = cv2.resize(frame, (IA_FRAME_SIZE), interpolation=cv2.INTER_LANCZOS4)

        # convert frame to gray scale 
        frame_gray = cv2.cvtColor(frame_gray, cv2.COLOR_BGR2GRAY)

        # detect face
        faces = self.detector_face(frame_gray, 1)

        for face in faces:
            cv2.rectangle( frame_gray, (face.left(), face.top()), (face.right(), face.bottom()), (255,0,0), 2 )
            
        return frame_gray
