import cv2
from deepface import DeepFace
from roboflow import Roboflow

ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mkv', 'mov'}

rf = Roboflow(api_key="5St3cP1vrmc1lm2qZ1xF")
project = rf.workspace().project("classroom-behavior")
model = project.version(4).model

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def process_video_anomalus(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'MP4V'), 20, (frame_width, frame_height))
    index = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if index%10 == 0:
            try:
                cv2.imwrite('temp.jpg', frame)
                predictions = model.predict('temp.jpg')
                predictions = dict(predictions.json())
                class_ = str(predictions['predictions'][0]['class'])
            except Exception as e:
                print(e)
        try:
            # cv2.rectangle(frame, (int(predictions['predictions'][0]['y']), int(predictions['predictions'][0]['x'])), (int(predictions['predictions'][0]['y'])+int(predictions['predictions'][0]['width']), int(predictions['predictions'][0]['x'])+int(predictions['predictions'][0]['height'])), color=(255,0,0), thickness=2)
            cv2.putText(frame, str(class_), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.imwrite('temp1.jpg', frame)
        except Exception as e:
            print(e)
            print("No error")

        index += 1
        out.write(frame)

    cap.release()
    out.release()

def process_video_emotion(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'MP4V'), 20, (frame_width, frame_height))
    index = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if index%10 == 0:
            try:
                result = DeepFace.analyze(frame, actions = ['emotion'])
            except:
                result = {}
                result['dominant_emotion'] = "Face not detected"
        try:
            cv2.putText(frame, result[0]['dominant_emotion'], (50, 50), cv2.FONT_HERSHEY_SIMPLEX ,  
                    2, (255, 0, 0), 2, cv2.LINE_AA)
        except:
            print("No error")

        index += 1
        out.write(frame)

    cap.release()
    out.release()


def process_video_face(input_path):
    result = DeepFace.verify(input_path,'faces\salman.jpg')
    return result
