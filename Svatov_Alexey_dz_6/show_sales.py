from sys import argv


def show_sales(_, start=0, finish=0):
    with open('bakery_sales.csv', 'r', encoding='utf-8') as b_sales:
        if not int(start):
            print(b_sales.read())
        else:
            if not int(finish):
                print(*b_sales.read().split('\n')[int(start) - 1:], sep='\n')
            else:
                print(*b_sales.read().split('\n')[int(start) - 1:int(finish)], sep='\n')


show_sales(*argv)
if '__name__' == '__main__':
    print("i'm batman")
