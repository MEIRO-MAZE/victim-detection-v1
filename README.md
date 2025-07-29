# Victim-Detection-v1  
*Light-weight YOLOv5n victim-detection pipeline for Jetson Nano → STM32 via serial*

---

## 📘 About the Research

- **Team / Division:** MEIRO
- **Lead Developer:** Luhur Pambudi  
- **Platform:** NVIDIA Jetson Nano 4 GB  
- **MCU Companion:** STM32F407VGT6 (UART `/dev/ttyUSB0`)  
- **Timeline:** 01 Aug 2023 – 30 May 2024  
- **Status:** ✅ v1.0 released  

---

## 📚 Background

KRSRI 2024 introduces **dummy victims** alongside real ones.  
To avoid wasting time on decoys we deploy a **YOLOv5n** model (1.9 M params, INT8) that:

- Runs **~10 FPS** on Jetson Nano  
- Sends **(x, y)** centroids over serial to STM32 for navigation & grasping  

---

## 🎯 Objectives

| General | Specific |
|---------|----------|
| Detect 5 real orange victims vs 3 dummies | mAP₅₀ ≥ 85 % on mixed set |
| Real-time inference | ~10 FPS @ 320×320 |
| Serial protocol to STM32 | 115 200 baud, 8-N-1 |

---

## 📁 Repository Structure

```
📦 victim-detection-v1
├── 📂 Final Release Jetson Nano YOLO
│   ├── detect.py                      → entry point
│   └── regional.onnx                  → quantized YOLOv5n
├── 📂 Trained_Model 
├── 📂 YOLO_Object_Detection_Korban
│   ├── 📂 .idea
│   ├── 📂 Lib
│   ├── 📂 Scripts
│   ├── 📂 share
│   └── 📄 pyvenv.cfg
└── 📜 README.md
```

---

## 🔬 Methodology

| Component | Description | Version |
|-----------|-------------|---------|
| **Hardware** | Jetson Nano 4 GB | JetPack 4.6.1 |
| **Deep-Learning** | YOLOv5n (1.9 M params) | Ultralytics v6.2 |
| **Runtime** | ONNX Runtime GPU | 1.15.1 |
| **Serial** | PySerial | 3.5 |
| **Image Size** | 320×320 RGB | - |
| **Quantisation** | INT8 via TensorRT | - |

---

## ⚙️ Quick Start

1. **Flash JetPack** and install dependencies on Nano:

```bash
sudo apt-get update
sudo apt-get install libopencv-dev python3-pip
pip3 install torch torchvision onnxruntime-gpu pyserial
```

2. **Clone repo**:

```bash
git clone https://github.com/MEIRO-MAZE/victim-detection-v1.git
cd victim-detection-v1
```

3. **Run inference**:

```bash
python3 "Final Release Jetson Nano YOLO/detect.py" \
        --source 0 \
        --weights "Final Release Jetson Nano YOLO/regional.onnx" \
        --conf-thres 0.40 \
        --serial /dev/ttyUSB0
```

4. **STM32 receives**  
   Serial packet = `[0x3C][0x3E][uint32_t x][uint32_t y]` (big-endian)

---

## 🧪 Experiments & Evaluation

| Scenario | Arena Size | Victims | Result |
|----------|------------|---------|--------|
| **KRSRI 2024 Wilayah** | 360 cm × 120 cm | 5 real + 3 dummy | mAP₅₀ = 88 %, latency 180 ms |
| **Latency on Jetson Nano** | – | – | 95 ms (incl. NMS + serial TX) |

---

## ✅ Next Steps

- Replace YOLOv5n with **jetson-inference** library  
- Add **depth estimation** (Intel RealSense D435i)  
- Integrate as **Git submodule** into `MEIRO-research-2024`

---

## 🕒 Revision History

| Version | Date | Description | Author |
|---------|------|-------------|--------|
| 1.0 | 2024-05-30 | Final release | Luhur Pambudi |
