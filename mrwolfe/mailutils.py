import poplib
from imapclient import IMAPClient, SEEN
import email


class IMAPService(object):

    def __init__(self, host, port=None):

        self.service = IMAPClient(host, port=port, ssl=True)

    def auth(self, usr, pwd):

        self.service.login(usr, pwd)

    def list(self):

        self.service.select_folder('INBOX')

        messages = self.service.search(['UNSEEN'])

        response = self.service.fetch(messages, ['RFC822'])

        for msg_id, data in response.iteritems():

            yield (msg_id, email.message_from_string(
                data['RFC822'].encode("utf-8", "ignore")))

    def quit(self):

        pass

    def mark_unread(self, msg_ids):

        self.service.remove_flags(msg_ids, [SEEN])


class POPService(object):

    def __init__(self, host, port=995):

        self.service = poplib.POP3_SSL(host, port)

    def auth(self, usr, pwd):

        self.service.user(usr)
        self.service.pass_(pwd)

    def list(self):

        nr_of_messages = len(self.service.list()[1])

        for i in range(nr_of_messages):
            msgstr = "\n".join(self.service.retr(i+1)[1])
            self.service.dele(i+1)  # flag for deletion
            yield (i, email.message_from_string(msgstr))

    def quit(self):

        self.service.quit()

    def mark_unread(self, msg_ids):

        # too bad we can't undelete 1 message. poplib only allows us
        # to reset ALL deletion marks.
        # this might be a bad idea! 1 bad email could lead to a loop??
        self.service.rset()
