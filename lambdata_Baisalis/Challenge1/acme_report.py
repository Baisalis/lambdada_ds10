from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['AWESOME', 'SHINY', 'IMPRESSIVE', 'PORTABLE', 'IMPROVED']
NOUNS = ['Anil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for i in range(num_products):
        name = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]
        price = randint(5, 100)
        weight = randint(5,100)
        flammability = uniform (0, 2.5)
        products.append(Product(name, price, weight, flammability))
    return products 



def average(number_list):
    return sum(number_list)/ len(number_list)



def inventory_report(products):
    name_list = [prod.name for prod in products]
    price_list = [prod.price for prod in products]
    weight_list = [prod.weight for prod in products]
    flammability_list = [prod.flammability for prod in products]
    unique_list = set(name_list)
    print("Acme corporation official inventory report")
    print("Unique products names:", len(unique_list))
    print("Average price:", average(price_list))
    print("Average weight:", average(weight_list))
    print("Average flammability:" , average(flammability_list))



if __name__ == '__main__':
    inventory_report(generate_products())


