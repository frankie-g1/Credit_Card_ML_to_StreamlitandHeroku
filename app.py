import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


@st.cache
def load_graph():
    bank = pd.read_csv(r'C:\Users\guarinof\PycharmProjects\ML\BankChurners.csv')
    return bank


data = load_graph()


def main():
    st.balloons()
    st.write(data)


if __name__ == "__main__":
    main()
