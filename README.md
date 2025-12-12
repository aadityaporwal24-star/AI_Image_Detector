# AI Image Detector using Vision Transformer (ViT)

A deep learning project that uses a pretrained Vision Transformer (ViT) model to classify images as **Real** or **AI-Generated (Fake)**.

## 📋 Project Overview

This project fine-tunes Google's `vit-base-patch16-224` model on the CIFAKE dataset to detect AI-generated images. The model achieves high accuracy in distinguishing between real and synthetic images.

## 🎯 Features

- **Pretrained ViT Model**: Uses Google's Vision Transformer for image classification
- **Binary Classification**: Detects Real vs AI-Generated images
- **Comprehensive Evaluation**: Includes multiple performance metrics and visualizations
- **Model Persistence**: Save and load trained models
- **Interactive Prediction**: Test on custom images

## 📊 Dataset

**CIFAKE Dataset** from Kaggle:
- Training images: REAL and FAKE categories
- Test images: REAL and FAKE categories
- Source: [CIFAKE Dataset](https://www.kaggle.com/datasets/birdy654/cifake-real-and-ai-generated-synthetic-images)

## 🛠️ Installation

### Prerequisites
- Python 3.12
- CUDA-compatible GPU (optional, for faster training)

### Required Packages
```bash
pip install torch torchvision transformers Pillow matplotlib scikit-learn tqdm kaggle
```

## 🚀 Usage

### 1. Download Dataset
Run the `download_data.py` script to download the CIFAKE dataset from Kaggle.

### 2. Train the Model
Open and run `main.ipynb` notebook sequentially:
- Install required packages
- Load and preprocess data
- Train the ViT model
- Evaluate performance
- Save the trained model

### 3. Make Predictions
Use the saved model to predict on new images:
- Load the saved model
- Input image filename
- Get prediction with confidence score

## 📈 Model Performance

The model provides:
- **Training metrics**: Loss and accuracy curves
- **Test accuracy**: Overall classification accuracy
- **ROC curve**: With AUC score
- **Precision-Recall curve**
- **Confusion matrix**: Both count and normalized
- **Per-class metrics**: Precision, Recall, F1-score
- **Confidence distributions**
- **Misclassified images analysis**

## 📁 Project Structure

```
AI_detect/
├── main.ipynb                 # Main training and evaluation notebook
├── download_data.py           # Script to download dataset
├── data/                      # Dataset directory (auto-downloaded)
│   ├── train/
│   │   ├── FAKE/
│   │   └── REAL/
│   └── test/
│       ├── FAKE/
│       └── REAL/
├── trained_vit_model/         # Saved model directory
│   ├── config.json
│   ├── model.safetensors
│   └── checkpoint.pth
└── README.md
```

## 🧠 Model Architecture

- **Base Model**: `google/vit-base-patch16-224`
- **Input Size**: 224x224 pixels
- **Output**: Binary classification (FAKE: 0, REAL: 1)
- **Parameters**: ~86M trainable parameters

## ⚙️ Training Configuration

- **Epochs**: 5
- **Learning Rate**: 2e-5
- **Batch Size**: 32
- **Optimizer**: AdamW
- **Scheduler**: CosineAnnealingLR
- **Loss Function**: CrossEntropyLoss

## 📊 Visualization Features

The notebook includes:
- Training loss and accuracy curves
- ROC and Precision-Recall curves
- Confusion matrices (count and percentage)
- Per-class performance bar charts
- Confidence distribution histograms
- Misclassified images visualization
- Comprehensive performance dashboard

## 💾 Model Saving

The trained model is saved in two formats:
1. **Pretrained format**: Compatible with Hugging Face Transformers
2. **PyTorch checkpoint**: Includes optimizer state and training history

## 🔮 Making Predictions

To predict on a new image:
1. Place the image in the root directory
2. Run the prediction cells in the notebook
3. Enter the filename when prompted
4. View results with confidence scores

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **Dataset**: CIFAKE dataset by birdy654 on Kaggle
- **Model**: Vision Transformer by Google Research
- **Framework**: PyTorch and Hugging Face Transformers

## 👤 Author

Aarav Aggarwal

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Note**: The trained model and dataset are not included in this repository due to size constraints. Follow the setup instructions to download and train the model.
