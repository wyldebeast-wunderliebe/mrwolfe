import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
VERSION = "1.2.0"
REQUIRES = ['django>=1.5', 'django-compressor',
            'django-attachments', 'django-haystack>=2.0', 'whoosh',
            'markdown', 'html2text', 'chardet',
            'jira-python', 'imapclient', 'tnefparse', 'django-bootstrap3'
            ]

setup(name='mrwolfe',
      version=VERSION,
      description='Django Issue tracker & support system',
      long_description=README,
      classifiers=[
          "Development Status :: 4 - Beta",
          "Framework :: Django",
          "Intended Audience :: Developers",
          "License :: Freely Distributable",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP :: Site Management",
          "Topic :: Software Development :: Libraries :: "
          "Application Frameworks"
      ],
      author='D.A.Dokter',
      author_email='dokter@w20e.com',
      license='beer-ware',
      url='https://github.com/wyldebeast-wunderliebe/mrwolfe/',
      keywords='django issue tracker support',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=REQUIRES,
      tests_require=REQUIRES,
      test_suite="mrwolfe",
      entry_points=""
      )
