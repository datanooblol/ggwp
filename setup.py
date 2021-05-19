import setuptools

import configparser

config_path = './resource/config.cfg'
# read config
parser = configparser.ConfigParser()
parser.read(config_path)
version = parser['default']['version']

# save README.md as var
with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = [
    "pandas",
    "numpy",
    "sklearn",
    "xgboost",
]

# version = "0.0.30"


setuptools.setup(
    name="ggwp", 
    version=version,
    license='MIT',
    author="Pathompol Nilchaikovit",
    author_email="data.noob.lol@gmail.com",
    description="Prepare Fast, Analyze Faster",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/datanooblol/ggwp",
    install_requires=requirements,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)