import setuptools
import os

FILE_PATH = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(FILE_PATH, 'README.md'), 'r') as fh:
    long_description = fh.read()

requirements_path = os.path.join(FILE_PATH, 'requirements.txt')
with open(requirements_path) as f:
    required = f.read().splitlines()

setuptools.setup(
    name='pydingbot',
    version='0.0.3',
    author='Wentao Li',
    author_email='clarmylee92510@gmail.com',
    description='A package to make dingbot easily to use',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Clarmy/pydingbot',
    include_package_data=True,
    package_data={'': ['*.csv', '*.config', '*.nl', '*.json']},
    packages=setuptools.find_packages(),
    install_requires=required,
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6'
)