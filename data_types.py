
class Purchase:
    def __init__(self, city,
                 zipcode, state, beds,
                 baths, sq__ft, home_type,
                 sale_date, price, latitude,
                 longitude):

        self.street = street
        self.city = city
        self.zipcode = zipcode
        self.state = state
        self.beds = beds
        self.baths = baths
        self.sq__ft
        self.home_type = home_type
        self.sale_date = sale_date
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

    def create_from_dict(lookup):
        return Purchase(
            lookup[city],
            lookup[zipcode],
            lookup[state],
            int(lookup[beds]),
            int(lookup[baths]),
            int(lookup[sq__ft]),
            lookup[home_type],
            lookup[sale_date],
            float(lookup[price]),
            float(lookup[latitude]),
            float(lookup[longitude]))