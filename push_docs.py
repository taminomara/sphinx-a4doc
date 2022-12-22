#!/usr/bin/env python3
import contextlib
import os
import shutil
import tempfile


REPO = 'git@github.com:taminomara/sphinx-a4doc.git'

DOCS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'docs'))
BUILD_PATH = os.path.join(DOCS_PATH, 'build', 'html')


@contextlib.contextmanager
def tmpdir():
    path = tempfile.mkdtemp()
    try:
        yield path
    finally:
        shutil.rmtree(path)


@contextlib.contextmanager
def cd(path):
    old_path = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(old_path)


def build_html():
    with cd(DOCS_PATH):
        os.system('make html')


def push_html():
    with tmpdir() as tmp:
        path = os.path.join(tmp, 'html')
        shutil.copytree(BUILD_PATH, path)
        with cd(path):
            shutil.rmtree('.doctrees', ignore_errors=True)
            os.system('git init')
            os.system('git add .')
            os.system('git commit -m "update docs"')
            os.system('git push -f ' + REPO + ' main:gh-pages')


if __name__ == '__main__':
    build_html()
    push_html()
