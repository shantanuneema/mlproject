from setuptools import find_packages, setup
from typing import List

HYPHEN_E = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """ function to read requirements for the package
        arg: file_path containing a list of packages from pypi required to run this project
    """
    requirements = []
    with open(file_path) as f:
        # read line-by-line and replace the newline char in the list
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements if req != HYPHEN_E]

    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Shantanu',
author_email='shantanuneema@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)