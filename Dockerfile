# Imagen base oficial de Python
FROM python:3.12-slim

# Configurar directorio de trabajo
WORKDIR /app

# Instalar uv (administrador de dependencias rápido)
RUN pip install uv

# Copiar archivo de dependencias
COPY pyproject.toml .

# Instalar dependencias definidas en pyproject.toml
RUN uv pip install -r pyproject.toml --system

# Copiar el código de la aplicación
COPY . .

# Comando por defecto (puedes ajustarlo según tu aplicación)
CMD ["python", "main.py"]