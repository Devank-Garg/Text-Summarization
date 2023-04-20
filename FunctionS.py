from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
def abs_summary(T):
    loaded_model = PegasusForConditionalGeneration.from_pretrained('weights', config='config.json')
    model_ckpt = "google/pegasus-xsum"

    tokenizer = AutoTokenizer.from_pretrained(model_ckpt)
    # text="""Astronomy enthusiasts are in for a treat as the year's first solar eclipse is about to happen. On April 20, 2023, we will witness a spectacular sight as the moon will pass between the Earth and the sun. A solar eclipse happens when the moon obstructs the sun's light and forms a ring-like structure as the Earth plunges into darkness for a short span of time. This astronomical event is quite a rare occurrence and there are several reasons why. 
    # Here's all you need to know about the Surya Grahan 2023, its timings, why it's special and food myths and things to keep in mind."""


    tokens = tokenizer(T, truncation=True, padding="longest", return_tensors="pt")

    summary = loaded_model.generate(**tokens)
    Res=tokenizer.decode(summary[0])


    return (Res)
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest



text=""" Astronomy enthusiasts are in for a treat as the year's first solar eclipse is about to happen. On April 20, 2023, we will witness a spectacular sight as the moon will pass between the Earth and the sun. A solar eclipse happens when the moon obstructs the sun's light and forms a ring-like structure as the Earth plunges into darkness for a short span of time. This astronomical event is quite a rare occurrence and there are several reasons why. Here's all you need to know about the Surya Grahan 2023, its timings, why it's special and food myths and things to keep in mind."""
def summarizer(rawdocs):
    stopwords=list(STOP_WORDS)
    nlp=spacy.load('en_core_web_sm')
    doc=nlp(rawdocs)
    tokens=[token.text for token in doc]
    word_freq={}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                    word_freq[word.text]=1
            else:
                    word_freq[word.text]+=1


    max_freq=max(word_freq.values())


    for word in word_freq.keys():
        word_freq[word]=word_freq[word]/max_freq

    sent_tokens=[sent for sent in doc.sents]
    sent_scores={}
    for sent in sent_tokens:
        for word in sent:
                if word.text in word_freq.keys():
                    if sent not in sent_scores.keys():
                            sent_scores[sent]=word_freq[word.text]
                    else:
                            sent_scores[sent]+=word_freq[word.text]
    select_len=int(len(sent_tokens)*0.4)
    summary=nlargest(select_len,sent_scores,key=sent_scores.get)
    final_summary=[word.text for word in summary]
    summary=" ".join(final_summary)
    return summary, doc , len(rawdocs.split(' ')), len(summary.split(' '))
    