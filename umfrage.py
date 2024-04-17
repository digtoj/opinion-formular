import streamlit as st

import matplotlib.pyplot as plt
import os
import pandas as pd


# Funktion zum Speichern der Daten in eine Excel-Datei
def save_data(data):
    filename = 'survey_results.xlsx'
    data_df = pd.DataFrame([data])
    if os.path.exists(filename):
        existing_df = pd.read_excel(filename)
        updated_df = pd.concat([existing_df, data_df], ignore_index=True)
    else:
        updated_df = data_df
    updated_df.to_excel(filename, index=False)

# Funktion zum Laden der Daten und Erstellen einer einfachen Plot
def load_and_plot_data():
    filename = 'survey_results.xlsx'
    if os.path.exists(filename):
        df = pd.read_excel(filename)
        satisfaction_counts = df['Zufriedenheit mit der Antwortgenauigkeit'].value_counts()
        plt.figure()
        satisfaction_counts.plot(kind='bar')
        plt.title('Zufriedenheit mit der Antwortgenauigkeit des Chatbots')
        plt.xlabel('Zufriedenheitslevel')
        plt.ylabel('Anzahl der Antworten')
        st.pyplot(plt)

# Erstellen des Umfrageformulars
def create_survey():
    st.title('Chatbot Umfrage')

    if 'submitted' not in st.session_state:
        st.session_state.submitted = False

    if not st.session_state.submitted:
        with st.form(key='survey_form'):
            studiengang = st.text_input("Studiengang")
            semester = st.text_input("Semester")
            usage = st.selectbox("Wie oft haben Sie den Chatbot bereits genutzt?", 
                                 ["Noch nie", "Einmal", "Ein paar Mal", "Regelmäßig"])
            info_type = st.multiselect("Für welche Art von Informationen haben Sie den Chatbot genutzt?",
                                       ["Studieninhalte", "Lehrveranstaltungen", "Prüfungsordnungen", 
                                        "Dozenteninformationen", "Sonstige"])
            satisfaction_accuracy = st.selectbox("Wie zufrieden sind Sie mit der Genauigkeit der Antworten, die der Chatbot liefert?",
                                                 ["Sehr unzufrieden", "Unzufrieden", "Neutral", "Zufrieden", "Sehr zufrieden"])
            satisfaction_speed = st.selectbox("Wie bewerten Sie die Geschwindigkeit der Antwortgebung durch den Chatbot?",
                                              ["Sehr unzufrieden", "Unzufrieden", "Neutral", "Zufrieden", "Sehr zufrieden"])
            intuitive = st.radio("War die Interaktion mit dem Chatbot intuitiv und benutzerfreundlich?", 
                                 ["Ja", "Nein", "Teilweise"])
            improvements = st.text_area("Welche Funktionen würden Sie sich zusätzlich wünschen oder was könnte verbessert werden?")
            additional_comments = st.text_area("Haben Sie weitere Kommentare oder Feedback, das Sie uns mitteilen möchten?")
            email_info = st.checkbox("Möchten Sie über die Ergebnisse oder Updates zum Chatbot informiert werden?")
            email = st.text_input("Bitte geben Sie Ihre E-Mail-Adresse ein, wenn Sie informiert werden möchten.") if email_info else ""

            submit_button = st.form_submit_button(label='Umfrage absenden')

            if submit_button:
                data = {
                    'Studiengang': studiengang,
                    'Semester': semester,
                    'Nutzungsfrequenz': usage,
                    'Art der Informationen': ", ".join(info_type),
                    'Zufriedenheit mit der Antwortgenauigkeit': satisfaction_accuracy,
                    'Zufriedenheit mit der Antwortgeschwindigkeit': satisfaction_speed,
                    'Benutzerfreundlichkeit': intuitive,
                    'Verbesserungsvorschläge': improvements,
                    'Weitere Kommentare': additional_comments,
                    'E-Mail für Updates': email
                }
                save_data(data)
                st.session_state.submitted = True
                st.success("Danke für Ihre Teilnahme an der Umfrage!")

def reset_form():
    st.session_state.submitted = False

def main():
    create_survey()

if __name__ == "__main__":
    main()
