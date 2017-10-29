from setuptools import setup

setup(name="imagipy",
      version="0.1.0",
      description="Image handling",
      long_description="Tools for loading, manipualting and saving image files",
      url="https://imagipy.samireland.com",
      author="Sam Ireland",
      author_email="mail@samireland.com",
      license="MIT",
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Other Audience",
                   "License :: OSI Approved :: MIT License",
                   "Topic :: Communications",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.5",
                   "Programming Language :: Python :: 3.6"],
      packages=["imagipy", "imagipy.models"],
      install_requires=[])
