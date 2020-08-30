try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='numcompress',
    packages=['numcompress'],
    version='0.1.1',
    description='Python package to convert numerical series into compressed strings',
    author='Amit Rathi',
    author_email='amit.juschill@gmail.com',
    url='https://github.com/amit1rrr/numcompress',
    license='MIT',
    download_url='',
    keywords=['compression', 'numerical', 'numbers into text'],
    classifiers=[],
    install_requires=['numpy'],
)
