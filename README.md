<h1 align="center">⚖️ Protein Molecular Weight Calculator</h1>

<p align="center">
    A command-line utility to compute the molecular weight of a protein sequence.
</p>

<p align="center">
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License"></a>
</p>

A modular, zero-dependency Python CLI that computes protein molecular weight from a raw sequence or a FASTA file. It sums residue masses across the chain and adds the terminal water mass to return the weight in Daltons.

## Install

Clone the repository directly:
```bash
git clone https://github.com/eben-vranken/protein-molecular-weight-calc.git
cd protein-molecular-weight-calc
```

## Usage

Pass a raw protein sequence with `-s`, or a FASTA file with `-f`. Exactly one of the two is required.

```bash
python protein-weight-calc.py -s MTEYKLVVVGAGGVGKSALTIQ
```

### FASTA Input

```bash
python protein-weight-calc.py -f data/Q8WZ42.fasta
```

### Example Output
```
3,816,060.63 Daltons
```

## Configuration Matrix

| Argument | Option / Choices | Default | Description |
| --- | --- | --- | --- |
| `-s`, `--sequence` | *Protein sequence string* | *None* | Raw protein sequence to weigh (e.g. `MTEYK`). Required unless `-f` is used. |
| `-f`, `--file` | *File path* | *None* | Path to a FASTA protein file. Required unless `-s` is used. |

## Feature Set

* **Sequence Parsing:** Reads a raw sequence directly, or extracts and concatenates the sequence lines from a FASTA file, skipping header lines.
* **Residue-Based Weighing:** Sums per-residue masses (dehydrated, post-peptide-bond) across the full sequence.
* **Terminal Water Correction:** Adds the 18.02 Da water mass retained by the free N- and C-termini, so the result reflects the mass of the actual linear peptide rather than a fully-dehydrated chain.
* **Formatted Output:** Prints the total weight in Daltons with thousands separators.

## License

MIT