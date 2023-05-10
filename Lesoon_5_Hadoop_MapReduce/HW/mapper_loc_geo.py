import sys
import csv

filename_one = sys.argv[1]
f_1 = open(filename_one, 'r')
csv_one = csv.DictReader(f_1)
list_one  = list(csv_one)

filename_two = sys.argv[2]
f_2 = open(filename_two, 'r')
csv_two= csv.DictReader(f_2)
list_two = list(csv_two)

print(list_one)
print(list_two)