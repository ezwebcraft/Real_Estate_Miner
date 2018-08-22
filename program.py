import os


def main():
    pass


def print_header():
    print('----------------------------------')
    print('      Real Estate Miner           ')
    print('----------------------------------')
    print()

def get_data_file():
    base_folder = os.path.dirname(__file__)
    os.path.join(base_folder,'data','SacramentoRealEstateTransactions2008.csv')

if __name__ == '__main__':
    main()