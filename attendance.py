import csv
import os
name_list = ["Anand", "Karthik", "Suresh", "Dilip", "Paul"]
nameq = input("What's your name?")
name = nameq[0].upper() + nameq[1:]
file_exists=os.path.isfile("attendance.csv")
if name in name_list:
    print("Hey there {0}!".format(name))
    with open("attendance.csv", "a",newline='') as csvfile:
        fn = ["Name", "Joined?"]
        writer = csv.DictWriter(csvfile, fieldnames=fn)
        if not file_exists:
            writer.writeheader()
        writer.writerow({'Name': name, 'Joined?': 'Yes'})
else:
    q = input("Are you new here? ")
    if q.lower() == 'yes':
        print("Welcome {}!".format(name))
        name_list.append(name)
        with open("attendance.csv", "a",newline='') as csvfile1:
            fn = ["Name", "Joined?"]
            writer1 = csv.DictWriter(csvfile1, fieldnames=fn)           
            writer1.writerow({'Name': name, 'Joined?': 'Newbie'})
