from panugan_project_product import Product

wrench = Product("Wrench")
wrench.loadSalesRecords()

print("Features:")
print("1 - Sales Records")
print("2 - Sales Performance")

button = int(input())

if button == 1:

    print("Product:", wrench.getProductName())
    print("Sales Records:", wrench.getSalesRecords())

    print("1 - Add Sale")
    print("2 - Sales Logs")
    add = int(input())

    if add == 1:
        date = input("Date: ")
        sold = int(input("Amount Spold: "))

        wrench.addSale(date, sold)

        print("New Sales Records:")
        print(wrench.getSalesRecords())

elif button == 2:
    startDate = input("Start Date: ")
    endDate = input("End Date: ")
    print("Performance")


elif button == 3:
    print("Exiting Application")