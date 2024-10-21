![Scheme Scanner Logo](/frontend/public/landing-page.webp)

# 🔍 Scheme Scanner

Scheme Scanner is a full-stack web application designed to scan and analyze PFD and P&ID schemes in real-time using your device's camera. You can also upload pre-captured images or files for scanning. The application utilizes a machine learning model, trained from scratch on 9,000+ images, ensuring accurate and efficient scheme detection.

## 📑 Table of Contents
- ⭐ [Features](#features)
- 🛠️ [How It Works](#how-it-works)
- 💻 [Installation](#installation)
- 📱 [Usage](#usage)
  - 📸 [Live Scan](#live-scan)
  - 📤 [File Upload](#file-upload)
- 🚀 [Technology Stack](#technology-stack)

## ⭐ Features
- **Live Scanning**: Scan schemes in real-time using your camera.
- **File Upload**: Upload files containing schemes for scanning.
- **Machine Learning Model**: Trained on over 9k images for more precise detection.
- **User-Friendly Interface**: Simple and intuitive interface for easy use.

## 🛠️ How It Works
Scheme Scanner uses a custom-built machine learning model that has been trained to identify and analyze schemes. You can either scan schemes live via your camera or upload them as files to get instant results. The model processes the images in the background and displays the relevant information to the user.

![How It Works](https://via.placeholder.com/400)

## 💻 Installation
To install and run Scheme Scanner locally:

1. Clone the repository:
```bash
https://github.com/RemiPR/Erasmus-BIP-Scheme-Scanner.git
```

2. Navigate to the project directory:
```bash
cd Erasmus-BIP-Scheme-Scanner/frontend
```

3. Install dependencies:
```bash
npm install
```

4. Start the local development server:
```bash
npm run dev
```

## 📱 Usage

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
