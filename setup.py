from setuptools import setup

setup(
    name = 'runlog',
    version = '0.0',
    packages = ['runlog'],
    entry_points = {
        'console_scripts': [
            'runlog = runlog.__main__:main'
        ]
    })
