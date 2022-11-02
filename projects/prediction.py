def getPredictions(pclass, sex, age, sibsp, parch, fare, C, Q, S):
    import pickle
    scaler = pickle.load(open("pythonnotebooks/titanicproject/scaler.sav", "rb"))
    model = pickle.load(open("pythonnotebooks/titanicproject/titanic_survival_ml_model.sav", "rb"))
    prediction = model.predict(scaler.transform([[pclass, sex, age, sibsp, parch, fare, C, Q, S]]))
    
    if prediction == 0:
        print("notsurvived")
        return "not survived"
    elif prediction == 1:
        print("survived")
        return "survived"
    else:
        return "error"

def getpredictioniris(sepallength,sepalwidth,petallength,petalwidth):
    import pickle
    import numpy
    model = pickle.load(open('pythonnotebooks/irisproject/model.pkl', 'rb'))
    int_features =[sepallength,sepalwidth,petallength,petalwidth]
    final_features = [numpy.array(int_features)]
    irisresul = model.predict(final_features)
    return irisresul
def get_predicted_price(area_type, location, sqft, balcony, bathroom, BHK):
    import pickle
    import json
    import math
    import numpy as np
    with open(r"pythonnotebooks/houseproject/bangalore_home_prices_model.pickle", 'rb') as f:
       __model = pickle.load(f)

    with open(r"pythonnotebooks/houseproject/Columns.json", 'r') as obj:
       __data_columns = json.load(obj)["Columns"]
       __area_types = __data_columns[4:8]
       __locations = __data_columns[8:]
    try:
        area_index = __data_columns.index(area_type.lower())
        loc_index = __data_columns.index(location.lower())
    except ValueError as e:
        area_index = -1
        loc_index = -1

    lis = np.zeros(len(__data_columns))
    lis[0] = sqft
    lis[1] = bathroom
    lis[2] = balcony
    lis[3] = BHK

    if loc_index >= 0 and area_index >= 0:
        lis[area_index] = 1
        lis[loc_index] = 1

    price = round(__model.predict([lis])[0], 2)
    strp = ' lakhs'

    if math.log10(price) >= 2:
        price = price / 100
        price = round(price, 2)
        strp = " crores"

    return str(price) + strp 

def my_form_post():
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    import nltk
    from string import punctuation
    import re
    from nltk.corpus import stopwords

    nltk.download('stopwords')

    set(stopwords.words('english'))

    stop_words = stopwords.words('english')
    #convert to lowercase
    #text1 = request.form['text1'].lower()
    
    #text_final = ''.join(c for c in text1 if not c.isdigit())
    
    #remove punctuations
    #text3 = ''.join(c for c in text2 if c not in punctuation)
        
    #remove stopwords    
    #processed_doc1 = ' '.join([word for word in text_final.split() if word not in stop_words])

    sa = SentimentIntensityAnalyzer()
    ##dd = sa.polarity_scores(text=processed_doc1)
    #compound = round((1 + dd['compound'])/2, 2)
