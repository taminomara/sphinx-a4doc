from setuptools import setup

setup(
    name='sphinx-a4doc',
    version='1.0.0',
    description='Sphinx domain and autodoc for Antlr4 grammar files',
    author='Vladimir Goncharov',
    author_email='dev.zelta@gmail.com',
    packages=[
        'sphinx_a4doc'
    ],
    install_requires=[
        'sphinx>=1.8.0,<2.0.0',
        'antlr4-python3-runtime==4.7.1',
        'PyYAML'
    ],
    zip_safe=False
)
