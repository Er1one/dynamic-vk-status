# dynamic-vk-status
Динамическая смена статуса страницы ВКонтакте

Требуется Python 3 + библиотеки vk_api, pyyaml
```
pip3 install vk_api
pip3 install pyyaml
```

Запуск: 
```
python3 main.py
```

## Настройка
1. Отредактируйте файл `settings.yml`
```
# Логин от ВКонтакте (Желательно номер, так как это помогает избежать доп. проверку)
vk-login: "74953583557"
# Пароль от ВКонтакте
vk-password: "SverxyUkazanNomerDurki"
# Нежелательно ставить значение менее, чем 20 секунд, так как у ВК есть защита от флуда запросами
timeout: 25
```

2. Внесите свои статусы в файл `statuses.txt` (Каждый новый статус - новая строка)
```
Мам, я программист
Этот статус меняется каждые 25 секунд :D
Java & Python developer www.github.com/Er1one
Ты и правда читаешь это?
Покажи мне свой код, и я скажу кто ты
Огурчики свежие, по 45 рублей - килограмм у меня в личке
```
