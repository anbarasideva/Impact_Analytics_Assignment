'''
# Question

In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.

  Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal

Test cases:

for 5 days: 14/29
for 10 days: 372/773
'''


import itertools

class GraduationAttendance:
    
    def __init__(self, days, consecutive_absent_limit):
        self.days = days
        self.consecutive_absent_limit = consecutive_absent_limit
        self.eligible_attendance = self.get_eligible_attendance()
        self.missing_graduation = self.get_missing_graduation()
    
    def generate_attendance_possibility(self):
        return (''.join(combination) for combination in itertools.product(['P', 'A'], repeat=self.days))
    
    def get_eligible_attendance(self):
        return [attendance for attendance in self.generate_attendance_possibility() if 'A' * self.consecutive_absent_limit not in attendance]
    
    def get_missing_graduation(self):
        return [attendance for attendance in self.eligible_attendance if attendance[-1] == 'A']
    
    def get_graduation_missing_probability(self):
        eligible_count = len(self.eligible_attendance)
        missed_count = len(self.missing_graduation)
        return f"{missed_count}/{eligible_count}"
    
if __name__ == '__main__':
    try:
        valid_input = False
        while not valid_input:
            try:
                days = int(input("Enter the number of days: "))
                valid_input = True
            except ValueError:
                print("Invalid input. Please enter an integer.")
        consecutive_absent_limit = 4
        graduation_attendance = GraduationAttendance(days, consecutive_absent_limit)
        graduation_missing_probability = graduation_attendance.get_graduation_missing_probability()
        print("For {} days: {}".format(days, graduation_missing_probability))
    except Exception as e:
        print(e)
