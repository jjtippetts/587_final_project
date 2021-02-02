# This code was provided courtesy of Neha Agrawal. It generates code that adheres to the Updated Wisoncsin Benchmark Schema that accounts for scalability

import csv
import numpy as np
import random
import string

def listToString(s):  
    str1 = ""   
    for ele in s:  
        str1 += ele    
    return str1

def convert(unique):
    rem=0
    temp=list("\0"*7)
    result=list("A"*7)
    i=6
    str = dict(zip(range(1, 27), string.ascii_uppercase))
    while(unique>0):
        rem=unique%26
        temp[i]=str[rem+1]
        i=i-1
        unique=(int)(unique/26)
    
    for i in range(i+1,7):
        result[i]=temp[i]

    return listToString(result)
    
def datagenerate(records, headers):
    with open("TENKTUP2.csv", 'wt', newline='') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        unique2,unique1=[],[]
        string4Array = ["AAAA","HHHH","OOOO","VVVV"]
        for i in range(records):
            unique2.append(i)
        unique1 = np.random.permutation(records)
        s1 = []
        s2 = []
        for i in range(45):
            s1.append('x')
        s11 = listToString(s1)
        for i in range(48):
            s2.append('x')
        s22 = listToString(s2)
        for i in range(records):

            stringu1converted = convert(unique1[i])
            stringu2converted = convert(unique2[i])
            str4Index = unique2[i]%4
            string4value = string4Array[str4Index]
            writer.writerow({
                    "unique1" : unique1[i],
                    "unique2" : unique2[i],
                    "two": unique1[i]%2,
                    "four" : unique1[i]%4,
                    "ten" : unique1[i]%10,
                    "twenty": unique1[i]%20,
                    "onePercent" : unique1[i]%100,
                    "tenPercent" : unique1[i]%10,
                    "twentyPercent" : unique1[i]%5,
                    "fiftyPercent" : unique1[i]%2,
                    "unique3" : unique1[i],
                    "evenOnePercent":(unique1[i]%100)*2,
                    "oddOnePercent": ((unique1[i]%100)*2)+1,
                    "stringu1": stringu1converted+s11,
                    "stringu2": stringu2converted+s11,
                    "string4": string4value+s22,
                    })
    
if __name__ == '__main__':
    records = 10000
    headers = ["unique1", "unique2", "two", "four", "ten", "twenty",
               "onePercent", "tenPercent", "twentyPercent", "fiftyPercent",
               "unique3", "evenOnePercent", "oddOnePercent", "stringu1", "stringu2", "string4"]
    datagenerate(records, headers)
    print("CSV generation complete!")

