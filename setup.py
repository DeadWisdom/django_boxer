"""
Django Boxer Setup.
"""

from setuptools import setup, find_packages

setup( name='django-boxer',
       version='1.0',
       description='Redirects outgoing emails to the database, letting you browse them. This is good for staging/qa servers.',
       author='Brantley Harris',
       author_email='brantley.harris@gmail.com',
       packages = find_packages(),
       include_package_data = True,
       zip_safe = False
      )
