# Usa una imagen oficial de Python
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 5000 para Flask (o FastAPI con Uvicorn)
EXPOSE 5000

# Comando para iniciar la app con recarga automática
CMD ["python", "app.py"]
