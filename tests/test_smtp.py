import gmail3
import time
from gmail3.message import Message

g = gmail3.login("xingjian.zhang228@gmail.com", "123098Zxc")


def test_send_to_self():
    test_subject = "TEST_SUBJ"
    test_body = "TEST_BODY"
    g.send_mail(g.username, test_subject, test_body)
    time.sleep(1.)
    latest: Message = g.inbox().mail()[-1]
    latest.fetch()
    assert latest.subject == test_subject
