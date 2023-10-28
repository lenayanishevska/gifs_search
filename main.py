from gif_search import search_gif_by_string

search_string = input("Enter a word to find gifs: ")
gif_links = search_gif_by_string(search_string)

print("Links for searched word: ")
for i in gif_links:
    print(i)
