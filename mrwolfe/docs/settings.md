Mr.Wolfe somes with a number of settings that you should override for
the application to do somethng useful. This of course includes
defining your own database settings. Other stuff you may want to change:


 * ISSUE_STATUS_CHOICES Defaults to open, closed, in progress
 * ISSUE_STATUS_DEFAULT Defaults to open
 * ALLOW_NON_CONTACTS If you wish to allow for non contacts of an SLA to post issues, set this to True.
 * NOTIFICATION_MAP You can override the email templates used with this setting
 * DEFAULT_FROM_ADDR Default from address for outgoing emails

Also, set these for outgoing emails:

 * EMAIL_HOST
 * EMAIL_PORT
 * EMAIL_HOST_USER
 * EMAIL_HOST_PASSWORD
 * EMAIL_USE_TLS
