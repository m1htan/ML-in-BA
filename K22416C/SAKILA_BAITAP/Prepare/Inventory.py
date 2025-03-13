class Inventory:
    def __init__(self, inventory_id, film_id, store_id, last_update):
        self.inventory_id=inventory_id
        self.film_id=film_id
        self.store_id=store_id
        self.last_update=last_update

    def __str__(self):
        ivt= f"{self.inventory_id}\t{self.film_id}\t{self.store_id}\t{self.last_update}"
        return ivt