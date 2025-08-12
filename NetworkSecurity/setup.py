'''
The setup.py file is an essential part of packaging and distributing Python projects. 
It is used by setuptools (or disutils in older Python versions) to define the configuration or your projects, 
such as its metadata, dependencies, and more
'''
from typing import List 
from setuptools import find_packages,setup


def get_requirements()->List[str]:
    '''
    This function will return list of requirements
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Read lines from the file 
            lines=file.readlines()
            ## Process each line 
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e.
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found')

    return requirement_lst

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Shinde Sudeep',
    author_email='shinde.s.sudeep@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)