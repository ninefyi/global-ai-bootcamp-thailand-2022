import pandas as pd
import pickle
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    play_tennis = pd.read_csv('play_tennis.csv')
    print(play_tennis.head())
    number = LabelEncoder()
    play_tennis['outlook'] = number.fit_transform(play_tennis['outlook'])
    play_tennis['temp'] = number.fit_transform(play_tennis['temp'])
    play_tennis['humidity'] = number.fit_transform(play_tennis['humidity'])
    play_tennis['windy'] = number.fit_transform(play_tennis['windy'])
    play_tennis['play'] = number.fit_transform(play_tennis['play'])

    print(play_tennis.head())

    features = ["outlook", "temp", "humidity", "windy"]
    target = "play"

    features_train, features_test, target_train, target_test = train_test_split(play_tennis[features], play_tennis[target], test_size=0.33, random_state=54)

    model = GaussianNB()
    model.fit(features_train, target_train)

    pred = model.predict(features_test)
    accuracy = accuracy_score(target_test, pred)

    print(accuracy)

    filename = '../api/classify/play_tennis.pkl'
    pickle.dump(model, open(filename, 'wb'))

if __name__ == "__main__":
    main()