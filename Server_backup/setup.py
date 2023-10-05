from setuptools import setup, find_packages

# Read the contents of your requirements.txt file
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name='App.py',
    version='1',  # Replace with your project version
    packages=find_packages(),  # Automatically discover and include all Python packages in your project directory
    install_requires=requirements,  # List of dependencies from requirements.txt
    entry_points={
        'console_scripts': [
            'App.py = App.py.main:main',  # Replace with the appropriate entry point for your project
        ],
    },
)