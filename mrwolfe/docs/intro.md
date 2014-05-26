Mr.Wolfe support system
=======================

Contents
--------
- Introduction (this document)
- [Installation](/install.md)
- [Configuration](/settings.md)
- [Look & Feel](/skin.md)
- [Wiki](/wiki.md)

Introduction
------------

Mr.Wolfe is an issue tracker for support issues. This is not the same
as a system for software issues, like Bugzilla, Ira, etc. In the
latter issues are related to software, and are tracked in terms of a
life cycle from incoming to resolving in a specific release (or closing
without a release). Mr.Wolfe tracks support issues, that may be
questions, performance problems, software failures, etc.
An issue in Mr.Wolfe may or may not result in a software issue.

Handling support issues is an art! Ehh, well, it's actually pretty
simple. Mr. Wolfe is based on the assumption that you always have a
Service Level Agreement with for a given application that you expect
issues for, and a fixed number of people that can send issues for this
SLA.  Issues are sent over email by valid contacts, or added ttw by
authenticated users that are valid contacts. No SLA, no issue. Simple
as that. If that is not the way your support organization works, don't
use this system.


Issues
------

An issue is a very generic concept. An issue is simply some perceived
problem with the application that is supported. This implies that an
issue is not necessarily a software issue. Mr. Wolfe therefore is not
a 'bug tracker', nor involves concepts about releases, software
versions, etc. An issue in terms of Mr.Wolfe _may_ result in a bug,
story or improvement in a tracking system that relates issues to
releases, like Jira or Bugzilla.

An issue can be mailed to one of the configured mail queues of
Mr.Wolfe.  The system will poll on the queue, fetch emails and
dispatch to the proper SLA, determined by the dispatch rules for a
SLA. When the issue has been accepted by the system, a notification is
sent back to the sender, with the acknowledgement and the issue
id. Any further response on the issue (as determined by the use of the
issue ID in the subject, will be added as comments on the same issue.


Resolving issues to an SLA
--------------------------

Issues are reported by email in general, so it is the system's
responsibility to attach incoming issues to the proper SLA. Resolving
this is done as per the rules that have been configured for a
SLA. These rules simply do regular expression matching on the email
message fields, like 'from', 'to', 'subject' or 'text'.

If no SLA can be found, the issue is 'orphaned' and needs to be
assigned to an SLA by the operator.


SLA
---

A Service Level Agreement consists of a number of services that have
been agreed upon. A service as basically a tuple of 'priority,
reaction time, solution time'.
