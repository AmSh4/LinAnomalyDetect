from setuptools import setup, find_packages

setup(
    name='linanomalydetect',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy>=1.26.0',
        'pandas>=2.2.0',
        'torch>=2.4.0',
        'matplotlib>=3.9.0',
        'pyyaml>=6.0.1',
    ],
    entry_points={
        'console_scripts': [
            'linanomaly = main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='Linux system anomaly detection tool using ML',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/LinAnomalyDetect',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.12',
)