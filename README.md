# Sparse 2D Image to 3D Model Reconstruction

This project focuses on reconstructing 3D scenes from sparse 2D images using a hybrid deep learning pipeline. It leverages voxel grids, 3D CNNs, Graph Neural Networks (GNNs), and Neural Radiance Fields (NeRF) to produce accurate 3D mesh representations of outdoor scenes, with data sourced from the KITTI dataset.

## 🧠 Motivation

Sparse 2D images are often all we have in real-world driving scenarios. This project addresses the challenge of generating detailed 3D representations from minimal input views—critical for autonomous driving, robotics, and scene understanding.

---

## 📌 Features

- ✅ Sparse 2D input support (few-view reconstruction)
- ✅ Voxel grid generation from 2D image inputs
- ✅ 3D Convolutional Neural Network for coarse geometry prediction
- ✅ GNN-based refinement of topological structure
- ✅ NeRF module for realistic surface rendering
- ✅ Final output as a textured 3D mesh or point cloud

---


## 🛠 Architecture Overview

Sparse 2D Images
↓
Preprocessing (resize, calibrate)
↓
Voxel Grid Generation
↓
3D CNN (Feature Extraction & Coarse Shape)
↓
Graph Neural Network (Refinement)
↓
NeRF (Photorealistic Reconstruction)
↓
3D Mesh / Point Cloud Output

---

## 📂 Dataset

- **Source**: [KITTI Vision Benchmark Suite](http://www.cvlibs.net/datasets/kitti/)
- **Preprocessing**: Image resizing, depth-map extraction, camera calibration
- **Split**: Train / Test / Validation (80 / 10 / 10)

---

