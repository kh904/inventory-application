import getpass
import csv
user_name = getpass.getuser()

print("----------------------")
print("PRODUCTS APPLICATION")
print("----------------------")
print("Welcome to the products app, " + (user_name) + "!")
print("")

#
# Read csv
#

products = []

#TODO: open the file and populate the products list with product dictionaries

csv_file_path = r"C:\Users\huynhk5\Desktop\Python Files\Inventory\db\products.csv"

with open(csv_file_path, "r") as csv_file:
    reader = list(csv.DictReader(csv_file, delimiter=','))
    for row in reader:
        products.append(row)

headers = ["id", "name", "aisle", "department", "price"]

new_header_info = [header for header in headers if header != "id"]

def load_id(product):
    return int(product["id"])

def new_auto_id():
    product_ids = map(load_id, products)
    return max(product_ids) + 1

print("There are {0} products in the database.".format(len(products))) # .format(len(products)) " + str(len(products)) + " this should return a dynamic count of the products in the database

#
# menu
#

menu = """
    command | operation | description
    ------- | --------- | -----------------
       1    | 'List'    | Display a list of product identifiers and names
       2    | 'Show'    | Show information about a product
       3    | 'Create'  | Add a new product
       4    | 'Update'  | Edit an existing product
       5    | 'Destroy' | Delete an existing product
Please select a command: """

new_operation = input(menu)
new_operation = new_operation.title()

d = {}
d["List"] = 1
d["Show"] = 2
d["Create"] = 3
d["Update"] = 4
d["Destroy"] = 5

#
# Define command operations
#

def list_products():
    print("")
    print("---- LISTING PRODUCTS:")
    print("")
    for product in products:
        print(" + Product #" + str(product["id"]) + ": " + product["name"])

def show_product():
    print("")
    product_number = input("What is the Product #? ")
    product = [n for n in products if n["id"] == product_number][0]
    print("")
    if product:
        print(" + The product you identified is: ", product)
    else:
        print("+ That Product # was not found", product)

def create_product():
    print("")
    print("---- Creating a Product...")
    print("")
    product = {"id": new_auto_id()}
    for header in new_header_info:
        product[header] = input("Please input the {0}: ".format(header))
    products.append(product)
    print("Product created. Your new product is: ", product)

def update_product():
    print("")
    product_id = input("---- Let's update a product. What product would you like to update? ")
    product = [n for n in products if n["id"] == product_id][0]
    print("")
    if product:
        print("Cool! Let's update the product.")
        for header in new_header_info:
            product[header] = input("Change '{0}' from '{1}' to: ".format(header, product[header]))
        print("Product has been updated to: ", product)
    else:
        print("Product not found ", product_id)

def destroy_product():
    print("")
    product_id = input("---- Which product would you like to destroy? ")
    product = [n for n in products if n["id"] == product_id][0]
    print("")
    if product:
        print("Product being destroyed: ", product)
        del products[products.index(product)]
    else:
        print("Product not found ", product_id)

if new_operation == "1": list_products()
elif new_operation == "2": show_product()
elif new_operation == "3": create_product()
elif new_operation == "4": update_product()
elif new_operation == "5": destroy_product()
else:
    print("")
    print("Something's not right. Please choose one of the available commands.")

#
# Write products to file

#TODO: open the file and write a list of dictionaries. each dict should represent a product.

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()
    for product in products:
        writer.writerow(product)

#Reste products from reset.py
def reset_products_file(filename="products.csv", from_filename="products_default.csv"):
     print("RESETTING DEFAULTS")
