# Python-Annotaion_with_YOLOv3
Make annotation(PASCAL VOC format ) with YOLOv3.

![image](https://user-images.githubusercontent.com/35373553/45597341-b3444a00-ba05-11e8-88c2-567f49b071bc.jpg)

```XML
<?xml version="1.0" ?>
<annotaion>
	<filename>huskies-273409_1920</filename>
	<size>
		<depth>3</depth>
		<width>1920</width>
		<height>1336</height>
	</size>
	<object>
		<name>dog</name>
		<pose>Unspecified</pose>
		<bndbox>
			<xmin>1404</xmin>
			<ymin>291</ymin>
			<xmax>1783</xmax>
			<ymax>1109</ymax>
		</bndbox>
	</object>
	<object>
		<name>dog</name>
		<pose>Unspecified</pose>
		<bndbox>
			<xmin>155</xmin>
			<ymin>45</ymin>
			<xmax>545</xmax>
			<ymax>1133</ymax>
		</bndbox>
	</object>
	<object>
		<name>dog</name>
		<pose>Unspecified</pose>
		<bndbox>
			<xmin>692</xmin>
			<ymin>163</ymin>
			<xmax>1170</xmax>
			<ymax>1177</ymax>
		</bndbox>
	</object>
	<object>
		<name>dog</name>
		<pose>Unspecified</pose>
		<bndbox>
			<xmin>1123</xmin>
			<ymin>368</ymin>
			<xmax>1456</xmax>
			<ymax>1163</ymax>
		</bndbox>
	</object>
</annotaion>

```


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

Place these files in model dir.
```
current_dir/  
    　│
    　├ make_annotaion.py  
    　├ data/  
	　├ utils/  
    　├ model/  
    　│　└ yolov3.cfg
　    │　└ yolov3.weights
　    │　└ coco.names
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
