import streamlit as st
from collections import Counter

st.set_page_config(page_title="AI Philosophy Quiz", layout="centered")
st.title("🤖 Che tipo di filosofo dell'AI sei?")
st.markdown("Rispondi alle 7 domande qui sotto per scoprire quale filosofia dell’intelligenza artificiale ti rappresenta di più.")

questions = [
    ("Quando vedi GPT scrivere testi impressionanti, cosa pensi?", 
     ["A. Funziona, non importa come.", "B. Funziona, ma serve struttura.", "C. Non è intelligenza senza corpo.", "D. Serve comprensione e generalizzazione."]),
    ("Quale frase ti rappresenta di più?",
     ["A. L’intelligenza è pattern recognition.", "B. La mente è un programma simbolico.", "C. Senza corpo e sensi non esiste pensiero.", "D. L’intelligenza è costruzione di concetti astratti."]),
    ("Hai un robot in casa. Cosa vuoi che sappia fare?",
     ["A. Parlare e riconoscere oggetti.", "B. Ragionare con regole.", "C. Apprendere esplorando.", "D. Costruire strategie da esempi."]),
    ("Un’AI generale, per te, nasce da:",
     ["A. Big data e deep learning.", "B. Simboli e logica.", "C. Cervello e corpo.", "D. Moduli, concetti e astrazione."]),
    ("Se dovessi costruire un’AI, da dove parti?",
     ["A. Dataset e GPU.", "B. Ontologie e regole.", "C. Teoria del neocortex.", "D. Architettura modulare e meta-learning."]),
    ("Un’AI che sbaglia, per te è:",
     ["A. Normale, migliora con i dati.", "B. Un errore logico da correggere.", "C. Una lezione biologica.", "D. Una possibilità di apprendere a più livelli."]),
    ("La tua ispirazione?",
     ["A. LeCun, Hinton, OpenAI.", "B. Russell, McCarthy, Turing.", "C. Hawkins, Varela, Friston.", "D. Chollet, Hofstadter, Minsky."])
]

responses = []

with st.form("quiz_form"):
    for i, (question, options) in enumerate(questions):
        st.markdown(f"**{i+1}. {question}**")
        choice = st.radio("", options, key=f"q{i}")
        responses.append(choice[0])  # Prendi la lettera iniziale (A, B, C, D)
    submitted = st.form_submit_button("Scopri il tuo profilo AI")

if submitted:
    count = Counter(responses)
    dominant = count.most_common(1)[0][0]

    st.subheader("🎯 IL TUO PROFILO AI")

    if dominant == "A":
        st.markdown("**👉 Connessionista Computazionale**\n\nCredi nel deep learning potente, nei dati e nei pattern. Vuoi risultati, anche se l’AI non capisce davvero.")
    elif dominant == "B":
        st.markdown("**👉 Simbolico Razionale**\n\nTi affidi alla logica, alle regole e alla chiarezza. L’intelligenza per te è ordine, non pattern sparsi.")
    elif dominant == "C":
        st.markdown("**👉 Neuro-Biologico Visionario**\n\nPer te la mente è nel cervello. L’AI deve partire dal corpo, dai sensi, dalla biologia vera.")
    elif dominant == "D":
        st.markdown("**👉 Ibrido Cognitivo-Astratto**\n\nVuoi il meglio dei mondi: moduli, generalizzazione, concetti, astrazione. Una vera mente flessibile.")

    if len(set(responses)) > 2:
        st.info("💡 Hai risposto in modo variegato: potresti essere un *ARCHITETTO DELL’INTELLIGENZA*. Complesso, integrativo, visione alta.")
