from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in cbigdl_education/__init__.py
from cbigdl_education import __version__ as version

setup(
	name="cbigdl_education",
	version=version,
	description="Education Management System",
	author="cbigdl",
	author_email="gkdevs50@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
