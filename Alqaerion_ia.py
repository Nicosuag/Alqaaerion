import tensorflow as tf
import numpy as np

def main():
    print(f"TensorFlow Version: {tf.__version__}")
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        print(f"GPUs disponibles: {gpus}")
        try:
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
            print("Crecimiento de memoria habilitado para GPUs.")
        except RuntimeError as e:
            print(f"Error al habilitar crecimiento de memoria: {e} (esto es normal si ya se inicializaron las GPUs)")
    else:
        print("No se encontraron GPUs, se usará CPU.")

    # 1. Definición del Modelo
    # Modelo secuencial con una capa de entrada de 64 unidades (para 64 características),
    # una capa oculta y una capa de salida con 1 unidad y activación sigmoide para clasificación binaria.
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(units=64, activation='relu', input_shape=(64,)),
        tf.keras.layers.Dense(units=32, activation='relu'), # Capa oculta adicional
        tf.keras.layers.Dense(units=1, activation='sigmoid')
    ])

    print("\n--- Resumen del Modelo ---")
    model.summary()

    # 2. Compilación del Modelo
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    print("\nModelo compilado.")

    # 3. Preparación de Datos de Ejemplo
    # 100 muestras, 64 características por muestra
    x_train = np.random.rand(100, 64)
    # 100 etiquetas, valores 0 o 1 (clasificación binaria)
    y_train = np.random.randint(0, 2, 100)
    print(f"\nForma de x_train: {x_train.shape}")
    print(f"Forma de y_train: {y_train.shape}")

    # 4. Entrenamiento del Modelo
    print("\n--- Iniciando Entrenamiento ---")
    history = model.fit(x_train, y_train, epochs=10, verbose=1) # verbose=1 para ver el progreso por época
    print("\n--- Entrenamiento Completado ---")

    # Opcional: Mostrar historial de entrenamiento
    print("\nHistorial de entrenamiento (pérdida y exactitud por época):")
    for epoch in range(len(history.history['loss'])):
        print(f"Epoch {epoch+1}: loss = {history.history['loss'][epoch]:.4f}, accuracy = {history.history['accuracy'][epoch]:.4f}")

if __name__ == '__main__':
    main()