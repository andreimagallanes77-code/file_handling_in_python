class IntegerProcessor:

    def process_numbers(self):
        source_file = open("integers.txt", "r")
        double_file = open("double.txt", "w")
        triple_file = open("triple.txt", "w")

        for line in source_file:
            number_value = int(line.strip())

            if number_value % 2 == 0:
                squared_value = number_value ** 2
                double_file.write(str(squared_value) + "\n")
            else:
                cubed_value = number_value ** 3
                triple_file.write(str(cubed_value) + "\n")