from setuptools import setup, find_packages

setup(
    name='cctexconvert',
    version='0.0.2',
    description='Converts Minecraft texture packs into ClassiCube texture packs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Fam0r',
    author_email='fam0r@mailbox.org',
    url='https://github.com/Fam0r/CCTexConvert',
    packages=find_packages(),
    install_requires=[
        'Pillow>=8.3.1'
    ],
    license='wtfpl',
    classifiers=[
        'Environment :: Console',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ],
    entry_points={
        'console_scripts': ['cctexconvert=cctexconvert.cli:main']
    }
)
