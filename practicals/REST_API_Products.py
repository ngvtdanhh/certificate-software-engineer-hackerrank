import requests


def count_products_in_price_range(category, min_price, max_price):
    count = 0
    page = 1

    while True:
        api_url = f"https://jsonmock.hackerrank.com/api/inventory?category={category}&page={page}"
        response = requests.get(api_url)
        result = response.json()

        total_pages = result.get('total_pages', 0)
        items = result.get('data', [])

        for product in items:
            price = product.get('price', 0)
            if min_price <= price <= max_price:
                count += 1

        if page >= total_pages:
            break

        page += 1

    return count

if __name__ == "__main__":
    category_name = "Accessories"
    min_price = 800.0
    max_price = 900.0

    matching_products = count_products_in_price_range(category_name, min_price, max_price)
    print(matching_products)
