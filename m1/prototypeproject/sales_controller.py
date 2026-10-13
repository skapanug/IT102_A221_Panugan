class SalesController:

    def __init__(self, product):

        self.product = product

    def addSale(
        self,
        date,
        amount
    ):

        self.product.addSale(
            date,
            amount
        )

    def updateSale(
        self,
        date,
        amount
    ):

        self.product.updateSale(
            date,
            amount
        )

    def deleteSale(
        self,
        date
    ):

        self.product.deleteSale(
            date
        )