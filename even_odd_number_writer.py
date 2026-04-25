class NumberSeparator:

    def __init__(self):
        self.source_filename = "numbers.txt"
        self.even_filename = "even.txt"
        self.odd_filename = "odd.txt"

    def separate_numbers(self):
        source_file = open(self.source_filename, "w")
        even_file = open(self.even_filename, "w")
        odd_file = open(self.odd_filename, "w")

        for number_line in source_file:
            number_value = int(number_line.strip())

            if number_value % 2 == 0:
                even_file.write(str(number_value) + "\n")
            else:
                odd_file.write(str(number_value) + "\n")