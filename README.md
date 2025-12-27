# AI Image Captioning System

## Live Demo
Try out the deployed application here:

🚀 **Streamlit App** → https://ai-image-captioning-ue2ps9fesx6jrwtwwrddd7.streamlit.app/

## Overview
An artificial intelligence–based system that generates descriptive natural language captions for images.  
This project demonstrates the integration of computer vision and natural language processing using transformer-based deep learning models.This project focuses on building an efficient and scalable image captioning pipeline using pre-trained vision–language models.

## Features
- Accepts image input in common formats (JPG, JPEG, PNG)
- Generates descriptive and context-aware captions
- Uses transformer-based vision–language architecture
- Modular and clean project structure
- Can be extended to web or API-based deployment

## Tech Stack
- Python  
- Streamlit  
- Hugging Face Transformers (BLIP)
- PyTorch  
- Pillow

## Project Structure
```text
AI-Speech-Recognition/
│
├── app.py # Streamlit UI and application logic
├── requirements.txt # Project dependencies
├── README.md # Project documentation
├── assets
│   └──Sample.jpg # Sample audio file  
│
├── ai_engine/
│   ├── init.py
│   └── model.py # Speech-to-text model logic
│
└── screenshots/ # Application screenshots
    ├── home.png
    ├── upload.png
    └── result.png
```

## Screenshots

### Application Interface
![Application Interface](<screenshots/Screenshot 2025-12-21 113723.png>)

### Image Upload
![Image Upload](<screenshots/Screenshot 2025-12-21 113801.png>)

### Caption Output
![Caption Output](<screenshots/Screenshot 2025-12-21 113846.png>)

## How It Works
First, all the required dependencies are installed within a virtual environment, and the application is launched. Once the application starts, the user is presented with a simple web-based interface.

The user uploads an image file through the file uploader and initiates the process by clicking the Generate button. The uploaded image is then preprocessed and passed to the BLIP (Bootstrapping Language–Image Pretraining) model. The model analyzes the visual content of the image and generates a descriptive caption.

After a short inference period, the generated caption is returned by the model and displayed on the user interface.

## Installation & Setup
1. Open your IDE (VS Code is recommended).
2. Clone or download the project files to your local system.
3. Create a virtual environment to avoid dependency conflicts:
   ```bash
   python -m venv venv
   venv\Scripts\activate
4. Install the required dependencies:
    pip install -r requirements.txt
5. Run the application:
    streamlit run app.py

## Usage
This application can be useful for users who want to generate meaningful descriptions for images. If you have an image and need a textual explanation such as image understanding, content description, or accessibility support you can simply upload the image and receive an automatically generated caption within seconds.

## Future Improvements
Improve caption quality using advanced decoding techniques
Generate multiple captions for a single image
Fine-tune the model on domain-specific datasets
Deploy the application as a web service or API
Add support for real-time image capture

## Learning Outcomes
Gained practical experience with vision–language models
Learned how to integrate computer vision and natural language processing
Understood image preprocessing and model inference workflows
Developed a complete AI application with a user interface
Improved skills in deploying AI models for real-world use
