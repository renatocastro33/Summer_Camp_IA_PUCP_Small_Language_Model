# nanochat

![nanochat logo](dev/nanochat.png)

> The best ChatGPT that $100 can buy.

This repo is for the Small Language Models Workshop in Summer AI Camp at PUCP.

Follow these steps:

1. git clone the repository
2. Install uv package manager: !curl -LsSf https://astral.sh/uv/install.sh | sh
3. Add os.environ['PATH'] = f"/root/.cargo/bin:/root/.local/bin:{os.environ['PATH']}"
4. Create a virtual environment and install dependencies !uv venv and !uv sync
5. pip install -e .
6. For the foundational notebooks, get into "Class" folder
7. Create an account in Modal website https://modal.com/ for the final pipeline 4.Deploying_Nanochat.ipynb so you can use the deployed Nanochat

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
