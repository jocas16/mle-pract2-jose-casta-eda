# Usa la imagen oficial de Python 3.9
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requerimientos al directorio de trabajo
COPY requirements.txt .

# Copia los archivos de la aplicación y los archivos utilitarios al directorio de trabajo
COPY app.py .
COPY utils.py .

# Instala las dependencias especificadas en el archivo de requerimientos
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8501 para que Streamlit pueda servir la aplicación
EXPOSE 8000

# Ejecuta la aplicación de Streamlit cuando el contenedor se inicia
CMD ["streamlit", "run", "app.py", "--host", "0.0.0.0", "--port", "8000"]

