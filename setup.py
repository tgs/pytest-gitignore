from setuptools import setup


setup(
    name = 'pytest-gitignore',
    version = '1.3',
    description = 'py.test plugin to ignore the same files as git',
    url = 'https://github.com/tgs/pytest-gitignore',
    long_description = open('README.txt').read(),
    author = 'Thomas Grenfell Smith',
    author_email = 'smithtg@ncbi.nlm.nih.gov',
    py_modules = ['pytest_gitignore'],
    entry_points = {
        'pytest11': [
            'gitignore = pytest_gitignore',
        ],
    },
    classifiers = [
        'License :: Public Domain',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing',
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Version Control',
    ],
    install_requires = [
        'pytest>=2.7',
    ],
)
