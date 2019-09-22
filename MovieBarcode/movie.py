class movie:
    def __init__ (self, name, height, width):
        self.name = name
        self.height = height
        self.width = width


def main():
    title = input("Enter the movie name: ")
    movType = input("Enter the type of the movie: ")
    name = "Files/%s" % title
    movie = movie()

main()
