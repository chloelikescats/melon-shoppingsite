"""Customers at Ubermelon."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self,
                 first_name,
                 last_name,
                 email,
                 password,
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about melon in console."""

        return "<Customer: {id}, {name}>".format(
            id=self.email, name=self.first_name + " " + self.last_name)


def read_customers_from_file(filepath):
    """Read melon type data and populate dictionary of melon types.

    Dictionary will be {id: email}
    """

    customers = {}

    for line in open(filepath):
        (first_name,
         last_name,
         email,
         password) = line.strip().split("|")

        customers[email] = Customer(first_name,
                                    last_name,
                                    email,
                                    password)

    return customers


def get_all():
    """Return list of customers.
    """

    # This relies on access to the global dictionary `customers`

    return customers.values()


def get_by_email(email):
    """Return a customer info, given their email."""

    # This relies on access to the global dictionary `melon_types`

    return customers[email]


# Dictionary to hold types of melons.
#
# Format is {id: Melon object, ... }

customers = read_customers_from_file("customers.txt")
