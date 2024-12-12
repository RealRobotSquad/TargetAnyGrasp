# Install Grounded-Light-HQSAM

Follow the steps below to set up and install **Grounded-Light-HQSAM**.

---

## 1. Create Conda Environment

First, create a new conda environment named `sam` and set the required environment variables:

```bash
conda create -n sam python=3.9
conda activate sam

# Set environment variables
export AM_I_DOCKER=False
export BUILD_WITH_CUDA=True
export CUDA_HOME=/path/to/cuda-11.8/
```


## 2. Install PyTorch
Install PyTorch with CUDA 11.8 support:

```bash
pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cu118
```


## 3. Install Required Libraries
Install additional dependencies as follows:
```bash
# Install Segment Anything and GroundingDINO
python -m pip install -e segment_anything
pip install --no-build-isolation -e GroundingDINO

# Upgrade diffusers and install other libraries
pip install --upgrade diffusers[torch]
pip install opencv-python pycocotools matplotlib onnxruntime onnx ipykernel
```


## 4. Download Pretrained Weights

### 4.1 Light-HQSAM Weights

Download the pretrained **Light-HQSAM** weights from the following link:

- [Download Light-HQSAM Weights](https://huggingface.co/lkeab/hq-sam/resolve/main/sam_hq_vit_tiny.pth)

Place the downloaded weights into the `EfficientSAM/` directory under `Grounded-Segment-Anything`:

```plaintext
Grounded-Segment-Anything/
  ├── EfficientSAM/
      ├── sam_hq_vit_tiny.pth
```


###  4.2 GroundingDINO Weights
Download the pretrained GroundingDINO weights (swin-tiny model):
```bash
cd Grounded-Segment-Anything

# Download the pretrained groundingdino-swin-tiny model
wget https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth
```