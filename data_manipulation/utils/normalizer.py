
class Normalizer:

    def __init__(self) -> None:
        pass

    
    def get_all_main_accords(self, data):
        main_accords = set()  # Usaremos un conjunto para evitar duplicados

        for item in data:
            if "main_accords" in item:  # Verificamos si la clave "main_accords" está presente
                accords = item["main_accords"]
                for accord in accords:  # Verificamos si la clave "Accord" está presente
                    if(main_accords.__contains__(accord["Accord"]) == False):
                        main_accords.add(accord["Accord"])
        return list(main_accords)

    def get_all_top_notes(self, data):
        top_notes = set()  # Usaremos un conjunto para evitar duplicados

        for item in data:
            if "top_notes" in item:
                notes = item["top_notes"]
                for note in notes:
                    if(top_notes.__contains__(note) == False):
                        top_notes.add(note)
        return list(top_notes)
    
    def get_all_middle_notes(self, data):
        middle_notes = set()  # Usaremos un conjunto para evitar duplicados

        for item in data:
            if "middle_notes" in item:
                notes = item["middle_notes"]
                for note in notes:
                    if(middle_notes.__contains__(note) == False):
                        middle_notes.add(note)
        return list(middle_notes)
    
    def get_all_base_notes(self, data):
        base_notes = set()

        for item in data:
            if "base_notes" in item:
                notes = item["base_notes"]
                for note in notes:
                    if(base_notes.__contains__(note) == False):
                        base_notes.add(note)
        return list(base_notes)

    # Normalizing data

    def normalizing_main_accords(self, fragance_row, main_accords):
        return_data = []
        accord_value = 0
        for accord in main_accords:
            if "main_accords" in fragance_row:
                for item in fragance_row["main_accords"]:
                    if item["Accord"] == accord:
                        accord_value = float(item["Value"]).__round__(2) 
                        break
                    else:
                        accord_value = 0
                return_data.append({accord: accord_value})
        return return_data
    
    def normalizing_top_notes(self, fragance_row, top_notes):
        top_notes_dict = dict.fromkeys(top_notes, 0)
        if "top_notes" in fragance_row:
            for item in fragance_row["top_notes"]:
                top_notes_dict[item] = 1
        return top_notes_dict
    
    def normalizing_middle_notes(self, fragance_row, middle_notes):
        middle_notes_dict = dict.fromkeys(middle_notes, 0)
        if "middle_notes" in fragance_row:
            for item in fragance_row["middle_notes"]:
                middle_notes_dict[item] = 1
        return middle_notes_dict
    
    def normalizing_base_notes(self, fragance_row, base_notes):
        base_notes_dict = dict.fromkeys(base_notes, 0)
        if "base_notes" in fragance_row:
            for item in fragance_row["base_notes"]:
                base_notes_dict[item] = 1
        return base_notes_dict
    

    def flatten_data(self, data, main_accords, top_notes, middle_notes, base_notes):
        flattened_data = []
        for item in data:
            flattened_item = {
                "id": item["_id"]["$oid"],
                "idNumber": item["idNumber"],
                "name": item["name"],
                "link": item["link"] if "link" in item else "",
                "img": item["img"] if "img" in item else "",
                "designer": item["designer"],
                "official_gender": item["official_gender"],
                "rating": item["rating"],
                "votes": item["votes"],
                "winter": item["seasons"]["winter"],
                "summer": item["seasons"]["summer"],
                "autumn": item["seasons"]["autumn"],
                "spring": item["seasons"]["spring"],
                "day": item["hours"]["day"],
                "night": item["hours"]["night"],
                "longevity_very_weak": item["fragance_aspects"]["longevity"]["very weak"],
                "longevity_weak": item["fragance_aspects"]["longevity"]["weak"],
                "longevity_moderate": item["fragance_aspects"]["longevity"]["moderate"],
                "longevity_long_lasting": item["fragance_aspects"]["longevity"]["long lasting"],
                "longevity_very_eternal": item["fragance_aspects"]["longevity"]["eternal"],
                "sillage_intimate": item["fragance_aspects"]["sillage"]["intimate"],
                "sillage_moderate": item["fragance_aspects"]["sillage"]["moderate"],
                "sillage_strong": item["fragance_aspects"]["sillage"]["strong"],
                "sillage_enormous": item["fragance_aspects"]["sillage"]["enormous"],
                "gender_female": item["fragance_aspects"]["gender"]["female"],
                "gender_more_female": item["fragance_aspects"]["gender"]["more female"],
                "gender_unisex": item["fragance_aspects"]["gender"]["unisex"],
                "gender_more_male": item["fragance_aspects"]["gender"]["more male"],
                "gender_male": item["fragance_aspects"]["gender"]["male"],
                "fragance_aspects": item["fragance_aspects"],
                "main_accords": self.normalizing_main_accords(item, main_accords),
                "top_notes": self.normalizing_top_notes(item, top_notes),
                "middle_notes": self.normalizing_middle_notes(item, middle_notes),
                "base_notes": self.normalizing_base_notes(item, base_notes)
            }
            flattened_data.append(self.flatten_json(flattened_item))
        return flattened_data
    
    def flatten_json(self, y):
        out = {}
    
        def flatten(x, name=''):
    
            # If the Nested key-value
            # pair is of dict type
            if type(x) is dict:
    
                for a in x:
                    flatten(x[a], name + a + '_')
    
            # If the Nested key-value
            # pair is of list type
            elif type(x) is list:
    
                i = 0
    
                for a in x:
                    flatten(a, name)
                    i += 1
            else:
                out[name[:-1]] = x
    
        flatten(y)
        return out