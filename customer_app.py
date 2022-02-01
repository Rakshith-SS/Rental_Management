class Customer:

    """
    Add customer manage rentals
    and get details of a customer as well
    """
    def __init__(self, name):
        """TODO: to be defined. """
        self.name = name

    def __str__(self):
        return f'Customer Name - {self.name}'


obj = Customer("Rakshith")
print(obj)
print(obj.name)
