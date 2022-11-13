docker-diffusers-jetson
---

See https://iomz.github.io/blog/docker-diffusers-jetson

# Synopsis

1. Clone this repo.
```sh
git clone https://github.com/iomz/docker-diffusers-jetson
```

2. Clone a model from Huging Face (e.g., runwayml/stable-diffusion-v1-5)
```sh
cd docker-diffusers-jetson/models
git clone https://huggingface.co/runwayml/stable-diffusion-v1-5
```

3. Build the image via `docker-compose.yml`
```sh
docker-compose build
```

4. Try the txt2img
```sh
docker-compose run --rm txt2img --model ./stable-diffusion-v1-5 "a computer science phd student is studying stable diffusion"
```

