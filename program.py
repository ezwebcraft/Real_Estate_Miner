import os


def main():
    print_header()
    filename = get_data_file()
    # print(filename)
    data = load_file(filename)
    print(data)


def print_header():
    print('----------------------------------')
    print('      Real Estate Miner           ')
    print('----------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    return []


if __name__ == '__main__':
    main()
