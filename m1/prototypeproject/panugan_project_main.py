from panugan_project_product import Tool
from panugan_project_data import FileManager

fileManager = FileManager()
wrench = Tool("Wrench", fileManager)
wrench.loadSalesRecords()


print("Menu:")
print("1 - Sales Records")
print("2 - Sales Performance")
print("3 - Exit")

button = int(input())

if button == 1:
    if button == 1:
        print("Product:", wrench.getProductName())
        print("Sales Records:", wrench.getSalesRecords())
        print("\nOptions:")
        print("1 - Add Sale")
        print("2 - Update Sale")
        print("3 - Delete Sale")

        option = int(input())

    if option == 1:

        date = input("Date: ")
        sold = int(input("Amount Sold: "))

        wrench.addSale(date, sold)

        print("Updated Records:")
        print(wrench.getSalesRecords())

    elif option == 2:

        date = input("Enter date to update: ")

        if date in wrench.getSalesRecords():

            sold = int(input("New Amount Sold: "))

            wrench.getSalesRecords()[date] = sold

            print("Record Updated")
            print(wrench.getSalesRecords())

        else:
            print("Date not found")

    elif option == 3:

        date = input("Enter date to delete: ")

        if date in wrench.getSalesRecords():

            del wrench.getSalesRecords()[date]

            print("Record Deleted")
            print(wrench.getSalesRecords())

        else:
            print("Date not found")

elif button == 2:

    startDate = input("Start Date: ")
    endDate = input("End Date: ")
    print("STATS")
    print("Showing sales performance from", startDate, "to", endDate)

elif button == 3:

    print("Exiting")
