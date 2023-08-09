# SEO-word-counter
Simple python script that lists the percentages of each word within a text of a [given website](specific-url). General words can be excluded.
After [fine tuning](#fine-tune), this script can be used to gather keyword ideas for writing search engine optimized texts.

# Requirements
Install the required packages by running the following command in your terminal: pip install -r .\requirements.txt

# Set-up
## Specify URL
Specify the URL you want to analyze:
'url = 'https://en.wikipedia.org/wiki/ELISA'
## Fine tune
The file 'exclude.py' contains a list, that is used to exclude certain words from your results table.
Add any word you want to exclude from your result into the list.

# Output
The script generates an Excel file ('output.xlsx') that consist of a table. The table contains two columns: the keyword and its occurence (in %).
