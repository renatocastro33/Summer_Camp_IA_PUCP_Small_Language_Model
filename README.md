# nanochat

![nanochat logo](dev/nanochat.png)

> The best ChatGPT that $100 can buy.

This repo is for the Small Language Models Workshop in Summer AI Camp at PUCP.

Follow these steps:

# Nanochat — Setup & Usage Guide

This repository contains the Nanochat project along with foundational notebooks and a deployment pipeline.

Follow the steps below to set up the environment and run the project locally.

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone <repository_url>
cd <repository_name>
```

### 2. Install the uv package manager

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. Add uv and Cargo binaries to your PATH (for Jupyter / Colab users)
If you are running inside Jupyter or Google Colab, execute:
```bash
import os
os.environ['PATH'] = f"/root/.cargo/bin:/root/.local/bin:{os.environ['PATH']}"
```

### 4. Create a virtual environment and install dependencies
```bash
uv venv
uv sync
```

### 5. Install the project in editable mode
```bash
pip install -e .
```

### 6. Run the foundational notebooks
Navigate to the Class/ folder to explore the foundational notebooks:
```bash
cd Class
```

### 7. Deploy Nanochat with Modal (Final Pipeline)
Navigate to the Class/ folder to explore the foundational notebooks:

For the final pipeline (4.Deploying_Nanochat.ipynb), you will need a Modal account or any GPU Provider. Modal gives $30 in credits. So take your chance!

Create an account at: https://modal.com

Follow the notebook instructions to deploy Nanochat in the cloud

Use the deployed Nanochat endpoint for inference


## Cite

If you find nanochat helpful in your research cite simply as:

```bibtex
@misc{nanochat,
  author = {Andrej Karpathy},
  title = {nanochat: The best ChatGPT that $100 can buy},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/karpathy/nanochat}
}
```

## License

MIT
