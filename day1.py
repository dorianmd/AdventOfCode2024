# Advent of Code 2024
# Day 1: https://adventofcode.com/2024/day/1
# Description:
# This challange is split into two parts.
# First is to

class AdventDay1:

    def __init__(self):
        self.left = []
        self.right = []
        with open('inputs\day1.txt') as f:
            for line in f.readlines():
                l, r = line.split()
                self.left.append(int(l))
                self.right.append(int(r))
        self.left.sort()
        self.right.sort()
        self.left_sim = self.sim_score(self.left)
        self.right_sim = self.sim_score(self.right)
        self.res1 = 0
        self.res2 = 0

    def get_sum(self):
        for i in range(len(self.left)):
            self.res1 += abs(self.left[i] - self.right[i])

    def get_sim_score(self):
        for key, value in self.right_sim.items():
            self.res2 += key * value * self.left_sim.get(key, 0)

    def sim_score(self, x):
        sim_count = {}
        for i in x:
            sim_count[i] = sim_count.get(i, 0) +1
        return sim_count





if __name__ == '__main__':
    a = AdventDay1()
    a.get_sum()
    a.get_sim_score()
    print(a.res1, a.res2)