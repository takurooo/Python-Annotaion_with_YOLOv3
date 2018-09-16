# Python-Annotaion_with_YOLOv3
Make annotation(PASCAL VOC format ) with YOLOv3.


# Requirement
- OpneCV 3.4.2
- numpy  


# Installation
Sample code need yolov3.cfg, yolov3.weights and coco.names.  

- yolov3.weights
```
wget https://pjreddie.com/media/files/yolov3.weights
```
- yolov3.cfg / coco.names  
[darknet-github](https://github.com/pjreddie/darknet)
```
darknet_root/  
    　│
    　├ data/  
    　│　└ coco.names
    　├ cfg/  
    　│　└ yolov3.cfg
```

# Usage
```
python make_annotaion.py <img_dir>
```
img_dir includes image files.  
make_annotaion.py processes all image in img_dir.

For example.

Directory before you execute.
```
current_dir/  
    　│
    　├ make_annotaion.py  
    　│
    　├ data/  
    　│　└ img/
　    │    └ huskies-273409_1920.jpg
　    │
```

You execute script.
```
python make_annotaion.py data/img
```


Execution result.
```
current_dir/  
    　│
    　├ make_annotaion.py  
    　│
    　├ data/  
    　│　└ img/
　    │    └ huskies-273409_1920.jpg
　    │    └ annotation
　    │          └ huskies-273409_1920.xml
　    │    └ img_with_box
　    │          └ huskies-273409_1920_with_box.jpg

```
"annotaion" directory includes annotaion PASCAL VOC format.

"img_with_box" directory includes images drawing bounding box.
