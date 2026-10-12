# Si MACE MLIP — Training & Lattice Parameter Test

## Dataset 

This project uses publicly released Si structures and VASP single-point outputs from:

**TFL600 — Claude Code Tutorial: MLIP Training Dataset Generation with VASP on ARCHER2**
🔗 [https://github.com/TFL600/claude-code-tutorial_MLIP-training](https://github.com/TFL600/claude-code-tutorial_MLIP-training)

All credit for dataset generation, VASP calculations, and workflow design belongs to the original author. The dataset includes 50 rattled + strained Si structures with parsed extxyz files (`train.xyz`, `val.xyz`, `test.xyz`).


---

## Workflow

Using the dataset of Si, we:

1. **Trained a MACE MLIP** for crystalline Si on local CPU/GPU (**mace_Si.model**)
2. **Converted the model** to LAMMPS format → [`mace_Si.model-lammps.pt`](https://github.com/ullaharslan/Si-Config/blob/main/Results/mace_Si.model-lammps.pt)
3. **Tested the potential** by computing the equilibrium lattice parameter of Si

| Property | DFT reference | MACE (this work) |
|---|---|---|
| Lattice parameter *a₀* (Å) | 5.43 | ~5.35 |

---

## License

MIT License (covers only original code and documentation in this repository).
External datasets remain under their respective licenses.

---

## Contact

**Irslan Ullah Ashraf** — Computational Physicist
📧 ullaharslan@gmail.com

**Hafsa Raza** — PhD Student
📧 hafsaraza2002@gmail.com
