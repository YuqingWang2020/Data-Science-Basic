"""
Date: 17.09.2021
iterrows()对dataframe进行遍历
df = pandas.read_csv(file_path)
predictions=right number/total number
values() only show content in dic, no title
"""
import numpy
import pandas
import statsmodels.api as sm

#class Solution:

predictions = {}
df = pandas.read_csv("titanic-data.csv", encoding = 'UTF-8')

for passenger_index, passenger in df.iterrows():
    passenger_id = passenger['PassengerId']

    # For example, let's assume that if the passenger
    # is a female, then the passenger survived.
    if passenger['Sex'] == 'male':
        predictions[passenger_id] = 0
    else:
        predictions[passenger_id] =1
print (predictions)

    #simple_heuristic(r'C:\Users\User\PycharmProjects\pythonProject1\venv\Scripts\titanic-data.csv')
    #a=Solution()
    #print(a.simple_heuristic(r'C:\Users\User\PycharmProjects\pythonProject1\venv\Scripts\titanic-data.csv'))
df2 = pandas.DataFrame({'1': df['Survived'], '2': predictions.values()})
print(sum(df2['1'] == df2['2']) / 891.0) #891 passengers