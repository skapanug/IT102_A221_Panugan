class Product:

    def __init__(self, productName):
        self.__productName = productName
        self.__salesRecords = {}

    def addSale(self, date, amount):
        self.__salesRecords[date] = amount
        with open("sales_records.txt", "a") as file:
            file.write(f"{self.__productName},{date},{amount}\n")

    def getSalesRecords(self):
        return self.__salesRecords

    def getProductName(self):
        return self.__productName

    def loadSalesRecords(self):
        try:
            with open("sales_records.txt", "r") as file:
                for line in file:
                    product, date, amount = line.strip().split(",")

                    if product == self.__productName:
                        self.__salesRecords[date] = int(amount)

        except FileNotFoundError:
            pass
