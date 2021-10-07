from setuptools import setup,find_packages

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    "Operating System :: OS Independent"
]
setup(
    name = "Pml Parser",
    version = "1.0.0",
    description = "An alternate to XML but very easy to retrieve data using this python library",
    long_description = open("README.md").read(),
    long_description_content_type ="text/markdown",
    url = "",
    author = "AbdulWahab",
    author_email="jr.abdulwahab@gmail.com",
    license = "MIT",
    classifiers = classifiers,
    keywords = "",
    packages = find_packages(),
    install_requires = [],    
    python_requires=">=3.5"              
)