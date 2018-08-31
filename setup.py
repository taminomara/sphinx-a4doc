from setuptools import setup

setup(
   name='sphinx_a4doc',
   version='1.0.0',
   description='Sphinx domain and autodoc for Antlr4 grammar files',
   author='Vladimir Goncharov',
   author_email='dev.zelta@gmail.com',
   install_requires=[
       'sphinx>=1.7.0,<2.0.0',
       'antlr4-python3-runtime==4.7.1',
       'PyYAML'
   ],
)
