from setuptools import setup, find_packages

# Lê o conteúdo de requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as req_file:
    requirements = [line.strip() for line in req_file if line.strip() and not line.startswith("#")]

setup(
    name="SportMonks-CSV-Fetcher",
    version="0.1.1",
    author="Davi Moreira, João Gabriel",
    author_email="davimoreiraf@gmail.com",
    description="Uma ferramenta para facilitar o acesso e processamento de dados da API SportMonks",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/meninojohnsons/SportMonks-CSV-Fetcher",
    packages=find_packages(exclude=["tests*", "data"]),
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.7",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    # Caso queira expor comandos via CLI, descomente abaixo:
    # entry_points={
    #     'console_scripts': [
    #         'sportmonk=sportmonk_facilitator.pipeline.controller:main',
    #     ],
    # },
)