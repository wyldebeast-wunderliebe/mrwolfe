Your own skin
=============

Do you prefer Mr.Wolfe in a different skin (say: a sheep skin)? Well,
you can do so without touching the original code by writing a skin
plugin.

The plugin needs to be an egg, with a setup section for 'entry_points', like so:


    entry_points = """\
    [mrwolfe.skin]
    css=<your egg name>:css
    """

and your egg root dir should contain an __init__.py file with at least
the following contents:

    def css():
        return ["mysheepskin.css"]

The actual css file (mysheepskin.css) should be in the usual place
(i.e. ./static/css).

Now add your skin egg to the buildout dependencies, and INSTALLED_APPS
setting, and all should be well. If your not using buildout to run the
project, things will be slightly more complicated. You're on your own!
