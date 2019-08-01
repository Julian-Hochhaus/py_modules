import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='tab2latex',
    version="0.1.2",
    description="A small Python package that puts your numpy arrays into latex files using the table/longtable environment",
    url="https://github.com/Julian-Hochhaus/py_modules/tree/master/modules/tab2latex",
    author="Julian Hochhaus",
    author_email="julian.hochhaus@tu-dortmund.de",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
	test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
