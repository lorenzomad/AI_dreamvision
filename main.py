from craiyon import Craiyon

def generate_dream(text):
    """generates pictures of the described dream"""
    generator = Craiyon()
    result = generator.generate(text)
    result.save_images()
    print("images generated")
    return result
