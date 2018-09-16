#------------------------------------------------------
# import
#------------------------------------------------------
import os
import argparse
import codecs
import time
import imghdr
import numpy as np
import cv2
print("opencv : ",cv2.__version__)
from utils.annotation_utils import PascalVOC_Writer
from model_wrapper import *
#------------------------------------------------------
# global
#------------------------------------------------------



#------------------------------------------------------
# function
#------------------------------------------------------
def imglist_from_dir(dir):
    dirs = []
    list = os.listdir(dir)
    for fname in list:
        abs_path = os.path.join(dir, fname)
        if os.path.isfile(abs_path):
            if imghdr.what(abs_path):
                dirs.append(abs_path)
    return dirs


def process_images(model, img_dir):
    # prepare dirs
    annotaion_dir = os.path.join(img_dir, 'annotation')
    imgbox_dir = os.path.join(img_dir, 'img_with_box')
    os.makedirs(annotaion_dir, exist_ok=True)
    os.makedirs(imgbox_dir, exist_ok=True)

    img_paths = imglist_from_dir(img_dir)
    for img_path in img_paths:

        img = cv2.imread(img_path)
        img_size = (img.shape[1], img.shape[0], img.shape[2])

        classes, scores, boxes = inference(model, img, draw=True)

        # write image with bbox
        base_fname, _ = os.path.splitext(os.path.basename(img_path))
        out_file_path = os.path.join(imgbox_dir, base_fname+'_with_box.jpg')
        cv2.imwrite(out_file_path, img.astype(np.uint8));
        print("save : ", out_file_path)

        # write annotation PASCAL VOC format
        writer = PascalVOC_Writer(annotaion_dir)
        writer.write(base_fname, img_size, classes, boxes)
        print("save : ", os.path.join(annotaion_dir, base_fname+'.xml'))



def arg_parser():
    parser = argparse.ArgumentParser(description="Annotate with YOLOv3.")
    parser.add_argument("img_dir", type=str, help="path2your_image", default=None)
    return parser


def main(args):
    process_images(load_model(), args.img_dir)


#------------------------------------------------------
# main
#------------------------------------------------------
if __name__ == '__main__':
    parser = arg_parser()
    args = parser.parse_args()
    main(args)
