shopping_dict = {
  "piekarnia": ["chleb", "bułki", "pączek"],
  "warzywniak": ["marchew", "seler", "rukola"]
}
for shop, products in shopping_dict.items():
  shop=shop.capitalize()
  products=[product.capitalize() for product in products]
  print(f"Idę do {shop} i kupuję tam {products}.")