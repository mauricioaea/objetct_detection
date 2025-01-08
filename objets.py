from ultralytics import YOLO
import cv2

class Camera:
    """Clase para manejar la interacción con la cámara."""
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cap = None

    def open(self):
        """Abre la cámara."""
        print("Intentando abrir la cámara...")
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            raise RuntimeError("Error: No se pudo acceder a la cámara. Verifica los permisos o el índice.")

    def read_frame(self):
        """Lee un frame de la cámara."""
        if not self.cap:
            raise RuntimeError("La cámara no está abierta.")
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("Error: No se pudo leer el frame.")
        return frame

    def release(self):
        """Libera los recursos de la cámara."""
        if self.cap:
            self.cap.release()

class YOLODetector:
    """Clase para manejar el modelo YOLO."""
    def __init__(self, model_path='yolov8n.pt'):
        self.model = YOLO(model_path)

    def predict(self, frame):
        """Realiza predicciones sobre un frame."""
        results = self.model(frame)
        return results[0].plot()

class RealTimeDetection:
    """Clase principal para gestionar la detección en tiempo real."""
    def __init__(self, detector: YOLODetector, camera: Camera):
        self.detector = detector
        self.camera = camera

    def start(self):
        """Inicia la detección en tiempo real."""
        try:
            self.camera.open()
            print("Cámara iniciada correctamente. Presiona 'q' para salir.")

            while True:
                frame = self.camera.read_frame()
                annotated_frame = self.detector.predict(frame)
                cv2.imshow("Detecciones en Tiempo Real", annotated_frame)

                # Salir presionando 'q'
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("Saliendo del programa...")
                    break
        except RuntimeError as e:
            print(e)
        finally:
            self.camera.release()
            cv2.destroyAllWindows()
            print("Recursos liberados y ventanas cerradas.")

# Uso del código refactorizado
if __name__ == "__main__":
    camera = Camera(camera_index=0)
    detector = YOLODetector(model_path='yolov8n.pt')
    realtime_detection = RealTimeDetection(detector, camera)
    realtime_detection.start()

