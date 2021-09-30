import gmail3

g = gmail3.login("xingjian.zhang228@gmail.com", "123098Zxc")

def test_login():
    assert g.logged_in


def test_inbox_message():
    inbox = g.inbox().mail()
    assert len(inbox) > 0

def test_logout():
    g.logout()
    assert not g.logged_in