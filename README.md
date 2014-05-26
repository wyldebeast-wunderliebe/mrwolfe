mrwolfe - "I'm Mr. Wolfe. I solve problems"
===========================================

Summary
-------
Mr.Wolfe is a tracker for support issues written on the Django
framework. It is not a tracker for software issues specifically, like
Bugzilla, Jira, etc. In the latter type of tracker, issues are related
to software, and are tracked in terms of a life cycle from incoming to
resolving in a specific software release (or closing without a
release). Mr.Wolfe on the other hand tracks support issues, that may
be questions, performance problems, software failures, etc. in terms
of a life cycle from perceived problem to solved problem. An issue in
Mr.Wolfe may or may not result in a software issue.

If this summary is gibberish to you, you don't need Mr. Wolfe...

Principles
----------
Issues in Mr.Wolfe are related to a Service Level Agreement, and are
handled according to the services agreed in the SLA. Several services
may be added to a SLA, like 'high priority, solve within 8 hours' or
'low priority, solve at your leisure'. The operator dashboard will use
these services to determine the status of the issue, like 'critical'
(deadline is soon) or 'normal' (sit back and relax).

Issues are read from one or more mail queues (let's face it, customers
will just keep sending those issues per mail anyway; POP and IMAP are
supported) and dispatched to the proper SLA if one can be
found. Otherwise, it is orphaned and shown on the operator dashboard.
The tracker is not intended for web access by customers; their only
interface to issues is email. Best to keep it that way, lest your
customers see the 'notification off' button...

The intended target audience of Mr.Wolfe is support teams and help
desks; it is an alternative to the well known OTRS, although it is
much simpler, offers less features and therefore also lacks the
incomprehensible admin interface.

See the docs directory in the package for further reading.

If you like this application, you may donate us a beer as per the
beer-ware licence. If you don't like it that much or find things that
don't work, let us know and we may fix it. Otherwise, fork us on
GitHub. If you think it totally and utterly sucks, tough luck! We
don't care! Hah, we're grown up developers! We don't need that. Well,
just a bit maybe.
