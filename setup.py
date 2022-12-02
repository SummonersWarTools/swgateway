from setuptools import find_packages, setup

setup(
    name='swgateway',
    packages=find_packages(include=['swgateway*']),
    version='0.1.1',
    description='Python binding for Com2Us Summoners War API.',
    author='ziddia',
    license='MIT',
    install_requires=['withhive @ git+ssh://git@github.com/SummonersWarTools/withhive.git#egg=withhive-0.1'],
)