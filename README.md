# Text Summarization Project
This project aims to provide both extractive and abstractive text summarization techniques for generating concise and informative summaries from large textual data. 
The project is designed to work with various types of text data, including news articles, research papers, and web pages.

# Table of Contents
*  Installation
-  Usage
+  Extractive Summarization
*  Abstractive Summarization
  
# Installation
Clone the repository to your local machine.
Install the required dependencies by running the following command:
pip install -r requirements.txt

# Usage
1. Download the zip file
2. Create a python env 
3. Install requirement.txt
4. Download the weight file from the drive link
5. [Drive Link For Weight File](https://drive.google.com/file/d/1ZnlUmouraXeiV1ilWk2AM5ErJ7BQqZTW/view?usp=sharing)
6. Place it the folder directory along with config.json
7. Run APPLICATION.py


# Extractive Summary
The extractive summarization technique involves selecting the most important sentences or phrases from the original text and combining them to form a summary. This technique is based on the assumption that the most important information in a text is typically contained in the most frequently occurring or most significant sentences.

The summarizer() function in the FunctionS.py uses natural language processing (NLP) techniques to identify and select the most important sentences from the input text. The function returns a summary that consists of a subset of the original sentences.

# Abstractive Summarization
The abstractive summarization technique involves generating a summary that may contain new phrases or sentences not present in the original text. This technique is more challenging than extractive summarization, as it requires the model to understand the meaning of the original text and generate a summary that captures its essence.

The abs_summary() function in the FunctionS.py uses a transformer based 'State Of The Art' model 'PEGASUS-XSUM' to generate a summary. The function first preprocesses the input text by tokenizing the sentences and applying various NLP techniques. It captures the essence of the original text.

