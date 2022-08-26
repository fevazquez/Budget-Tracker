#!/usr/bin/python

import os
import sys
import csv
import gspread
import time
from datetime import datetime

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

def get_final_name_and_category(transaction):
  category, name = '',''

  if 'COINBASE' in transaction:
    category = 'Investing'
    name = 'Coinbase - BTC/ETH'

  elif 'AMERICANEXPRESS' in transaction:
    category = 'Savings'
    name = 'AMEX transfer'

  elif 'DES:AAA' in transaction or 'PENTAGON' in transaction:
    category = 'Car'
    name = 'Car payment' if 'PENTAGON' in transaction else 'AAA Insurance'
  
  elif 'CHASE' in transaction or 'Credit Card' in transaction:
    category = 'Shopping'
    name = 'CHASE' if 'CHASE' in transaction else 'BOFA'
    name += ' Credit card payment'

  elif 'ADOBE' in transaction or 'SPOTIFY' in transaction:
    category = 'Subscriptions'
    name = 'Spotify' if 'SPOTIFY' in transaction else 'ADOBE'
    name = 'Gym' if 'GYM' in transaction else name
    name += ' payment'

  else:
    category = 'Personal'
    name = transaction

  return name, category


def format_data(transactions):

  formatted_entries = []
  for entry in transactions:
    entry = ''.join(i for i in entry).split('  ')
    entry = [i for i in entry if i]

    date, transaction, amount = entry[0], entry[1], float(entry[2])
    if amount < 0:
      name, category = get_final_name_and_category(transaction)
      formatted_entries.append([name, category, date, '', abs(amount)])

  sorted(formatted_entries, key=lambda x: x[3])
    
  return formatted_entries 


def upload_transactions(transactions, month=None, year=None):
  if not month or not year:
    print(f'Please provide month and year.')
    sys.exit()
    
  sa = gspread.service_account()
  sh = sa.open("Budget Tracking")

  wks = sh.worksheet(f'{month} {year}')
  start = 7
  for idx, transaction in enumerate(transactions):
    wks.insert_row(transaction, start+idx)
  

def main():
  month,year = get_date()
  files = get_files(month, year)

  print(f'\nFetching transations from {month} {year}')
  transactions = get_transactions(files, month, year)
  print(f'Success. Found {len(transactions)}\n\n')

  print('Preparing each entry for upload... \n')
  formatted_transactions = format_data(transactions)

  print('Uploading transactions to budget tracker.... \n\n')
  upload_transactions(formatted_transactions, month, year)
  print('Success!')
  

if __name__ == '__main__':
  main()