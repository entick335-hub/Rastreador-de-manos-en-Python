import cv2
import mediapipe as mp

# Deteccion de manos
mp_hands = mp.solutions.hands

# Dibujo de las conexiones
mp_draw = mp.solutions.drawing_utils

# Captura o camara
cap = cv2.VideoCapture(2)
cap.set(3, 1280)
cap.set(4, 720)


def main():
    while True:
        attempt = 0
        success, img = cap.read()
        while not success and attempt < 5:
            time.sleep(0.2)
            success, img = cap.read()
            attempt += 1
        if not success:
            print("Failed to read frame")
            break

if __name__ == "__main__":
    main()