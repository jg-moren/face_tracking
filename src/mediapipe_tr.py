import cv2
import mediapipe as mp

#
# links ref:
#   https://ai.google.dev/edge/mediapipe/solutions/vision/face_landmarker
#   https://github.com/google-ai-edge/mediapipe/wiki/MediaPipe-Face-Mesh
#   https://github.com/google-ai-edge/mediapipe/blob/master/docs/solutions/face_mesh.md#face-landmark-model
#

# frame resolution to tracking
IA_FRAME_SIZE = (256, 256)

class MediaPipeTr:
    def __init__(self):

        model_path = '/absolute/path/to/face_landmarker.task'

            




    def face_points(self, frame):

        # scale frame reduction
        scale_x = float(frame.shape[1] / IA_FRAME_SIZE[0]) 
        scale_y = float(frame.shape[0] / IA_FRAME_SIZE[1])        
        
        # resize frame 
        frame_gray = cv2.resize(frame, (IA_FRAME_SIZE), interpolation=cv2.INTER_LANCZOS4)

        # convert frame to gray scale 
        frame_gray = cv2.cvtColor(frame_gray, cv2.COLOR_BGR2GRAY)

        # detect face
        


        return frame_gray

