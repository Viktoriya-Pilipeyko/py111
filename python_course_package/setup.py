import setuptools
from setuptools import version

setuptools.setup(
    name = "python_course_package_demo",
    version = "0.0.1",
    author = "PVV",
    long_description = "test package",
    long_descriprion_content_type = "text/markdown",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independet",
    ],
    python_requires = ">=3.6"
)   