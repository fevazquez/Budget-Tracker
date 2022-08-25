#!/usr/bin/python

import os
import sys
import csv
import gspread
import time

category = ["Car","Social","Shopping","Subscriptions","Food","Personal","Drinks","Invest,Savings"]

usage = '''
Budget tracker uploader

Usage: 
    python automater.py MONTH YEAR

Must have A directory named MONTH YEAR with the bank statement inside the directory. 
'''

def get_date():
  if len(sys.argv) < 3:
    return None, None

  return sys.argv[1].lower().capitalize(), sys.argv[2]

def get_files(month, year):
  if not os.path.isdir(f'./{month} {year}'):
    print(f'Directory {month} {year} not found.')
    print(usage)
    sys.exit()

  return os.listdir(f'./{month} {year}')

def get_transactions(files, month, year):
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

def get_category(transaction_name):
  

def format_data(transactions):

  formatted_entries = []
  for entry in transactions:
    entry = ''.join(i for i in entry).split('  ')
    entry = [i for i in entry if i]

    date, transaction_name, amount = entry[0], entry[1], float(entry[2])
    if amount < 0:
      formatted_entries.append([date, transaction_name, str(abs(amount))])
    
  return formatted_entries 


def main():
  month,year = get_date()
  files = get_files(month, year)
  transactions = get_transactions(files, month, year)
  
  formatted_transactions = format_data(transactions)
  for i in formatted_transactions:
    print(i)

  # sa = gspread.service_account()
  # sh = sa.open("Budget Tracking")

  # wks = sh.worksheet(f'{month} {year}')
  # wks.insert_row(['test','Car','8/8'], 10)


if __name__ == '__main__':
  main()