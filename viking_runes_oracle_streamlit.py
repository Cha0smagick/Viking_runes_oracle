import streamlit as st
import random

# Rune Symbols And Meanings

class Rune:
    def __init__(self, name, description, keywords):
        self.name = name
        self.description = description
        self.keywords = keywords

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
fehu = Rune("Fehu", "Cattle/Wealth", ["Abundance", "Luck", "Hope", "Prosperity", "Wealth", "Fortune"])
uruz = Rune("Uruz", "Ox", ["Strength", "Endurance", "Health", "Courage", "Vigour", "Vitality", "Force", "Perseverance"])
thurisaz = Rune("Thurisaz", "Mallet/Giant/Thorn", ["Defence", "Challenge", "Danger", "Protection", "Attack", "Strength"])
ansuz = Rune("Ansuz", "Message", ["Revelation", "Signs", "Visions", "Insight", "Message", "Knowledge", "Communication"])
raidho = Rune("Raidho", "Journey", ["Progress", "Movement", "Evolution", "Perspective", "Journey", "Travel"])
kenaz = Rune("Kenaz", "Torch", ["Enlightenment", "Knowledge", "Comprehension", "Insight", "Illumination", "Calling", "Purpose", "Idea"])
gebo = Rune("Gebo", "Gift", ["Generosity", "Partnership", "Gifts", "Talents", "Charity", "Service", "Assistance", "Luck", "Fortune"])
wunjo = Rune("Wunjo", "Joy", ["Pleasure", "Joy", "Feast", "Celebration", "Comfort", "Belonging", "Community", "Success", "Festivities"])

# Define runes for Heimdall's Aett
hagalaz = Rune("Hagalaz", "Hail", ["Destruction", "Natural Wrath", "Uncontrolled Forces", "Testing", "Change", "External Input"])
nauthiz = Rune("Nauthiz", "Needs", ["Need", "Restriction", "Disagreements", "Resistance", "Survival", "Necessity", "Lacking"])
isa = Rune("Isa", "Ice", ["Suspension", "Delay", "Stillness", "Frustration", "Blocks", "Pause", "Waiting"])
jera = Rune("Jera", "Harvest", ["Year", "Conclusion", "Harvest", "Life Cycle", "Endings and Beginnings", "Abundance", "Learnings", "Growth"])
eihwaz = Rune("Eihwaz", "Yew", ["Connection", "Inspiration", "Endurance", "Sacred Knowledge", "Protection", "Life Cycle’s", "Divinity"])
perthro = Rune("Perthro", "Destiny", ["Fate", "Mysteries", "Occult", "Feminine Fertility", "Chance", "Fortune", "Mysticism", "Unknown"])
algiz = Rune("Algiz", "Elk", ["Protection", "Guardian", "Awakening", "Courage", "Defence", "Instincts"])
sowilo = Rune("Sowilo", "Sun", ["Success", "Vitality", "Inspiration", "Justice", "Success", "Joy", "Happiness", "Abundance"])

# Define runes for Tyr's Aett
tiwaz = Rune("Tiwaz", "Victory", ["Leadership", "Rationality", "Victory", "Honour", "Bravery", "Courage", "Strength", "Perseverance", "Endurance"])
berkana = Rune("Berkana", "Birch", ["Fertility", "Growth", "Renewal", "New Beginnings", "Birth", "Creation", "New Projects", "Creativity"])
ehwaz = Rune("Ehwaz", "Horse", ["Progress", "Movement", "Harmony", "Trust", "Loyalty", "Friendship", "Assistance", "Duality", "Animal Instincts"])
mannaz = Rune("Mannaz", "Man", ["Humanity", "Collective", "Mortality", "Community", "Relationships", "Morals", "Values"])
laguz = Rune("Laguz", "Lake", ["Water", "Intuition", "Imagination", "Healing", "Dreams", "Mysteries", "Insight", "Instinct", "Knowing"])
ingwaz = Rune("Ingwaz", "Fertility", ["Fertility", "Virility", "Inner Growth", "Virtue", "Peace", "Harmony"])
othala = Rune("Othala", "Heritage", ["Legacy", "Inheritance", "Spiritual Growth", "Abundance", "Values", "Contribution"])
dagaz = Rune("Dagaz", "Dawn", ["Day", "Awakening", "Consciousness", "Clarity", "Hope", "Balance", "Growth", "New Cycles"])

# Create rune sets
freyrs_aett = RuneSet("Freyr's", "Freyr", [fehu, uruz, thurisaz, ansuz, raidho, kenaz, gebo, wunjo])
heimdalls_aett = RuneSet("Heimdall's", "Heimdall", [hagalaz, nauthiz, isa, jera, eihwaz, perthro, algiz, sowilo])
tyrs_aett = RuneSet("Tyr's", "Tyr", [tiwaz, berkana, ehwaz, mannaz, laguz, ingwaz, othala, dagaz])

# Streamlit App
st.title("Rune Sets Explorer")

# User input to select Aett
selected_aett = st.selectbox("Select Aett", [freyrs_aett.name, heimdalls_aett.name, tyrs_aett.name])

# Display selected Aett
if selected_aett == freyrs_aett.name:
    display_aett = freyrs_aett
elif selected_aett == heimdalls_aett.name:
    display_aett = heimdalls_aett
else:
    display_aett = tyrs_aett

st.header(display_aett.name)
st.write(f"{display_aett.aett} Aett")

# User input to select the number of runes for the reading
num_runes = st.selectbox("Select the number of runes", [1, 2, 3])

# Button to perform a rune reading
if st.button("Make a Trow"):
    # Logic to perform a rune reading based on the selected number of runes
    selected_runes = random.sample(display_aett.runes, num_runes)
    
    st.success("Trown Results:")
    
    for i, rune in enumerate(selected_runes):
        # Determine if the rune is upright or reversed
        orientation = "Upwards" if random.choice([True, False]) else "Backwards"
        
        # Display the rune, its description, keywords, order, and orientation
        st.write(f"{i+1}. {rune.name} - {rune.description} ({orientation}): {', '.join(rune.keywords)}")
