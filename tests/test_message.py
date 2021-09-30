import gmail3
from gmail3.message import Message

g = gmail3.login("xingjian.zhang228@gmail.com", "123098Zxc")


def test_unread():
    inbox = g.inbox().mail()
    message: Message = inbox[-1]
    message.fetch()
    message.unread()
    assert not message.is_read()


def test_read():
    inbox = g.inbox().mail()
    message: Message = inbox[-1]
    message.fetch()
    message.read()
    assert message.is_read()


def test_starred():
    inbox = g.inbox().mail()
    message: Message = inbox[-1]
    message.fetch()
    message.star()
    assert message.is_starred()


def test_unstarred():
    inbox = g.inbox().mail()
    message: Message = inbox[-1]
    message.fetch()
    message.unstar()
    assert not message.is_starred()


def test_add_label():
    inbox = g.inbox().mail()
    message: Message = inbox[-1]
    message.fetch()
    message.add_label("test_label")
    assert message.has_label("test_label")


def test_remove_label():
    inbox = g.inbox().mail()
    message: Message = inbox[-1]
    message.fetch()
    if not message.has_label("test_label"):
        message.add_label("test_label")
    message.remove_label("test_label")
    assert not message.has_label("test_label")
