from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()
    readme = readme[:readme.find('<!--- cut --->')]

setup(
    name='sphinx-a4doc',
    version='1.0.1',
    description='Sphinx domain and autodoc for Antlr4 grammars',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Vladimir Goncharov',
    author_email='dev.zelta@gmail.com',
    url='https://github.com/AmatanHead/sphinx-a4doc',
    packages=find_packages(),
    install_requires=[
        'sphinx>=1.8.0,<2.0.0',
        'antlr4-python3-runtime==4.7.1',
        'PyYAML'
    ],
    python_requires='>=3.7',
    license='MIT',
    keywords='sphinx antlr4 autodoc',
    project_urls={
        'Documentation': 'https://amatanhead.github.io/sphinx-a4doc/',
        'Source': 'https://github.com/AmatanHead/sphinx-a4doc',
        'Tracker': 'https://github.com/AmatanHead/sphinx-a4doc/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Extension',
        'Topic :: Software Development :: Documentation',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
    ],
    zip_safe=False,
    package_data={
        'sphinx_a4doc': ['_static/a4_railroad_diagram.css'],
    },
)
