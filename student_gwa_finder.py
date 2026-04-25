class StudentGWAFinder:

    def __init__(self):
        self.filename = "students.txt"

    def find_highest_gwa(self):
        file = open(self.filename, "r")
