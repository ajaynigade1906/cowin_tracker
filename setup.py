import pathlib

from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='cowin_tracker',
    version='1.0.1',
    description='Python wrapper for CoWin APIs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ajay Nigade',
    author_email='ajay.nigade2012@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Environment :: Console',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='cowin, vaccine booking, cowin registrarion, vaccine, python cowin, cowin pip',
    include_package_data=True,
    python_requires='>=3.6, <4',
    install_requires=[
        'fake-useragent==0.1.11',
        'pytest==6.2.3',
        'requests==2.25.1'
    ],
    project_urls={  # Optional

    },
)
