import cv2
import os

label = input("¿Qué vas a capturar? (circle/square): ")
save_path = f"dataset/{label}"
os.makedirs(save_path, exist_ok=True)

cap = cv2.VideoCapture(0)
counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Captura (Presiona 's' para guardar, 'q' para salir)", frame)

    key = cv2.waitKey(1)
    if key == ord("s"):
        filename = os.path.join(save_path, f"{label}_{counter:03}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Guardado {filename}")
        counter += 1
    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
