shopping_dict = {
  "piekarnia": ["chleb", "bułki", "pączek"],
  "warzywniak": ["marchew", "seler", "rukola"]
}
for shop, products in shopping_dict.items():
  shop=shop.capitalize()
  products=[product.capitalize() for product in products]
  print(f"Idę do {shop} i kupuję tam {products}.")
  number_of_products = sum(len(products) for products in shopping_dict.values())
  print(f"W sumie kupuję {number_of_products} produktów.")