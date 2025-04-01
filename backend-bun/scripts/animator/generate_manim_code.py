# scripts/animator/generate_manim_code.py

import json
import re
from pathlib import Path

TEMPLATE = """
from manim import *

class {scene_name}(Scene):
    def construct(self):
        title = Text("{title}", font_size=64).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        content = Text("{content}", font_size=36).next_to(title, DOWN)
        self.play(FadeIn(content))
        self.wait(3)
"""

def slugify(text):
    # Scoate tot ce nu e litera, cifră sau underscore
    text = re.sub(r"[^\w\s]", "", text)  # elimină ' " ( ) etc.
    return (
        text.replace(" ", "_")
            .replace("-", "")
            .replace(".", "")
            .replace(",", "")
            .replace("ă", "a").replace("â", "a").replace("î", "i")
            .replace("ș", "s").replace("ş", "s")
            .replace("ț", "t").replace("ţ", "t")
            .lower()
    )

def generate_from_structura(structura, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    idx = 1
    for capitol in structura:
        for subcapitol in capitol.get("subcapitole", []):
            for concept in subcapitol.get("concepte", []):
                scene_name = f"Scene{idx}_{slugify(concept)}"[:50]
                title = subcapitol.get("subcapitol", "Concept")
                content = concept
                code = TEMPLATE.format(scene_name=scene_name, title=title, content=content)

                file_path = output_dir / f"{scene_name}.py"
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(code)

                print(f"✅ Generat: {file_path}")
                idx += 1

def generate_manim_script(input_json, output_dir):
    with open(input_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    if "nodes" in data:
        print("➡️ Generare din noduri tip mindmap")
        for idx, node in enumerate(data["nodes"], start=1):
            scene_name = f"Scene{idx}_{slugify(node['label'])}"[:50]
            title = node["label"]
            content = f"Acesta este conceptul: {title}"
            code = TEMPLATE.format(scene_name=scene_name, title=title, content=content)

            file_path = Path(output_dir) / f"{scene_name}.py"
            Path(output_dir).mkdir(parents=True, exist_ok=True)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(code)

            print(f"✅ Generat: {file_path}")

    elif "structura" in data:
        print("➡️ Generare din structură AI completă")
        generate_from_structura(data["structura"], output_dir)
    else:
        print("⚠️ Format JSON necunoscut. Nu există 'nodes' sau 'structura'.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python generate_manim_code.py path_to_data.json output_dir")
    else:
        generate_manim_script(sys.argv[1], sys.argv[2])
