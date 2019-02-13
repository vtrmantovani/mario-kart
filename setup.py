from setuptools import find_packages, setup

setup(
    name='mario-kart',
    version='0.0.0',
    packages=find_packages(
        exclude=[
            '*.tests',
            '*.tests.*',
            'tests.*',
            'tests'
        ]
    ),
    entry_points={
        'console_scripts': [
            'mario-kart=mkart.__main__:main'
        ]
    },
)
