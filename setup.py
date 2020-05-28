import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="agpypeline",
    version="0.0.1",
    author="Jacob van der Leeuw",
    author_email="jvanderleeuw@email.arizona.edu",
    description="Installable package for entrypoint and drone-specific environment code within a transformer",
    long_description="Package containing entrypoint.py from entrypoint code and transformer_class.py "
                     "for drone-specific environment code. This allows for transformers to have"
                     "common entrypoint and environment code in an installable package",
    long_description_content_type="text/markdown",
    url="https://github.com/AgPipeline/agpypeline",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: BSD 3-Clause License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=['setuptools', 'numpy', 'influxdb', 'laspy', 'requests==2.21.0', 'python-dateutil', 'utm',
                      'matplotlib', 'Pillow', 'scipy', 'piexif', 'cryptography']

)
