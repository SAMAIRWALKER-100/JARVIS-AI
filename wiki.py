"""import wikipedia
result = wikipedia.summary("India", sentences = 2)
print(result)"""

import wikipedia
page_object = wikipedia.page(input("What would you like to search: "))
print(page_object.html)
print(page_object.original_title)
print(page_object.links[0:10])