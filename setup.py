from setuptools import setup, find_packages

setup(
    name='notelink',
    version='0.0.1',
    author='Agung Yuliyanto',
    author_email='agung.96tm@gmail.com',
    description='Management your favorite link using CLI.',
    long_description='Management your favorite link using CLI.',
    packages=find_packages(
        exclude=['tests', 'docs',]
    ),
    include_package_data=True,
    install_requires=[i.strip() for i in open("requirements.txt").readlines()],
    entry_points={
        'console_scripts': [
            'notelink = src.main:cli',
        ],
    },
    classifiers=[
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
