# PianoAI

**PianoAI** is an **AI-powered music generation** tool that allows users to create melodies dynamically through an API.

## Link

[piano.mathi3u.com](https://piano.mathi3u.com/)

## Example

### Request :
```sh
GET http://localhost:8000/music/g/a%20a%20a/52/0.5
```

### Response :
```
a a a d b3 d b a f d e2 d e f g f e d e f g a b c d c b a b a g f g a b c b
```

## Usage
#### Clone the repository
   ```sh
   git clone https://github.com/mathieumarcelino/PianoAIAPI.git
   ```

#### Build and run the project using Docker
   ```sh
   docker-compose up --build
   ```

#### Access the application
   [http://localhost:8000/music/g/[prompt]/[length]/[creativity]](http://localhost:8000/music/g/a%20a%20a/100/0.5)