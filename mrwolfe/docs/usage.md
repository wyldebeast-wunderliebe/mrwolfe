Usage
=====

To be able to use Mr.Wolfe at all, you'll need some Service Level
Agreements, add contacts and rules to those, and configure a mailqueue
to read mail from. To actually read that mail, you can run the
./bin/django (or manage.py) 'readmail' command.  Best put it in a cron
job, since you'll want to be notified of issues the soonest possible.