import os

class FileManager:

    FILE_PATH = os.path.join(
        os.path.dirname(__file__),
        "sales_records.txt"
    )

    def loadRecords(self, productName):

        records = []

        try:

            with open(self.FILE_PATH, "r") as file:

                for line in file:

                    product, date, amount = line.strip().split(",")

                    if product == productName:

                        records.append(
                            [product, date, amount]
                        )

        except FileNotFoundError:

            pass

        return records


    def addRecord(self, productName, date, amount):

        with open(self.FILE_PATH, "a") as file:

            file.write(
                f"{productName},{date},{amount}\n"
            )


    def updateRecord(self, productName, date, amount):

        lines = []

        with open(self.FILE_PATH, "r") as file:

            for line in file:

                product, oldDate, oldAmount = (
                    line.strip().split(",")
                )

                if (
                    product == productName and
                    oldDate == date
                ):

                    lines.append(
                        f"{productName},{date},{amount}\n"
                    )

                else:

                    lines.append(line)

        with open(self.FILE_PATH, "w") as file:

            file.writelines(lines)


    def deleteRecord(self, productName, date):

        lines = []

        with open(self.FILE_PATH, "r") as file:

            for line in file:

                product, oldDate, amount = (
                    line.strip().split(",")
                )

                if not (
                    product == productName and
                    oldDate == date
                ):

                    lines.append(line)

        with open(self.FILE_PATH, "w") as file:

            file.writelines(lines)