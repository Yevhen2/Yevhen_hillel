"""
Для файла ideas_for_test/work_with_xml/groups.xml.

створіть функцію пошуку по group/number і повернення значення
timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо

"""

import logging
from xml.etree import ElementTree as ET
import requests
from pathlib import Path


def setup_logger(log_file: str):
    """
    Configures the logger to write messages to the specified log file.

    :param log_file: Path to the log file.
    """
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


def download_and_parse_xml(url: str, temp_file: Path) -> ET.Element:
    """
    Downloads an XML file from the given URL and parses it.

    :param url: URL of the XML file to download.
    :param temp_file: Path to save the temporary file locally.
    :return: The root element of the parsed XML.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raises HTTPError for bad responses

    # Save the file locally
    with open(temp_file, 'wb') as file:
        file.write(response.content)

    # Parse the XML and return the root element
    tree = ET.parse(temp_file)
    return tree.getroot()


def find_timing_by_group_number(xml_root: ET.Element, group_number: str):
    """
    Finds the `timingExbytes/incoming` value for a specific `group/number`

    in the XML file.

    :param xml_root: The root element of the XML file.
    :param group_number: The group number to search for.
    :return: The value of `timingExbytes/incoming` if found, otherwise None.
    """
    for group in xml_root.findall('./group'):
        number = group.find('number')
        if number is not None and number.text == group_number:
            timing = group.find('timingExbytes/incoming')
            if timing is not None:
                logging.info(f'Value for group/number={group_number}: '
                             f'{timing.text}')
                print(f'INFO: Value for group/number={group_number}: '
                      f'{timing.text}')
                return timing.text

    logging.info(f'Value for group/number={group_number} not found.')
    print(f'INFO: Value for group/number={group_number} not found.')
    return None


# Configuration
log_file = 'xml__nakhaba.log'
setup_logger(log_file)

# URL of the XML file
xml_url = ('https://raw.githubusercontent.com/dntpanix/automation_qa/'
           'main/ideas_for_test/work_with_xml/groups.xml')
temp_xml_file = Path('groups_temp.xml')

# Download and parse XML file
try:
    xml_root = download_and_parse_xml(xml_url, temp_xml_file)

    # Search for a specific group/number
    find_timing_by_group_number(xml_root, '5')  # Replace
except Exception as e:
    logging.error(f'Error: {str(e)}')
    print(f'ERROR: {str(e)}')
