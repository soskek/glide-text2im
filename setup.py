from setuptools import setup

setup(
    name="glide-text2im",
    packages=["glide_text2im", "glide_text2im.tokenizer", "glide_text2im.clip"],
    install_requires=[
        "Pillow",
        "attrs",
        "torch",
        "filelock",
        "requests",
        "tqdm",
    ],
    data_files = [
        ("tokenizer", ["tokenizer/bpe_simple_vocab_16e6.txt.gz", "tokenizer/encoder.json.gz", "tokenizer/vocab.bpe.gz"]),
        ("clip", ["clip/config.yaml"]),
    ],
    author="OpenAI",
)
