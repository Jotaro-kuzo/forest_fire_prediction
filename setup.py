from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    '''
    Docstring for get_requirements : This function return the installing package list of requirements
    
    :param file_path: Description
    :type file_path: str
    :return: installing packages list (requirements.txt)
    :rtype: List[str]
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements] #removing \n while reading requirements.txt file

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements




setup(
name = 'forestfireprediction',
version= '0.0.1',
author = 'Santhosh P',
author_email = 'sk6724486@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')


)

