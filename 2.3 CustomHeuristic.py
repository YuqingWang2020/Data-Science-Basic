import numpy
import pandas

def custom_heuristic(file_path):
    prediction = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        if passenger['Sex'] == 'female' and passenger['Pclass'] != 3:
            prediction[passenger_id] = 1
        elif passenger['Age'] < 18 and passenger['Pclass'] != 3:
            prediction[passenger_id] = 1
        elif passenger['Fare'] >= 57:
            prediction[passenger_id] = 1
        elif passenger['Sex'] == 'female' and passenger['Pclass'] == 3 and passenger['Embarked'] != 'S':
            prediction[passenger_id] = 1
        elif passenger['Sex'] == "male" and passenger['Pclass'] == 3 and passenger['Age'] <= 9 and passenger['SibSp'] <= 2:
            prediction[passenger_id] = 1
        else:
            prediction[passenger_id] = 0
    return prediction

#print custom_heuristic("titanic-data.csv")
predictions=custom_heuristic("titanic-data.csv")

df = pandas.read_csv("titanic-data.csv")
df2=pandas.DataFrame({'1':df['Survived'],'2':predictions.values()})
print (sum(df2['1'] == df2['2'])/891)