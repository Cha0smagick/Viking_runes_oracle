import streamlit as st
import random
import google.generativeai as genai
from IPython.display import Markdown

# Rune Symbols And Meanings

class Rune:
    def __init__(self, name, description, keywords, ascii_art):
        self.name = name
        self.description = description
        self.keywords = keywords
        self.ascii_art = ascii_art

    def __str__(self):
        return f"{self.name} - {self.description}\nKeywords: {', '.join(self.keywords)}"


class RuneSet:
    def __init__(self, name, aett, runes):
        self.name = name
        self.aett = aett
        self.runes = runes

    def __str__(self):
        return f"{self.name} ({self.aett} Aett)\n\n{', '.join(str(rune) for rune in self.runes)}"


# Define runes for Freyr's Aett
fehu = Rune("Fehu", "Cattle/Wealth", ["Abundance", "Luck", "Hope", "Prosperity", "Wealth", "Fortune"], "/ᚠ/")
uruz = Rune("Uruz", "Ox", ["Strength", "Endurance", "Health", "Courage", "Vigour", "Vitality", "Force", "Perseverance"], "/ᚢ/")
thurisaz = Rune("Thurisaz", "Mallet/Giant/Thorn", ["Defence", "Challenge", "Danger", "Protection", "Attack", "Strength"], "/ᚦ/")
ansuz = Rune("Ansuz", "Message", ["Revelation", "Signs", "Visions", "Insight", "Message", "Knowledge", "Communication"], "/ᚨ/")
raidho = Rune("Raidho", "Journey", ["Progress", "Movement", "Evolution", "Perspective", "Journey", "Travel"], "/ᚱ/")
kenaz = Rune("Kenaz", "Torch", ["Enlightenment", "Knowledge", "Comprehension", "Insight", "Illumination", "Calling", "Purpose", "Idea"], "/ᚲ/")
gebo = Rune("Gebo", "Gift", ["Generosity", "Partnership", "Gifts", "Talents", "Charity", "Service", "Assistance", "Luck", "Fortune"], "/ᚷ/")
wunjo = Rune("Wunjo", "Joy", ["Pleasure", "Joy", "Feast", "Celebration", "Comfort", "Belonging", "Community", "Success", "Festivities"], "/ᚹ/")

# Define runes for Heimdall's Aett
hagalaz = Rune("Hagalaz", "Hail", ["Destruction", "Natural Wrath", "Uncontrolled Forces", "Testing", "Change", "External Input"], "/ᚺ/")
nauthiz = Rune("Nauthiz", "Needs", ["Need", "Restriction", "Disagreements", "Resistance", "Survival", "Necessity", "Lacking"], "/ᚾ/")
isa = Rune("Isa", "Ice", ["Suspension", "Delay", "Stillness", "Frustration", "Blocks", "Pause", "Waiting"], "/ᛁ/")
jera = Rune("Jera", "Harvest", ["Year", "Conclusion", "Harvest", "Life Cycle", "Endings and Beginnings", "Abundance", "Learnings", "Growth"], "/ᛃ/")
eihwaz = Rune("Eihwaz", "Yew", ["Connection", "Inspiration", "Endurance", "Sacred Knowledge", "Protection", "Life Cycle’s", "Divinity"], "/ᛇ/")
perthro = Rune("Perthro", "Destiny", ["Fate", "Mysteries", "Occult", "Feminine Fertility", "Chance", "Fortune", "Mysticism", "Unknown"], "/ᛈ/")
algiz = Rune("Algiz", "Elk", ["Protection", "Guardian", "Awakening", "Courage", "Defence", "Instincts"], "/ᛉ/")
sowilo = Rune("Sowilo", "Sun", ["Success", "Vitality", "Inspiration", "Justice", "Success", "Joy", "Happiness", "Abundance"], "/ᛊ/")

# Define runes for Tyr's Aett
tiwaz = Rune("Tiwaz", "Victory", ["Leadership", "Rationality", "Victory", "Honour", "Bravery", "Courage", "Strength", "Perseverance"], "/ᛏ/")
berkano = Rune("Berkano", "Birch Goddess", ["Growth", "New Beginnings", "Fertility", "Rejuvenation", "Renewal", "Motherhood"], "/ᛒ/")
ehwaz = Rune("Ehwaz", "Horse", ["Transportation", "Change", "Progress", "Stamina", "Horse", "Movement", "Adaptation"], "/ᛖ/")
mannaz = Rune("Mannaz", "Man", ["Humanity", "Awareness", "Social Connections", "Intelligence", "Cooperation", "Mankind", "Divine Structure"], "/ᛗ/")
laguz = Rune("Laguz", "Water", ["Flow", "Life Energy", "Unconscious", "Intuition", "Transformation", "Subconscious", "Dreams"], "/ᛚ/")
ingwaz = Rune("Ingwaz", "Fertility God", ["Fertility", "New Beginnings", "Internal Growth", "Male Fertility God", "Harvest"], "/ᛜ/")
othala = Rune("Othala", "Ancestral Property", ["Ancestral Property", "Inheritance", "Homeland", "Nobility", "Ancestors", "Inherited Traits"], "/ᛟ/")

# Define Rune Sets
freyrs_aett = RuneSet("Freyr's", "First", [fehu, uruz, thurisaz, ansuz, raidho, kenaz, gebo, wunjo])
heimdalls_aett = RuneSet("Heimdall's", "Second", [hagalaz, nauthiz, isa, jera, eihwaz, perthro, algiz, sowilo])
tyrs_aett = RuneSet("Tyr's", "Third", [tiwaz, berkano, ehwaz, mannaz, laguz, ingwaz, othala])

# All Rune Sets
all_rune_sets = [freyrs_aett, heimdalls_aett, tyrs_aett]

# Streamlit App
st.title("Norse Oracle")

# Sidebar
st.sidebar.header("Select Rune Set")
selected_set = st.sidebar.selectbox("Choose a Rune Set", all_rune_sets)

# Main App
st.write(selected_set)

# Function to generate random runes
def generate_runes(num_runes):
    runes = random.sample(selected_set.runes, num_runes)
    return runes

# Number of runes to draw
num_runes = st.sidebar.slider("Number of Runes to Draw", min_value=1, max_value=3, value=1)

# Draw Runes
draw_runes_button = st.sidebar.button("Draw Runes")
if draw_runes_button:
    selected_runes = generate_runes(num_runes)
    st.sidebar.success("Runes Drawn!")

    # Display ASCII representation of selected runes
    for i, rune in enumerate(selected_runes):
        st.sidebar.write(f"Rune {i + 1}: {rune.ascii_art}")
        st.sidebar.write(rune.description)
else:
    selected_runes = []

# User Question
user_question = st.text_input("Ask the Oracle a Question", "")

# Configure Gemini API
genai.configure(api_key='AIzaSyCVqyQJSEN3vZcYRmCogVmHxlmYkzCUxdQ')

# Gemini model for text-only prompts
gemini_model = genai.GenerativeModel('gemini-pro')

# Function to interact with Gemini API
def ask_gemini(question, runes_info):
    # Prepare prompt for Gemini API
    prompt = f"act as a viking oracle and answer the question for the user. {runes_info}\n\n{question}"

    # Generate response from Gemini API
    response = gemini_model.generate_content(prompt)

    return response.text

# Button to perform a rune reading and consult Gemini
if st.button("Ask the Runes"):
    # Prepare runes information for Gemini
    runes_info = "\n".join([f"{rune.name} - {rune.description}" for rune in selected_runes])

    # Call Gemini API to get additional response
    gemini_response = ask_gemini(user_question, runes_info)

    # Display Gemini response
    st.success("Rune Reading Results:")
    st.write("Gemini Response:")
    st.write(gemini_response)

    # Display ASCII representation of selected runes
    for i, rune in enumerate(selected_runes):
        st.write(f"Rune {i + 1}: {rune.ascii_art}")
        st.write(rune.description)

    st.write(f"User Question: {user_question}")
