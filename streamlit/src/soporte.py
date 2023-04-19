import pickle
import pandas as pd
import streamlit as st

# encoding Contract 
with open('data/ML/pkl/encodingContract.pkl', 'rb') as contract:
    encoding_contract = pickle.load(contract)

# encoding Device Protection 
with open('data/ML/pkl/encodingDevice Protection Plan.pkl', 'rb') as contract:
    encoding_contract = pickle.load(contract)

