import pandas as pd
import statistics
from collections import Counter
import matplotlib.pyplot as plt

Document = pd.read_excel('Document.xlsx')
Class = pd.read_excel('Class.xlsx')
Document_Token = pd.read_excel('DocumentTokens.xlsx')

# FOR DOCUMENT FILE
# hold ID's of users
user_list = []
bekar_user_list = []
evli_user_list = []
cocuklu_user_list = []

# text = tweets && hold number of characters for each tweet
length_of_text = []
length_of_bekar_text = []
length_of_evli_text = []
length_of_cocuklu_text = []

for x in range(len(Document["text"])):
    # user_list
    if Document["doc_id"][x] not in user_list:
        user_list.append(Document["doc_id"][x])

    if Document["class_id"][x] == 1:
        length_of_bekar_text.append(len(Document["text"][x]))
        if Document["doc_id"][x] not in bekar_user_list:
            bekar_user_list.append(Document["doc_id"][x])
    elif Document["class_id"][x] == 2:
        length_of_evli_text.append(len(Document["text"][x]))
        if Document["doc_id"][x] not in evli_user_list:
            evli_user_list.append(Document["doc_id"][x])
    else:
        length_of_cocuklu_text.append(len(Document["text"][x]))
        if Document["doc_id"][x] not in cocuklu_user_list:
            cocuklu_user_list.append(Document["doc_id"][x])

        length_of_text.append(len(Document["text"][x]))

# 1 - a,b,c
print("Total number of tweets:", len(Document["text"]), "\nAverage number of characters = ", statistics.mean(length_of_text), "\nStandard Deviation of characters = ", statistics.stdev(length_of_text), "\n")

# 2 - a,b,c
print("Total number of tweets of 'BEKAR':", len(length_of_bekar_text), "\nAverage number of characters = ", statistics.mean(length_of_bekar_text), "\nStandard Deviation of characters = ", statistics.stdev(length_of_bekar_text), "\n")
print("Total number of tweets of 'EVLİ':", len(length_of_evli_text), "\nAverage number of characters = ", statistics.mean(length_of_evli_text), "\nStandard Deviation of characters = ", statistics.stdev(length_of_evli_text), "\n")
print("Total number of tweets of 'ÇOCUKLU':", len(length_of_cocuklu_text), "\nAverage number of characters = ", statistics.mean(length_of_cocuklu_text), "\nStandard Deviation of characters = ", statistics.stdev(length_of_cocuklu_text), "\n")

# Total users and users for each class
print("\nTotal number of users:", len(user_list))
print("Total number of 'BEKAR' users:", len(bekar_user_list))
print("Total number of 'EVLİ' users:", len(evli_user_list))
print("Total number of 'ÇOCUKLU' users:", len(cocuklu_user_list), "\n\n")

# draws pie chart for distribution of users
labels = 'BEKAR', 'EVLİ', 'ÇOCUKLU'
rates = [len(bekar_user_list), len(evli_user_list), len(cocuklu_user_list)]
plt.pie(rates, labels=labels, autopct='%1.1f%%', shadow=False)
plt.show()

# FOR DOCUMENT TOKEN FILE
length_token_text = []
# hold length of tweet in words
length_tweet = []
length_bekar_tweet = []
length_evli_tweet = []
length_cocuklu_tweet = []
previous_id = 1
length_value = 0
# tokens for each class
bekar_tokens = []
evli_tokens = []
cocuklu_tokens = []

less_from_five = []
less_from_five_bekar = []
less_from_five_evli = []
less_from_five_cocuklu = []


for x in range(len(Document_Token["token_text"])):

    # lists of words which are less than five characters
    if len(Document_Token["token_text"][x]) < 5:
        less_from_five.append(Document_Token["token_text"][x])
        if Document_Token["c_id"][x] == 1:
            less_from_five_bekar.append(Document_Token["token_text"][x])
        elif Document_Token["c_id"][x] == 2:
            less_from_five_evli.append(Document_Token["token_text"][x])
        else:
            less_from_five_cocuklu.append(Document_Token["token_text"][x])

    # lists of all words for each class
    if Document_Token["c_id"][x] == 1:
        bekar_tokens.append(Document_Token["token_text"][x])
    elif Document_Token["c_id"][x] == 2:
        evli_tokens.append(Document_Token["token_text"][x])
    else:
        cocuklu_tokens.append(Document_Token["token_text"][x])

    # lists of length of tweets for whole dataset and each class
    current_id = Document_Token["tweet_id"][x]
    if current_id == previous_id:
        length_value += 1
        previous_id = current_id
    else:
        length_tweet.append(length_value)
        if Document_Token["c_id"][x - 1] == 1:
            length_bekar_tweet.append(length_value)
        elif Document_Token["c_id"][x - 1] == 2:
            length_evli_tweet.append(length_value)
        else:
            length_cocuklu_tweet.append(length_value)
        length_value = 0
        previous_id = Document_Token["tweet_id"][x]
        length_value += 1

    if x == len(Document_Token["token_text"]) - 1:
        length_tweet.append(length_value)
        if Document_Token["c_id"][x - 1] == 1:
            length_bekar_tweet.append(length_value)
        elif Document_Token["c_id"][x - 1] == 2:
            length_evli_tweet.append(length_value)
        else:
            length_cocuklu_tweet.append(length_value)
        length_value = 0

    # list of length of tokens in characters
    length_token_text.append(len(Document_Token["token_text"][x]))

# Total number of tokens for whole dataset and mean and std dev of lengths
print("Total number of tokens:", len(Document_Token["token_text"]), "\nAverage number of characters = ", statistics.mean(length_token_text), "\nStandard Deviation of characters = ", statistics.stdev(length_token_text), "\n")

# 1 - d,e
print("Total number of tweets in words:", len(length_tweet), "\nAverage number of words for a tweet = ", statistics.mean(length_tweet), "\nStandard Deviation of words for a tweet = ", statistics.stdev(length_tweet), "\n")

# 2 - d,e
print("Total number of 'BEKAR' tweets in words:", len(length_bekar_tweet), "\nAverage number of words for a tweet = ", statistics.mean(length_bekar_tweet), "\nStandard Deviation of words for a tweet = ", statistics.stdev(length_bekar_tweet), "\n")
print("Total number of 'EVLİ' tweets in words:", len(length_evli_tweet), "\nAverage number of words for a tweet = ", statistics.mean(length_evli_tweet), "\nStandard Deviation of words for a tweet = ", statistics.stdev(length_evli_tweet), "\n")
print("Total number of 'ÇOCUKLU' tweets in words:", len(length_cocuklu_tweet), "\nAverage number of words for a tweet = ", statistics.mean(length_cocuklu_tweet), "\nStandard Deviation of words for a tweet = ", statistics.stdev(length_cocuklu_tweet), "\n")

# 1 - f,g
result10 = pd.DataFrame(Counter(Document_Token["token_text"]).most_common(10), columns=['Word', 'Frequency']).set_index('Word')
result50 = pd.DataFrame(Counter(Document_Token["token_text"]).most_common(50), columns=['Word', 'Frequency']).set_index('Word')

print("FOR WHOLE DATASET")
print("\nFirst 10 words\n", result10)
print("\nFirst 50 words\n", result50)

# 2 - f,g
result10 = pd.DataFrame(Counter(bekar_tokens).most_common(10), columns=['Word', 'Frequency']).set_index('Word')
result50 = pd.DataFrame(Counter(bekar_tokens).most_common(50), columns=['Word', 'Frequency']).set_index('Word')
print("\nBEKAR TOKENS")
print("\nFirst 10 words\n", result10)
print("\nFirst 50 words\n", result50)

result10 = pd.DataFrame(Counter(evli_tokens).most_common(10), columns=['Word', 'Frequency']).set_index('Word')
result50 = pd.DataFrame(Counter(evli_tokens).most_common(50), columns=['Word', 'Frequency']).set_index('Word')
print("\nEVLİ TOKENS")
print("\nFirst 10 words\n", result10)
print("\nFirst 50 words\n", result50)

result10 = pd.DataFrame(Counter(cocuklu_tokens).most_common(10), columns=['Word', 'Frequency']).set_index('Word')
result50 = pd.DataFrame(Counter(cocuklu_tokens).most_common(50), columns=['Word', 'Frequency']).set_index('Word')
print("\nÇOCUKLU TOKENS")
print("\nFirst 10 words\n", result10)
print("\nFirst 50 words\n", result50)

# 1 and 2 - h
result = pd.DataFrame(Counter(less_from_five).most_common(10), columns=['Word', 'Frequency']).set_index('Word')
print("\nWHOLE DATASET - LESS FROM FIVE CHARACTER WORDS")
print(result)
result = pd.DataFrame(Counter(less_from_five_bekar).most_common(10), columns=['Word', 'Frequency']).set_index('Word')
print("\nBEKAR - LESS FROM FIVE CHARACTER WORDS")
print(result)
result = pd.DataFrame(Counter(less_from_five_evli).most_common(10), columns=['Word', 'Frequency']).set_index('Word')
print("\nEVLİ - LESS FROM FIVE CHARACTER WORDS")
print(result)
result = pd.DataFrame(Counter(less_from_five_cocuklu).most_common(10), columns=['Word', 'Frequency']).set_index('Word')
print("\nÇOCUKLU - LESS FROM FIVE CHARACTER WORDS")
print(result)

