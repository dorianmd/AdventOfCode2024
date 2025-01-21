# Advent of Code 2024
# Day 2: https://adventofcode.com/2024/day/2
# Description:
# Goal of this challange is to analyze list of reactor reports and check if they are safe.
# Safe repot is a list where difference between each element is 1, 2 or 3 and list is either only increasing
# or decreasing.
# Second part of the challange implements Problem Dampener to check if there is a way to make a report safe by removing
# one element.


class AdventDay2:
    def __init__(self):
        self.reports = []
        with open('inputs\day2.txt') as f:
            for line in f.readlines():

                self.reports.append([int(x) for x in line.split()])
        self.res1 = 0
        self.res2 = 0
        self.bad = []

    def analyze(self, row):
        # Checks if provided row is safe. Returns boolean.
        is_row_safe = {row[i] - row[i - 1] for i in range(1, len(row))}
        return (is_row_safe <= {1, 2, 3} or
                is_row_safe <= {-1, -2, -3})

    def analyze_one_bad(self, row, i=0):
        # Checks if provided row is safe after removing one element. Returns boolean.
        if i>= len(row):
            return False
        x = row[:i] + row[i+1:]

        is_row_safe = {x[j] - x[j - 1] for j in range(1, len(x))}
        if is_row_safe <= {1, 2, 3} or is_row_safe <= {-1, -2, -3}:
            return True
        else:
            return self.analyze_one_bad(row, i + 1)



    def get_safe_score(self):
        # Calls self.analyze for each row to check if it's safe.

        for report in self.reports:
            if self.analyze(report):
                self.res1 += 1
                self.res2 += 1
            else:
                self.bad.append(report)

    def get_dampener_safe_score(self):
        # Calls self.analyze_one_bad for each row to check if it's safe after removing one element.
        for row in self.bad:
            if self.analyze_one_bad(row):
                self.res2 += 1


if __name__ == '__main__':
    a = AdventDay2()
    a.get_safe_score()
    a.get_dampener_safe_score()
    print(a.res1, a.res2)