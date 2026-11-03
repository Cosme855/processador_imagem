from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    page_description = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="processador_imagens",
    version="0.0.1",
    author="Silvio Cosme",
    author_email="cosme8556@gmail.com",
    description="Um pacote simples de processamento de imagens para integração com análise de dados",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cosme855/sistema-bancario-python", # Pode ajustar para o repositório correto depois
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)