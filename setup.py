import os
import setuptools


def requirements():
    with open(os.path.join(os.path.dirname(__file__), 'requirements.txt'), encoding='utf-8') as f:
        return f.read().splitlines()


setuptools.setup(
    name="task12",
    version="1.0.53",
    license='MIT',
    author="judy3378",
    author_email="judykim1718@gmail.com",
    description="tools for Natural Language Processing: doc classification",
    long_description=open('README.md').read(),
    url="https://https://github.com/t3q-intern2023-2/task12",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={
        'ratsnlp.nlpbook.classification': ['*.html']
    },
    install_requires=requirements(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
