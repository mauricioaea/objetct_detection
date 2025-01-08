Hola amigos por aqui le dejo la Detección de Objetos con YOLOv8

Este proyecto implementa un modelo de detección de objetos utilizando YOLOv8 y OpenCV. El sistema es capaz de identificar múltiples objetos en tiempo real mediante una cámara o utilizando videos pregrabados.

## Requisitos previos
Antes de comenzar, asegúrate de cumplir con los siguientes requisitos:

## Instalar Python

Descarga e instala Python 3.9 o superior desde python.org.
Instalar Git

## Descarga e instala Git desde git-scm.com.
Clonar el repositorio

Usa el siguiente comando para clonar este proyecto:
bash
Copiar código
git clone https://github.com/mauricioaea/objetct_detection.git
cd objetct_detection
Crear un entorno virtual

## Para aislar las dependencias del proyecto, crea y activa un entorno virtual:
bash
Copiar código
python -m venv env
env\Scripts\activate  # En Windows
source env/bin/activate  # En macOS/Linux
Instalar dependencias

## Instala las librerías necesarias desde el archivo requirements.txt:
bash
Copiar código
pip install -r requirements.txt
Ejecución del código
1. Uso con cámara en tiempo real

## Para ejecutar la detección de objetos en tiempo real utilizando tu cámara, ejecuta el siguiente comando:

bash
Copiar código
python objects.py
2. Uso con un video pregrabado
Si deseas usar un video como fuente, modifica el archivo objects.py en la sección correspondiente (reemplaza el índice de la cámara con la ruta del archivo de video):

python
Copiar código
self.cap = cv2.VideoCapture('ruta_al_video.mp4')  # Cambia aquí
Luego, ejecuta:

bash
Copiar código
python objects.py
## Descarga del modelo YOLOv8
Debido a restricciones de tamaño, el archivo del modelo preentrenado (yolov8n.pt) no está incluido en este repositorio.
Descárgalo directamente desde Ultralytics y guárdalo en la raíz del proyecto, lo encontraras al final de este archivo.

## Estructura del proyecto
bash
Copiar código
.
├── env/                  # Entorno virtual (no incluido en Git)
├── objects.py            # Código principal del proyecto
├── requirements.txt      # Librerías necesarias
├── README.md             # Documentación del proyecto
└── yolov8n.pt            # Modelo preentrenado (descargar por separado)

## Notas importantes
Evita subir el entorno virtual (env/): Ya está excluido en .gitignore.
Tamaño máximo en GitHub: Si planeas realizar cambios, verifica que los archivos no superen el límite de 100 MB.

## Problemas comunes:
Si obtienes un error relacionado con OpenCV, asegúrate de que tu cámara está conectada y funciona correctamente.
Usa Python 3.9+ para evitar incompatibilidades con ciertas librerías.
Contribuciones
Si deseas contribuir a este proyecto, por favor abre un "Pull Request" o crea un "Issue". ¡Tu colaboración es bienvenida!


## Descargar el modelo preentrenado

Para utilizar este proyecto, es necesario descargar el modelo preentrenado `yolov8n.pt`. Puedes descargarlo desde el siguiente enlace:

[Descargar yolov8n.pt](https://github.com/ultralytics/ultralytics/releases) 

tambien lo puedes descargar en este enlace -> https://huggingface.co/Ultralytics/YOLOv8/blob/main/yolov8n.pt

## sientete libre de contactarme si necesitas ayuda, [mauricioandreserazo@outlokk.com] 

## Nota

## para la ejecución en tu terminal usa python objets.py


