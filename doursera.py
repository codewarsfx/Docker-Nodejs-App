#!/usr/bin/env python3
import re 
import operator
import csv

error_entery ={}
user_entry={}


def convert_to_tuple(main):
    turple_users = []
    for name,value in main:
        new_tuple = (name,value["INFO"],value["ERROR"])
        turple_users.append(new_tuple)
    return turple_users

def convert_to_csv(arr,type):
    if type== 'error':
        with open('error_message.csv','w') as f:
            writer = csv.writer(f)
            for row in arr:
                writer.writerow(row)
    if type== 'info':
        with open('user_statistics.csv','w') as f:
            writer = csv.writer(f)
            for row in arr:
                writer.writerow(row)




def add_to_object(entry,obj):
        if entry in obj.keys():
                obj[entry] =obj[entry] + 1
        else:
                obj[entry] = 1
def add_user(usr,obj,type):
    if usr in obj.keys():
        if type == 'error':
            obj[usr]["ERROR"] += 1
        elif type == 'info':
              obj[usr]["INFO"] += 1
    else:
        if type == 'error':
              obj[usr] = {
                "INFO":0,
                "ERROR":1
              }
        elif type == 'info':
              obj[usr] = {
                "INFO":1,
                "ERROR":0
              }

with open('syslog.log','r') as f:
    for line in f:
        name=re.search(r"([\w.]+)",re.search(r"(\(.*\))$", line).group(1)).group(1)
        error_search= re.search(r"ticky: ERROR ([\w ]*) ", line)
        info_search= re.search(r"ticky: INFO ([\w ]*) ", line)
        if error_search and name:
            type= "error"
            message = error_search.group(1)
            add_to_object(message,error_entery)
            add_user(name,user_entry,type)
        elif info_search and name:
            type= "info"
            add_user(name,user_entry,type)
    f.close()
    sorted_errors = sorted(error_entery.items(), key=operator.itemgetter(1),reverse=True)
    sorted_users =convert_to_tuple(sorted(user_entry.items(), key=operator.itemgetter(0)))
    sorted_errors.insert(0,  ("Error", "Count"))
    sorted_users.insert(0, ("Username", "INFO", "ERROR"))
    
    convert_to_csv(sorted_users,'info')
    convert_to_csv(sorted_errors,'error')
    

