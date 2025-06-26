from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    requirementslst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirements=line.strip()
                if requirements and requirements!='-e .':
                    requirementslst.append(requirements)

    except FileNotFoundError:
        print("requirements.txt not found")

    return requirementslst

print(get_requirements())

setup(
    name="Networksecurity",
    author="Sumit yesade",
    author_email="sumityesade14@gmail.com",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements(),

)

