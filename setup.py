import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

VERSION = "1.0.4a"

REQUIRES = ['pu_in_core', 'pu_in_content', 'django-compressor',
            'django-attachments', 'django-haystack', 'whoosh',
            'markdown', 'html2text', 'chardet'
            ]

setup(name='mrwolfe',
      version=VERSION,
      description='Django Issue tracker & support system',
      long_description=README,
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: Freely Distributable",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Software Development :: Libraries :: Application Frameworks"
        ],
      author='D.A.Dokter',
      author_email='dokter@w20e.com',
      license='beer-ware',
      url='https://github.com/wyldebeast-wunderliebe/mrwolfe/',
      keywords='django issuetracking support',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires = REQUIRES,
      tests_require= REQUIRES,
      test_suite="mrwolfe",
      entry_points = ""
      )
