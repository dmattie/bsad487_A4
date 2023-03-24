#!/usr/bin/env python3

# Import necessary packages
from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader
import os
import logging, sys
logging.disable(sys.maxsize)

os.environ['OPENAI_API_KEY'] = 'sk-###GET FROM MOODLE###'

# Loading from a directory
location="./documents"
print(f"Reading from the documents in {location}")
documents = SimpleDirectoryReader(location).load_data()
print("All caught up!\n")
# Construct a simple vector index
index = GPTSimpleVectorIndex(documents)

print("What do you want to know?")
my_question=input()

# Querying the index
print("... processing ...")
response = index.query(my_question)
print(response)