from flask import Flask, render_template, request

from FunctionS import summarizer, abs_summary
app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods=['GET','POST'])
def result():
    if request.method=="POST":
        R_TEXT=request.form['TEXT']
        summary,original_text,text_len, summary_len=summarizer(R_TEXT)
        abst_summary=abs_summary(R_TEXT)
        


    return render_template("result.html",summary=summary,original_text=original_text,text_len=text_len,summary_len=summary_len,abst_summary=abst_summary)



if __name__=='__main__':
    app.run(debug= True) 

