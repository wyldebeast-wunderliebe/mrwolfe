Installation
============

[index](/intro.md)

We assume that you'll install Mr.Wolfe on a Linux (or Unix) based
system. We strongly advise against using Windows systems for anything
other than playing games or throwing off high buildings.

The easiest way to start using Mr.Wolfe (provided you know how to use
buildout) is to checkout the mrwolfe_buildout project from GitHub
(https://github.com/wyldebeast-wunderliebe/mrwolfe_buildout) and read
the instructions in that project.

Otherwise, install this app like you install other Django apps. If you
don't know how to do that, ask your smart cousin, or check out
http://www.djangoproject.com/. Make sure you install the dependencies
as well. These you can find in the setup.py file.

There is some settings you may wish to override. The mrwolfe_buildout
project provides an easy way of doing so. Otherwise, read the
settings.py file within the mrwolfe sources and adapt to your needs.

Check the CHANGES.txt when upgrading for database changes. We're too
lazy to provide migrations.
