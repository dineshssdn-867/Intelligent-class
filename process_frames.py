import cv2
from deepface import DeepFace


ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mkv', 'mov'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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