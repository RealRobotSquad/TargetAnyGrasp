<img src="docs/TargetAnyGrasp.jpg" width="90%">

## 🏠 Getting Started
### Requirements
- Python 3.9

### Installation

We provide the installation guide [here](Install/install.md). You can install locally or use docker and verify the installation easily.

### Pipeline
Now you can run the code that uses AnyGrasp SDK & Grounded-Light-HQ-SAM.

1. Sampling
```
cd TargetedAnyGrasp
conda activate sam
cd grasp_detection
python sample_realsense.py
# s - save
# q - exit
```
Then you can find the image (RGB+depth) captured in the "out" folder named by timestamps.

2. Query
```
conda activate sam
cd Grounded-Segment-Anything/EfficientSAM
python grounded_light_hqsam.py
```
Then you will get the grounded detection and segmentation results under ./grasp_detection/out/.

3. Select
```
conda activate sam
cd grasp_detection

# for mask
python select_mask_region.py

# for bounding box
python select_region.py

```

4. Grasp Pose Generation
```
conda activate anygrasp
cd grasp_detection
sh demo_real_query.sh
```
Finally, you will get the gripper_pose.json.

## Demo
You can run the code for example scene and the queried case - "bear" (under ./grasp_detection/out/1/).
