class StudentGWAFinder:

    def __init__(self):
        self.filename = "students.txt"

    def find_highest_gwa(self):
        file = open(self.filename, "r")

        top_student_name = ""
        top_student_gwa = 999

        for line in file:
            data = line.strip().split()

            student_name = " ".join(data[:-1])
            student_gwa = float(data[-1])