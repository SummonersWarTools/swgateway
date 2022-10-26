from setuptools import find_packages, setup

setup(
    name='swgateway',
    packages=find_packages(include=['swgateway']),
    version='0.1.0',
    description='Python binding for Com2Us Summoners War API.',
    author='ziddia',
    license='MIT',
    install_requires=['hive @ git+ssh://git@github.com/SummonersWarTools/hive.git#egg=hive-0.1'],
)