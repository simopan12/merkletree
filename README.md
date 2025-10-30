# MYMERKLETREE

**MYMERKLETREE** is a small Python library that implements a Merkle-tree-style compression to reduce arbitrarily long messages to a fixed 32-byte value using a salt.  
It exports a single function:

```python
from mymerkletree import merkletree
```

Given a message `m` and a salt `s`, the function:
1. returns `m` directly if `m` is **≤ 32 bytes**,
2. otherwise splits/pads the message to blocks of 32 bytes, hashes pairs of blocks together with the salt using **SHAKE-256** and recurses until a single 32-byte value remains.

---

## 1. Prerequisites

- **Python 3.8+**
- **uv** installed (Astral’s Python package manager)

If you don’t have `uv`, follow [the official uv documentation](https://docs.astral.sh/uv/getting-started/installation/)
.

---
### Development Envitonment Setup

1. **Download the repository**:
    ```bash
    unzip merkletree.zip
    cd merkletree
    ```
2. **Install dependencies and set up the environment**:
    ```bash
    uv sync
    ```
This command will:
- create the virtual environment (`.venv/`)
- install the project dependencies
- make the project ready to run

3. **Activate the virtual environment**:

```bash
# Linux / macOS
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\activate
```

---

## Running the tests

This project uses Python’s built-in **unittest**.

Run all tests with:

```bash
uv run python -m unittest discover -s tests
```

This command will search the `tests/` directory and execute all test cases.

### Test output

- **OK** → all tests passed  
- **FAIL / ERROR** → something is wrong in the implementation or the test; the traceback will tell you which test failed and why

---

## Usage example

Here’s a minimal example using your actual code:

```python
from mymerkletree import merkletree

m = "abcdefghijklmnopqrstuvwxyz1234567"   # longer than 32 bytes
s = "salt12345678901234567890123456"      # 32-byte-ish salt

digest = merkletree(m, s)

print(len(digest))   # 32
print(digest.hex())  # printable form
```

- You can pass **str** or **bytes** for both `m` and `s` — the function converts strings to bytes internally.
- If `m` is **≤ 32 bytes**, the function just returns the message bytes unchanged.

---

## Notes

- Ensure that your Python version is 3.8 or higher to avoid compatibility issues.
- The `uv sync` command simplifies the setup process by handling environment creation and dependency installation in one step.

---