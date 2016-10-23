#encoding:utf-8
from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(name='qn',
      version=version,
      description="上传图片到七牛云存储",
      long_description="""上传图片到七牛云存储""",
      classifiers=[],
      keywords='python qiniu image upload',
      author='recall',
      author_email='tk657309822@gmail.com',
      url='https://github.com/recall704',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['qiniu','sevencow'],
      entry_points={
        'console_scripts':[
            'qn = qn.qn:main'
        ]
      },
)
