# CLI de Procesamiento de Transacciones Bancarias

## Introducción
Esta aplicación de línea de comandos (CLI) procesa un archivo CSV con transacciones bancarias y genera un reporte que incluye:
- **Balance Final**: suma de todos los montos de tipo “Crédito” menos la suma de los montos de tipo “Débito”.  
- **Transacción de Mayor Monto**: ID y monto de la transacción con el valor más alto.  
- **Conteo de Transacciones**: número total de transacciones de cada tipo (“Crédito” y “Débito”).

## Instrucciones de Ejecución

1. **Clonar el repositorio**  
   ```bash
   git clone https://github.com/tu-usuario/interbank-academy-25.git
   cd interbank-academy-25
   ```

2. **Instalar dependencias**  
   > Esta aplicación utiliza únicamente la librería estándar de Python. No hay paquetes adicionales que instalar.

3. **Ejecutar la aplicación**  
   ```bash
   py main.py data.csv
   python main.py data.csv
   C:/.../AppData/Local/Programs/Python/Python313/python.exe main.py data.csv
   ```
   - **Parámetros**  
     - `data.csv`: ruta al archivo CSV con columnas `id,tipo,monto`.

## Enfoque y Solución

1. **Lectura del CSV**  
   - Se emplea `csv.DictReader` para acceder a cada fila por nombre de columna (`id`, `tipo`, `monto`).

2. **Procesamiento de datos**  
   - Conversión de `monto` a `float`.  
   - Acumulación de totales de crédito y débito.  
   - Conteo de transacciones por tipo.  
   - Seguimiento de la transacción con el monto más alto.

3. **Manejo de errores**  
   - Omite filas con montos no numéricos o tipos desconocidos (se registran advertencias en stderr).  
   - Finaliza con mensaje de error si el archivo no existe o faltan columnas obligatorias.

## Estructura del Proyecto
```
interbank-academy-25/
├── main.py               # Código fuente de la CLI
├── data.csv      # Ejemplo de datos de entrada
└── README.md             # Documentación del proyecto
```

## Documentación y Calidad del Código
- **Comentarios inline** en `main.py` describen la finalidad de cada función y la lógica clave.  
- **Funciones y variables descriptivas** para mejorar la legibilidad.  
- **Mensajes claros** en la terminal para reportar el estado y errores.  
- Código organizado en responsabilidades únicas, facilitando pruebas y mantenimiento.