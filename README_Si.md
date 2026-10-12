# Si MACE MLIP — Training & Lattice Parameter Test

## Dataset Attribution

This project uses publicly released Si structures and VASP single-point outputs from:

**TFL600 — Claude Code Tutorial: MLIP Training Dataset Generation with VASP on ARCHER2**
🔗 [https://github.com/TFL600/claude-code-tutorial_MLIP-training](https://github.com/TFL600/claude-code-tutorial_MLIP-training)

All credit for dataset generation, VASP calculations, and workflow design belongs to the original author. The dataset includes 50 rattled + strained Si structures with parsed extxyz files (`train.xyz`, `val.xyz`, `test.xyz`).

>  If you have HPC access, we recommend generating rattled structures yourself using the original tutorial above.

---

## What We Did

Using the attributed dataset, we:

1. **Trained a MACE MLIP** for crystalline Si on local CPU/GPU
2. **Converted the model** to LAMMPS format → [`mace_Si.model-lammps.pt`](https://github.com/ullaharslan/Si-Config/blob/main/Results/mace_Si.model-lammps.pt)
3. **Tested the potential** by computing the equilibrium lattice parameter of Si

| Property | DFT reference | MACE (this work) |
|---|---|---|
| Lattice parameter *a₀* (Å) | 5.469 | ~5.47 |

---

## License

MIT License — covers only original code and documentation in this repository.
External datasets remain under their respective licenses.

---

## Contact

**Irslan Ullah Ashraf** — Computational Physicist
🔗 [github.com/ullaharslan](https://github.com/ullaharslan) · 📧 ullaharslan@gmail.com
