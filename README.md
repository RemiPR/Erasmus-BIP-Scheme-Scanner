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

## 🛠️ How It Works

Scheme Scanner uses a custom-built machine learning model that has been trained to identify and analyze schemes. You can either scan schemes live via your camera or upload them as files to get instant results. The model processes the images in the background and displays the relevant information to the user.

## 💻 Installation

### Easier, more automated way to install with good computer only(minimum 4 CPU cores and 8 GB RAM):

**1. Install Docker Desktop and login. After login minimise the app and do not close it:**  
[https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-win-amd64](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-win-amd64)  
<br>

**2. Open an IDE of your choice (Visual Studio Code preferably.) and open your terminal with git bash. Use cd command to move to your desired location where you want to download the project.**  
<br>

**3. Clone the repository:**

```bash
git clone https://github.com/RemiPR/Erasmus-BIP-Scheme-Scanner.git
```

**4. Navigate to the project directory:**

```bash
cd Erasmus-BIP-Scheme-Scanner
```

**5. Install the dependencies using Docker inside the IDE terminal**

```bash
docker-compose build --no-cache
```

**6. Once the installation is finished, start the local development server:**

```bash
docker-compose up
```
**7. Open a browser of your choice(Google Chrome recommended) and go to localhost:3000**

### Slower, more manual way to install and run Scheme Scanner locally:

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

**8. Open a browser of your choice(Google Chrome recommended) and go to localhost:3000**

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

### Front-end Structure

Components

- **svgAnimation.vue**: This component is responsible for handling SVG-based animations displayed on the landing page.

Pages

- **index.vue (Landing Page)**: Serves as the main entry point to the application, featuring introductory content
  and providing navigation to key functionalities such as real-time scanning and image uploaging for object detection.
- **scan.vue**: Implements real-time object detection through the integration of the user's webcam,
  allowing for live scanning and recognition of objects.
- **upload.vue**: Facilitates the upload of images, enabling object detection to be performed on the uploaded files.

Public Folder

- Contains essential assets, including the logo, landing page images, and animations.
  These are utilized for both documentation purposes and in the user interface.

Layouts

- **default.voe**: Defines the overall layour structure, incorporating a navigation bar and global design components
  that are consistent across the application.

### Script Architecture

The app's logic is modularized into the following core areas:

References

- **DOM Elements**: Manages references to video and canvas elements for rendering the webcam feed and drawing bounding boxes, alongside state management for detected items.

State Management

- **Reactive Maps and Refs**: Handle object detection, webcam feed, and canvas rendering.
- **Computed Properties**: Convert reactive maps into arrays for easier manipulation within the template.

Lifecycle Hooks

- **onMounted**: Initializes the video feed, loads the YOLO object detection model from Roboflow, and sets up continuous detection.
- **onBeforeUnmount**: Cleans up by removing event listeners.

Detection Logic

- **initializeApp()**: Starts the video stream and loads the YOLO model for real-time detection.
- **detectFrame()**: Captures video frames for object detection.
- **updateDetectedItems(predictions)**: Updates detected items based on predictions from the model.
- **renderPredictions(predictions)**: Draws bounding boxes and labels for detected objects on the canvas.
- **resizeCanvas()**: Aligns the canvas size with the video for accurate rendering.

### Core Functions

Video Stream

- **startVideoStream()**: Accesses the webcam, sets it as the video source, and adjusts the canvas for rendering object detection results.

Model Loading

- **loadModel()**: Loads the YOLO object detection model from Roboflow using the provided publishable key.

Object Detection

- **detectFrame()**: Continuously detects objects in video frames, updating the state with their names and confidence levels.

State and Render Updates

- **updateDetectedItems(predictions)**: Tracks detected objects, updating their names, confidence levels, and visibility based on timestamps.
- **renderPredictions(predictions)**: Draws bounding boxes and labels for each detected object on the canvas.
- **getConfidenceClass(confidence)**: Applies dynamic color classes (green, yellow, red) based on detection confidence levels.

File Upload and Image Processing

- **uploadFile()**: Manages image uploads to Cloudinary, retrieving the URL for further processing.
- **processImage()**: Uses the YOLO model to detect objects in the uploaded image and draws bounding boxes around them.

### Frontend Pages Breakdown

1. **Landing Page (index.vue)**

- **Video Animation**: Integrates a background animation using the .webm video format.
- **Navigation**: Buttons provide navigation to the real-time object detection page (scan.vue) and the image upload page (upload.vue).
- **Visual Design**: Utilizes Tailwind CSS for gradients and blob shapes, giving the page a modern and fluid look.

2. Real-time Object Detection (scan.vue)

- **Video Feed**: Displays the live webcam feed with a canvas overlay for real-time object detection (bounding boxes around detected objects).
- **Detection Results**: A list of detected objects is shown, including each object's name and confidence score.
- **Responsive Layout**: Ensures an optimal experience across mobile and desktop devices.

3. Image Upload and Detection (upload.vue)

- **Image Upload**: Allows users to upload images for object detection.
- **Image Preview**: Displays the uploaded image with bounding boxes overlaid for detected objects.
- **Detection List**: Shows the detected objects and their confidence levels.

### Styles and Design

The project utilizes Tailwind CSS for all styling. Key design elements include:

- **Background Gradients**: Smooth transitions from light blue to purple for a modern, polished look.
- **Blob Shapes**: Dynamic, organic shapes that break the grid layout, adding a fluid and visually appealing design.
- **Responsiveness**: The grid layout adjusts seamlessly across various screen sizes, ensuring an optimal user experience on both desktop and mobile devices.

### Dependencies

- **Nuxt3**: Used for server-side rendering and modern Vue 3-based development.
- **Tailwind CSS**: Utility-first CSS framework for creating a responsive UI.
- **Roboflow**: Machine learning API for integrating YOLO object detection.
- **Cloudinary**: Manages image uploads and storage, used in the upload.vue component for object detection.

## 💡 Challenges and Solutions

The development journey of Scheme Scanner came with several problems that significantly shaped the final product:

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

```bash
nitro: {
    cors: true,
  },
```
