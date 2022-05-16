from distutils.core import setup

import setuptools

setup(
    name="fcommon",
    version="1.0",
    description="common modules for mal",
    author="dagrons",
    author_email="heyuehuii@126.com",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[        
        'mongoengine',        
    ]
)
