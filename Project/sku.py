# PyScript
from pyscript import display, document 
import random

def generate_sku(e):
    category = document.getElementById("category").value
    product = document.getElementById("product").value

#If the user does not input a product, it displays this error message
    if product == "":
        display("Please enter a product.", target="result")
        return

# The [:3] on category and product takes the first 3 characters of each and displays them on the generated SKU 
# The random.randint generates a number betweek 10 - 99, to meet the required random two digit number for the SKU
    sku = category[:3] + product[:3] + str(random.randint(10, 99))

#.upper converts all to uppercase
    display("Your SKU is: " + sku.upper(), target="result")

    # Sources 
    # Slicing of Strings :  https://www.w3schools.com/python/python_strings_slicing.asp
    # Used for the SKU generator to take the first 3 letters/characters of the Product and Category 

    # Use of Randit https://www.w3schools.com/python/ref_random_randint.asp
    # Used for the SKU generator to generate a number from 10 to 99 for the random two-digit number 