
import contractions
import re
import pandas as pd

def limpiar_texto(text, nlp, stop_words, remover_digitos=False):
    if isinstance(text, str):
        text = contractions.fix(text)

        text = text.lower()
        text = re.sub(r"[^\w\s]", "", text)

        if remover_digitos:
            text = re.sub(r"\d+", "", text)

        text = re.sub(r"\s+", " ", text)
        text = text.strip()
        doc = nlp(text)

        tokens = [token.lemma_ for token in doc if token.text not in stop_words]
        return tokens
    
def get_index_from_name(df: pd.DataFrame, name):
    try:
        return df[df.productName == name].index[0]
    except:
        print(f"No se ha encontrado el index de: {name}")

def get_name_from_index(df: pd.DataFrame, index):
    try:
        return df[df.index == index]["productName"].values[0]
    except:
        print(f"No se ha encontrado el nombre del index: {index}", NameError())