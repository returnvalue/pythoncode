from abc import ABC, abstractmethod


class Networkdevice(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def poweron(self):
        pass


class Routify(ABC):
    @abstractmethod
    def route(self):
        pass


class Router(Networkdevice, Routify):
    def __init__(self):
        super().__init__()

    def poweron(self):
        print('Ready to process traffic')

    def route(self):
        print('Routify success')


r = Router()
r.poweron()
r.route()
