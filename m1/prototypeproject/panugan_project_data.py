class FileManager:

    def loadRecords(self, productName):
        records = []
        try:
            with open("sales_records.txt", "r") as file:
                for line in file:
                    product, date, amount = line.strip().split(",")
                    if product == productName:
                        records.append([product, date, amount])

        except FileNotFoundError:
            pass
        return records


    def addRecord(self, productName, date, amount):
        with open("sales_records.txt", "a") as file:
            file.write(f"{productName},{date},{amount}\n")


    def updateRecord(self, productName, date, amount):
        lines = []
        with open("sales_records.txt", "r") as file:
            for line in file:
                product, oldDate, oldAmount = (line.strip().split(","))

                if (product == productName and oldDate == date):
                    lines.append(f"{productName},{date},{amount}\n")
                else:
                    lines.append(line)
        with open("sales_records.txt", "w") as file:
            file.writelines(lines)


    def deleteRecord(self, productName, date):
        lines = []
        with open("sales_records.txt", "r") as file:
            for line in file:
                product, oldDate, amount = (
                    line.strip().split(",")
                )
                if not (
                    product == productName and
                    oldDate == date
                ):
                    lines.append(line)

        with open("sales_records.txt", "w") as file:
            file.writelines(lines)