#!/usr/bin/env python

import pathlib
import sys

from setuptools import find_packages, setup

import versioneer

LONG_DESCRIPTION = """
Ibis is a productivity-centric Python big data framework.

See http://docs.ibis-project.org
"""

VERSION = sys.version_info.major, sys.version_info.minor

impala_requires = ['hdfs>=2.0.16', 'sqlalchemy>=1.1', 'requests']
if VERSION == (3, 5):
    impala_requires.append('impyla<0.14.2')
else:
    impala_requires.append('impyla>=0.15.0')

sqlite_requires = ['sqlalchemy>=1.1']
postgres_requires = sqlite_requires + ['psycopg2']
mysql_requires = sqlite_requires + ['pymysql']

if VERSION == (3, 5):
    mapd_requires = ['pymapd>=0.8.3,<0.11.0']
else:
    mapd_requires = ['pymapd>=0.12.0']
kerberos_requires = ['requests-kerberos']
visualization_requires = ['graphviz']
clickhouse_requires = ['clickhouse-driver>=0.0.8', 'clickhouse-cityhash']
bigquery_requires = ['google-cloud-bigquery>=1.0.0', 'pydata-google-auth']
hdf5_requires = ['tables>=3.0.0']

if VERSION == (3, 5):
    parquet_requires = ['pyarrow<0.12.0']
else:
    parquet_requires = ['pyarrow>=0.12.0']
spark_requires = ['pyspark>=2.4.3']

geospatial_requires = ['geoalchemy2', 'geopandas', 'shapely']

all_requires = (
    impala_requires
    + postgres_requires
    + mapd_requires
    + mysql_requires
    + kerberos_requires
    + visualization_requires
    + clickhouse_requires
    + bigquery_requires
    + hdf5_requires
    + parquet_requires
    + spark_requires
    + geospatial_requires
)

develop_requires = all_requires + [
    'click',
    'flake8',
    'isort',
    'mypy',
    'pre-commit',
    'pygit2',
    'pytest>=4.5',
]

install_requires = [
    line.strip()
    for line in pathlib.Path(__file__)
    .parent.joinpath('requirements.txt')
    .read_text()
    .splitlines()
]

setup(
    name='ibis-framework',
    url='https://github.com/ibis-project/ibis',
    packages=find_packages(),
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    install_requires=install_requires,
    python_requires='>=3.5',
    extras_require={
        'all': all_requires,
        'develop:python_version > "3.5"': develop_requires + ['black'],
        'develop:python_version == "3.5"': develop_requires,
        'impala': impala_requires,
        'kerberos': kerberos_requires,
        'postgres': postgres_requires,
        'mapd': mapd_requires,
        'mysql': mysql_requires,
        'sqlite': sqlite_requires,
        'visualization': visualization_requires,
        'clickhouse': clickhouse_requires,
        'bigquery': bigquery_requires,
        'hdf5': hdf5_requires,
        'parquet': parquet_requires,
        'spark' : spark_requires,
        'geospatial': geospatial_requires,
    },
    description="Productivity-centric Python Big Data Framework",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
    ],
    license='Apache License, Version 2.0',
    maintainer="Phillip Cloud",
    maintainer_email="phillip.cloud@twosigma.com",
)
