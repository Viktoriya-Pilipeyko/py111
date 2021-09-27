from abc import *



class syusers(ABC):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        print(f"Имя: {self.name}, {self.surname}")
    @abstractmethod
    def printt(self):
        pass

class sysadmins(syusers, ABC):
    def __init__(self, name, surname, sysadm):
        super().__init__(name, surname)
        self.sysadm = sysadm
    def printt(self):
        return print(f"Сисадмин: {self.sysadm}")
    @abstractmethod
    def wall(self):
        pass

class ewall(sysadmins):
    def __init__(self, name, surname, sysadm, ewallet):
        super().__init__(name, surname, sysadm)
        self.ewallet = ewallet
    def wall(self):
        print(f"ЭКошелек: {self.ewallet}")

a = ewall('name', 'surname','sysadm','ewallet')

a.printt()
a.wall()


