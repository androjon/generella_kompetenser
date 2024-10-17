import streamlit as st
import json

def läsa_in_json_fil(filnamn):
    with open(filnamn) as fil:
        innehåll = fil.read()
    utdata = json.loads(innehåll)
    return utdata

number_of_selected = 0

st.session_state.choosen_generic_skills = []

generic_data = läsa_in_json_fil("generic_skill_groups.json")
st.header("**Generella kompetenser**")
st.write("Kompetenser som gäller i princip alla yrken. Ofta kallas de också mjuka kompetenser eller soft skills. Här kan du du utforska och förstå de generella kompetenserna. Kan vara viktiga att lyfta fram i ett CV då många arbetsgivare värderar dessa högt.  \n\nVälj tre stycken generella kompetenser som kännetecknar dig mest i olika jobbsituationer.")

st.divider()

st.session_state.all_generic_skills_keys_definition = {}

for i in generic_data:
    number_of_generic_skills = 0
    st.write(f"**{i['name']}**  - {i['defintion']}")
    col1, col2 = st.columns(2)
    for g in i["generic_skills"]:
        keyname = g['name']
        st.session_state.all_generic_skills_keys_definition[g['name']] = [g['label'][0], g['definition']]
        if (number_of_generic_skills % 2) == 0:
            col1.checkbox(f"**{g['label'][0]}** - {g['name']}", help = f"{g['definition']}", key = keyname)
        else:
            col2.checkbox(f"**{g['label'][0]}** - {g['name']}", help = f"{g['definition']}", key = keyname)
        number_of_generic_skills += 1
    st.divider()

def save_selected_generic():
    for key in list(st.session_state.all_generic_skills_keys_definition.keys()):
        if st.session_state[key]:
            text_input_key = f"input_{key}"
            if st.session_state[text_input_key]:
                selected = {st.session_state.all_generic_skills_keys_definition[key][0]: st.session_state[text_input_key]}
            else:
                selected = {st.session_state.all_generic_skills_keys_definition[key][0]: None}
            st.session_state.choosen_generic_skills.append(selected)
    with st.sidebar:
        st.write(st.session_state.choosen_generic_skills)

st.button("Spara din val och se om dina val kan hjälpa dig med ett CV", on_click = save_selected_generic)

st.write("Det är inte ovanligt att arbetsgivare frågar efter hur du har hanterat olika jobbsituationer utifrån generella kompetenser.")
col1, col2, col3 = st.columns(3)

for key in list(st.session_state.all_generic_skills_keys_definition.keys()):
    if st.session_state[key]:
        definition = st.session_state.all_generic_skills_keys_definition.get(key)
        generic_skill_label = definition[0]
        number_of_selected += 1
        if (number_of_selected % 3) == 1:
            col1.text_area(f"**{generic_skill_label}**  \n{key}", value = "", key = f"input_{key}", height = 400, help = definition[1], placeholder = "Ge exempel på situationer du varit det")
        elif (number_of_selected % 3) == 2:
            col2.text_area(f"**{generic_skill_label}**  \n{key}", value = "", key = f"input_{key}", height = 400, help = definition[1], placeholder = "Ge exempel på situationer du varit det")
        else:
            col3.text_area(f"**{generic_skill_label}**  \n{key}", value = "", key = f"input_{key}", height = 400, help = definition[1], placeholder = "Ge exempel på situationer du varit det")

