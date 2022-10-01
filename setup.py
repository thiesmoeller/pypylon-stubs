import os
from distutils.core import setup
from typing import List

from setuptools import find_packages


with open('README.md', 'r') as f:
    readme = f.read()

def find_stub_files(name: str) -> List[str]:
    result = []
    for root, dirs, files in os.walk(name):
        for file in files:
            if file.endswith('.pyi'):
                if os.path.sep in root:
                    sub_root = root.split(os.path.sep, 1)[-1]
                    file = os.path.join(sub_root, file)
                result.append(file)
    return result


setup(
    name="pypylon-stubs",
    version="0.0.1",
    description='PEP484 stubs for pypylon',
    long_description=readme,
    long_description_content_type='text/markdown',
    license='MIT',
    url="https://github.com/thies.moeller/pypylon-stubs",
    author="Thies Moeller",
    author_email="thies.moeller@gmail.com",
    py_modules=[],
    python_requires='>=3.6',
    install_requires=['pypylon'],
    packages=['pypylon-stubs', *find_packages()],
    package_data={'pypylon-stubs': find_stub_files('pypylon-stubs')},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
        'Programming Language :: Python :: 3.8'
        'Programming Language :: Python :: 3.9'
        'Programming Language :: Python :: 3.10'
    ]
)

