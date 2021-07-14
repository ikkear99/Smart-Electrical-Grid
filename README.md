# Smart Electrical Grid

This is the repo implementing phase 1 of the Smart Electrical Grid project using the yolo V5 model

Folder structure:
- Metadata: contains training data
- Result: contains the initial result
- Data/Annotations: the label of the image data is assigned in the format yoloV5
- Run/detect: Image detect with our trained model
 
### Train Custom Data
#### 1. Clone YoloV5 model

> $ git clone https://github.com/ultralytics/yolov5  # clone repo
>
> $ cd yolov5
> 
> $ pip install -r requirements.txt  # install
> 

#### 2. Using Meta_data/Grid.yaml 

>
> train: Meta_data/images/train/
> 
>val: Meta_data/images/valid/
>
> % number of classes
>
>nc: 3
>
>% class names
>
> names: [ 'ong_noi', 'khoa_neo',  'tru_su']
> 
#### 3. Using labeling at: *data/Annotations* 
Example
``` <annotation>
	<folder>Ong noi</folder>
	<filename>DJI_0164.JPG</filename>
	<path>E:\DIEN_OEGalaxy\Data\Ong noi\DJI_0164.JPG</path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width>4056</width>
		<height>2280</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>ong_noi</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>1617</xmin>
			<ymin>1345</ymin>
			<xmax>2124</xmax>
			<ymax>1472</ymax>
		</bndbox>
	</object>
</annotation>
```

#### 4. Select a Model
Select a pretrained model to start training from. Here we select YOLOv5s, the smallest and fastest model available. See our README table for a full comparison of all models.

![alt](https://github.com/ultralytics/yolov5/releases/download/v1.0/model_comparison.png)

#### 5. Train
Train a YOLOv5s model on COCO128 by specifying dataset, batch-size, image size and either pretrained --weights yolov5s.pt (recommended), or randomly initialized --weights '' --cfg yolov5s.yaml (not recommended). Pretrained weights are auto-downloaded from the latest YOLOv5 release.
> Train YOLOv5s on COCO128 for 5 epochs
> 
> $ python train.py --img 640 --batch 16 --epochs 5 --data coco128.yaml --weights yolov5s.pt
>

### My Result:
![alt](https://github.com/ikkear99/Smart-ElectricalGrid/blob/master/runs/detect/exp/DJI_0402.JPG?raw=true)

