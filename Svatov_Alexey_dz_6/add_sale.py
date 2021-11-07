from sys import argv


def add_sale(argv):
    with open('bakery_sales.csv', 'a', encoding='utf-8') as b_sales:
        b_sales.write(f'{argv[1][:7]}\n')


add_sale(argv)
if '__name__' == '__main__':
    print("i'm batman")
