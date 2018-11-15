# coding: utf-8

"""
    wordcount_search

    Apps that count the number of specific characters  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: ghwlchlaks@naver.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="wordcount_search",
    author_email="ghwlchlaks@naver.com",
    url="",
    keywords=["Swagger", "wordcount_search"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Apps that count the number of specific characters  # noqa: E501
    """
)
