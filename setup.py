from setuptools import setup

setup(
    name='neko',
    packages=['neko'],
    version='0.0.1',
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
