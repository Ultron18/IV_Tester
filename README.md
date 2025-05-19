# Large File Split & Merge Utility for GitHub Compatibility

This repository contains Python scripts to help manage large files exceeding GitHub's file size limits by splitting and merging them efficiently.

---

## Why This?

GitHub limits file size to 100 MB, and recommends files be under 50 MB for smooth usage.  
This tool helps you:

- **Split large files (>100 MB) into smaller chunks (~100 MB)** before pushing to GitHub.  
- **Merge those chunks back into the original large files** after cloning or pulling from GitHub.

---

## Files

- `split_large_files.py`  
  Walks through the repository and splits files larger than 100 MB into parts named like `filename_part_aa`, `filename_part_ab`, etc., and deletes the original large files.

- `merge_small_files.py`  
  Finds split parts (matching `_part_??`) and merges them back into the original file with a `.raw` extension, then deletes the split parts.

---

## How to Use

### 1. Clone the repository

```bash
git clone https://github.com/Ultron18/IV_Tester.git
cd IV_Tester
```

### 2. Merge split files after cloning (using Git Bash)
After pulling/cloning the repo, run the merge script to reconstruct the original files:

```bash
python3 merge_small_files.py
```
This will scan the repo (excluding `.git`), find all split parts, and merge them into their original `.raw` files.

## Notes
- Both scripts exclude the .git directory during file scanning to avoid unnecessary operations on git internals.

- The scripts assume usage with Git Bash on Windows for compatibility with Unix-style commands and paths.

## Requirements
- Python 3.x
- Git Bash (if on Windows)

---
---

# IV_Tester Repository Overview

This repository contains tools, simulations, and documentation related to IV Tester development, LTspice subcircuit generation, and solar cell simulation projects.

---

## Repository Structure
```
IV_Tester/
├── Continuous bus probing for unanimous voltage and current probing for PV array/
├── Simulation/
├── lines.ipynb
├── merge_small_files.py
├── split_large_files.py
```


---

## Directory Details

### `Continuous bus probing for unanimous voltage and current probing for PV array/`

- Contains all content related to **IV Tester LTspice `.subckt` generation and usage**.  
- Excludes research papers and project updates, which are documented separately under the **Sem 7** folder for your BTP.

### `Simulation/`

- Holds various versions of Python simulations utilizing the **ltspice** Python module to:  
  - Create netlists  
  - Run LTspice simulations  
  - Parse `.raw` files to obtain time-evolving datasets of node voltages and component currents.

- The different versions address additional features or fix flaws found in previous iterations.

- Also includes LTspice files for subcircuits developed during **Sem 7**:
  - `IV_Tester_Probing_LTSpice/`
  - `SPICE_to_ref/`
  - Measurement circuitry for:
    - FVMI method: `FV_MI_with_FEM/`
    - FIMV method: `FI_MV_with_FEM/`

- Additional files:  
  - `resistance_eval.ipynb` — Evaluates parameters measured for input into the FEM solar cell simulation netlist creation.  
  - To-Do files (`ToDo_New_Apr16.txt` and `ToDo_Overview.txt`) — Personal tracking documents that can be ignored for general use.

---

## `Simulation` Directory Structure
```
Simulation/
├── FEM_ForRef/
├── FEM_Mk0/
├── FEM_Mk1/
├── FEM_Mk2/
├── FEM_Mk3/
├── FEM_Mk4/
├── FEM_Mk5/
├── FEM_Mk6/
├── FEM_Mk7_ForSpiceCheck/
├── FEM_Mk8/
├── FEM_Mk9/
├── FI_MV_with_FEM/
├── FV_MI_with_FEM/
├── IV_Tester_Probing_LTSpice/
├── IterativeCode/
├── SPICE_to_ref/
├── resistance_eval.ipynb
├── ToDo_New_Apr16.txt
└── ToDo_Overview.txt
```

---
---
# Instructions to follow
If merging is done, go to `Simulation` directory to see the different versions of simulation work performed in Sem 8.
