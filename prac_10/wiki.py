import wikipedia

search_phrase = input("Enter search phrase: ")
print(search_phrase.title())
print(wikipedia.summary(search_phrase))
print(search_phrase.url)
