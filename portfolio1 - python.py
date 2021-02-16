import pandas as pd
import numpy as np
import csv

insurance = pd.read_csv('insurance.csv')
print(insurance.head())

ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []
#function to load data
def load_data(lst, csv_file, column):
    with open(csv_file) as csv_info:
        csv_dict = csv.DictReader(csv_info)
        for row in csv_dict:
            lst.append(row[column])
        return lst
#load all the datas
load_data(ages, 'insurance.csv', 'age')
load_data(sexes, 'insurance.csv', 'sex')
load_data(bmis, 'insurance.csv', 'bmi')
load_data(num_children, 'insurance.csv', 'children')
load_data(smoker_statuses, 'insurance.csv', 'smoker')
load_data(regions, 'insurance.csv', 'region')
load_data(insurance_charges, 'insurance.csv', 'charges')

#create class and methods
class PatientInfo():
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, patients_smoker_statuses, patients_regions, patients_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_charges = patients_charges

    # create dictionary method w/ patient info
    def create_dict(self):
        self.patients_dictionary = {}
        self.patients_dictionary['age'] = [int(age) for age in self.patients_ages]
        self.patients_dictionary['sex'] = self.patients_sexes
        self.patients_dictionary['bmi'] = self.patients_bmis
        self.patients_dictionary['children'] = self.patients_num_children
        self.patients_dictionary['smoker'] = self.patients_smoker_statuses
        self.patients_dictionary['regions'] = self.patients_regions
        self.patients_dictionary['charges'] = [int(charge) for charge in self.patients_charges]
        return self.patients_dictionary

    # What is the average age of the patients in the dataset?
    def analyze_age(self):
        total_age = 0
        for age in self.patients_ages:
            total_age += int(age)
        return('Average Patient Age: {age} years old'.format(age = round(total_age / len(self.patients_ages), 2)))

    # Which region are the majority from?
    def unique_regions(self):
        southwest = 0
        southeast = 0
        northwest = 0
        northeast = 0
        for region in self.patients_regions:
            if region == 'southwest':
                southwest += 1
            elif region == 'southeast':
                southeast += 1
            elif region == 'northwest':
                northwest += 1
            elif region == 'northeast':
                northeast += 1
        return "Southwest: {sw}, Southeast: {se}, Northwest: {nw}, Northeast: {ne}".format(sw = southwest, se = southeast, nw = northwest, ne = northeast)

    # What is the difference in average cost between smokers vs. non-smokers?
    def diff_cost_smokers(self):
        smokers = 0
        non_smokers = 0
        smoker_charges = 0
        non_smoker_charges = 0
        for i in range(len(self.patients_smoker_statuses)):
                if self.patients_smoker_statuses[i] == 'yes':
                    smokers += 1
                    smoker_charges += float(self.patients_charges[i])
                elif self.patients_smoker_statuses[i] == 'no':
                    non_smokers += 1
                    non_smoker_charges += float(self.patients_charges[i])
        return "Average smoker charges: ${smoke}, Average non-smoker charges: ${non_smoke}, Difference in cost: ${diff}".format(smoke = round(smoker_charges/smokers, 2), non_smoke = round(non_smoker_charges/non_smokers, 2), diff = round((smoker_charges/smokers) - (non_smoker_charges/non_smokers), 2))

    # What is the average age for someone who has at least one child?
    def average_age_children(self):
        age = 0
        children = 0
        for i in range(len(self.patients_num_children)):
            if int(self.patients_num_children[i]) >= 1:
                children += 1
                age += int(self.patients_ages[i])
        return "Average age for person with at least one child: {number}".format(number = round(age/children, 2))
#instance the class
patient_info = PatientInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)

print(patient_info.average_age_children())