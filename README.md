# PianoAI

## Utilisation avec Docker

### Prérequis
Avant de commencer, assurez-vous d'avoir installé les logiciels suivants :
- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation et exécution

1. Clonez le projet :
   ```sh
   git clone https://github.com/mathieumarcelino/PianoAIAPI.git
   ```

2. Accédez au dossier du projet :
   ```sh
   cd PianoAIAPI
   ```

3. Construisez et lancez le projet avec Docker :
   ```sh
   docker-compose up --build
   ```

4. Accédez à l'application via :
   [http://localhost:8000/music/g/a%20a%20a/100/0.5](http://localhost:8000/music/g/a%20a%20a/100/0.5)

### Dépannage
- Si un port est déjà utilisé, modifiez le port d'écoute dans `docker-compose.yml`.
- Pour relancer proprement le conteneur :
  ```sh
  docker-compose down && docker-compose up --build
  ```

### Arrêt de l'application
Pour arrêter l'application, exécutez :
```sh
  docker-compose down
```

