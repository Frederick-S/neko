from setuptools import setup, find_packages

setup(
    name='neko',
    packages=find_packages(exclude=['tests']),
    version='0.0.9',
    entry_points={
        'console_scripts': [
            'neko = neko.main:main'
        ]
    },
    description='A simple static site generator.',
    url='https://github.com/Frederick-S/neko',
    install_requires=[
        'python-frontmatter',
        'Markdown',
        'Jinja2'
    ],
    include_package_data=True
)
