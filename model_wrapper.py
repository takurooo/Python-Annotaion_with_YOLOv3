#------------------------------------------------------
# import
#------------------------------------------------------
import time
from model.yolo_opencv import YOLO_OpenCV
from utils.draw_utils import draw_results


#------------------------------------------------------
# global
#------------------------------------------------------



#------------------------------------------------------
# function
#------------------------------------------------------
def load_model():
    model = YOLO_OpenCV(config='model/yolov3.cfg',
                         weights='model/yolov3.weights',
                         classfile='model/coco.names',
                         width=416, height=416, score_th=0.7, nms_th=0.5)
    return model

def inference(model, img, draw=True):
    start = time.time()
    classes, scores, boxes = model.fit(img)
    end = time.time()

    print("inference time : {} sec".format(end-start))

    if draw:
        draw_results(img, classes, scores, boxes)

    return classes, scores, boxes
