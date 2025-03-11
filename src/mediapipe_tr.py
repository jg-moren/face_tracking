import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_detection = mp.solutions.face_detection

# links ref:
#   https://ai.google.dev/edge/mediapipe/solutions/vision/face_landmarker
#   https://github.com/google-ai-edge/mediapipe/wiki/MediaPipe-Face-Mesh
#   https://github.com/google-ai-edge/mediapipe/blob/master/docs/solutions/face_mesh.md#face-landmark-model
#

class MediaPipeTr:
    def __init__(self):

        self.detector = mp_face_detection.FaceDetection(
            model_selection=0, min_detection_confidence=0.5)

    def draw_face(image, results):
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles
                    .get_default_face_mesh_tesselation_style())
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles
                    .get_default_face_mesh_contours_style())
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_IRISES,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles
                    .get_default_face_mesh_iris_connections_style())



    def face_points(self, frame):

                
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        detection_result = self.detector.process(image)

        #print(detection_result.detections)

        if detection_result.detections:
            result = detection_result.detections[0].location_data.relative_bounding_box
            #print(result)
            point1 = (int(result.xmin * frame.shape[1]), int(result.ymin * frame.shape[0]))
            point2 = (int((result.xmin + result.width) * frame.shape[1]), int((result.ymin + result.height) * frame.shape[0]))
            
            cv2.rectangle( frame, point1, point2, (255,0,0), 2)
            frame = frame[point1[1]:point2[1], point1[0]:point2[0]]
            frame = cv2.flip(frame, 1)

        return frame


        #cv2.rectangle( frame, (0,0), (frame.shape[1], frame.shape[0]), (255,0,0), frame.shape[0])

        #MediaPipeTr.draw_face(frame,detection_result)
        
        #point = ( int(frame.shape[0]), int(frame.shape[1]) )

        #cv2.circle( frame, point, 3, (255,255,0), -1)

        #frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        


        return frame
    




