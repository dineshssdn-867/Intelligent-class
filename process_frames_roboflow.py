from roboflow import Roboflow
import cv2 as cv


rf = Roboflow(api_key="5St3cP1vrmc1lm2qZ1xF")
project = rf.workspace().project("classroom-behavior")
model = project.version(4).model


while(f.isOpened()):
  # f.read() methods returns a tuple, first element is a bool 
  # and the second is frame
    ret, frame = f.read()
    if ret == True:
        # save frame as a “temporary” jpeg file
        cv.imwrite('temp.jpg', frame)
        # run inference on “temporary” jpeg file (the frame)
        predictions = model.predict('temp.jpg')
        predictions_json = predictions.json()
        # printing all detection results from the image
        print(predictions_json)

        # accessing individual predicted boxes on each image
        for bounding_box in predictions:
            # x0 = bounding_box['x'] - bounding_box['width'] / 2#start_column
            # x1 = bounding_box['x'] + bounding_box['width'] / 2#end_column
            # y0 = bounding_box['y'] - bounding_box['height'] / 2#start row
            # y1 = bounding_box['y'] + bounding_box['height'] / 2#end_row
            class_name = bounding_box['class']
            confidence_score = bounding_box['confidence']
        
            detection_results = bounding_box
            class_and_confidence = (class_name, confidence_score)
            print(class_and_confidence, '\n')

    elif cv.waitKey(1) == ord('q'):
        break
    else:
        break

f.release()
cv.destroyAllWindows()