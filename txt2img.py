#!/usr/bin/env python3
import argparse
import torch
from diffusers import StableDiffusionPipeline

def null_safety(images, **kwargs):
    return images, False

parser = argparse.ArgumentParser(description="run diffuser")
parser.add_argument("prompt", type=str, help="A text string to be passed as the prompt")
parser.add_argument("--model", type=str, default="/app/models/stable-diffusion-v1-5", help="The path to the model")
parser.add_argument("--device", type=str, default="cuda", help="The device")
parser.add_argument("--nis", type=int, default=51, help="The value for num_inference_steps")
parser.add_argument("--out", type=str, default="out.png", help="The result image file")
args = parser.parse_args()

pipe = StableDiffusionPipeline.from_pretrained(args.model, torch_dtype=torch.float16, revision="fp16")
pipe = pipe.to(args.device)

## Recommended if your computer has < 64 GB of RAM
#pipe.enable_attention_slicing()

# Detour the NSFW checker
pipe.safety_checker = null_safety

prompt = args.prompt

# Results match those from the device after the warmup pass.
with torch.autocast(args.device):
    image = pipe(prompt, num_inference_steps=args.nis).images[0]
    image.save(args.out)

