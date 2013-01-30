mrwolfe - "I'm Mr. Wolfe. I solve problems"
===========================================

This system works with the assumption that issues may be posted only,
if there is an Service Level Agreement for the sender. Issues are sent
over email (this is what customers do anyway, regardless of other
procedures), or added ttw by authenticated users that are valid
contacts for a given SLA. No SLA, no issue. Simple as that.  If that
is not the way your support organisation works, don't use this system.

Issues
------

An issue is a very generic concept. An issue is simply some percieved
problem with the application that is supported. This implies that an
issue is not necessarily a software issue. Mr. Wolfe therefore is not
a 'bug tracker', nor involves concepts about releases, software
versions, etc. An issue in terms of Mr.Wolfe _may_ result in a bug,
story or improvement in a tracking system that relates issues to
releases, like Jira or Bugzilla.

An issue can be mailed to one of the configured mailqueues of
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
