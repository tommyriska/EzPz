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

    author='Tommy Riska'
    author_email='tommy.riska@icloud.com'
    description='Filesharing made easy'
    keywords='ezpz easy file sharing python sockets'
    url='https://github.com/tommyriska/ezpz'
)
