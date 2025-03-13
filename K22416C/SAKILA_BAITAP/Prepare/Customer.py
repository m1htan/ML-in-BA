class Customer:
    def __init__(self, customer_id, store_id, first_name, last_name, email, address_id, active, create_date, last_update):
        self.customer_id=customer_id
        self.store_id=store_id
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.address_id=address_id
        self.activate=active
        self.create_date=create_date
        self.last_update=last_update

    def __str__(self):
        ctm= f"{self.customer_id}\t{self.store_id}\t{self.first_name}\t{self.last_name}\t{self.email}\t{self.address_id}\t{self.activate}\t{self.create_date}\t{self.last_update}"
        return ctm