class MyLifeWriter:

    def write_lines(self):
        file = open("mylife.txt", "w")

        while True:
            line_text = input("Enter line: ")
            file.write(line_text + "\n")

            more_lines = input("Are there more lines y/n? ")

            if more_lines.lower() == "n":
                break

        file.close()
        print("Lines saved to mylife.txt")


def main():
    writer = MyLifeWriter()
    writer.write_lines()


main()
