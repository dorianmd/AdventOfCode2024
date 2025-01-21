class AdventDay4:
    def __init__(self):
        self.lines = []
        with open('inputs/day4.txt') as f:
            for line in f.readlines():
                self.lines.append([x for x in line if x != '\n'])
        for line in self.lines:
            print(line)
        self.word = ['XMAS', 'SAMX']
        self.word2 = ['MAS', 'SAM']
        self.n =  len(self.lines)
        self.m = len(self.lines[0])
        self.res1 = 0
        self.res2 = 0

    def find_word(self):
        self._find_row()
        self._find_col()
        self._find_diag()

    def _find_row(self):
        for row in self.lines:
            for i in range(self.m-  3):
                self.res1 += ''.join(row[i:i+4]) in self.word

    def _find_col(self):
        for col in zip(*self.lines):
            for i in range(self.m - 3):
                self.res1 += ''.join(col[i:i+4]) in self.word


    def _find_diag(self):
        for row in range(self.n-3):
            for col in range(self.m-3):
                diag1 = ''.join([self.lines[row][col],
                                 self.lines[row+1][col+1],
                                 self.lines[row+2][col+2],
                                 self.lines[row+3][col+3]])
                diag2 = ''.join([self.lines[row][col+3],
                                 self.lines[row+1][col+2],
                                 self.lines[row+2][col+1],
                                 self.lines[row+3][col]])
                self.res1 += diag1 in self.word
                self.res1 += diag2 in self.word

    def find_mas(self):
        for row in range(self.n-2):
            for col in range(self.m-2):
                diag1 = ''.join([self.lines[row][col],
                                 self.lines[row + 1][col + 1],
                                 self.lines[row + 2][col + 2]])
                diag2 = ''.join([self.lines[row][col + 2],
                                 self.lines[row + 1][col + 1],
                                 self.lines[row + 2][col]])
                self.res2 +=1 if diag1 in self.word2 and diag2 in self.word2 else 0


if __name__ == "__main__":
    a = AdventDay4()
    a.find_word()
    a.find_mas()
    print(a.res1, a.res2)