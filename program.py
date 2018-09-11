import os
import csv
from data_types import Purchase

try:
    import statistics

except:

    import statistics_py2 as statistics


def main():
    print_header()
    filename = get_data_file()
    # print(filename)
    data = load_file(filename)
    query_data(data)


def print_header():
    print('----------------------------------')
    print('      Real Estate Miner           ')
    print('----------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    # return []
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            # print(type(row),row)
            # print("Bed count: {}, type: {}".format(row['beds'], type(row['beds'])))
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        # header = fin.readline().strip()
        # reader = csv.reader(fin, delimiter=',')
        # for row in reader:
        # print(type(row),row)
        return purchases
        # print(purchases[0].__dict__)
        # header = fin.readline().strip()
        # print('found header: ' + header)
        # lines = []
        # for line in fin:
        # line_data = line.strip().split(',')
        # bed_count = line_data[4]
        # lines.append(line_data)
        # print(lines[:5])


def get_price(p):
    return p.price


def query_data(data):  #: list[Purchase]):
    # if data was sorted by price
    data.sort(key=lambda p: p.price)

    # Most expensive house?
    high_purchase = data[-1]
    print("Most expensive house is ${:,} with {} beds and {} bath room".format(high_purchase.price, high_purchase.beds,
                                                                               high_purchase.baths))

    # least expensive house?
    low_purchase = data[0]
    print("Least expensive house is ${:,} with {} beds and {} bath room".format(low_purchase.price, low_purchase.beds,
                                                                                low_purchase.baths))

    # average price house?
    prices = []

    # for pur in data:
    #     prices.append(pur.price)
    #
    # avg_price = statistics.mean(prices)

    prices = [
        p.price
        for p in data
    ]

    avg_price = statistics.mean(prices)

    print("The average home prices is {:,}".format(int(avg_price)))

    # average price of 2 bedroom houses
    # prices = []
    #
    # for pur in data:
    #     if pur.beds == 2:
    #         prices.append(pur.price)

    two_bed_homes = [
        p
        for p in data
        if p.beds == 2
    ]
    avg_price = statistics.mean([p.prices for p in two_bed_homes])
    avg_baths = statistics.mean([p.baths for p in two_bed_homes])
    avg_sqft = statistics.mean([p.sq__ft for p in two_bed_homes])

    print("The average home prices for 2-bedrooms is {:,}, baths={}, sq ft={:,}".format(int(avg_price),avg_baths,avg_sqft))


if __name__ == '__main__':
    main()
