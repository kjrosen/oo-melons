"""Classes for melon orders."""

class AbstractMelonOrder:

    def __init__(self, species, qty, country_code = "USA", flat_fee=0):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code
        self.flat_fee = flat_fee

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        
        if self.species == "Christmas melon":
            base_price *= 1.5
        
        if self.country_code != "USA" and self.qty < 10:
            self.flat_fee = 3

        total = (1 + self.tax) * self.qty * base_price + self.flat_fee

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    tax = 0.8
    shipping_type = "domestic"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    tax = 0.17
    shipping_type = "International"
    

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
