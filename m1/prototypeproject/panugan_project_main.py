from panugan_project_product import Product

wrench = Product("Wrench")

# Load records from file
wrench.loadSalesRecords()

print("Features:")
print("1 - Sales Records")
print("2 - Sales Performance")

button = int(input())

if button == 1:

    print("Product:", wrench.getProductName())
    print("Sales Records:", wrench.getSalesRecords())

    print("Add Sale - 1")
    add = int(input())

    if add == 1:
        date = input("Date: ")
        sold = int(input("Amount Sold: "))

        wrench.addSale(date, sold)

        print("New Sales Records:")
        print(wrench.getSalesRecords())
