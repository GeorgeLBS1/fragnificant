
class Normalizer:
    def get_all_main_accords(data):
        main_accords = set()  # Usaremos un conjunto para evitar duplicados

        for item in data:
            if "main_accords" in item:  # Verificamos si la clave "main_accords" está presente
                accords = item["main_accords"]
                for accord in accords:  # Verificamos si la clave "Accord" está presente
                    main_accords.add(accord["Accord"])

        return list(main_accords)

    def get_all_top_notes(data):
        top_notes = set()  # Usaremos un conjunto para evitar duplicados

        for item in data:
            if "top_notes" in item:
                notes = item["top_notes"]
                for note in notes:
                    top_notes.add(note)

        return list(top_notes)

    def get_all_middle_notes(data):
        middle_notes = set()  # Usaremos un conjunto para evitar duplicados

        for item in data:
            if "middle_notes" in item:
                notes = item["middle_notes"]
                for note in notes:
                    middle_notes.add(note)

        return list(middle_notes)