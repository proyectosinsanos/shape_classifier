import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("model/shape_model.h5")
labels = ['circle', 'square']

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    resized = cv2.resize(frame, (64, 64))
    normalized = resized / 255.0
    input_img = np.expand_dims(normalized, axis=0)
    prediction = model.predict(input_img)
    label = labels[np.argmax(prediction)]

    cv2.putText(frame, f"Predicción: {label}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Clasificador de Forma", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
