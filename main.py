import pandas as pd

#data = pandas.read_csv("weather_data .csv")
# print(data['temp'])
#
# temp_list = data['temp'].to_list()
# print(temp_list)
# total = 0
# count =0
# for item in temp_list:
#     total+= item
#     count +=1
#
# average = round(total/count, 2)
# print(f"Average of the temperature is {average}")
# print(data['temp'].max())
# print(data['temp'].min())

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp*1.8+32
# print(monday_temp)

#data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#print(data)
# fur_color = data['Primary Fur Color']
# gray = 0
# Cinnamon =0
# black =0
# for color in fur_color:
#     if color == "Gray":
#         gray+=1
#     elif color == "Cinnamon":
#         Cinnamon+=1
#     else:
#         black +=1

#print(f"grey = {gray}\n Cinnamon = {Cinnamon}\n black ={black}")
result = []
total = 0

student_data = {"student": ['Anshika', 'Archit Gupta','Divyanshi','Drishya','Himanshu Aggarwal',
                            'Ichha','Imran Khan','Ishaan','Japesh Wason','Khyati Daksha','Kshit Sharma',
                            'Manas Saluja','Manya','Niharika','Pragya','Prisha','Priyanka','Raghav Gpyal',
                            'Sanskar','Sarthak','Satvik','Shivam Sharma','Shivam Grover','Shivam Kashyap',
                            'Simran Khanna','Shudhanshu','Sumera','Utsav','Vinayak','Vrati','Prakarti',
                            'Ananya','Arohi','Badal','Bhumika','Chaitanya','Chirag','Deepakar','Deepesh',
                            'Drishti','Garima','Hardik','Harshit','Jishnu','Khushi','Lucky Roy','Nehal Nagpal',
                            'Nikhil','Nishant','Pankaj','Pranav','Rishabh Gupta','Riya','Rohit Singh','Sagar Dabas',
                            'Shruti','Tanmay','Udit Gupta','Yash','Yatharth'],

                "CGPA":[6,7,6,7,8,8,9,7,8,6,
                        7,8,9,6,8,9,7,8,9,8,
                        7,7,8,7,8,7,8,9,9,7,
                        6,7,9,6,7,9,9,6,8,7,
                        8,9,7,9,6,9,7,6,8,7,
                        7,8,8,9,6,8,6,8,8,7],

                "Communication Skills":[6,5,7,3,4,5,7,3,9,2,
                                        1,6,8,9,4,5,6,3,2,6,
                                        7,8,2,6,3,5,6,7,3,7,
                                        8,9,2,1,4,6,8,9,5,6,
                                        3,4,6,7,2,4,3,2,4,2,
                                        3,6,7,8,8,4,6,9,2,3],

                "Problem-Solving Ability":[2,4,5,6,7,8,8,2,4,5,
                                           6,7,8,9,2,4,5,6,7,8,
                                           1,3,5,6,7,8,9,3,2,4,
                                           3,2,4,3,3,4,7,7,8,4,
                                           5,6,7,3,4,3,2,4,5,6,
                                           6,7,8,9,3,5,6,5,4,6],

                "Adaptability":[1,2,4,6,3,4,6,7,8,8,
                                9,4,6,3,2,4,5,3,4,7,
                                8,5,4,3,2,4,2,1,3,4,
                                3,6,7,4,6,3,2,6,8,9,
                                8,7,6,8,7,3,5,4,6,3,
                                6,2,5,3,1,3,2,3,1,3],

                "Technical Knowledge":[8,9,7,6,7,8,9,5,4,2,
                                       5,3,2,2,3,4,5,3,2,1,
                                       2,1,3,4,2,3,1,5,6,7,
                                       8,4,3,2,3,4,5,3,2,4,
                                       6,7,4,3,5,3,6,3,2,1,
                                       3,3,1,2,5,6,5,6,7,4],

                "Teamwork and Collaboration":[1,2,3,4,2,3,1,3,2,3,
                                              5,4,5,2,3,5,6,6,3,7,
                                              8,9,6,8,8,9,6,8,9,5,
                                              7,4,2,4,5,6,7,7,8,9,
                                              5,7,3,3,4,2,4,5,3,2,
                                              3,4,6,6,3,2,1,6,7,7],

                "Enthusiasm and Motivation":[2,3,1,2,3,4,2,4,5,6,
                                             7,5,6,7,8,9,4,5,7,3,
                                             6,3,5,2,5,3,5,2,5,7,
                                             8,6,8,9,4,6,7,8,9,5,
                                             6,7,8,4,6,7,8,4,6,7,
                                             8,4,2,2,6,6,7,3,4,1],
                "Learning Ability":[3,4,2,8,9,8,9,8,9,7,
                                    9,7,9,6,5,7,4,7,4,7,
                                    4,7,8,7,8,5,5,4,4,6,
                                    8,3,7,3,7,3,8,8,8,8,
                                    7,9,6,8,9,5,7,5,7,8,
                                    8,3,7,4,3,3,2,5,2,6],
                "Attention to Detail":[9,8,9,8,9,7,6,8,6,9,
                                        6,8,9,5,7,8,4,8,5,2,
                                        6,8,5,8,3,3,6,3,7,4,
                                        1,4,5,2,5,5,4,3,5,3,
                                        5,3,6,2,3,2,1,1,3,2,
                                        1,3,4,3,2,3,2,4,6,6],
                "Confidence":[6,7,8,9,6,8,5,8,9,4,
                              5,6,7,4,7,8,9,9,3,5,
                              3,6,3,6,7,8,5,8,4,8,
                              7,3,6,4,3,3,6,8,6,3,
                              2,6,4,5,3,5,2,5,1,4,
                              2,1,1,2,3,3,4,5,2,4],


                }


df = pd.DataFrame(student_data, columns=['student',
                                         'CGPA',
                                         'Communication Skills',
                                         'Problem-Solving Ability',
                                         'Adaptability',
                                         'Technical Knowledge',
                                         'Teamwork and Collaboration',
                                         'Enthusiasm and Motivation',
                                         'Learning Ability',
                                         'Attention to Detail',
                                         'Confidence'])


#df.to_csv('student_data.csv')
#print("Given Dataframe :\n", df)

#print("\nIterating over rows using index attribute :\n")

# iterate through each row and select
# 'Name' and 'Stream' column respectively.
for i in df.index:
    total = (df['CGPA'][i]+
    df['Communication Skills'][i]+
        df['Problem-Solving Ability'][i]+
        df['Adaptability'][i]+
        df['Technical Knowledge'][i]+
        df['Teamwork and Collaboration'][i]+
        df['Enthusiasm and Motivation'][i]+
        df['Learning Ability'][i]+
        df['Attention to Detail'][i]+
        df['Confidence'][i])
    #print(total)

    if total/10 >= 6.5:
        result.append("Yes")
    elif((5.5 <= total/10 <=6.5) &
           (df['Technical Knowledge'][i]> 7) &
           (df['Problem-Solving Ability'][i] > 7)):
         result.append("Yes")
    elif((4.5 < total/10 < 5.5) &
          (df['Technical Knowledge'][i] > 7) &
          (df['Problem-Solving Ability'][i] > 6) &
          (df['Enthusiasm and Motivation'][i] > 7)):
         result.append("Yes")
    else:
        result.append("No")
#print(result)
# for item in result:
#
#     df.insert(11, "Result", item, True)
#df['Result'] = result
df.loc[:, "Result"] = result

#print(df)

df.to_csv('student_data.csv')
#print(df['Result'].value_counts()['Yes'])
