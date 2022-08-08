#!/usr/bin/python

import os
import sys
import csv
import gspread
import time

def get_date():
  if len(sys.argv) < 3:
    return None, None

  return sys.argv[1].lower().capitalize(), sys.argv[2]

def get_files(month, year):
  if not os.path.isdir(f'./{month} {year}'):
    print(f'Directory {month} {year} not found.')
    sys.exit()

  return os.listdir(f'./{month} {year}')

def read_data(files, month, year):
  data = []
  for file in files:
    path = f'./{month} {year}/{file}'

    with open(path, mode='r') as csv_file:
      csv_reader = csv.reader(csv_file)

      # This skips the first row of the CSV file.
      next(csv_reader)
      for row in csv_reader:
        data.append(row)
    
  return data

def cleanse_data(data):
  pass


def main():
  month,year = get_date()

  files = get_files(month, year)

  transactions = read_data(files, month, year)
  for row in transactions:
    print(row)

  # sa = gspread.service_account()
  # sh = sa.open("Budget Tracking")

  # wks = sh.worksheet(f'{month} {year}')
  # wks.insert_row(['test','Car','8/8'], 10)


if __name__ == '__main__':
  main()