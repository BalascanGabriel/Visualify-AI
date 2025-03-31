# scripts/generate_image.py
import sys
from diffusers import StableDiffusionPipeline
import torch

def main():
    prompt = sys.argv[1]
    output_path = sys.argv[2]

    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    )

    if torch.cuda.is_available():
        pipe = pipe.to("cuda")

    image = pipe(prompt).images[0]
    image.save(output_path)
    print(f"✅ Imagine generată: {output_path}")

if __name__ == "__main__":
    main()
