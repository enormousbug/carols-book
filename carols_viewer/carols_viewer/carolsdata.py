import json

class CarolsData():
    def __init__(self, name2text):
        self.__data = {}
        with open(name2text, 'r') as file:
            for item in json.load(file):
                self.__data[item['name'].lower()] = item['text']
        
    def get(self, name):
        return self.__data.get(name)

    def getText(self, name):
        return self.get(name)

    def getNames(self):
        return sorted([k for k, v in self.__data.items()])

    def add(self, name, text):
        self.__data[name] = text

    def remove(self, name):
        #self.__data.erase(name)
        pass