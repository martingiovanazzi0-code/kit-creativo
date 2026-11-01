#!/usr/bin/env python3
"""Sincroniza lo compartido dentro de cada skill y arma los .zip para claude.ai.

Correlo cada vez que cambies algo en compartido/ (el render o una marca), antes de commitear:
  python3 tools/build.py

Qué hace:
  1. Copia compartido/*.py      → plugins/creativos/skills/<skill>/scripts/ (render, aplanar_foto)
  2. Copia compartido/marcas/   → plugins/creativos/skills/<skill>/marcas/
  3. Arma dist/<skill>.zip (la carpeta de la skill, lista para subir en claude.ai → Skills)
Cada skill queda autocontenida: funciona igual instalada como plugin o subida sola.
"""
import shutil
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
COMPARTIDO = RAIZ / "compartido"
SKILLS = RAIZ / "plugins" / "creativos" / "skills"
DIST = RAIZ / "dist"


def main():
    DIST.mkdir(exist_ok=True)
    for skill in sorted(p for p in SKILLS.iterdir() if (p / "SKILL.md").exists()):
        (skill / "scripts").mkdir(exist_ok=True)
        for script in COMPARTIDO.glob("*.py"):
            shutil.copy2(script, skill / "scripts" / script.name)
        if (skill / "marcas").exists():
            shutil.rmtree(skill / "marcas")
        shutil.copytree(COMPARTIDO / "marcas", skill / "marcas")

        zip_path = DIST / f"{skill.name}.zip"
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(skill.rglob("*")):
                if f.is_file() and f.name != ".DS_Store" and "__pycache__" not in f.parts:
                    z.write(f, Path(skill.name) / f.relative_to(skill))
        print(f"ok  {skill.name}: scripts y marcas sincronizados, {zip_path.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
