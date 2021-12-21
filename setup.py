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
    package_data={'glide_text2im': ['tokenizer/*.gz', 'clip/config.yaml']},
    author="OpenAI",
)
