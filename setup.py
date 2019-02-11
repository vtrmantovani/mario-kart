from setuptools import find_packages, setup

setup(
    name='mario-kart',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mario-kart=mkart.__main__:main'
        ]
    },
)
