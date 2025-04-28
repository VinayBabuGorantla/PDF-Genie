from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    Returns a list of requirements from the given file
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="PDF Genie - Chat with PDF using Open-Source LLMs",
    version='0.1.0',
    author="Vinay Babu Gorantla",
    author_email="vinayc.gorantla@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
