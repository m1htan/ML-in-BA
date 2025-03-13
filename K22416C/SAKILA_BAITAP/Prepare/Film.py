class Film:
    def __init__(self, film_id, title, description, release_year, language_id, original_language_id,
                 rental_duration, rental_rate, length, replacement_cost, rating, special_features,
                 last_update):

        self.film_id=film_id
        self.title=title
        self.description=description
        self.release_year=release_year
        self.language_id=language_id
        self.original_language_id=original_language_id
        self.rental_duration=rental_duration
        self.rental_rate=rental_rate
        self.length=length
        self.replacement_cost=replacement_cost
        self.rating=rating
        self.special_features=special_features
        self.last_update=last_update

    def __str__(self):
        film= f"{self.film_id}\t{self.title}\t{self.description}\t{self.release_year}\t{self.language_id}\t{self.original_language_id}\t{self.rental_duration}\t{self.rental_rate}\t{self.length}\t{self.replacement_cost}\t{self.rating}\t{self.special_features}\t{self.last_update}"
        return film