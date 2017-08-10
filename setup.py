from setuptools import setup

setup(
    name='ezpz',
    version='0.1',
    py_modules=['ezpz'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        ezpz=ezpz:menu
    ''',
)
