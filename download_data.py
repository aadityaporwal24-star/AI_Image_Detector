import os
import subprocess
import sys

def install_kaggle():
    """Install kaggle package if not already installed"""
    try:
        import kaggle
        print("Kaggle package already installed")
    except ImportError:
        print("Installing kaggle package...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "kaggle"])
        print("Kaggle package installed successfully")

def download_cifake_dataset():
    """Download the CIFAKE dataset from Kaggle"""
    # Install kaggle if needed
    install_kaggle()
    
    # Import kaggle after installation
    from kaggle.api.kaggle_api_extended import KaggleApi
    
    # Initialize Kaggle API
    api = KaggleApi()
    api.authenticate()
    
    # Dataset identifier
    dataset = "birdy654/cifake-real-and-ai-generated-synthetic-images"
    
    # Download path
    download_path = "./data"
    
    # Create directory if it doesn't exist
    os.makedirs(download_path, exist_ok=True)
    
    print(f"Downloading dataset: {dataset}")
    print(f"Download location: {download_path}")
    
    # Download dataset
    api.dataset_download_files(dataset, path=download_path, unzip=True)
    
    print("Dataset downloaded successfully!")
    print(f"Files saved to: {os.path.abspath(download_path)}")

if __name__ == "__main__":
    download_cifake_dataset()
