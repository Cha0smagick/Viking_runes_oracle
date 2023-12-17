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
st.markdown(
    """
    **Author:** cha0smagick the Techno Wizard  
    **Created for the blog:** [El Rincon Paranormal](https://elrinconparanormal.blogspot.com)  
    **Project's main page:** [Technowizard Cha0smagick's Viking Runes Oracle](hhttps://elrinconparanormal.blogspot.com/2023/12)  
    """
)

# User input to select Aett
selected_aett = st.selectbox("Select Aett", ["Freyr's Aett", "Heimdall's Aett", "Tyr's Aett"])

# User Question
user_question = st.text_input("Ask the Oracle a Question", "")

# Configure Gemini API
genai.configure(api_key='your_google_api_key')

# Gemini model for text-only prompts
gemini_model = genai.GenerativeModel('gemini-pro')

# User input to select the number of runes for the reading
num_runes = st.select_slider("Select the number of runes", [1, 2, 3])

# Button to perform a rune reading
if st.button("Ask the Runes"):
    # Logic to perform a rune reading based on the selected Aett
    if selected_aett == "Freyr's Aett":
        display_aett = freyrs_aett
    elif selected_aett == "Heimdall's Aett":
        display_aett = heimdalls_aett
    elif selected_aett == "Tyr's Aett":
        display_aett = tyrs_aett
    
    # Logic to perform a rune reading based on the selected number of runes
    selected_runes = random.sample(display_aett.runes, num_runes)
    
    # Display ASCII representation of selected runes
    runes_display = "  ".join([rune.ascii_art for rune in selected_runes])
    st.markdown(f"<p style='font-size:40px; font-weight:bold; text-align:center;'>{runes_display}</p>", unsafe_allow_html=True)
    
    st.success("Rune Reading Results:")
    
    # Updated code to use the Gemini API
    for i, rune in enumerate(selected_runes):
        # Determine if the rune is upright or reversed
        orientation = "Upwards" if random.choice([True, False]) else "Backwards"
        
        # Display the rune, its description, keywords, order, orientation, and the user's question
        if num_runes == 1:
            st.write(f"Trown result: {rune.name} - {rune.description} ({orientation}): {', '.join(rune.keywords)}")
        elif num_runes == 2:
            st.write(f"{'Past' if i == 0 else 'Future'}: {rune.name} - {rune.description} ({orientation}): {', '.join(rune.keywords)}")
        elif num_runes == 3:
            st.write(f"{'Past' if i == 0 else 'Present' if i == 1 else 'Future'}: {rune.name} - {rune.description} ({orientation}): {', '.join(rune.keywords)}")
    
    st.write(f"User Question: {user_question}")

    # Call the Gemini API and display the response
    gemini_response = gemini_model.generate_content(f"act as a viking oracle and interpret the the answer and give the answer for the question for the user. {user_question} - answer: {runes_display}")
    gemini_text = gemini_response.text

    st.write("Gemini API Response:")
    st.write(gemini_text)
