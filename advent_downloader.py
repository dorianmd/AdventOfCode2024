# This script automates downloading input for Advent of Code and automatically creates code files.
#
# It is based on Browser Cookie by boisbabic, and due to it being outdated, only few browsers are currently working
# with it, including Firefox.
#
# Browser Cookie: https://github.com/borisbabic/browser_cookie3

import os.path
import browser_cookie3
import requests

class AdventDownloader:
    def __init__(self, x):
        # Initializes downloader. Path is predefined for purpose of running from other directory.
        self.day = x
        self.url = f'https://adventofcode.com/2024/day/{self.day}/input'
        self.path = r'C:\Users\doria\PycharmProjects\AdventofCode2024'
        print(f"URL: {self.url}")

    def create(self):
        # Calls both methods
        self._create_input_file()
        self._new_code_file()

    # Download
    def _create_input_file(self):
        # Write input from GET request to the file.
        self._get_input_file()
        input_file_path = os.path.join(self.path, f"inputs\\day{self.day}.txt")
        print(f"Creating input file at: {input_file_path}")
        with open(input_file_path, 'wb') as f:
            f.write(self._get_input_file())

    def _get_input_file(self):
        # Send GET request to Advent Of Code website to retrieve input, returns content of the website.
        cj = browser_cookie3.firefox(domain_name='adventofcode.com')
        r = requests.get(self.url, cookies=cj)
        print(f"Response status code: {r.status_code}")
        return r.content


    def _new_code_file(self):
        # Create code file for the day.
        code_file_path = os.path.join(self.path, f"day{self.day}.py")
        print(f"Creating code file at: {code_file_path}")
        with open(code_file_path, 'w') as code:
            code.close()


if __name__ == "__main__":
    day = input("Day number: ")
    a = AdventDownloader(day)
    a.create()