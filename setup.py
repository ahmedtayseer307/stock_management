from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in stok_managment/__init__.py
from stok_managment import __version__ as version

setup(
	name="stok_managment",
	version=version,
	description="app description",
	author="ahmedtayseer",
	author_email="app@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
