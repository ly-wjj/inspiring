import conf

class Contacts():
    def __init__(self):
        self.__name = conf.getConfig("contacts","name")
        self.__group = conf.getConfig("contacts","group")
        self.__email = conf.getConfig("contacts","email")
        self.mobile = conf.getConfig("contacts","mobile")

    def get_mobile(self):
        return self.mobile


#receiver = receivers()
#print receiver.get_mobile()