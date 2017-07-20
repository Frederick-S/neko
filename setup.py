from setuptools import setup, find_packages

setup(
    name='neko',
    version='0.0.11',
    description='A simple static site generator.',
    url='https://github.com/Frederick-S/neko',
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'neko = neko.main:main'
        ]
    },
    install_requires=[
        'python-frontmatter',
        'Markdown',
        'Jinja2'
    ],
    include_package_data=True,
    test_suite="tests"
)
