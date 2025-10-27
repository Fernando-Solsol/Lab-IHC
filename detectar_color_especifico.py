import cv2
import numpy as np

def detectar_color_especifico(ruta_imagen, color_nombre="Rojo"):
    # 1. Cargar la imagen
    imagen = cv2.imread(ruta_imagen)

    if imagen is None:
        print(f"Error: No se pudo cargar la imagen en {ruta_imagen}. Verifica la ruta o el formato del archivo.")
        return

    # Mostrar la imagen original para referencia
    cv2.imshow('Imagen Original', imagen)

    # 2. Convertir la imagen al espacio de color HSV
    # HSV (Hue, Saturation, Value) es ideal para la segmentación de colores porque
    # el "Hue" (matiz) representa el color en sí, independientemente de su brillo o intensidad.
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

    # 3. Definir los rangos para el color deseado en HSV
    # Cada color tiene un rango de valores de Hue, Saturation y Value.
    # El rojo es especial porque su rango de Hue se "envuelve" alrededor del espectro,
    # así que necesita dos rangos.

    if color_nombre.lower() == "rojo":
        # Rangos para el color rojo en HSV
        # Hue (matiz): 0-179 (OpenCV escala el hue de 0-360 a 0-179)
        # Saturation (saturación): 0-255
        # Value (valor/brillo): 0-255
        lower_bound_1 = np.array([0, 100, 100])
        upper_bound_1 = np.array([10, 255, 255])
        lower_bound_2 = np.array([160, 100, 100])
        upper_bound_2 = np.array([179, 255, 255])

        # Crear dos máscaras para el rojo y combinarlas
        mask1 = cv2.inRange(hsv, lower_bound_1, upper_bound_1)
        mask2 = cv2.inRange(hsv, lower_bound_2, upper_bound_2)
        final_mask = mask1 + mask2
        print(f"Detectando el color: {color_nombre}")

    elif color_nombre.lower() == "azul":
        # Rangos para el color azul en HSV
        lower_bound = np.array([90, 50, 50])
        upper_bound = np.array([130, 255, 255])
        final_mask = cv2.inRange(hsv, lower_bound, upper_bound)
        print(f"Detectando el color: {color_nombre}")

    elif color_nombre.lower() == "verde":
        # Rangos para el color verde en HSV
        lower_bound = np.array([40, 50, 50])
        upper_bound = np.array([80, 255, 255])
        final_mask = cv2.inRange(hsv, lower_bound, upper_bound)
        print(f"Detectando el color: {color_nombre}")

    else:
        print("Color no reconocido. Por favor, elige 'rojo', 'azul' o 'verde'.")
        return

    # 4. Aplicar la máscara a la imagen original
    # La máscara es una imagen binaria (blanco y negro) donde el blanco representa
    # los píxeles que caen dentro del rango de color definido.
    # cv2.bitwise_and combina la imagen original con la máscara,
    # mostrando solo los píxeles del color detectado.
    resultado_color = cv2.bitwise_and(imagen, imagen, mask=final_mask)

    # 5. Mostrar los resultados
    cv2.imshow(f'Color {color_nombre} Detectado', resultado_color)

    # Esperar indefinidamente hasta que se presione una tecla y luego cerrar las ventanas
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#Ejemplos para la deteccion de colores con la imagen en la misma carpeta:

detectar_color_especifico('colores_varios.png', "rojo")
# detectar_color_especifico('colores_varios.png', "azul")
# detectar_color_especifico('colores_varios.png', "verde")
