class MyLifeWriter:

    def write_lines(self):
        file = open("mylife.txt", "w")

        while True:
            line_text = input("Enter line: ")
            file.write(line_text + "\n")