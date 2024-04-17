import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data():
    filename = 'survey_results.xlsx'
    if os.path.exists(filename):
        return pd.read_excel(filename)
    else:
        return pd.DataFrame()

def plot_data(question, title):
    df = load_data()
    if not df.empty and question in df.columns:
        value_counts = df[question].value_counts()
        plt.figure()
        value_counts.plot(kind='bar')
        plt.title(title)
        plt.xlabel('Antworten')
        plt.ylabel('Anzahl')
        st.pyplot(plt)

def main():
    st.title('Ergebnisse der Chatbot-Umfrage')

    df = load_data()
    if not df.empty:
        st.write("### Detaillierte Ergebnisse")
        plot_data('Nutzungsfrequenz', 'Nutzungshäufigkeit des Chatbots')
        plot_data('Art der Informationen', 'Arten der genutzten Informationen')
        plot_data('Zufriedenheit mit der Antwortgenauigkeit', 'Zufriedenheit mit der Antwortgenauigkeit')
        plot_data('Zufriedenheit mit der Antwortgeschwindigkeit', 'Zufriedenheit mit der Antwortgeschwindigkeit')
        plot_data('Benutzerfreundlichkeit', 'Benutzerfreundlichkeit des Chatbots')

        # Für offene Fragen können Sie einfache Listen der Antworten anzeigen
        if 'Verbesserungsvorschläge' in df.columns:
            st.write("### Verbesserungsvorschläge")
            st.write(df['Verbesserungsvorschläge'].dropna().tolist())
        
        if 'Weitere Kommentare' in df.columns:
            st.write("### Weitere Kommentare")
            st.write(df['Weitere Kommentare'].dropna().tolist())

    else:
        st.write("Keine Daten verfügbar.")

if __name__ == "__main__":
    main()
