def read_only():
    try:
        file1 = open('new_data.txt', 'r') # r = read only which is also the default
        text = file1.read()
        print(text)
        file1.close()
    except FileNotFoundError:
        text = None
        print(text)

def write_only():
    file2 = open('more_data.txt', 'w')
    file2.write('tomato town')

# with open('data.txt') as f:
#     txt = f.read()
#     print(txt)
def read_food_sales():
    all_dates = []
    with open('sampledatafoodsales.csv') as f:
        data = f.readlines()
        
        for food_sale in data:
            split_food_sale = food_sale.split(',')

            order_date = split_food_sale[0]
            print(order_date)

            all_dates.append(order_date)

    print(all_dates)

    with open('dates.txt', 'w') as f:
        for date in all_dates:
            f.write(date)
            f.write('\n')

def write_regions():
    all_regions = []
    with open('sampledatafoodsales.csv') as f:
        data = f.readlines()

        for food_sale in data:
            split_food_sale = food_sale.split(',')

            order_region = split_food_sale[1]

            all_regions.append(order_region)

    with open('regions.txt', 'w') as f:
        for region in all_regions:
            f.write(region)
            f.write('\n')

def write_input_to_file():
    user_input = input('Hello, enter your name:\n')
    with open('names.txt', 'w') as f:
        f.write(user_input)

if __name__ == '__main__':
    # read_only()
    # write_only()
    # read_food_sales()
    # write_regions()
    write_input_to_file()