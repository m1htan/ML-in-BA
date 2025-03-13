class Rental:
    def __init__(self, rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, last_update):
        self.rental_id=rental_id
        self.rental_date=rental_date
        self.inventory_id=inventory_id
        self.customer_id=customer_id
        self.return_date=return_date
        self.staff_id=staff_id
        self.last_update=last_update

    def __str__(self):
        rt= f"{self.rental_id}\t{self.rental_date}\t{self.inventory_id}\t{self.customer_id}\t{self.return_date}\t{self.staff_id}\t{self.last_update}"
        return rt