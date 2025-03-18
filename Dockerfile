FROM python:3.7

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY required.txt ./

# Installer les dépendances
RUN pip install --no-cache-dir -r required.txt

# Copier le reste des fichiers
COPY . .

# Exposer le port utilisé par Flask
EXPOSE 8000

# Lancer l'application
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
