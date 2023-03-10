from setuptools import setup, find_packages

remove = '-e .'
def get_requirements(requirements_file):
    with open(requirements_file, 'r') as f:
        requirements = f.read().splitlines()
    if remove in requirements:
        requirements.remove(remove)
    return list(requirements)

print(get_requirements(requirements_file='requirements.txt'))

setup(
    name='mlproject',
    version='0.1.0',
    author='Akshat',
    description='A small example package for an ML project',
    packages=find_packages(),
    # install_requires=['pandas', 'numpy', 'scikit-learn', 'seaborn']
    install_requires=get_requirements(requirements_file='requirements.txt'),

)