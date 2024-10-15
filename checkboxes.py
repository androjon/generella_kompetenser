import streamlit as st
import json

def läsa_in_json_fil(filnamn):
    with open(filnamn) as fil:
        innehåll = fil.read()
    utdata = json.loads(innehåll)
    return utdata

generic_data = läsa_in_json_fil("generic_skill_groups.json")
st.header("Generella kompetenser")
st.write("Kompetenser som gäller i princip alla yrken. Ofta kallas de också mjuka kompetenser eller soft skills. Här kan du du utforska och förstå de generella kompetenserna. Kan vara viktiga att lyfta fram i ett CV då många arbetsgivare värderar dessa högt.")
st.write("Välj tre stycken generella kompetenser som kännetecknar dig mest i olika jobbsituationer.")
st.divider()

for i in generic_data:
    number_of_generic_skills = 0
    st.write(i["name"])
    st.write(i["defintion"])
    col1, col2 = st.columns(2)
    for g in i["generic_skills"]:
        if (number_of_generic_skills % 2) == 0:
            col1.checkbox(f"{g['label'][0]}", help = f"{g['name']}  \n{g['definition']}")
        else:
            col2.checkbox(f"{g['label'][0]}", help = f"{g['name']}  \n{g['definition']}")
        number_of_generic_skills += 1
    st.divider()
    

# st.write('Select three known variables:')
# opts = [ ('s', 'displacement'), ('u', 'initial velocity'), ('v', 'final velocity'), ('a', 'acceleration'), ('t', 'time') ]
# known_variables = {symbol: st.checkbox(f"{name} ({symbol})") for symbol, name in opts}    
# if sum(known_variables.values()) < 3:
#     st.write('You have to select minimum 3 variables.')
# elif sum(known_variables.values()) == 3:
#     st.write('Now put the values of your selected variables in SI units.')

# else:
#     st.write('You can select maximum 3 variables.')