# Message class Implementation
# @author: Gaurav Yeole <gauravyeole@gmail.com>

class Message:
    class Request:
        def __init__(self, action="", data=None):
            self.action = action
            self.data = data

    class Rsponse:
        def __init__(self):
            self.status = False
            self.data = None

    def __init__(self):
        pass

    def set_request(self):
        pass

    def response(self):
        pass