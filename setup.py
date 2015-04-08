from setuptools import setup


setup(
    name = 'pytest-gitignore',
    version = '1.0',
    description = 'py.test plugin to ignore the same files as git',
    long_description = open('README.txt').read(),
    author = 'Thomas Grenfell Smith',
    author_email = 'smithtg@ncbi.nlm.nih.gov',
    py_modules = ['pytest_gitignore'],
    entry_points = {
        'pytest11': [
            'gitignore = pytest_gitignore',
        ],
    },
)
