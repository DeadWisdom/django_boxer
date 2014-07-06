from models import Email


class EmailBackend(object):
    """
    Redirects messages to the database.
    """
    def __init__(self, fail_silently=False, **kwargs):
        self.fail_silently = fail_silently

    def open(self):
        pass

    def close(self):
        pass

    def send_messages(self, email_messages):
        """
        Sends one or more EmailMessage objects and returns the number of email
        messages sent.
        """
        created = []
        for m in email_messages:
            html = ''
            for alt, mime in m.alternatives:
                if mime == 'text/html':
                    html = alt
            email = Email.objects.create(
                text = m.body,
                html = html,
                fro = m.from_email,
                to = ", ".join(m.to),
                cc = ", ".join(m.cc),
                bcc = ", ".join(m.bcc),
                subject = m.subject
            )
            created.append( email )
        return len(created)
