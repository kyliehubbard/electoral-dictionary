"""
CISC-121 2023W
Name: Kylie Hubbard
Student Number: 20294570
Email: kylie.hubbard@queensu.ca
Date: 2023-03-07
I confirm that this assignment solution is my own work and conforms to Queen’s
standards of Academic Integrity
"""

import time
from functions3 import electoralDictionary, displayInfo, uniqueDistricts, findMax, findMin, totalVotes, selectionSort, binarySearch
from pprint import pprint

new_dictionary = []
electoralDictionary(new_dictionary)

x = ' ' # for QOL
print("Hello! This program analyzes a dataset from the Canadian Elections.")
time.sleep(1)
print(x)

print("Your options are:\n"
      "1. Display information for an electoral district\n"
      "2. Show unique districts by the given province\n"
      "3. Find the maximum value of a key\n"
      "4. Find the minimum value of a key\n"
      "5. Display the total number of ballots cast in each province/territory\n"
      "6. Sort the data by specific key\n"
      "7. Find the percentage of voter turnout in a district")

time.sleep(1)
print(x)
choice = input("How would you like to proceed? Please type the corresponding number from the options list. \n")


if choice == "1":
    new_choice = input("Okay great! What electoral number would you like to find more information on? \n")
    displayInfo(new_choice)

elif choice == "2":
    another_choice = input("Okay great! What province would you like to find the electoral districts for? \n")
    print(uniqueDistricts(another_choice))

elif choice == "3":
    newer_choice = input("Okay great! What section would you like to find the maximum value of? \n")
    print(findMax(newer_choice))

elif choice == "4":
    second_choice = input("Okay great! What section would you like to find the minimum value of? \n")
    print(findMin(second_choice))

elif choice == "5":
    print("Okay great! Here are the total votes for each province/territory: ")
    print(totalVotes(new_dictionary))

elif choice == "6":
    secondary_choice = input("Okay great! What section would you like to sort the data by? \n")
    print("Sorted by " + str(secondary_choice))
    pprint(selectionSort(new_dictionary, secondary_choice))

elif choice == "7":
    the_choice = input("Okay great! What electoral district would you like to find the voter turnout for? \n")
    print("Found: " + binarySearch(new_dictionary, the_choice))

else:
    print("Please choose an option from the list above.")
