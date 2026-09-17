class Product:

    def __init__(self, productName, fileManager):

        self.__productName = productName
        self.__salesRecords = {}
        self.__fileManager = fileManager

    def loadSalesRecords(self):

        self.__salesRecords = self.__fileManager.loadRecords(
            self.__productName
        )

    def addSale(self, date, amount):

        self.__salesRecords[date] = amount

        self.__fileManager.saveSale(
            self.__productName,
            date,
            amount
        )

    def getSalesRecords(self):
        return self.__salesRecords

    def getProductName(self):
        return self.__productName


class Tool(Product):

    def getCategory(self):
        return "Tool"