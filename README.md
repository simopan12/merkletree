# 1) Clone the repo and access the folder
git clone https://github.com/simopan12/merkletree.git
cd merkletree

# 2) Install dependencies (creates .venv automatically)
uv sync

# 3) Run tests (unittest discovery)
uv run python -m unittest discover -s tests

