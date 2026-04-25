class StudentGWAFinder:

    def __init__(self):
        self.filename = "students.txt"

    def find_highest_gwa(self):
        file = open(self.filename, "r")

        top_student_name = ""
        top_student_gwa = 999

        for line in file:
            data = line.strip().split()

            print(data)  # DEBUG: shows how each line is read

            student_name = " ".join(data[:-1])
            student_gwa = float(data[-1])

            if student_gwa < top_student_gwa:
                top_student_gwa = student_gwa
                top_student_name = student_name

        file.close()

        print("\nHighest GWA Student:")
        print("Name:", top_student_name)
        print("GWA:", top_student_gwa)


def main():
    student_finder = StudentGWAFinder()
    student_finder.find_highest_gwa()


main()

