# PianoAI

**PianoAI** is an **AI-powered music generation tool** in **Python** that allows users to dynamically **create melodies** via an API.

## Link

[piano.mathi3u.com](https://piano.mathi3u.com/)

## Example

| Letter | Note   |
|--------|--------|
| A      | La     |
| B      | Si     |
| C      | Do     |
| D      | Ré     |
| E      | Mi     |
| F      | Fa     |
| G      | Sol    |

### Request :
```sh
GET http://localhost:8000/music/g/a%20a%20a/52/0.5
```
- a%20a%20a (a a a) : The prompt, the first ones that start the melody
- 52 : Length of the response
- 0.5 : Creativity of the response


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