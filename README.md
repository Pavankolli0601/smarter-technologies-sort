# smarter-technologies-sort

A Python utility that routes packages to the correct handling stack based on physical dimensions and weight.

## Background

In an automated warehouse environment, not all packages can be processed the same way. This module implements the core classification logic that determines whether a package should go through standard processing, flagged for special handling, or rejected entirely.

## How It Works

The `sort()` function takes four arguments — width, height, length (in cm), and mass (in kg) — and returns one of three stack labels:

- **STANDARD** — package is neither bulky nor heavy, normal processing applies
- **SPECIAL** — package is either bulky or heavy, requires manual handling  
- **REJECTED** — package is both bulky and heavy, cannot be processed

**Bulky** means volume ≥ 1,000,000 cm³ or any single dimension ≥ 150 cm.  
**Heavy** means mass ≥ 20 kg.

## Usage
```python
from sort import sort

sort(10, 10, 10, 5)       # "STANDARD"
sort(150, 1, 1, 5)        # "SPECIAL"
sort(100, 100, 100, 20)   # "REJECTED"
```

## Running the Tests

No external dependencies — just Python 3.
```bash
python sort.py
```

Covers 15 cases including boundary values, float inputs, and all three stack outcomes.

## Requirements

- Python 3.6+
