try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name='numcompress',
    packages=['numcompress'],
    version='0.1.2',
    description='Python package to convert numerical series & numpy arrays into compressed strings',
    long_description_content_type = "text/markdown",
    long_description = long_descr,
    author='Amit Rathi',
    author_email='amit.juschill@gmail.com',
    url='https://github.com/amit1rrr/numcompress',
    license='MIT',
    download_url='',
    keywords=['compression', 'numerical', 'numbers into text'],
    classifiers=[],
    install_requires=['numpy'],
)
