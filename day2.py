class AdventDay1:

    def __init__(self):
        self.reports = []
        with open('inputs\day2.txt') as f:
            for line in f.readlines():

                self.reports.append([int(x) for x in line.split()])
        self.res1 = 0

    def analyze(self, row):
        self.is_row_safe = {row[i] - row[i - 1] for i in range(1, len(row))}
        print(self.is_row_safe)
        return (self.is_row_safe <= {1, 2, 3} or
                self.is_row_safe <= {-1, -2, -3})

    def get_safe_score(self):
        for report in self.reports:
            if self.analyze(report):
                self.res1 += 1


a = AdventDay1()
a.get_safe_score()
print(a.res1)