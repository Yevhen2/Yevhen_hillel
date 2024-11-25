"""

Ваша команда та ви розробляєте систему входу для веб-додатка.

і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
import os


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити,
    логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f'Login event - Username: {username}, Status: {status}'

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
    )
    logger = logging.getLogger('log_event')

    # Логування події
    if status == 'success':
        logger.info(log_message)
    elif status == 'expired':
        logger.warning(log_message)
    else:
        logger.error(log_message)


def clear_loggers():
    """Clear all active loggers."""
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)


def test_log_success():
    """Verification of successful event logging."""
    clear_loggers()
    username = 'test_user'
    status = 'success'
    log_file = 'login_system.log'

    if os.path.exists(log_file):
        os.remove(log_file)

    log_event(username, status)

    with open(log_file, 'r') as file:
        logs = file.read()
    assert f'Login event - Username: {username}, Status: {status}' in logs


def test_log_expired():
    """Checking event logging with an expired password."""
    clear_loggers()  # Очистити конфігурацію логера
    username = 'expired_user'
    status = 'expired'
    log_file = 'login_system.log'

    if os.path.exists(log_file):
        os.remove(log_file)

    log_event(username, status)

    with open(log_file, 'r') as file:
        logs = file.read()
    assert f'Login event - Username: {username}, Status: {status}' in logs


def test_log_failed():
    """Checking event logging with an incorrect password."""
    clear_loggers()
    username = 'failed_user'
    status = 'failed'
    log_file = 'login_system.log'

    if os.path.exists(log_file):
        os.remove(log_file)

    log_event(username, status)

    with open(log_file, 'r') as file:
        logs = file.read()
    assert f'Login event - Username: {username}, Status: {status}' in logs


print('Start testing...')
test_log_success()
print('test_log_success pass')
test_log_expired()
print('test_log_expired pass')
test_log_failed()
print('test_log_failed pass')
