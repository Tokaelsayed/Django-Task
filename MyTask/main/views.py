
from typing import Text
import collections
from django.db.models.aggregates import Count
from django.http.response import HttpResponseRedirect, JsonResponse
from django.db.models import Sum, base
from django.shortcuts import render
from  django.http import HttpResponse
from django.views.generic import View
import csv
from json import dumps
from datetime import datetime


# Create your views here.


def Barcharts(response):
    Labels = []
    data = []
    unique_list = []
    #########################################
    

    with open('train_users_2.csv') as csv_file: ## Open train_user2 dataset
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            Labels.append(row[9])    
            line_count += 1     
    for x in Labels:
        #Represent only unique values
        if x not in unique_list:
            unique_list.append(x)
    print(unique_list) #unique values
    occurrences = collections.Counter(Labels)   
    print(occurrences)  
    i = 0
    for i in occurrences:
      data.append((occurrences[i]/213453)*100) #calculate precentage (occur/total)*100

    #send data to FrontEnd
    dataDictionary ={
        'labels': unique_list,
        'data': data,
         }
    dataJSON = dumps(dataDictionary)
    return render( 
        response,
        "main/Barchart.html",
        {'data': dataJSON})


def SecondBarcharts(response):

    Labels = []
    data = []
    precentage = []
    #########################################
    

    with open('train_users_2.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            Labels.append(row[10])    
            line_count += 1     
    for x in Labels:
        if x not in precentage:
            precentage.append(x)
    print(precentage) #unique values
    occurrences = collections.Counter(Labels)   
    print(occurrences)  
    i = 0
    for i in occurrences:
      data.append((occurrences[i]/213453)*100)
    
      #########################################################

    
    dataDictionary ={
        'labels': precentage,
        'data': data,
         }
    dataJSON = dumps(dataDictionary)
    return render(
        response,
        "main/SecondBarchart.html",
        {'data': dataJSON})

def ThirdBarcharts(response):
    Labels = []
    data = []
    precentage = []
    #########################################
    

    with open('train_users_2.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            Labels.append(row[15])    
            line_count += 1     
    for x in Labels:
        # Represent Unique values
        if x not in precentage:
            precentage.append(x)
    print(precentage) #unique values
    occurrences = collections.Counter(Labels)  # Occurrence no. according to whole Dataset 
    print(occurrences)  
    i = 0
    for i in occurrences:
      data.append((occurrences[i]))
      #########################################################

    
    dataDictionary ={
        'labels': precentage,
        'data': data,
         }
    dataJSON = dumps(dataDictionary)
    return render(
        response,
        "main/ThirdBarchart.html",
        {'data': dataJSON})

def FourthBarcharts(response):
    Labels = ["Android","Moweb","Web","iOS"]
    #########################################
    age1 = [0,0,0,0]
    age2 = [0,0,0,0]
    age3 = [0,0,0,0]
    age4 = [0,0,0,0]
    age5 = [0,0,0,0]
    age6 = [0,0,0,0]
    age7 = [0,0,0,0]
    
    list_of_ages = []

    with open('train_users_2.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
        if line_count == 0:
           # print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:   
            line_count += 1     
            age = row[5]
            if age == '':
              continue
            else:
                age= float(age)
            if 18 <= age  <= 20:
                for i in range(4):
                    if Labels[i]==row[12]:
                        age1[i]+=1
            elif 20 < age <= 30:
                for i in range(4):
                    if Labels[i]==row[12]:
                        age2[i]+=1
            elif 30 <  age <= 40:
                for i in range(4):
                    if Labels[i]==row[12]:
                        age3[i]+=1
            elif 40 < age <= 50:
                for i in range(4):
                    if Labels[i]==row[12]:
                        age4[i]+=1
            elif 50 < age <= 60:
                for i in range(4):
                    if Labels[i]==row[12]:
                        age5[i]+=1
            elif 60 < age <= 70:
                for i in range(4):
                    if Labels[i]==row[12]:
                        age6[i]+=1
            elif 70 < age :
                for i in range(4):
                    if Labels[i]==row[12]:
                        age7[i]+=1
      ########################################################
    
    dataDictionary ={
        'labels': Labels,
        'data1': age1,
        'data2': age2,
        'data3': age3,
        'data4': age4,
        'data5': age5,
        'data6': age6,
        'data7': age7,
         }
    dataJSON = dumps(dataDictionary)
    return render(
        response,
        "main/FourthBarchart.html",
        {'data': dataJSON})

def Dategraph(response):
    Labels = []
    data = []
    unique_list = []
    #########################################
    

    with open('train_users_2.csv') as csv_file: ## Open train_user2 dataset
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            Labels.append(row[1])    
            line_count += 1  
    Labels.sort()
    occurrences = collections.Counter(Labels)
    print(occurrences)     
    currentusers = 0
    for x in Labels:
        #Represent only unique values
        if x not in unique_list:
            unique_list.append(x)
    print(unique_list) #unique values

    for y in unique_list:
        currentusers += occurrences[y] 
        data.append(occurrences[y])
   

    #send data to FrontEnd
    dataDictionary ={
        'labels': unique_list,
        'data': data,
         }
    dataJSON = dumps(dataDictionary)
    return render( 
        response,
        "main/datecreatedgraph.html",
        {'data': dataJSON})


def SecondDategraph(response):
    Labels = []
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    data6 = []
    data7 = []
    unique_list = []
    age1 = []
    age2 = []
    age3 = []
    age4 = []
    age5 = []
    age6 = []
    age7 = []

    #########################################
    

    with open('train_users_2.csv') as csv_file: ## Open train_user2 dataset
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            age = row[5]
            if age == '':
               continue
            else:
                age= float(age)
            if 18 <= age  <= 20:
                age1.append(row[1])
                Labels.append(row[1])
            elif 20 < age <= 30:
                age2.append(row[1])
                Labels.append(row[1])
            elif 30 <  age <= 40:
                age3.append(row[1])
                Labels.append(row[1])
            elif 40 <age <= 50:
                age4.append(row[1])
                Labels.append(row[1])
            elif 50 < age <= 60:
                age5.append(row[1])
                Labels.append(row[1])
            elif 60 < age <= 70:
                age6.append(row[1])
                Labels.append(row[1])
            elif 70 < age :
                age7.append(row[1])
                Labels.append(row[1])  
            line_count += 1  
    Labels.sort()
    occurrences1 = collections.Counter(age1)
    occurrences2 = collections.Counter(age2)
    occurrences3 = collections.Counter(age3)
    occurrences4 = collections.Counter(age4)
    occurrences5 = collections.Counter(age5)
    occurrences6 = collections.Counter(age6)
    occurrences7 = collections.Counter(age7)
     
    currentusers = 0
    for x in Labels:
        #Represent only unique values
        if x not in unique_list:
            unique_list.append(x)
    print(unique_list) #unique values

    for y in unique_list:
        
        data1.append(occurrences1[y])
        data2.append(occurrences2[y])
        data3.append(occurrences3[y])
        data4.append(occurrences4[y])
        data5.append(occurrences5[y])
        data6.append(occurrences6[y])
        data7.append(occurrences7[y])
   

    #send data to FrontEnd
    dataDictionary ={
        'labels': unique_list,
        'data1': data1,
        'data2': data2,
        'data3': data3,
        'data4': data4,
        'data5': data5,
        'data6': data6,
        'data7': data7,
        
         }
    dataJSON = dumps(dataDictionary)
    return render( 
        response,
        "main/Seconddategraph.html",
        {'data': dataJSON})


def ThirdDategraph(response):
    Labels = []
    data1 = []
    data2 = []
    data3 = []
    data4 = []
   
    unique_list = []
    method1 = []
    method2 = []
    method3 = []
    method4 = []
   

    #########################################
    

    with open('train_users_2.csv') as csv_file: ## Open train_user2 dataset
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
             
            if row[12] == "Android":
                method1.append(row[1])
                Labels.append(row[1])
            elif row[12] == "Moweb":
                method2.append(row[1])
                Labels.append(row[1])
            elif row[12] == "Web":
                method3.append(row[1])
                Labels.append(row[1])
            elif row[12] == "iOS":
                method4.append(row[1])
                Labels.append(row[1])
            
            line_count += 1  
    Labels.sort()
    occurrences1 = collections.Counter(method1)
    occurrences2 = collections.Counter(method2)
    occurrences3 = collections.Counter(method3)
    occurrences4 = collections.Counter(method4)

    for x in Labels:
        #Represent only unique values
        if x not in unique_list:
            unique_list.append(x)
    print(unique_list) #unique values

    for y in unique_list:
        
        data1.append(occurrences1[y])
        data2.append(occurrences2[y])
        data3.append(occurrences3[y])
        data4.append(occurrences4[y])
     
    #send data to FrontEnd
    dataDictionary ={
        'labels': unique_list,
        'data1': data1,
        'data2': data2,
        'data3': data3,
        'data4': data4,
        
         }
    dataJSON = dumps(dataDictionary)
    return render( 
        response,
        "main/Thirddategraph.html",
        {'data': dataJSON})



    
  

  

