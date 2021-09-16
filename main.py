#import libraries
import csv
import datetime

#setup variables
price = 40
DateTime = datetime.datetime.now()

#Define the user prompt
def prompt():
    action = input("What would you like to do, (L)og, (R)eview, or (C)lear?")
    if action == ("L") or action == ("l") or action == ("log") or action == ("Log"):
        #Run logging function
        log()
    elif action == ("R") or action == ("r") or action == ("review") or action == ("Review"):
        #Run review function
        review()
    elif action == ("C") or action == ("c") or action == ("clear") or action == ("Clear"):
        #Run review function
        clear()
    else:
        print ("Naw kid, try again..")
    prompt()

#define log function
def log():
    with open('Historical_Data.csv', 'a') as csv_file:
        price_writer = csv.writer(
            csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        price_writer.writerow(
            [DateTime.strftime("%Y-%m-%d %X"), ('%.6f' % (price))])
        print("Logged data to file..")

#define review function
def review():
    with open('Historical_Data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print("on" f'\t{row[0]} The Current XTZ price was: {row[1]}')
                line_count += 1
        print(f'Processed {line_count} lines.')

#define clear function
def clear():
    with open('Historical_Data.csv', 'a') as csv_file:
        price_writer = csv.writer(
            csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        price_writer.writerow()
        print("File Cleared...")

#Prompt the user for their action
prompt()


