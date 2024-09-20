# Arecanut Classification and Grading Using Deep Learning

## Overview

This project focuses on the classification and grading of Arecanut using deep learning techniques. The system is designed to automate the process of identifying the quality of Arecanut nuts based on various parameters. The primary objective is to improve the accuracy and efficiency of grading by leveraging image processing and deep learning models.

---

## Features

- **Image Classification**: Automatically classify Arecanut based on captured images.
- **Grading System**: Grade Arecanut based on predefined quality metrics.
- **User Interface**: Simple and intuitive user interface using Flask for web-based interaction.
- **Real-time Prediction**: Upload an image of Arecanut and get real-time predictions on its classification and grade.

---

## Technologies Used

- **Deep Learning Framework**: TensorFlow
- **Programming Language**: Python
- **Web Framework**: Flask
- **Frontend**: HTML, CSS, Bootstrap
- **Development Environment**: Anaconda, Visual Studio Code
- **Operating System**: Ubuntu 22.04 LTS

---

## System Architecture

The project is divided into several main components:

1. **Data Collection**: Images of Arecanut nuts are collected and labeled for training.
2. **Model Building**: A deep learning model is trained using TensorFlow to classify and grade the Arecanut based on the input images.
3. **Web Interface**: A Flask web application that allows users to upload Arecanut images and receive real-time grading results.
4. **User Interface**: Frontend designed with HTML, CSS, and Bootstrap for an easy-to-use web interface.

---

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shivan-kulal-git/Arecanut_final.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd Arecanut_final
   ```

3. **Create a virtual environment using Anaconda**:
   ```bash
   conda create --name arecanut_env python=3.8
   conda activate arecanut_env
   ```

4. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Flask application**:
   ```bash
   python app.py
   ```

6. **Access the application**:
   Open a browser and go to `http://localhost:5000` to interact with the Arecanut grading system.

---

## Usage

1. **Upload Image**: Upload an image of an Arecanut nut through the web interface.
2. **Get Prediction**: The model will classify the Arecanut based on its appearance and provide the grading results.
3. **Review Results**: View the predicted grade and classification in real-time.

---

## Dataset

The dataset used in this project includes labeled images of different Arecanut quality levels. The images are preprocessed and used to train the deep learning model. Details about the dataset can be found in the project documentation.

---

## Future Enhancements

- **Expand Dataset**: Collect more images to improve the model's accuracy and robustness.
- **Advanced Grading Metrics**: Implement additional features for more granular grading.
- **Mobile Application**: Develop a mobile version of the application for easy access in the field.

---

## Contributing

We welcome contributions to enhance the system. If you would like to contribute, feel free to fork the repository, make changes, and submit a pull request.

---
