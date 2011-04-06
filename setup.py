from setuptools import setup, find_packages

setup(
    name = "txtlocal",
	packages = find_packages(),
    include_package_data=True,
    install_requires=[
    ],
    version = "1.0",
    description = "Incuna app for sending SMS messages via http://www.txtlocal.co.uk",
    author = "Incuna Ltd",
    author_email = "admin@incuna.com",
    url = "http://incuna.com/",
)
