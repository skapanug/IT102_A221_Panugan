class Product:

    def __init__(self, productName, fileManager):
        self.__productName = productName
        self.__fileManager = fileManager

    def loadSalesRecords(self):
        print("[Loading Sales Records]")

    def addSale(self):
        print("Sale Added")

    def updateSale(self):
        print("Updated Sale")

    def deleteSale(self):
        print("Deleted Sale")

    def getProductName(self):
        return self.__productName


class Tool(Product):
    def getCategory(self):
        return "Tool"