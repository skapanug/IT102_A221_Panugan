class Product:


    def __init__(self, productName):

        self.__productName = productName

        self.__salesRecords = {}


    def addSale(self, date, amount):

        self.__salesRecords[date] = amount


    def getSalesRecords(self):

        return self.__salesRecords


    def getProductName(self):

        return self.__productName
