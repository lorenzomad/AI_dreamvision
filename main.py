from craiyon import Craiyon

generator = Craiyon()


text = "dream of " + input("please insert the text of your dream \n")
result = generator.generate(text)
result.save_images()

print("images generated")
