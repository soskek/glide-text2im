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
    author="OpenAI",
)
