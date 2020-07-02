from setuptools import setup, find_packages

setup(
    name='shuffleddp',
    version='1.0.0',
    url='https://github.com/adriagascon/amplification-by-shuffling.git',
    author='Borja Balle',
    author_email='bballe@gmail.com',
    description='Python implementation of the privacy amplification by shuffling results proved in the privacy blanket paper',
    packages=find_packages(),
    install_requires=['scipy > 1.5.0'],
)
