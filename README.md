![Scheme Scanner Logo](/frontend/public/landing-page.webp)

# 🔍 Scheme Scanner

Scheme Scanner is a full-stack web application designed to scan and analyze PFD and P&ID schemes in real-time using your device's camera. You can also upload pre-captured images or files for scanning. The application utilizes a custom machine learning model, trained from scratch on 9,000+ images, ensuring accurate and efficient scheme detection.

## 📑 Table of Contents
- ⭐ [Features](#features)
- 🛠️ [How It Works](#how-it-works)
- 💻 [Installation](#installation)
- 📱 [How To Use](#how-to-use)
  - 📸 [Live Scan](#live-scan)
  - 📤 [File Upload](#file-upload)
- 🚀 [Technology Stack](#technology-stack)
- 🔧 [Technical Implementation](#technical-implementation)
- 💡 [Challenges and Solutions](#challenges-and-solutions)
  
## ⭐ Features
- **Live Scanning**: Scan schemes in real-time using your camera.
- **File Upload**: Upload files containing schemes for scanning.
- **Machine Learning Model**: Trained on over 9k images for more precise detection.
- **User-Friendly Interface**: Simple and intuitive interface for easy use.
- 
## 🛠️ How It Works
Scheme Scanner uses a custom-built machine learning model that has been trained to identify and analyze schemes. You can either scan schemes live via your camera or upload them as files to get instant results. The model processes the images in the background and displays the relevant information to the user.

## 💻 Installation
To install and run Scheme Scanner locally:

**1. if not installed, install git:**  
[https://git-scm.com/download/win](https://git-scm.com/download/win)  
<br>

**2. if not installed, install Node.js:**  
[https://nodejs.org/dist/v20.18.0/node-v20.18.0-x64.msi](https://nodejs.org/dist/v20.18.0/node-v20.18.0-x64.msi)  
<br>

**3. Open an IDE of your choice (Visual Studio Code etc.) and open your terminal with git bash. Use cd command to move to your desired location where you want to download the project.**  
<br>

**4. Clone the repository:**
```bash
git clone https://github.com/RemiPR/Erasmus-BIP-Scheme-Scanner.git
```

**5. Navigate to the project directory:**
```bash
cd Erasmus-BIP-Scheme-Scanner/frontend
```

**6. Install dependencies:**
```bash
npm install
```

**7. Start the local development server:**
```bash
npm run dev
```

## 📱 How To Use

### 📸 Live Scan
1. Open the application and select the option to scan schemes via your camera.
2. Grant camera access when prompted.
3. Point your camera at the scheme, and the system will automatically detect it.

### 📤 File Upload
1. Choose the option to upload a scheme image from your device.
2. Upload the file, and the model will analyze it for you.
   
## 🚀 Technology Stack

### Frontend:
- [Nuxt.js](https://nuxt.com/)
- HTML5
- [Tailwind CSS](https://nuxt.com/modules/tailwindcss)

### Additional front-end libraries and modules:
- [Nuxt/icon](https://nuxt.com/modules/icon)

### Backend:
- Python

### Machine Learning:
- YOLO (You Only Look Once)
- Roboflow

## 🔧 Technical Implementation
### Template Structure
The HTML structure includes:
* A video element to display the camera feed
* A canvas element overlaying the video for rendering detection results
* A section for displaying the detected objects

### Script Architecture
The logic is organized into several key areas:
* **References**: Defines `video` and `canvas` references to interact with the DOM elements
* **State Management**: Uses a reactive map to manage detected items
* **Lifecycle Hooks**: Initializes the application when the component is mounted and cleans up on unmounting
* **Detection Logic**: Functions for starting the video stream, loading the model, detecting frames, updating detected items, and rendering predictions

### Core Functions
* `initializeApp()`: Initializes the application by starting the video stream and loading the model
* `startVideoStream()`: Accesses the webcam and sets the video source
* `loadModel()`: Loads the YOLO model for object detection from Roboflow
* `detectFrame()`: Captures a frame from the video and runs detection, updating results
* `updateDetectedItems(predictions)`: Updates the state with detected items and their confidence levels
* `renderPredictions(predictions)`: Draws bounding boxes and labels on the canvas for detected objects
* `resizeCanvas()`: Adjusts the canvas size based on the video dimensions

## 💡 Challenges and Solutions
The development journey of Scheme Scanner came with several problems that significantly shaped the final product:

- Initial Setup: At first, we aimed to integrate OpenCV with TensorFlow for object detection. However, this approach quickly became complex due to the need for extensive customization and performance tuning.

- Model Selection: After facing difficulties with OpenCV and TensorFlow, we switched to Roboflow and YOLO for object detection, which provided a more streamlined setup and better-suited architecture for real-time detection tasks.

- Training the Model: Training the YOLO model required considerable effort, taking over 5 hours to process more than 9,000 images. This extensive dataset was necessary to improve accuracy and ensure that the model could reliably recognize diverse scheme types.

### File Upload Issues
**Problem:** During the development phase, we encountered issues with file uploads, specifically handling large image files, which led to timeouts or application crashes.

**Solution:** We implemented an image compression technique using the sharp library to reduce the file size before sending it to the server. Additionally, we configured the server to allow larger file sizes and implemented progress tracking to improve user experience.

### Asynchronous Model Loading
**Problem:** Loading the machine learning model asynchronously on the frontend caused delays in the application initialization. Sometimes, the Roboflow model was not ready when the user attempted to scan a scheme.

**Solution:** We introduced a polling mechanism that checks for the model’s availability and ensures it is loaded before allowing the user to interact with the app.

### Webcam and File Input Conflicts
**Problem:** The system had conflicts when switching between live camera input and file upload, leading to the webcam feed failing or canvas rendering issues.

**Solution:** We restructured the application to handle separate input streams more efficiently, ensuring that switching between the two modes would not cause conflicts. We added event listeners to properly terminate the webcam stream when users opt for file uploads.

### Cross-Origin Resource Sharing (CORS) Errors
**Problem:** Due to security settings on the Roboflow and Cloudinary APIs, we encountered CORS-related issues that blocked requests from the frontend.

**Solution:** We added appropriate CORS headers and ensured that API keys were configured correctly. Also, we configured `nuxt.config.ts` to allow nitro to use allow CORS by adding the necessary configuration:


``` bash
nitro: {
    cors: true,
  },
```
