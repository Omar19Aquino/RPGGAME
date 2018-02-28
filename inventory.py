class Inventory():
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def drop(self, item):
        self.items.remove(item)

    def list(self):
        print "you are carrying:"
        for item in self.items:
            print item.get_name()


class Item():
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name



class Literature(Item):
    def __init__(self, name, contents="This item is blank."):
        Item.__init__(self, name)
        self.contents = contents

    def read(self):
        print self.contents

    def set_content(self, contents):
        self.contents = contents


class Flaslight(Item):
    def __init__(self, name, battery_level=100, state="off"):
        Item.__init__(self, name)
        self.battery_level = battery_level
        self.state = state

    def turn_on(self):
        self.state = "on"

    def turn_off(self):
        self.state = "off"

    def change_batteries(self):
        self.battery_level=100
        
    def compute_usage(self):
        pass