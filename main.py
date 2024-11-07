from faker import Faker 
 
 
import random 
import file_operations 
import os 
 
 
fake = Faker("ru_RU") 
RUNIC_SKILLS = [] 
ALL_SKILLS = [ 
    "Электрический выстрел", "Стремительный удар", 
    "Огненный заряд", "Ледяной удар", 
    "Стремительный прыжок", "Тайный побег" 
] 
 
 
def main(): 
    for letters in letters_mapping: 
        letter = letters_mapping[letters] 
        ALL_SKILLS[0] = ALL_SKILLS[0].replace(letters, letter) 
        ALL_SKILLS[1] = ALL_SKILLS[1].replace(letters, letter) 
        ALL_SKILLS[2] = ALL_SKILLS[2].replace(letters, letter) 
        ALL_SKILLS[3] = ALL_SKILLS[3].replace(letters, letter) 
        ALL_SKILLS[4] = ALL_SKILLS[4].replace(letters, letter) 
        ALL_SKILLS[5] = ALL_SKILLS[5].replace(letters, letter) 
    RUNIC_SKILLS.append(ALL_SKILLS) 
    os.makedirs("new_folders", mode=0o777, exist_ok=True) 
 
 
if __name__ == "__main__": 
    letters_mapping = { 
        'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠', 
        'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠', 
        'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠', 
        'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋', 
        'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒', 
        'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠', 
        'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠', 
        'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋', 
        'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋', 
        'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋', 
        'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋', 
        'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠', 
        'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е', 
        'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠', 
        'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋', 
        'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒', 
        'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠', 
        'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠', 
        'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋', 
        'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋', 
        'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋', 
        'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋', 
        ' ': ' ' 
    } 
    RUNIC_SKILLS 
    ALL_SKILLS 
    main() 
    for result_file in range(10):
        skill_sample = random.sample(ALL_SKILLS, 3) 
        skill_1 = skill_sample[0] 
        skill_2 = skill_sample[1] 
        skill_3 = skill_sample[2] 
        context = { 
            "first_name": fake.first_name_female(), 
            "last_name": fake.last_name_female(), 
            "job": fake.job(), 
            "town": fake.city(), 
            "strength": random.randint(1, 10),
            "agility": random.randint(1, 10),
            "endurance": random.randint(1, 10),
            "intelligence": random.randint(1, 10),
            "luck": random.randint(1, 10),
            "skill_1": skill_1, 
            "skill_2": skill_2, 
            "skill_3": skill_3 
            }  
        file_name = "result.svg" 
        file_name = (f'{result_file}{file_name}') 
        folder_name = "new_folders" 
        folder_path = os.path.join(folder_name, file_name) 
        file_operations.render_template("charsheet.svg", folder_path, context)