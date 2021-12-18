# Task - Text summarization service with Python

## Current implementation
- Sumy library for simple text summarization
- Flask for provising a REST endpoint
- SQLLite, which is already part of Python

## Features
- Same documents are only generated once
- Different algorithms from sumy could be used:  "TextRankSummarizer", "LexRankSummarizer", "LuhnSummarizer" "LsaSummarizer"
- Data is stored in database and will survive server restarts
- REST endpoints following the REST pattern for get and save
- Invalid data is handled with 400, 404 erros

The implementation is using Flask as a REST service endpoint. It provides the capability to summarize any text
which could be later retrived with an unique document id.

## Usage
- start `main.py` to start the server
- call REST endpoints with any REST client or framework 

**GET**
call to `http://127.0.0.1:5000/summary/document_id`

**POST**
call to `http://127.0.0.1:5000/summary`

`{
    "text" : "The Jedi and their troops set a trap for Grievous and confronted the cyborg general once he arrived. However, Grievous was able to eliminate several clone troopers, and after sustaining injuries, escape to the castle's secret command center. Sealing off the exits, the Confederate general trapped the Jedi and clones inside his castle. While Grievous was repaired by his caretaker droid, the general pitted the Jedi and the remaining clones against the castle's defenses—a molten incinerator pit and the general's pet roggwart, Gor. The clones were killed, but the Jedi were able to eliminate Gor."
}`

## Possible improvements
- Make the summary in sentence amount linear the original text. Larger original text will then produce larger summary text
- Using better NLP approaches like transformers (BERT) and transfer learning, which are able to produce better summarizations of text
- Containerize solution and consider horizontal scaling possibilities
- Create index on DOCUMENT_ID field in the database to improve access speed
- Use a real and scalable database to store the data. Think of NoSQL databases to stpore the texts
- Better hashing methods to generate document_id
- Support different languages
- More extended and detailed tests