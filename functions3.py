"""
CISC-121 2023W
Name: Kylie Hubbard
Student Number: 20294570
Email: kylie.hubbard@queensu.ca
Date: 2023-03-07
I confirm that this assignment solution is my own work and conforms to Queen’s
standards of Academic Integrity
"""

import csv
from pprint import pprint

new_dictionary = []

def electoralDictionary(dictionary):
    with open("table_tableau11.csv", "r") as file:
        dict_reader = csv.DictReader(file)
        for item in dict_reader:
            new_dictionary.append(item)
        return (new_dictionary)


def displayInfo(electoral_num):
    a_list = new_dictionary
    district = None
    for k in a_list:
        if k["Electoral District Number"] == electoral_num:
            district = k
            break
    polling_stations = int(district["Polling Stations"])
    valid_ballots = int(district["Valid Ballots"])
    total_ballots = int(district["Total Ballots Cast"])
    percentage_turnout = district["Percentage of Voter Turnout"]

    print("Polling Stations: " + str(polling_stations))
    print("Valid Ballots: " + str(valid_ballots))
    print("Total Ballots Cast: " + str(total_ballots))
    print("Voter Turnout: " + str(percentage_turnout))


def uniqueDistricts(province_name):
    a_list = new_dictionary
    districts = []
    for k in a_list:
        if k["ï»¿Province"] == province_name:
            districts.append(k["Electoral District Name"])
    return districts


def findMax(key):
    a_list = new_dictionary
    max_value = None
    max_district = None
    for k in a_list:
        value = int(k[key])
        if max_value is None or value > max_value:
            max_value = value
            max_district = k
    return (max_district, max_value)


def findMin(key):
    a_list = new_dictionary
    min_value = None
    min_district = None
    for k in a_list:
        value = int(k[key])
        if min_value is None or value < min_value:
            min_value = value
            min_district = k
    return (min_district, min_value)


def totalVotes(dictionary):
    another_dictionary = {}
    total_sum = 0
    for item in new_dictionary:
        province = item["ï»¿Province"]
        total_ballots = item["Total Ballots Cast"]
        if province in another_dictionary:
            another_dictionary[province] += total_ballots
        else:
            another_dictionary[province] = total_ballots
    result = []
    for province, total_ballots in another_dictionary.items():
        result.append({province:total_ballots})
    return result


def selectionSort(dictionary,key):
    size = len(new_dictionary)
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if new_dictionary[min_index][key] > new_dictionary[j][key]:
                min_index = j
        new_dictionary[i], new_dictionary[min_index] = new_dictionary[min_index], new_dictionary[i]
    return new_dictionary


def binarySearch(dictionary, electoral_district):
    start = 0
    end = len(new_dictionary) - 1
    while start <= end:
        mid = (start + end) // 2
        if new_dictionary[mid]["Electoral District Number"] == electoral_district:
            return new_dictionary[mid]["Percentage of Voter Turnout"]
        elif electoral_district < new_dictionary[mid]["Electoral District Number"]:
            end = mid - 1
        else:
            start = mid + 1
    return None
