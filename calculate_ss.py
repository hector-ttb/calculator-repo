import random
import csv

def get_ss(file):
  ss= []
  with open file as ss_list:
    csvreader = csv.reader(ss_list)
    for row in csvreader:
      ss.append(row)
    random.shuffle(ss)
  return ss
