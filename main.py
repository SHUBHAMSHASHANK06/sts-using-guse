import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub

module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
model = hub.load(module_url)
print("module %s loaded" % module_url)

def embed(input):
  return model(input)

def score(text1, text2):
  similarity_matrix = embed([text1, text2])
  ans = np.inner(similarity_matrix,similarity_matrix)
  return ans[0][1] # or ans[1][0]
