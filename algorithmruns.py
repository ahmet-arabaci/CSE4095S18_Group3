import pandas as pd
import statistics
import numpy as np

from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_score

ten_fold_list = []

df = pd.read_csv('Document.csv', sep=',', encoding='latin1',
                 names=['id', 'doc_id', 'text', 'class_id', 'chars', 'words'])

ids = df.id.tolist()
users = df.doc_id.tolist()
users = list(set(users))

length_list = []
words_list = []
user_length_list = []
user_words_list = []
class_list = []

counter = 1
user_counter = 0
previous_id = 1
previous_class = -1
for i in range(0, df.shape[0]):

    if i in ids:
        text = df.loc[counter, 'text']
        words = len(text.split())

        user_id = int(df.iloc[counter]['doc_id'])
        class_id = int(df.iloc[counter]['class_id'])
        if previous_class == -1:
            previous_class = class_id

        if previous_id == user_id:
            number_of_char = int(df.iloc[counter]['chars'])
            user_length_list.append(number_of_char)
            word = int(df.iloc[counter]['words'])
            user_words_list.append(word)
        else:
            length_list.append(statistics.mean(user_length_list))
            words_list.append(statistics.mean(user_words_list))
            class_list.append(previous_class)
            user_length_list[:] = []
            number_of_char = int(df.iloc[counter]['chars'])
            user_length_list.append(number_of_char)
            word = int(df.iloc[counter]['words'])
            user_words_list.append(word)

        previous_id = user_id
        previous_class = class_id

    counter += 1
    user_counter += 1

print(length_list)
print(len(length_list))

print(words_list)
print(len(words_list))

print(class_list)
print(len(class_list))
my_dataset = []
temp_list = []

for i in range(0, len(words_list)):
    temp_list.append(length_list[i])
    temp_list.append(words_list[i])
    my_dataset.append([length_list[i], words_list[i]])

my_dataset = np.array(my_dataset)

# fit a k-nearest neighbor model to the data
model = KNeighborsClassifier()
scores = cross_val_score(model, my_dataset, class_list, cv=10, scoring='accuracy')
print("KNN 10 fold Scores: ", scores)
print("KNN 10 fold mean of scores(Accuracy): ", scores.mean(), "\n")
ten_fold_list.append(scores.mean())
model.fit(np.array(my_dataset), class_list)
print("#########################################  KNN  ###################################################")
print(model)
# make predictions
expected = class_list
predicted = model.predict(my_dataset)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))


print("#########################################  NB  ###################################################")

model = GaussianNB()
scores = cross_val_score(model, my_dataset, class_list, cv=10, scoring='accuracy')
print("NB 10 fold Scores: ", scores)
print("NB 10 fold mean of scores(Accuracy): ", scores.mean(), "\n")
ten_fold_list.append(scores.mean())
model.fit(np.array(my_dataset), class_list)

print(model)
# make predictions
expected = class_list
predicted = model.predict(my_dataset)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))


print("#########################################  LR  ###################################################")

model = LogisticRegression()
scores = cross_val_score(model, my_dataset, class_list, cv=10, scoring='accuracy')
print("LR 10 fold Scores: ", scores)
print("LR 10 fold mean of scores(Accuracy): ", scores.mean(), "\n")
ten_fold_list.append(scores.mean())
model.fit(np.array(my_dataset), class_list)
print(model)
# make predictions
expected = class_list
predicted = model.predict(my_dataset)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
