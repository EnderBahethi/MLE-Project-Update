The Rizz Calculator Function works as follows.

Use the Rizz Calculator Function in order to calculate your Rizz.
It accepts Your Gender (Out of "Man" , "Woman" , "Non-Binary")
Your Primary Preference (Out of "Man" , "Woman" , "Non-Binary" , "Bi-Sexual" , "None")
If "None" is selected the function does not produce a Like/Date Graph and does not calculate a Dateability score.
If "None" is selected your Likeability and Rizz will be calculated to be the same number.
If “None” is selected your Likeability and Rizz will be calculated using all Genders

and Your Major (Out of the list of Majors within the RizzCalculatorMLEProject.py file or RizzCategories.txt file)
Your Major can be inputted as a list in which case each major’s Rizz will be calculated separately and added to the total.

Rizz Calculation first removes all of the responses that are not from the Primary Preference Gender towards the Gender of the User. It then goes to the responses of the User’s Major and calculates the average of the Likeability and Dateability Scores and averages them to get a Rizz Score for the Major. It then creates a Preliminary Opinion Weight by gathering the total number of responses by the number of responses that had opinions on that major. It repeats this for every Superlative Question that is answered and then multiplies the Likeability and Dateability Scores for by the Normalized Opinion Weight. What this means is that if more respondents had an opinion the average of those answers (Likeability, Dateability) values more. Then the Weighted Likeability and Weighted Dateability Scores are summed (the Rizz is calculated from the average of those values) resulting in the Users Rizz. The function will spit out a Like/Date Graph of the User’s Rizz compared to the Rizz of just the User’s Major without Superlative answer.

Issues:
Due to lack of data Selecting Non-Binary for Gender and or Primary Preference may result in a "Insufficient Data" error.

You can use the DataStats.txt to see the Raw Likeability, Dateability, and Rizz of each Major and Superlative Question.
