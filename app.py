from flask import Flask,render_template,request
from sklearn.naive_bayes import GaussianNB
import pickle
from nltk.stem.porter import PorterStemmer
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import re
from nltk.corpus import stopwords
import nltk
import warnings
warnings.filterwarnings('ignore')
nltk.download('stopwords')
app=Flask(__name__)
@app.route("/")
def fjkfjk():
    return render_template('news.html')
@app.route('/info',methods=['GET','POST'])
def fjkfj():
    def cleaning(data):
        ps=PorterStemmer()
        for i in data.index:
            temp=re.sub('[^a-z A-Z]','',data['text'][i])
            data['text'][i]=' '.join([ps.stem(word) for word in temp.split() if word.lower() not in stopwords.words('english')])
        return data
    
    if(request.method=='POST'):
        news=request.form['n']
        print(news)
        test=pd.DataFrame({'text':[news]})
        test=cleaning(test)
        cv=pickle.load(open('cv.pkl','rb'))
        test_news=cv.transform(test).toarray()
        model=pickle.load(open('mymodel.pkl','rb'))
        ans=model.predict(test_news)
        if(ans==1):
            disp="Real news"
        else:
            disp="Fake news"
        return render_template('news.html',answer=disp)
app.run()
print("Hello")
print("How are you")