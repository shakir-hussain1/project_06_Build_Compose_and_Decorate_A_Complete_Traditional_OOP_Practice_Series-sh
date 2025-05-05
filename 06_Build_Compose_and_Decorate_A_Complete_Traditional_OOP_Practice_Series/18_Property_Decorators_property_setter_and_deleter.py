class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    @property
    def price(self):
        """Getter for the price."""
        return self._price

    @price.setter
    def price(self, value):
        """Setter for the price."""
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @price.deleter
    def price(self):
        """Deleter for the price."""
        print("Deleting price...")
        del self._price


# Example usage
if __name__ == "__main__":
    product = Product(100)
    print("Initial price:", product.price)

    product.price = 150
    print("Updated price:", product.price)

    del product.price
    # Accessing product.price now will raise AttributeError unless redefined
