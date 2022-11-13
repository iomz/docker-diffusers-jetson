docker-diffusers-jetson
---

[Diffusers](https://github.com/huggingface/diffusers) for NVIDIA Jetson with the [NVIDIA L4T PyTorch] container.

See my post: https://iomz.github.io/blog/docker-diffusers-jetson

# Synopsis

1. Clone this repo.
```sh
git clone https://github.com/iomz/docker-diffusers-jetson
```

2. Clone a model from Huging Face (e.g., runwayml/stable-diffusion-v1-5)
```sh
mkdir -p docker-diffusers-jetson/models && cd $_
git clone https://huggingface.co/runwayml/stable-diffusion-v1-5
```

3. Try the txt2img
```sh
docker-compose run --rm txt2img --model models/stable-diffusion-v1-5 "abandoned building in forest with beautiful glass windows"
```

