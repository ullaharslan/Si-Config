"""
Reads VASP OUTCAR files from a directory of single-point calculations
and writes train/val/test splits in extxyz format for MACE training.

Directory layout expected:
    vasp-singlepoints/
        0000/OUTCAR
        0001/OUTCAR
        ...

Output:
    training_data/train.xyz   (first 40 structures)
    training_data/val.xyz     (next 5 structures)
    training_data/test.xyz    (remaining structures)

Usage:
    python prepare_mace_dataset.py
"""

import pathlib
import random
from ase.io import read, write

RANDOM_SEED = 42
TRAIN_COUNT = 40
VAL_COUNT = 5

random.seed(RANDOM_SEED)

calc_root = pathlib.Path("vasp-singlepoints")
calc_dirs = sorted(calc_root.glob("[0-9]*/"))
print(f"Located {len(calc_dirs)} OUTCAR directories under {calc_root}/")

all_structures = []

for folder in calc_dirs:
    outcar_path = folder / "OUTCAR"
    atoms = read(str(outcar_path), format="vasp-out")

    energy = atoms.get_potential_energy()
    forces = atoms.get_forces()
    stress = atoms.get_stress(voigt=False).flatten().tolist()

    atoms.info["REF_energy"] = energy
    atoms.info["REF_stress"] = stress
    atoms.arrays["REF_forces"] = forces

    atoms.calc = None

    all_structures.append(atoms)
    print(f"  {folder.name}  energy = {energy:.6f} eV")

random.shuffle(all_structures)

train_set = all_structures[:TRAIN_COUNT]
val_set = all_structures[TRAIN_COUNT:TRAIN_COUNT + VAL_COUNT]
test_set = all_structures[TRAIN_COUNT + VAL_COUNT:]

out_dir = pathlib.Path("training_data")
out_dir.mkdir(exist_ok=True)

write(str(out_dir / "train.xyz"), train_set)
write(str(out_dir / "val.xyz"), val_set)
write(str(out_dir / "test.xyz"), test_set)

print(f"\nDataset written to {out_dir}/")
print(f"  train : {len(train_set)} structures")
print(f"  val   : {len(val_set)} structures")
print(f"  test  : {len(test_set)} structures")
