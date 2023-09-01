import spacy
nlp = spacy.load("en_core_web_sm")

doc = nlp("""Diego Armando Maradona (30 October 1960 – 25 November 2020) was an Argentine professional football player and manager. Widely regarded as one of the greatest players in the history of the sport, he was one of the two joint winners of the FIFA Player of the 20th Century award. Maradona's vision, passing, ball control, and dribbling skills were combined with his small stature, which gave him a low centre of gravity and allowed him to manoeuvre better than most other players. His presence and leadership on the field had a great effect on his team's general performance, while he would often be singled out by the opposition. In addition to his creative abilities, he possessed an eye for goal and was known to be a free kick specialist. A precocious talent, Maradona was given the nickname "El Pibe de Oro" ("The Golden Boy"), a name that stuck with him throughout his career. He also had a troubled off-field life and was banned in both 1991 and 1994 for abusing drugs. FIFA awarded him the FIFA Player of the 20th Century award.""")

ORG = "ORG: "
Percent = "Percent: "
Date = "Date: "
Money = "Money: "
Event = "Event: "
Person = "Person: "

# Loop through the entities in the processed text
for ent in doc.ents:
    if ent.label_ == "ORG":
        ORG += ent.text + ", "
    elif ent.label_ == "MONEY":
        Money += ent.text + ", "
    elif ent.label_ == "DATE":
        Date += ent.text + ", "
    elif ent.label_ == "PERCENT":
        Percent += ent.text + ", "
    elif ent.label_ == "EVENT":
        Event += ent.text + ", "
    elif ent.label_ == "PERSON":
        Person += ent.text + ", "

# Print the categorized entities
print(ORG)
print(Percent)
print(Date)
print(Money)
print(Event)
print(Person)



