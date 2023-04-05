"""Setup config for Versatuple."""
from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='versatuple',
    url='https://github.com/ChipMcCallahan/Versatuple',
    author='Chip McCallahan',
    author_email='thisischipmccallahan@gmail.com',
    # Needed to actually package something
    packages=['versatuple'],
    package_dir={'versatuple': 'src'},
    # Needed for dependencies
    install_requires=[],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='LICENSE',
    description='Extension of namedtuple.',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
