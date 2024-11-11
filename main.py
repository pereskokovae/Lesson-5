from faker import Faker


import random
import file_operations
import os


LETTERS_MAPPING = {
    'а': 'а͠',
    'б': 'б̋',
    'в': 'в͒͠',
    'г': 'г͒͠',
    'д': 'д̋',
    'е': 'е͠',
    'ё': 'ё͒͠',
    'ж': 'ж͒',
    'з': 'з̋̋͠',
    'и': 'и',
    'й': 'й͒͠',
    'к': 'к̋̋',
    'л': 'л̋͠',
    'м': 'м͒͠',
    'н': 'н͒',
    'о': 'о̋',
    'п': 'п̋͠',
    'р': 'р̋͠',
    'с': 'с͒',
    'т': 'т͒',
    'у': 'у͒͠',
    'ф': 'ф̋̋͠',
    'х': 'х͒͠',
    'ц': 'ц̋',
    'ч': 'ч̋͠',
    'ш': 'ш͒͠',
    'щ': 'щ̋',
    'ъ': 'ъ̋͠',
    'ы': 'ы̋͠',
    'ь': 'ь̋',
    'э': 'э͒͠͠',
    'ю': 'ю̋͠',
    'я': 'я̋',
    'А': 'А͠',
    'Б': 'Б̋',
    'В': 'В͒͠',
    'Г': 'Г͒͠',
    'Д': 'Д̋',
    'Е': 'Е',
    'Ё': 'Ё͒͠',
    'Ж': 'Ж͒',
    'З': 'З̋̋͠',
    'И': 'И',
    'Й': 'Й͒͠',
    'К': 'К̋̋',
    'Л': 'Л̋͠',
    'М': 'М͒͠',
    'Н': 'Н͒',
    'О': 'О̋',
    'П': 'П̋͠',
    'Р': 'Р̋͠',
    'С': 'С͒',
    'Т': 'Т͒',
    'У': 'У͒͠',
    'Ф': 'Ф̋̋͠',
    'Х': 'Х͒͠',
    'Ц': 'Ц̋',
    'Ч': 'Ч̋͠',
    'Ш': 'Ш͒͠',
    'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠',
    'Ы': 'Ы̋͠',
    'Ь': 'Ь̋',
    'Э': 'Э͒͠͠',
    'Ю': 'Ю̋͠',
    'Я': 'Я̋',
    ' ': ' '
}
ALL_SKILLS = [
    "Электрический выстрел",
    "Стремительный удар",
    "Огненный заряд",
    "Ледяной удар",
    "Стремительный прыжок",
    "Тайный побег"
]


def main():
    runic_skills = ALL_SKILLS.copy()
    for letters in LETTERS_MAPPING:
        letter = LETTERS_MAPPING[letters]
        for cyrillic_skills in runic_skills:
            cyrillic_skills = cyrillic_skills.replace(letters, letter)
    os.makedirs("new_folders", mode=0o777, exist_ok=True)
    for result_file in range(10):
        skill_sample = random.sample(cyrillic_skills, 3)
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


if __name__ == "__main__":
    fake = Faker("ru_RU")
    runic_skills = []
    main()
