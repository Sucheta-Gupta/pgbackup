from setuptools import find_packages,setup

with open('README.md','r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='Sucheta Gupta',
    description = 'A utility for backing up PostgresSQL',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AstroSucheta/pgbackup',
    packages=find_packages('src'),
    package_dir={'':'src'},
    install_requires=['boto3'],
    entry_points={
        'console_scripts': [
            'pgbackup=pgbackup.cli:main',
        ],
    }
)