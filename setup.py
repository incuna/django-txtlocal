from setuptools import setup, find_packages

setup(
    name='django-txtlocal',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['requests>=1.2.3'],
    version='0.2',
    description='App for sending and receiving SMS messages via http://www.textlocal.com',
    author='Incuna Ltd',
    author_email='admin@incuna.com',
    url='https://github.com/incuna/django-txtlocal/',
)
