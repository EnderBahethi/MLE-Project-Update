import numpy as np
from matplotlib import pyplot as plt
import math
import pandas as pd
from collections import Counter 
"""
List of Majors:
Architecture
Architectural Sciences	 	
Building Conservation
Informatics and Architecture
Lighting 	 	 	 
Aeronautical Engineering
Biomedical Engineering
Chemical Engineering
Civil Engineering
Computer and Systems Engineering
Decision Sciences and Engineering Systems
Electric Power Engineering
Electrical Engineering
Engineering Physics
Engineering Science
Environmental Engineering
Industrial and Management Engineering
Manufacturing Systems Engineering
Materials Engineering
Mechanical Engineering
Mechanics
Nuclear Engineering
Operations Research and Statistics
Transportation Engineering	 	 	 	 
Cognitive Science
Communication
Communication and Rhetoric
Ecological Economics
Ecological Economics, Values, and Policy
Economics
Electronic Arts
Electronic Media, Arts, and Communication
Human-Computer Interaction
Philosophy
Psychology
Science, Technology, and Society
Science and Technology Studies
Technical Communication	 	 	 	 	 	 	 	 
Management 	 	 	 	 	 	 
Astronomy
Applied Science
Biology
Biochemistry and Biophysics
Bioinformatics and Molecular Biology
Chemistry
Computer Science
Engineering Principles in Technology Education
Environmental Science
Geology
Hydrogeology
Mathematics
Applied Mathematics
Multidisciplinary Science
Natural Sciences
Physics
Applied Physics
Interdisciplinary Science	 	 	 	 	 	 
Information Technology
Games and Simulation Arts and Sciences
Design, Innovation, and Society
"""
CategoriesFile = open('RizzCategories.txt', 'r')
Categories=CategoriesFile.read()
ListCategories=Categories.split("\n")
for i in range(len(ListCategories)):
    ListCategories[i]=ListCategories[i].strip()
RizzData = pd.read_csv('RizzCalculator171.csv')
def Rizz_Calc(G,P,M):
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
                            plt.scatter([np.average(Likeability)],[np.average(Dateability)])
                    else:
                        print("Insufficient Data")
                        return
                    Superlatives=[]
                    Superlatives.append(input("Are you in a Frat or Sorority? Yes/No: "))         
                    Superlatives.append(input("Do you own Pet(s)? Yes/No: "))
                    Superlatives.append(input("Do you read Books? Yes/No: "))
                    Superlatives.append(input("Do you play Video Games? Yes/No: "))
                    Superlatives.append(input("Are you an Internet Moderator? Yes/No: "))
                    Superlatives.append(input("Do you drive a Truck? Yes/No: "))
                    Superlatives.append(input("Are you a Twitch Streamer? Yes/No: "))
                    Superlatives.append(input("Do you Exercise Regularly? Yes/No: "))
                    Superlatives.append(input("Do you Hygiene Regularly? Yes/No: "))
                    Superlatives.append(input("Do you play an Instrument? Yes/No: "))
                    Superlatives.append(input("Do you play an Sport? Yes/No: "))
                    Superlatives.append(input("Do you watch Anime? Yes/No: "))
                    Superlatives.append(input("Do you enjoy Spicy Food? Yes/No: "))
                    Superlatives.append(input("Do you read Comics? Yes/No: "))
                    Superlatives.append(input("Do you use Twitter? Yes/No: "))
                    Superlatives.append(input("Are you Goth? Yes/No: "))
                    Superlatives.append(input("Are you a Youtuber? Yes/No: "))
                    Superlatives.append(input("Are you Funny? Yes/No: "))
                    Superlatives.append(input("Do you readily Apply Information? Yes/No: "))
                    Superlatives.append(input("Do you enjoy the Outdoors? Yes/No: ")) 
                    for j in range(len(Superlatives)):
                        if Superlatives[j] == "Yes":
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
                                print("Insufficient Data")
                                return
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
                    print("Likeability: ", sum(Likeability))
                    if P != "None":
                        print("Dateability: ", sum(Dateability))
                        plt.scatter([sum(Likeability)],[sum(Dateability)])
                        plt.xlim(0,10)
                        plt.ylim(0,10)
                        plt.xlabel("Likeability")
                        plt.ylabel("Dateability")
                        plt.legend(["Standard Rizz", "Your Rizz"])
                        plt.show()
                    print("Rizz:        ", sum(Rizz))
                    print("Which Major likes you the most:  ", Counter(AttractedMajors).most_common()[0][0])
                    print("Which Major likes you the least: ", Counter(UnattractedMajors).most_common()[0][0])
                    return
                else:
                    print("Insufficient Data") 
                    return
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
                        plt.scatter([np.average(Likeability)],[np.average(Dateability)])  
                else:
                    print("Insufficient Data")
                    return
                Superlatives=[]
                Superlatives.append(input("Are you in a Frat or Sorority? Yes/No: "))         
                Superlatives.append(input("Do you own Pet(s)? Yes/No: "))
                Superlatives.append(input("Do you read Books? Yes/No: "))
                Superlatives.append(input("Do you play Video Games? Yes/No: "))
                Superlatives.append(input("Are you an Internet Moderator? Yes/No: "))
                Superlatives.append(input("Do you drive a Truck? Yes/No: "))
                Superlatives.append(input("Are you a Twitch Streamer? Yes/No: "))
                Superlatives.append(input("Do you Exercise Regularly? Yes/No: "))
                Superlatives.append(input("Do you Hygiene Regularly? Yes/No: "))
                Superlatives.append(input("Do you play an Instrument? Yes/No: "))
                Superlatives.append(input("Do you play an Sport? Yes/No: "))
                Superlatives.append(input("Do you watch Anime? Yes/No: "))
                Superlatives.append(input("Do you enjoy Spicy Food? Yes/No: "))
                Superlatives.append(input("Do you read Comics? Yes/No: "))
                Superlatives.append(input("Do you use Twitter? Yes/No: "))
                Superlatives.append(input("Are you Goth? Yes/No: "))
                Superlatives.append(input("Are you a Youtuber? Yes/No: "))
                Superlatives.append(input("Are you Funny? Yes/No: "))
                Superlatives.append(input("Do you readily Apply Information? Yes/No: "))
                Superlatives.append(input("Do you enjoy the Outdoors? Yes/No: "))     
                for j in range(len(Superlatives)):
                    if Superlatives[j] == "Yes":
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
                            print("Insufficient Data")
                            return               
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
                print("Likeability: ", sum(Likeability))
                if P != "None":
                    print("Dateability: ", sum(Dateability))
                    plt.scatter([sum(Likeability)],[sum(Dateability)])
                    plt.xlim(0,10)
                    plt.ylim(0,10)
                    plt.xlabel("Likeability")
                    plt.ylabel("Dateability")
                    plt.legend(["Standard Rizz", "Your Rizz"])
                    plt.show()
                print("Rizz:        ", sum(Rizz))
                print("Which Major likes you the most:  ", Counter(AttractedMajors).most_common()[0][0])
                print("Which Major likes you the least: ", Counter(UnattractedMajors).most_common()[0][0])
                return
            else:
                print("Input Valid Field(s) of Study")
                return
        else:
            print("Input Valid Preference")
            return
    else:
        print('Input Valid Gender')
        return