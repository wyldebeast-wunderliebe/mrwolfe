OpenID authentication
=====================

To prevent your stressed out sysadmin from suffering a complete
breakdown, the user admin task can be more or less transferred to some
third party that provides OpenID, like Google or Yahoo.

To achieve this, you'll need to enable two more eggs:
django_openid_auth and python-openid. Best to use the openid.cfg in
the buildout for Mr.Wolfe. Also, some patches are needed for
django_openid_auth to make it compatible with newer versions of
Django, and to enable authentication of a user based on an email
address. The patches file also resides in the buildout package,
directory patches. The openid.cfg runs the patches automatically.

You may want to change some of the settings concerning OpenID. These
are in the OpenID section of the Mr.Wolfe settings.