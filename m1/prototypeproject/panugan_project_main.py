from panugan_project_product import Product

wrench = Product("Wrench")


wrench.addSale("2026-09-01", 1000)

wrench.addSale("2026-09-02", 1500)

wrench.addSale("2026-09-03", 1200)


print("Product:", wrench.getProductName())

print("Sales Records:", wrench.getSalesRecords())
 
