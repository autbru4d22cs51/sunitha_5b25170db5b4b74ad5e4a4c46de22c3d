"""
write a function called linear_search_product that takes the list of products and a target product
name as input. The function should perform a linear seach to find the target product in the list and 
return alist of indices of all occurrence of the product if found, or an empty list if the product is not
found.
"""


def linearsearchproduct(productlist, targetproduct):
  indices = []

  for index, product in enumerate(productlist):
    if product == targetproduct:
      indices.append(index)

  return indices


# Example usage:
products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
target2 = 'apple'
result = linearsearchproduct(products, target2)
print(result)