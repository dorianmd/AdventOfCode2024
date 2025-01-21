# Advent of Code 2024
# Day 1: https://adventofcode.com/2024/day/1
# Description:
# Goal of this challange is to calculate distance (difference) between two sorted lists.
# Second part of the challange implements similarity score between two sorted lists, which is calculated by counting
# occurences of each element in both lists and multiplying them by amount of occurences in the other list.

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
        self.left_sim = self._sim_score(self.left)
        self.right_sim = self._sim_score(self.right)
        self.res1 = 0
        self.res2 = 0

    def get_sum(self):
        # Calculates sum of absolute differences between two lists
        for i in range(len(self.left)):
            self.res1 += abs(self.left[i] - self.right[i])

    def get_sim_score(self):
        # Searches the same values in both dicts, calculates sim score per formula:
        # sim_score = value * occurences_in_left * occurences_in_right
        for key, value in self.right_sim.items():
            self.res2 += key * value * self.left_sim.get(key, 0)

    def _sim_score(self, x):
        # Counts occurence of each element in each list, returns dict
        sim_count = {}
        for i in x:
            sim_count[i] = sim_count.get(i, 0) +1
        return sim_count


if __name__ == '__main__':
    a = AdventDay1()
    a.get_sum()
    a.get_sim_score()
    print(a.res1, a.res2)