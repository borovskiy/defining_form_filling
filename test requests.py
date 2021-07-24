import requests

print('Тест 1')
get_req = requests.post('http://127.0.0.1:5000', data={'f_name1': 'value1', 'f_name6': '+79503886510'})
print(get_req.text)
print()
print('Тест 2')
get_req2 = requests.post('http://127.0.0.1:5000', data={'field_name_3': '24.06.1991',
                                                        'field_name_4': 'ru@yandex.ru',
                                                        'field_name_5': '+79503886510',
                                                        'field_name_6': '+79503886510',
                                                        'field_name_7': 'cccccc', })
print(get_req2.text)
print()
print('Тест 3')
get_req3 = requests.post('http://127.0.0.1:5000', data={'field_name_5': '+79503886510',
                                                        'field_name_6': '+79503886510',
                                                        'field_name_7': 'cccccc', })
print(get_req3.text)
print()
print('Тест 4')
get_req4 = requests.post('http://127.0.0.1:5000', data={'field_name_6': '+79503886510',
                                                        'field_name_7': 'cccccc', })
print(get_req4.text)
