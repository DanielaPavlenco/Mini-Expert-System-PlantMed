# Baza de date simulata cu simptome si bolile asociate
database = {
    "Frunze galbene si cazatoare": "Carenta de fier",
    "Petice albe pe frunze": "Mucegaiul pudrei",
    "Frunze mici si lipsa cresterii": "Deficit de azot",
    "Prezenta unor insecte pe frunze": "Atac de insecte",
    "Tulpina ingalbenita si invinetita": "Fusarioza",
    "Pete brune pe frunze": "Putregaiul cenusiu",
    "Frunze uscate si cazute": "Carenta de apa",
    "Aspect lipicios pe frunze": "Atac de afide",
    "Mucegai albicios pe frunze": "Putregaiul radacinilor",
    "Frunze galbene si caderea florilor": "Exces de udare",
    "Frunze intunecate si caderea fructelor": "Atac de ciuperci",
    "Pete negre pe frunze si tulpini": "Cercosporioza",
    "Frunze atrofiate si deformate": "Virusuri de plante",
    "Frunze decolorate si caderea lastarilor": "Atac de trips",
    "Mucegai verde pe frunze si fructe": "Oidium",
    "Frunze ruginii si pierderea frunzelor": "Ruginirea frunzelor",
    "Miros neplacut la nivelul radacinilor": "Putregaiul radacinilor",
    "Radacini moi si carunte": "Fusarioza radacinilor",
    "Pete negre sau maronii pe tulpini": "Patarea tulpinilor",
    "Radacini albe sau maronii": "Putrezirea radacinilor",
    "Tulpini ingalbenite si moi": "Putrezirea tulpinilor",
    "Lastari slabiti si cazuti": "Virusul mozaicului tutunului",
    "Frunze galbene si caderea radacinilor": "Patarea radacinilor",
    "Miros puternic de putrefactie": "Fusarioza",
    "Mucegai albicios si sol usor compactat": "Oidium",
    "Frunze atrofiate si caderea florilor": "Botrytis"
    # To add more
}

# Baza de date simulata imaginile corespunzatoare bolilor asociate
disease_images = {
    "Carenta de fier": "carenta_fier.jpg",
    "Mucegaiul pudrei": "mucegai_pudra.jpg",
    "Deficit de azot": "deficit_azot.jpg",
    "Atac de insecte": "atac_insecte.jpg",
    "Fusarioza": "fusarioza.jpg",
    "Putregaiul cenusiu": "putregai_cenusiu.jpg",
    "Carenta de apa": "carenta_apa.jpg",
    "Atac de afide": "atac_afide.jpg",
    "Putregaiul radacinilor": "putregai_radacini.jpg",
    "Exces de udare": "exces_udare.jpg",
    "Atac de ciuperci": "atac_ciuperci.jpg",
    "Cercosporioza": "cercosporioza.jpg",
    "Virusuri de plante": "virusuri_plante.jpg",
    "Atac de trips": "atac_trips.jpg",
    "Oidium": "oidium.jpg",
    "Ruginirea frunzelor": "ruginirea_frunzelor.jpg",
    "Fusarioza radacinilor": "fusarioza_radacini.jpg",
    "Patarea tulpinilor": "patare_tulpini.jpg",
    "Putrezirea radacinilor": "putrezire_radacini.jpg",
    "Putrezirea tulpinilor": "putrezire_tulpini.jpg",
    "Virusul mozaicului tutunului": "virus_mozaic_tutun.jpg",
    "Patarea radacinilor": "patare_radacini.jpg",
    "Botrytis": "botrytis.jpg",
    # To add more
}

# Functia pentru cautarea unui simptom exact in baza de date si returnarea bolii asociate
def search_exact_symptom(symptom):
    if symptom.lower() in database:
        return database[symptom.lower()]
    else:
        return "Nu s-a gasit nicio boala asociata acestui simptom."

# Functia pentru cautarea cuvintelor cheie si simptomelor exacte in baza de date si afisarea bolilor asociate
def search_symptoms(symptoms):
    matched_diseases = []
    if not any(symptoms):
        return ["Nu ati adaugat niciun simptom, va rog adaugați unul!"]
    for symptom in symptoms:
        if symptom:
            # Verifica daca simptomul introdus corespunde exact unui simptom din baza de date
            if symptom.lower() in database:
                matched_diseases.append(f"{symptom.capitalize()} -> {database[symptom.lower()]}")
            else:
                if symptom.lower() in ["radacini"]:
                    matched_diseases.append(
                        "Radacini moi și carunte -> Fusarioza radacinilor\nRadacini albe sau maronii -> Putrezirea radacinilor")
                elif symptom.lower() in ["mucegai"]:
                    matched_diseases.append(
                        "Mucegai albicios pe frunze -> Putregaiul radacinilor\nMucegai verde pe frunze și fructe -> Oidium\nMucegai albicios și sol usor compactat -> Oidium")
                elif symptom.lower() in ["tulpina"]:
                    matched_diseases.append(
                        "Tulpina ingalbenita si invinetita -> Fusarioza\nPete negre pe frunze si tulpini -> Cercosporioza\nPete negre sau maronii pe tulpini -> Patarea tulpinilor\nTulpini ingalbenite si moi -> Putrezirea tulpinilor")
                elif symptom.lower() == "frunze":
                    matched_diseases.append(
                        "Frunze galbene si cazatoare -> Carenta de fier\nFrunze galbene si caderea florilor -> Exces de udare\nFrunze galbene si caderea radacinilor -> Patarea radacinilor")
                else:
                    for key in database.keys():
                        if symptom.lower() in key.lower():
                            matched_diseases.append(f"{key.capitalize()} -> {database[key]}")
                            break
        else:
            matched_diseases.append("Nu ati adaugat niciun simptom, va rog adaugati unul!")
    return matched_diseases

# Functia pentru procesarea simptomelor si returnarea bolilor asociate
def process_symptoms(symptoms):
    matched_diseases = search_symptoms(symptoms)
    return matched_diseases

# Functia pentru generarea simptomelor complete si afisarea bolilor asociate
def generate_symptoms_and_diseases():
    symptoms_and_diseases = []
    for symptom, disease in database.items():
        symptom_description = f"{symptom.capitalize()} -> {disease}"
        symptoms_and_diseases.append(symptom_description)
    return symptoms_and_diseases