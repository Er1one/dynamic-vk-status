# -*- coding: utf-8 -*-
import sys

import vk_api
import time
import yaml


def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция.
    """

    # Код двухфакторной аутентификации
    key = input("| Введите код 2fa авторизации: ")

    # Если: True - сохранить, False - не сохранять.
    remember_device = Truef

    return key, remember_device


def captcha_handler(captcha):
    """ При возникновении капчи вызывается эта функция и ей передается объект
        капчи. Через метод get_url можно получить ссылку на изображение.
        Через метод try_again можно попытаться отправить запрос с кодом капчи
    """

    key = input("| Введите капчу {0}: ".format(captcha.get_url())).strip()

    # Пробуем снова отправить запрос с капчей
    return captcha.try_again(key)


def getStatuses():
    """ Получение всех строк из файла
    """

    lines = []

    # Открываем файл в кодировке utf-8
    file = open("statuses.txt", encoding='utf-8')
    # Перебираем каждую строчку в файле и добавляем ее в список
    for i in file.readlines():
        lines.append(i)

    # Закрываем файл
    file.close()

    return lines


def sleep(timeout):
    """ Функция добавляет анимацию анимации
    """

    # Перебираем от 1 до указанного таймаута
    for i in range(1, timeout):
        # Выводим новую строку с модификатором \r, который заменяет прошлую строку
        sys.stdout.write("\r| Ожидание")

        # Добавляем к прошлой строке точку
        for j in range(i):
            sys.stdout.write(".")
            sys.stdout.flush()

        # Ждем 1 секунду
        time.sleep(1)

    # Возвращаемся к прошлой строке о очищаем ее
    sys.stdout.flush()
    sys.stdout.write("\r")


def main():
    """ Открываем файл с настройками и записываем каждое значение в перменную
    """

    with open("settings.yaml") as file:
        auth = yaml.load(file, Loader=yaml.FullLoader)
        login = auth["vk-login"]
        password = auth["vk-password"]
        timeout = int(auth["timeout"])

    # Указание данных для VkApi
    vk_session = vk_api.VkApi(login, password, auth_handler=auth_handler, captcha_handler=captcha_handler)
    vk = vk_session.get_api()

    # Выводим информацию для пользователя
    print("| -- VkDynamicStatus by Er1one (vk.com/er1one) -- ")
    print("| ")
    print("| Загружено " + str(len(getStatuses())) + " статусов")

    # Попытка авторизации от имени страницы
    try:
        vk_session.auth()

    # Если пароль неверный, то оповещаем пользователя и прекращаем выполнение программы
    except vk_api.exceptions.BadPassword:
        print("| Неверный пароль, проверьте его в файле settings.yaml")
        return

    # Выводим информацию о странице (Имя, фамилию, короткую ссылку)
    print("| Вы вошли как {0} {1} (vk.com/{2})"
          .format(vk.account.getProfileInfo()['last_name'],
                  vk.account.getProfileInfo()['first_name'],
                  vk.account.getProfileInfo()['screen_name']))

    # Ждем 3 секунды
    time.sleep(3)

    # Постоянно: Перебираем список со статусами
    while True:
        for i in getStatuses():
            # Устанавливаем статус
            vk.status.set(text=i)

            # Оповещаем пользователя об установке статуса
            print(f'| Установил статус на "{i.strip()}"')

            # Ждем таймаут
            sleep(timeout)


if __name__ == "__main__":
    main()
