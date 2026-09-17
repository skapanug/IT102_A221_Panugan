class FileManager:

    def loadRecords(self, productName):
        salesRecords = {}
        try:
            with open("sales_records.txt", "r") as file:
                for line in file:
                    product, date, amount = line.strip().split(",")
                    if product == productName:
                        salesRecords[date] = int(amount)

        except FileNotFoundError:
            pass
        return salesRecords

    def saveSale(self, productName, date, amount):
        with open("sales_records.txt", "a") as file:
            file.write(f"{productName},{date},{amount}\n")