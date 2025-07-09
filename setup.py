from setuptools import setup, find_packages

setup(
    name='genesisblock0',
    version='0.2',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'nun = genesis_cli.nun_cli:main'
        ]
    },

    author='Bojan Petar Milanović',
    description='Genesis Block 0: Foundation of the NuN Blockchain',
    url='https://github.com/bis3946/GenesisBlock0_NuN',
)
