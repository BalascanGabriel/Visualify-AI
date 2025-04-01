import subprocess
from pathlib import Path

SCENE_DIR = Path("scripts/animator/generated_scenes")

for file in SCENE_DIR.glob("*.py"):
    scene_name = file.stem
    print(f"🎬 Rulez: {scene_name}")
    subprocess.run([
        "manim",
        "-pql",                         # poți schimba în -pqh sau -pqm pentru calitate mai mare
        str(file),
        scene_name
    ])
