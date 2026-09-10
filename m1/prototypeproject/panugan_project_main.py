from panugan_project_product import Product

wrench = Product("Wrench")


wrench.addSale("2026-09-01", 1000)

wrench.addSale("2026-09-02", 1500)

wrench.addSale("2026-09-03", 1200)

print("Features: Product(Wrench Example) Sales Records - 1, Sales Performance - 2")
button = int(input())

if button == 1:
        print("Product:", wrench.getProductName())

        print("Sales Records:", wrench.getSalesRecords())

        print("Add Sales - 1")

        add = int(input())
        if add == 1:
                date = input()
                sold = int(input())
                wrench.addSale(date+", ", sold)
                print("New Sales Records:", wrench.getSalesRecords())
        else:
            print()
else: 
        print()