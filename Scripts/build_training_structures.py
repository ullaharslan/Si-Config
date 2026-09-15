"""
Create displaced and strained structures from a reference POSCAR
for use in machine-learning interatomic potential training.

Each output structure has:
    - small random atomic displacements applied
    - a small random symmetric strain applied to the cell

Results are saved as individual POSCARs under vasp-singlepoints/<NNN>/
and also collected into a single extended XYZ file.

Usage:
    python build_training_structures.py
    python build_training_structures.py --count 100 --disp 0.03 --strain 0.01
"""

import argparse
import numpy as np
from pathlib import Path
from ase.io import read, write


def apply_random_strain(atoms, strain_magnitude, rng):
    """Perturb the unit cell with a small symmetric strain tensor."""
    raw = rng.normal(0.0, strain_magnitude, (3, 3))
    sym_strain = (raw + raw.T) / 2.0
    deformed_cell = atoms.cell[:] @ (np.eye(3) + sym_strain)
    atoms.set_cell(deformed_cell, scale_atoms=True)
    return atoms


def parse_args():
    p = argparse.ArgumentParser(description="Generate perturbed VASP structures")
    p.add_argument("--count",  type=int,   default=50,   help="Number of structures (default: 50)")
    p.add_argument("--disp",   type=float, default=0.05, help="Displacement stdev in Angstrom (default: 0.05)")
    p.add_argument("--strain", type=float, default=0.02, help="Strain tensor stdev (default: 0.02)")
    p.add_argument("--seed",   type=int,   default=42,   help="Random seed (default: 42)")
    return p.parse_args()


def main():
    args = parse_args()

    master_rng = np.random.default_rng(args.seed)

    reference_path = Path("vasp-inputs") / "POSCAR"
    reference = read(str(reference_path))
    print(f"Reference structure loaded: {len(reference)} atoms")

    output_root = Path("vasp-singlepoints")
    output_root.mkdir(exist_ok=True)

    collected = []

    for idx in range(args.count):
        structure = reference.copy()

        apply_random_strain(structure, args.strain, master_rng)

        child_seed = int(master_rng.integers(2**31))
        structure.rattle(stdev=args.disp, rng=np.random.default_rng(child_seed))

        folder = output_root / f"{idx:03d}"
        folder.mkdir(exist_ok=True)
        write(str(folder / "POSCAR"), structure, format="vasp", direct=True)

        collected.append(structure)
        print(f"  {idx:03d} written")

    xyz_out = Path("generated_structures.xyz")
    write(str(xyz_out), collected, format="extxyz")

    print(f"\nDone.")
    print(f"  POSCAR directories : {output_root}/")
    print(f"  Combined XYZ file  : {xyz_out}")
    print(f"  Total structures   : {len(collected)}")


if __name__ == "__main__":
    main()
