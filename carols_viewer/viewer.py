import sys
from carolsdata import CarolsData

def main(path):
    data = CarolsData(path)
    print(data.getNames())
    print(data.getText('bracia patrzcie jeno'))

if __name__ == "__main__":
        main(sys.argv[1])