
from setuptools import find_packages,setup
from typing import List

hyper='-e .'
def get_requirements(filepath:str)->List[str]:
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if hyper in requirements:
            requirements.remove(hyper)
    return requirements
setup(
    name='mlendtoend',
    version='0.0.1',
    author='naveen',
    author_email='naveenkumarchapala686@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
