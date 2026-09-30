class Product:

    def __init__(self, productName, fileManager):
        self.__productName = productName
        self.__fileManager = fileManager

    def loadSalesRecords(self):
        return self.__fileManager.loadRecords(
            self.__productName
        )

    def addSale(self, date, amount):
        self.__fileManager.addRecord(
            self.__productName,
            date,
            amount
        )

    def updateSale(self, date, amount):
        self.__fileManager.updateRecord(
            self.__productName,
            date,
            amount
        )

    def deleteSale(self, date):
        self.__fileManager.deleteRecord(
            self.__productName,
            date
        )

    def getProductName(self):
        return self.__productName


class Tool(Product):

    def getCategory(self):
        return "Tool"