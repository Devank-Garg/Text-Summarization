from flask import Flask, render_template, request
from urllib.parse import urlparse
from c_t1 import text
from FunctionS import summarizer, abs_summary


app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods=['GET','POST'])
def result():
    if request.method=="POST":
        input_text=request.form['TEXT']
        
        # Check if input is a URL
        try:
            url = urlparse(input_text)
            if all([url.scheme, url.netloc]):
                # Input is a URL, get the text from the URL
                new_text = text(input_text)
               
        except:
            pass

        # Process the input text
        summary, original_text, text_len, summary_len = summarizer(new_text)
        abst_summary = abs_summary(new_text)

        # Render the result page
        return render_template('result.html', summary=summary, original_text=original_text, text_len=text_len, summary_len=summary_len, abst_summary=abst_summary)





if __name__=='__main__':
    app.run(debug= True) 

