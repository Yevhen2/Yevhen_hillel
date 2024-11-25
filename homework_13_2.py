"""
Провалідуйте, чи усі файли у папці.

ideas_for_test/work_with_json є валідними json.
результат для невалідного файлу
виведіть через логер на рівні еррор у файл json__<your_second_name>.log

"""

import json
import logging
from pathlib import Path

import requests


def validate_json_files(output_log_file: str, json_urls: list):
    """
    Завантажує JSON-файли з URL.

    перевіряє їх валідність і логує помилки у файл.
    """
    logging.basicConfig(
        filename=output_log_file,
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )

    print(f'Лог файл: {output_log_file}')

    """Temporary folder for saving files."""
    temp_folder = Path('temp_json_files')
    temp_folder.mkdir(exist_ok=True)

    for url in json_urls:
        print(f'Обробка: {url}')
        try:
            response = requests.get(url)
            response.raise_for_status()

            """Save the downloaded file."""
            file_name = url.split('/')[-1]
            file_path = temp_folder / file_name
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(f'Файл збережено: {file_path}')

            """JSON validation"""
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    json.load(file)
                print(f'Файл {file_name} валідний')
            except json.JSONDecodeError as e:
                logging.error(f'Файл {file_name} невалідний: {e}')
                print(f'Помилка: файл {file_name} невалідний')

        except requests.RequestException as e:
            logging.error(f'Не вдалося завантажити файл з {url}: {e}')
            print('Не вдалося завантажити файл:')


json_urls = [
    'https://raw.githubusercontent.com/dntpanix/automation_qa/main/'
    'ideas_for_test/work_with_json/localizations_en.json',

    'https://raw.githubusercontent.com/dntpanix/automation_qa/main/'
    'ideas_for_test/work_with_json/localizations_ru.json',

    'https://raw.githubusercontent.com/dntpanix/automation_qa/'
    'refs/heads/main/ideas_for_test/work_with_json/login.json',

    'https://raw.githubusercontent.com/dntpanix/automation_qa/'
    'refs/heads/main/ideas_for_test/work_with_json/swagger.json',
]

validate_json_files('json__nakhaba.log', json_urls)
