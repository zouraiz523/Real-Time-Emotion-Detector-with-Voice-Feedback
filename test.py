import cv2
from fer import FER
import pyttsx3

# Initialize the emotion detector
emotion_detector = FER()

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

# Start the webcam
cap = cv2.VideoCapture(0)

# Initialize a variable to track the last detected emotion
last_emotion = None

# Define a list of all possible emotions detected by FER
all_emotions = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

while(True):
    ret, frame = cap.read()

    if not ret:
        break

    # Detect emotions on the frame
    emotions = emotion_detector.detect_emotions(frame)

    if emotions:  # Check if any emotions were detected
        # Draw bounding boxes and emotions on the frame
        for emotion in emotions:
            (x, y, w, h) = emotion["box"]
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Get the dominant emotion
            dominant_emotion = max(emotion["emotions"], key=emotion["emotions"].get)
            
            # Print all detected emotions with percentages
            emotion_text = ', '.join([f"{emot}: {round(emotion['emotions'][emot]*100, 2)}%" for emot in all_emotions])
            cv2.putText(frame, emotion_text, (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (36, 255, 12), 2)
            cv2.putText(frame, dominant_emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

            # Speak the detected emotion only if it's different from the last detected one
            if dominant_emotion != last_emotion:
                engine.say(dominant_emotion)
                engine.runAndWait()

                # Update the last emotion to the current one
                last_emotion = dominant_emotion

    # Display the frame
    cv2.imshow('Emotion Detector', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
