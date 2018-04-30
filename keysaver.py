import sqlite3
import os

def print_menu():
    print('''
    Select mode:\n
    \t1 - insert element\n
    \t2 - remove element by key\n
    \t3 - remove element by value\n
    \t4 - search''')

def is_key_exists(key):
    res = c.execute("SELECT * FROM ")

def insert_value():
    print("Select key:", end='')
    key = input()
    pr

if not os.path.exists("keys.db"):
    conn = sqlite3.connect("keys.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE keys 
                (key text, value text)''')
    conn.commit()
    conn.close()

conn = sqlite3.connect("keys.db")
c = conn.cursor()
while True:
    print_menu()
    mode = input()
    try:
        mode = int(mode)
        if mode in range(1, 5):
            if mode == 1:

    except:
        print("Enter correct mode number!")
        continue
