# Real-Time-Emotion-Detector-with-Voice-Feedback

This project is a real-time emotion detection system that captures emotions through your Webcam, recognizes various facial expressions (like happy, sad, angry, etc.), and speaks out the detected emotion using text-to-speech.

## Features

- Detects seven emotions: **happy, sad, angry, fear, surprise, disgust, and neutral**.
- Real-time webcam feed with bounding boxes around detected faces.
- Speaks the detected dominant emotion using the text-to-speech feature.
- Displays confidence levels for all emotions detected on screen.

## Demo

![Emotion Detector Demo](demo.gif)  
*An example of detecting and speaking emotions in real-time.*

## Prerequisites

Make sure you have **Python 3.6+** installed on your system. You can download it from [python.org](https://www.python.org/).

### Libraries

You need the following Python libraries to run the project:

- `opencv-python`
- `fer`
- `pyttsx3`
- `tensorflow` (required for `fer`)

You can install these using `pip`:

```bash
pip install opencv-python fer pyttsx3 tensorflow
```

## How to Run

1. Clone this repository to your local machine:

    ```bash
    git clone: https://github.com/zouraiz523/Real-Time-Emotion-Detector-with-Voice-Feedback.git
    ```

2. Navigate to the project directory:

    ```bash
    cd real-time-emotion-detector
    ```

3. Run the Python script:

    ```bash
    python emotion_detector.py
    ```

4. Allow access to your webcam, and the emotion detection will start in real-time!

## Usage

- The application will open a window displaying your webcam feed.
- It will recognize emotions in real-time and draw a bounding box around each detected face.
- The dominant emotion will be displayed above each face.
- The program will speak the detected emotion out loud.
- Press **'q'** to quit the program.

## Project Structure

```bash
.
├── emotion_detector.py     # Main script to run the emotion detection
├── README.md               # Project documentation
└── requirements.txt        # List of required dependencies
```

## Potential Improvements

- Add support for more emotions by using advanced machine learning models.
- Improve speech by adding more voice options and customizing text-to-speech speed and tone.
- Integrate face recognition to map emotions to specific individuals.

## Contributing

Contributions are welcome! If you have any ideas or improvements, feel free to create a pull request. Please make sure your contributions are well-documented and tested.

1. Fork the project.
2. Create your feature branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a pull request.

