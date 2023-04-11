import tensorflow as tf
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
from tensorflow.python.keras.optimizers import *
import numpy as np
from matplotlib import pyplot as plt
from numpy import genfromtxt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.linear_model import SGDRegressor
import math
import pandas as pd

CategoriesFile = open('RizzCategories.txt', 'r')
Categories=CategoriesFile.read()
ListCategories=Categories.split("\n")

for i in range(len(ListCategories)):
    ListCategories[i]=ListCategories[i].strip()

RizzData = pd.read_csv('RizzCalculator171.csv')

LikeCounter=0
DateCounter=0
LikeTotal=0
DateTotal=0

RawLikeDateRizzList=[]

RawHighestLikeList=[]
RawHighestDateList=[]
RawHighestRizzList=[]
RawReportingNumbersLikeDateRizz=[]

RawManLikeDateRizzList=[]

RawManHighestLikeList=[]
RawManHighestDateList=[]
RawManHighestRizzList=[]
RawManReportingNumbersLikeDateRizz=[]

RawWomanLikeDateRizzList=[]

RawWomanHighestLikeList=[]
RawWomanHighestDateList=[]
RawWomanHighestRizzList=[]
RawWomanReportingNumbersLikeDateRizz=[]




# j=5


# while j<=RizzData.shape[1]:
#     for i in range(RizzData.shape[0]):
#         if math.isnan(RizzData.iat[i,j]) == True:
#             LikeCounter=LikeCounter 
#         else:
#                 LikeCounter=LikeCounter+1
#                 LikeTotal=LikeTotal+RizzData.iat[i,j]
#         if math.isnan(RizzData.iat[i,j+1]) == True:
#                 DateCounter=DateCounter    
#         else:
#                 DateCounter=DateCounter+1
#                 DateTotal=DateTotal+RizzData.iat[i,j+1]
#     if LikeCounter != 0 and DateCounter != 0:
#         RawLikeDateRizzList.append((LikeTotal/LikeCounter))
#         RawLikeDateRizzList.append((DateTotal/DateCounter))
#         RawLikeDateRizzList.append(((LikeTotal/LikeCounter)/2)+((DateTotal/DateCounter)/2))
#         RawReportingNumbersLikeDateRizz.append(LikeCounter)
#         RawReportingNumbersLikeDateRizz.append(DateCounter)
#         RawReportingNumbersLikeDateRizz.append((LikeCounter+DateCounter))
#     j=j+3
#     LikeCounter=0
#     DateCounter=0
#     LikeTotal=0
#     DateTotal=0
    
#Men    
j=5

while j<=RizzData.shape[1]:
    for i in range(RizzData.shape[0]):
        if RizzData.iat[i,2] == 'Man':
            if math.isnan(RizzData.iat[i,j]) == True:
                LikeCounter=LikeCounter 
            else:
                LikeCounter=LikeCounter+1
                LikeTotal=LikeTotal+RizzData.iat[i,j]
            if math.isnan(RizzData.iat[i,j+1]) == True:
                DateCounter=DateCounter    
            else:
                DateCounter=DateCounter+1
                DateTotal=DateTotal+RizzData.iat[i,j+1]
    if LikeCounter != 0 and DateCounter != 0:
        RawManLikeDateRizzList.append((LikeTotal/LikeCounter))
        RawManLikeDateRizzList.append((DateTotal/DateCounter))
        RawManLikeDateRizzList.append(((LikeTotal/LikeCounter)/2)+((DateTotal/DateCounter)/2))
        RawManReportingNumbersLikeDateRizz.append(LikeCounter)
        RawManReportingNumbersLikeDateRizz.append(DateCounter)
        RawManReportingNumbersLikeDateRizz.append((LikeCounter+DateCounter))
    
    j=j+3
    LikeCounter=0
    DateCounter=0
    LikeTotal=0
    DateTotal=0
    
#Women
j=5

while j<=RizzData.shape[1]:
    for i in range(RizzData.shape[0]):
        if RizzData.iat[i,2] == 'Woman':
            if math.isnan(RizzData.iat[i,j]) == True:
                LikeCounter=LikeCounter 
            else:
                LikeCounter=LikeCounter+1
                LikeTotal=LikeTotal+RizzData.iat[i,j]
            if math.isnan(RizzData.iat[i,j+1]) == True:
                DateCounter=DateCounter    
            else:
                DateCounter=DateCounter+1
                DateTotal=DateTotal+RizzData.iat[i,j+1]
    if LikeCounter != 0 and DateCounter != 0:
        RawWomanLikeDateRizzList.append((LikeTotal/LikeCounter))
        RawWomanLikeDateRizzList.append((DateTotal/DateCounter))
        RawWomanLikeDateRizzList.append(((LikeTotal/LikeCounter)/2)+((DateTotal/DateCounter)/2))
        RawWomanReportingNumbersLikeDateRizz.append(LikeCounter)
        RawWomanReportingNumbersLikeDateRizz.append(DateCounter)
        RawWomanReportingNumbersLikeDateRizz.append((LikeCounter+DateCounter))
    
    j=j+3
    LikeCounter=0
    DateCounter=0
    LikeTotal=0
    DateTotal=0
    

    

# l=0
# k=0

# while l<len(ListCategories):
#     print(ListCategories[l])
#     print('Likeability: ',RawLikeDateRizzList[k], 'from', RawReportingNumbersLikeDateRizz[k],'people')
#     RawHighestLikeList.append(RawLikeDateRizzList[k])
#     k=k+1
#     print('Dateability: ',RawLikeDateRizzList[k], 'from', RawReportingNumbersLikeDateRizz[k],'people')
#     RawHighestDateList.append(RawLikeDateRizzList[k])
#     k=k+1
#     print('Rizz:        ',RawLikeDateRizzList[k],'created from', RawReportingNumbersLikeDateRizz[k],'datapoints')
#     RawHighestRizzList.append(RawLikeDateRizzList[k])
#     l=l+1
#     k=k+1
    
#Men
l=0
k=0

#print('For Men')
while l<len(ListCategories):
    #print(ListCategories[l])
    #print('Likeability: ',RawManLikeDateRizzList[k], 'from', RawManReportingNumbersLikeDateRizz[k],'people')
    RawManHighestLikeList.append(RawManLikeDateRizzList[k])
    k=k+1
    #print('Dateability: ',RawManLikeDateRizzList[k], 'from', RawManReportingNumbersLikeDateRizz[k],'people')
    RawManHighestDateList.append(RawManLikeDateRizzList[k])
    k=k+1
    #print('Rizz:        ',RawManLikeDateRizzList[k],'created from', RawManReportingNumbersLikeDateRizz[k],'datapoints')
    RawManHighestRizzList.append(RawManLikeDateRizzList[k])
    l=l+1
    k=k+1
    
#Women
l=0
k=0

print('For Women')
while l<len(ListCategories):
    print(ListCategories[l])
    print('Likeability: ',RawWomanLikeDateRizzList[k], 'from', RawManReportingNumbersLikeDateRizz[k],'people')
    RawWomanHighestLikeList.append(RawWomanLikeDateRizzList[k])
    k=k+1
    print('Dateability: ',RawWomanLikeDateRizzList[k], 'from', RawManReportingNumbersLikeDateRizz[k],'people')
    RawWomanHighestDateList.append(RawWomanLikeDateRizzList[k])
    k=k+1
    print('Rizz:        ',RawWomanLikeDateRizzList[k],'created from', RawManReportingNumbersLikeDateRizz[k],'datapoints')
    RawWomanHighestRizzList.append(RawWomanLikeDateRizzList[k])
    l=l+1
    k=k+1

LikeDiff=list()
DateDiff=list()
RizzDiff=list()

for Man, Woman in zip(RawManHighestLikeList, RawWomanHighestLikeList):
    LikeDiff.append(Man-Woman)
for Man, Woman in zip(RawManHighestDateList, RawWomanHighestDateList):
    DateDiff.append(Man-Woman)
for Man, Woman in zip(RawManHighestRizzList, RawWomanHighestRizzList):
    RizzDiff.append(Man-Woman)

print('Difference Scores')
print(np.mean(LikeDiff))
print(np.mean(DateDiff))
print(np.mean(RizzDiff))

#Remove Superlative Questions
# for i in range(20):
#     del RawHighestLikeList[-1]
#     del RawHighestDateList[-1]
#     del RawHighestRizzList[-1]

# RawHighestLikeListSorted=sorted(RawHighestLikeList, key = float, reverse=True)
# RawHighestDateListSorted=sorted(RawHighestDateList, key = float, reverse=True)
# RawHighestRizzListSorted=sorted(RawHighestRizzList, key = float, reverse=True)

# print('')
# print('High Scores')
# print('')
# print('Likeability')
# print(ListCategories[RawHighestLikeList.index(RawHighestLikeListSorted[0])])
# print(RawHighestLikeListSorted[0])
# print(ListCategories[RawHighestLikeList.index(RawHighestLikeListSorted[1])])
# print(RawHighestLikeListSorted[1])
# print(ListCategories[RawHighestLikeList.index(RawHighestLikeListSorted[2])])
# print(RawHighestLikeListSorted[2])
# print('')
# print('Dateability')
# print(ListCategories[RawHighestDateList.index(RawHighestDateListSorted[0])])
# print(RawHighestDateListSorted[0])
# print(ListCategories[RawHighestDateList.index(RawHighestDateListSorted[1])])
# print(RawHighestDateListSorted[1])
# print(ListCategories[RawHighestDateList.index(RawHighestDateListSorted[2])])
# print(RawHighestDateListSorted[2])
# print('')
# print('Rizz')
# print(ListCategories[RawHighestRizzList.index(RawHighestRizzListSorted[0])])
# print(RawHighestLikeListSorted[0])
# print(ListCategories[RawHighestRizzList.index(RawHighestRizzListSorted[1])])
# print(RawHighestRizzListSorted[1])
# print(ListCategories[RawHighestRizzList.index(RawHighestRizzListSorted[2])])
# print(RawHighestRizzListSorted[2])

#Men
# print('For Men')
# Remove Superlative Questions
# for i in range(20):
#     del RawManHighestLikeList[-1]
#     del RawManHighestDateList[-1]
#     del RawManHighestRizzList[-1]

# RawManHighestLikeListSorted=sorted(RawManHighestLikeList, key = float, reverse=True)
# RawManHighestDateListSorted=sorted(RawManHighestDateList, key = float, reverse=True)
# RawManHighestRizzListSorted=sorted(RawManHighestRizzList, key = float, reverse=True)

# print('High Scores')
# print('Likeability')
# print(ListCategories[RawManHighestLikeList.index(RawManHighestLikeListSorted[0])])
# print(RawManHighestLikeListSorted[0])
# print(ListCategories[RawManHighestLikeList.index(RawManHighestLikeListSorted[1])])
# print(RawManHighestLikeListSorted[1])
# print(ListCategories[RawManHighestLikeList.index(RawManHighestLikeListSorted[2])])
# print(RawManHighestLikeListSorted[2])
# print('Dateability')
# print(ListCategories[RawManHighestDateList.index(RawManHighestDateListSorted[0])])
# print(RawManHighestDateListSorted[0])
# print(ListCategories[RawManHighestDateList.index(RawManHighestDateListSorted[1])])
# print(RawManHighestDateListSorted[1])
# print(ListCategories[RawManHighestDateList.index(RawManHighestDateListSorted[2])])
# print(RawManHighestDateListSorted[2])
# print('Rizz')
# print(ListCategories[RawManHighestRizzList.index(RawManHighestRizzListSorted[0])])
# print(RawManHighestLikeListSorted[0])
# print(ListCategories[RawManHighestRizzList.index(RawManHighestRizzListSorted[1])])
# print(RawManHighestRizzListSorted[1])
# print(ListCategories[RawManHighestRizzList.index(RawManHighestRizzListSorted[2])])
# print(RawManHighestRizzListSorted[2])

#Women
print('For Women')
#Remove Superlative Questions
for i in range(20):
    del RawWomanHighestLikeList[-1]
    del RawWomanHighestDateList[-1]
    del RawWomanHighestRizzList[-1]

RawWomanHighestLikeListSorted=sorted(RawWomanHighestLikeList, key = float, reverse=True)
RawWomanHighestDateListSorted=sorted(RawWomanHighestDateList, key = float, reverse=True)
RawWomanHighestRizzListSorted=sorted(RawWomanHighestRizzList, key = float, reverse=True)

print('High Scores')
print('Likeability')
print(ListCategories[RawWomanHighestLikeList.index(RawWomanHighestLikeListSorted[0])])
print(RawWomanHighestLikeListSorted[0])
print(ListCategories[RawWomanHighestLikeList.index(RawWomanHighestLikeListSorted[1])])
print(RawWomanHighestLikeListSorted[1])
print(ListCategories[RawWomanHighestLikeList.index(RawWomanHighestLikeListSorted[2])])
print(RawWomanHighestLikeListSorted[2])
print('Dateability')
print(ListCategories[RawWomanHighestDateList.index(RawWomanHighestDateListSorted[0])])
print(RawWomanHighestDateListSorted[0])
print(ListCategories[RawWomanHighestDateList.index(RawWomanHighestDateListSorted[1])])
print(RawWomanHighestDateListSorted[1])
print(ListCategories[RawWomanHighestDateList.index(RawWomanHighestDateListSorted[2])])
print(RawWomanHighestDateListSorted[2])
print('Rizz')
print(ListCategories[RawWomanHighestRizzList.index(RawWomanHighestRizzListSorted[0])])
print(RawWomanHighestLikeListSorted[0])
print(ListCategories[RawWomanHighestRizzList.index(RawWomanHighestRizzListSorted[1])])
print(RawWomanHighestRizzListSorted[1])
print(ListCategories[RawWomanHighestRizzList.index(RawWomanHighestRizzListSorted[2])])
print(RawWomanHighestRizzListSorted[2])
