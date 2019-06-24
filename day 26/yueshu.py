# -*- coding: utf-8 -*-
class BaseMessage(object):
    def send(self):
        raise NotImplementedError("error")
class Email(BaseMessage):
    def send(self):
        pass
obj = Email()
obj.send()