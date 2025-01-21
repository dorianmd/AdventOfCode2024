# Advent of Code 2024
# Day 3: https://adventofcode.com/2024/day/1
# Description:
import re


class AdventDay3:
    def __init__(self):
        self.mults1 = []
        with open('inputs\day3.txt') as f:
            self.data = f.read()
        self.mults1 = self.find_mults(self.data, self.mults1)
        self.valid_instructions_finder()
        self.res1 = 0
        self.res2 = 0

    def get_mult_score(self):
        for pair in self.mults1:
            self.res1 += pair[0] * pair[1]

    def get_mult_w_instructions(self):
        self.find_mults_w_instructions()

    def find_mults(self, string, arr):
        if string:
            for i in re.findall(r'mul\(\d+,\d+\)', string):
                numbers = (re.findall(r'\d+', i))
                arr.append([int(num) for num in numbers])
            return arr

    def valid_instructions_finder(self):
        self.valid_instructions = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", self.data)

    def find_mults_w_instructions(self):
        mult = True
        for i in self.valid_instructions:
            if i == 'do()':
                mult = True
            elif i == "don't()":
                mult = False
            elif mult:
                x = re.findall(r'\d+', i)
                self.res2 += int(x[0]) * int(x[1])


if __name__ == "__main__":
    a = AdventDay3()
    a.get_mult_score()
    a.get_mult_w_instructions()
    print(a.res1, a.res2)