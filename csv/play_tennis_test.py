import pickle
filename = '../api/classify/play_tennis.pkl'
model = pickle.load(open(filename, 'rb'))
result =model.predict([[2,1,0,0]])
print(result) 