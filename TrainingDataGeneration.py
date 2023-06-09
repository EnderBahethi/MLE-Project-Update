import math
import pandas as pd
from collections import Counter 
import csv
import random
from matplotlib import pyplot as plt

CategoriesFile = open('RizzCategories.txt', 'r')
Categories=CategoriesFile.read()
ListCategories=Categories.split("\n")

for i in range(len(ListCategories)):
    ListCategories[i]=ListCategories[i].strip()

RizzData = pd.read_csv('RizzCalculator171.csv')

def Rizz_Train(G,P,M,Superlatives):
    if G=="Man" or G=="Woman" or G=="Non-Binary":
        if P=="Man" or P=="Woman" or P=="Non-Binary" or P=="Bi-Sexual" or P=="None":
            if type(M) == list:
                for i in range(len(M)):
                    if M[i] in ListCategories and ListCategories.index(M[i])<60:
                        pass
                    else:
                        print("Input Valid Field(s) of Study")
                        return
                Dateability=[]
                Likeability=[]
                OpinionWeights=[]
                AttractedMajors=[]
                UnattractedMajors=[]
                for i in range(len(M)):
                    a=ListCategories.index(M[i])
                    b=5+a*3
                
                    LikeCounter=0
                    DateCounter=0
                    LikeTotal=0
                    DateTotal=0
                    OpinionCounter=0
                    if P=="Bi-Sexual":
                        for i in range(RizzData.shape[0]):
                            if (RizzData.iat[i,1]== "Man" or "Woman") and RizzData.iat[i,2]== G:
                                if RizzData.iat[i,b-1] =="Yes":
                                    OpinionCounter=OpinionCounter+1
                                    if math.isnan(RizzData.iat[i,b]) == False and RizzData.iat[i,b]>5 and math.isnan(RizzData.iat[i,b+1]) == False and RizzData.iat[i,b+1]>5: 
                                        AttractedMajors.append(RizzData.iat[i,3])
                                    elif math.isnan(RizzData.iat[i,b]) == False and RizzData.iat[i,b]<=5 and math.isnan(RizzData.iat[i,b+1]) == False and RizzData.iat[i,b+1]<=5: 
                                        UnattractedMajors.append(RizzData.iat[i,3])
                                    if math.isnan(RizzData.iat[i,b]) == False:
                                        LikeCounter=LikeCounter+1
                                        LikeTotal=LikeTotal+RizzData.iat[i,b]
                                    if math.isnan(RizzData.iat[i,b+1]) == False:
                                        DateCounter=DateCounter+1
                                        DateTotal=DateTotal+RizzData.iat[i,b+1]
                    elif P=="None":
                        for i in range(RizzData.shape[0]):
                            if RizzData.iat[i,2]== G:
                                if RizzData.iat[i,b-1] =="Yes":
                                    OpinionCounter=OpinionCounter+1
                                    if math.isnan(RizzData.iat[i,b]) == False and RizzData.iat[i,b]>5 and math.isnan(RizzData.iat[i,b+1]) == False and RizzData.iat[i,b+1]>5: 
                                        AttractedMajors.append(RizzData.iat[i,3])
                                    elif math.isnan(RizzData.iat[i,b]) == False and RizzData.iat[i,b]<=5 and math.isnan(RizzData.iat[i,b+1]) == False and RizzData.iat[i,b+1]<=5: 
                                        UnattractedMajors.append(RizzData.iat[i,3])
                                    if math.isnan(RizzData.iat[i,b]) == False:
                                        LikeCounter=LikeCounter+1
                                        LikeTotal=LikeTotal+RizzData.iat[i,b]
                    else:
                        for i in range(RizzData.shape[0]):
                            if RizzData.iat[i,1]== P and RizzData.iat[i,2]== G:
                                if RizzData.iat[i,b-1] =="Yes":
                                    OpinionCounter=OpinionCounter+1
                                    if math.isnan(RizzData.iat[i,b]) == False and RizzData.iat[i,b]>5 and math.isnan(RizzData.iat[i,b+1]) == False and RizzData.iat[i,b+1]>5: 
                                        AttractedMajors.append(RizzData.iat[i,3])
                                    elif math.isnan(RizzData.iat[i,b]) == False and RizzData.iat[i,b]<=5 and math.isnan(RizzData.iat[i,b+1]) == False and RizzData.iat[i,b+1]<=5: 
                                        UnattractedMajors.append(RizzData.iat[i,3])
                                    if math.isnan(RizzData.iat[i,b]) == False:
                                        LikeCounter=LikeCounter+1
                                        LikeTotal=LikeTotal+RizzData.iat[i,b]
                                    if math.isnan(RizzData.iat[i,b+1]) == False:
                                        DateCounter=DateCounter+1
                                        DateTotal=DateTotal+RizzData.iat[i,b+1]
                                    
                    if LikeCounter != 0:
                    
                        Likeability.append(LikeTotal/LikeCounter)
                        OpinionWeights.append(OpinionCounter/RizzData.shape[0])
                        
                        if P != "None":
                            Dateability.append(DateTotal/DateCounter)
                            
                    else:
                        return "Insufficient Data"
                    
                    for j in range(len(Superlatives)):
                        if Superlatives[j] == 1:
                            b=RizzData.shape[1]-59+(j*3)
                            LikeCounter=0
                            DateCounter=0
                            LikeTotal=0
                            DateTotal=0
                            OpinionCounter=0
                            if P=="Bi-Sexual":
                                for i in range(RizzData.shape[0]):
                                    if (RizzData.iat[i,1]== "Man" or "Woman") and RizzData.iat[i,2]== G:
                                        if RizzData.iat[i,b-1] =="Yes":
                                            OpinionCounter=OpinionCounter+1
                                            if math.isnan(RizzData.iat[i,b]) == False:
                                                LikeCounter=LikeCounter+1
                                                LikeTotal=LikeTotal+RizzData.iat[i,b]
                                            if math.isnan(RizzData.iat[i,b+1]) == False:
                                                DateCounter=DateCounter+1
                                                DateTotal=DateTotal+RizzData.iat[i,b+1]
                            elif P=="None":
                                for i in range(RizzData.shape[0]):
                                    if RizzData.iat[i,2]== G:
                                        if RizzData.iat[i,b-1] =="Yes":
                                            OpinionCounter=OpinionCounter+1
                                            if math.isnan(RizzData.iat[i,b]) == False:
                                                LikeCounter=LikeCounter+1
                                                LikeTotal=LikeTotal+RizzData.iat[i,b]
                            else:
                                for i in range(RizzData.shape[0]):
                                    if RizzData.iat[i,1]== P and RizzData.iat[i,2]== G:
                                        if RizzData.iat[i,b-1] =="Yes":
                                            OpinionCounter=OpinionCounter+1
                                            if math.isnan(RizzData.iat[i,b]) == False:
                                                LikeCounter=LikeCounter+1
                                                LikeTotal=LikeTotal+RizzData.iat[i,b]
                                            if math.isnan(RizzData.iat[i,b+1]) == False:
                                                DateCounter=DateCounter+1
                                                DateTotal=DateTotal+RizzData.iat[i,b+1]            
                            
                            if LikeCounter != 0:
                                
                                Likeability.append(LikeTotal/LikeCounter)
                                OpinionWeights.append(OpinionCounter/RizzData.shape[0])
                                
                                if P != "None":
                                    Dateability.append(DateTotal/DateCounter)
                            else:
                                return "Insufficient Data"
                    
                    Rizz=[]
                    OpinionWeightsTotal=sum(OpinionWeights)
                    for i in range(len(OpinionWeights)):
                        OpinionWeights[i]=(OpinionWeights[i]/OpinionWeightsTotal)
                        Likeability[i]=Likeability[i]*OpinionWeights[i]
                        if P=="None":
                            Rizz.append((Likeability[i]/2))
                        else:
                            Dateability[i]=Dateability[i]*OpinionWeights[i]
                            Rizz.append((Likeability[i]/2)+(Dateability[i]/2))
                    if len(AttractedMajors)==0:
                        AttractedMajors.append("None")
                        
                        

                    
                    return sum(Rizz), Counter(AttractedMajors).most_common()[0][0]
                    
                else:
                    return "Insufficient Data"
            elif M in ListCategories and ListCategories.index(M)<60:
                a=ListCategories.index(M)    
                b=5+a*3
                LikeCounter=0
                DateCounter=0
                LikeTotal=0
                DateTotal=0
                OpinionCounter=0
                AttractedMajors=[]
                UnattractedMajors=[]
                if P=="Bi-Sexual":
                    for i in range(RizzData.shape[0]):
                        if (RizzData.iat[i,1]== "Man" or "Woman") and RizzData.iat[i,2]== G:
                            if RizzData.iat[i,b-1] =="Yes":
                                OpinionCounter=OpinionCounter+1
                                if math.isnan(RizzData.iat[i,b]) == False and RizzData.iat[i,b]>5 and math.isnan(RizzData.iat[i,b+1]) == False and RizzData.iat[i,b+1]>5: 
                                    AttractedMajors.append(RizzData.iat[i,3])
                                elif math.isnan(RizzData.iat[i,b]) == False and RizzData.iat[i,b]<=5 and math.isnan(RizzData.iat[i,b+1]) == False and RizzData.iat[i,b+1]<=5: 
                                    UnattractedMajors.append(RizzData.iat[i,3])
                                if math.isnan(RizzData.iat[i,b]) == False:
                                    LikeCounter=LikeCounter+1
                                    LikeTotal=LikeTotal+RizzData.iat[i,b]
                                if math.isnan(RizzData.iat[i,b+1]) == False:
                                    DateCounter=DateCounter+1
                                    DateTotal=DateTotal+RizzData.iat[i,b+1]
                elif P=="None":
                    for i in range(RizzData.shape[0]):
                        if RizzData.iat[i,2]== G:
                            if RizzData.iat[i,b-1] =="Yes":
                                OpinionCounter=OpinionCounter+1
                                if math.isnan(RizzData.iat[i,b]) == False and RizzData.iat[i,b]>5 and math.isnan(RizzData.iat[i,b+1]) == False and RizzData.iat[i,b+1]>5: 
                                    AttractedMajors.append(RizzData.iat[i,3])
                                elif math.isnan(RizzData.iat[i,b]) == False and RizzData.iat[i,b]<=5 and math.isnan(RizzData.iat[i,b+1]) == False and RizzData.iat[i,b+1]<=5: 
                                    UnattractedMajors.append(RizzData.iat[i,3])
                                if math.isnan(RizzData.iat[i,b]) == False:
                                    LikeCounter=LikeCounter+1
                                    LikeTotal=LikeTotal+RizzData.iat[i,b]
                else:
                    for i in range(RizzData.shape[0]):
                        if RizzData.iat[i,1]== P and RizzData.iat[i,2]== G:
                            if RizzData.iat[i,b-1] == "Yes":
                                OpinionCounter=OpinionCounter+1
                                if math.isnan(RizzData.iat[i,b]) == False and RizzData.iat[i,b]>5 and math.isnan(RizzData.iat[i,b+1]) == False and RizzData.iat[i,b+1]>5: 
                                    AttractedMajors.append(RizzData.iat[i,3])
                                elif math.isnan(RizzData.iat[i,b]) == False and RizzData.iat[i,b]<=5 and math.isnan(RizzData.iat[i,b+1]) == False and RizzData.iat[i,b+1]<=5: 
                                    UnattractedMajors.append(RizzData.iat[i,3])
                                if math.isnan(RizzData.iat[i,b]) == False:
                                    LikeCounter=LikeCounter+1
                                    LikeTotal=LikeTotal+RizzData.iat[i,b]
                                if math.isnan(RizzData.iat[i,b+1]) == False:
                                    DateCounter=DateCounter+1
                                    DateTotal=DateTotal+RizzData.iat[i,b+1]
                
                if LikeCounter != 0:
                    
                    Likeability=[LikeTotal/LikeCounter]
                    OpinionWeights=[OpinionCounter/RizzData.shape[0]]
                    if P != "None":
                        Dateability=[DateTotal/DateCounter]
                        
                else:
                    return "Insufficient Data"
                    
                
                for j in range(len(Superlatives)):
                    if Superlatives[j] == 1:
                        b=RizzData.shape[1]-59+(j*3)
                        LikeCounter=0
                        DateCounter=0
                        LikeTotal=0
                        DateTotal=0
                        if P=="Bi-Sexual":
                            for i in range(RizzData.shape[0]):
                                if (RizzData.iat[i,1]== "Man" or "Woman") and RizzData.iat[i,2]== G:
                                    if RizzData.iat[i,b-1] =="Yes":
                                        OpinionCounter=OpinionCounter+1
                                        if math.isnan(RizzData.iat[i,b]) == False:
                                            LikeCounter=LikeCounter+1
                                            LikeTotal=LikeTotal+RizzData.iat[i,b]
                                        if math.isnan(RizzData.iat[i,b+1]) == False:
                                            DateCounter=DateCounter+1
                                            DateTotal=DateTotal+RizzData.iat[i,b+1]
                        elif P=="None":
                            for i in range(RizzData.shape[0]):
                                if RizzData.iat[i,2]== G:
                                    if RizzData.iat[i,b-1] =="Yes":
                                        OpinionCounter=OpinionCounter+1
                                        if math.isnan(RizzData.iat[i,b]) == False:
                                            LikeCounter=LikeCounter+1
                                            LikeTotal=LikeTotal+RizzData.iat[i,b]
                        else:
                            for i in range(RizzData.shape[0]):
                                if RizzData.iat[i,1]== P and RizzData.iat[i,2]== G:
                                    if RizzData.iat[i,b-1] =="Yes":
                                        OpinionCounter=OpinionCounter+1
                                        if math.isnan(RizzData.iat[i,b]) == False:
                                            LikeCounter=LikeCounter+1
                                            LikeTotal=LikeTotal+RizzData.iat[i,b]
                                        if math.isnan(RizzData.iat[i,b+1]) == False:
                                            DateCounter=DateCounter+1
                                            DateTotal=DateTotal+RizzData.iat[i,b+1]            
                                
                        if LikeCounter != 0:
                            Likeability.append(LikeTotal/LikeCounter)
                            OpinionWeights.append(OpinionCounter/RizzData.shape[0])
                            if P != "None":
                                Dateability.append(DateTotal/DateCounter)
                        else:
                            return "Insufficient Data"
                        
                OpinionWeightsTotal=sum(OpinionWeights)
                Rizz=[]
                for i in range(len(OpinionWeights)):
                    OpinionWeights[i]=(OpinionWeights[i]/OpinionWeightsTotal)
                    Likeability[i]=Likeability[i]*OpinionWeights[i]
                    if P=="None":
                        Rizz.append((Likeability[i]/2))
                    else:
                        Dateability[i]=Dateability[i]*OpinionWeights[i]
                        Rizz.append((Likeability[i]/2)+(Dateability[i]/2))
                if len(AttractedMajors)==0:
                    AttractedMajors.append("None")
                
                # plt.scatter([sum(Likeability)],[sum(Dateability)])
                # plt.xlim(0,10)
                # plt.ylim(0,10)
                # plt.xlabel("Likeability")
                # plt.ylabel("Dateability")
                
                return sum(Rizz), Counter(AttractedMajors).most_common()[0][0]
                
            else:
                print("Input Valid Field(s) of Study")
                return
        else:
            print("Input Valid Preference")
            return
    else:
        print('Input Valid Gender')
        return 
    
TrainingDataInputs=[]
TrainingDataAnswers=[]   
Genders=["Man","Woman"] 
Preferences=["Man","Woman","Bi-Sexual"]

import time
for i in range(1):
  st = time.time()
  while len(TrainingDataInputs)!=10000*(i+1):
    A=random.randint(0,1)
    B=random.randint(0,2)
    C=random.randint(0,59)
    D=random.randint(0,1)
    E=random.randint(0,59)
    F=[]
    for j in range(20):
        F.append(random.randint(0,1)) 
    A=Genders[A]
    B=Preferences[B]
    C=ListCategories[C]
    if D==1:
        C=[C,ListCategories[E]]
    if Rizz_Train(A,B,C,F)!="Insufficient Data":
        TrainingDataInputs.append([A,B,C,F])
        TrainingDataAnswers.append(Rizz_Train(A,B,C,F))
  et = time.time()    
  elapsed_time = et - st
  print('Execution time:', elapsed_time, 'seconds')


                plt.show()  
    
with open('TrainingDataInputs.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    if file.tell() == 0:
        writer.writerow(['Gender', 'Preference', 'Categories', 'Superlatives'])
    for input_data in TrainingDataInputs:
        writer.writerow(input_data)

with open('TrainingDataAnswers.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    if file.tell() == 0:
        writer.writerow(['Rizz','Most Attracted Major'])
    for output_data in TrainingDataAnswers:
        writer.writerow(output_data)