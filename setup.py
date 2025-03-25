from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of dependencies.
    """
    with open(file_path, "r") as file_obj:
        requirements = [req.strip() for req in file_obj.readlines() if req.strip()]

        # Remove '-e .' if present (used for editable installs)
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Umesh Maurya",
    author_email="umeshmaurya625@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)