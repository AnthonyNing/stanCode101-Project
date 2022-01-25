"""
File: extension.py
Name: Anthony Ning
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        # Capture codes under 'td'.
        items = soup.find_all('td')
        # Select numbers in items and put them into a list.
        numbers = []
        for item in items:
            number = item.text
            if not number.isalpha():
                numbers.append(number)
        numbers = numbers[1: len(numbers)-2]

        # The numbers may contain ',', so we have to manipulate the numbers.
        # After manipulating them, we turn them into integers, and put them into a new list.
        int_numbers = []
        for number in numbers:
            int_number = string_manipulation(number)
            int_numbers.append(int(int_number))

        # We now address the new list, and count the numbers of male and female from 1990s to 2010s.
        boy_counter = 0
        girl_counter = 0
        for i in range(len(int_numbers)):
            if i % 3 == 1:
                boy_counter += int_numbers[i]
            elif i % 3 == 2:
                girl_counter += int_numbers[i]
            else:
                pass
        print('Male Number:', boy_counter)
        print('Female Number:', girl_counter)


def string_manipulation(number):
    # The numbers may contain ',', so we have to manipulate the numbers.
    new_number = ''
    for ch in number:
        if ch != ',':
            new_number += ch
    return new_number


if __name__ == '__main__':
    main()
