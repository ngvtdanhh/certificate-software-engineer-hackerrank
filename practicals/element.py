#!/bin/python3

import requests
import os

# Function to get the number of products in a given price range and category
def get_products_in_range(category, min_price, max_price):
    count = 0
    page_number = 1

    while True:
        endpoint = f"https://jsonmock.hackerrank.com/api/inventory?category={category}&page={page_number}"
        response = requests.get(endpoint)
        payload = response.json()

        for product in payload.get("data", []):
            price = product.get("price", 0)
            if min_price <= price <= max_price:
                count += 1

        if page_number >= payload.get("total_pages", 0):
            break

        page_number += 1

    return count


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        cat_input = input().strip()
        min_input = int(input().strip())
        max_input = int(input().strip())

        matched_count = get_products_in_range(cat_input, min_input, max_input)
        fptr.write(f"{matched_count}\n")
