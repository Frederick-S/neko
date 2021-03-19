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
        'python-frontmatter==0.4.2',
        'Markdown==2.6.8',
        'Jinja2==2.11.3'
    ],
    include_package_data=True,
    test_suite="tests"
)
