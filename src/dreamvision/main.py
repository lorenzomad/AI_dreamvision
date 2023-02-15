import os

#local imports
from dreamvision import Dreamvision
   
def main():
    if not os.path.exists("./generated/"):
        os.mkdir("./generated/")
    dreamvision = Dreamvision()
    dreamvision.run()
    dreamvision.close_connection()



if __name__ == "__main__":
    main()
    