import datetime


def telephone_check(enter_string_data: str) -> bool:
    """функция проверки числа на принадлежность к номеру телефона"""
    if enter_string_data[0] == '8':
        truncated_number = enter_string_data[1:]
    elif enter_string_data[0:2].strip() in ['7', '+7']:
        truncated_number = enter_string_data[1:]
    else:
        return False
    if truncated_number.isdigit():
        return True
    else:
        return False


def validate_email(string: str) -> bool:
    string_after_point = string.split('.')[-1]
    string_after_dog = string.split('@')[-1].replace('.' + string_after_point, '')
    if string_after_point.isalpha() and string_after_dog.isalpha():
        name_email = string.split('@')[0]
        if name_email.find('._-') == -1 and name_email[-1] not in ['.', '-', '_', ] and name_email[0] not in ['.', '-',
                                                                                                              '_', ]:
            return True
    return False


def date_check(enter_string_date: str) -> bool:
    """Функция проверки даты на валидность"""
    try:
        if len(enter_string_date) == 10 and enter_string_date.count('.') == 2:
            if enter_string_date[:6].count('.') == 2:
                datetime.datetime.strptime(enter_string_date, '%d.%m.%Y')
                return True
            elif enter_string_date[:6].count('.') == 1:
                datetime.datetime.strptime(enter_string_date, '%Y.%m.%d')
                return True
            else:
                return False
    except ValueError:
        return False


def check_data(value_data: str) -> str:
    if date_check(value_data):
        return 'date'
    elif telephone_check(value_data):
        return 'phone'
    elif '.' and '@' in value_data and validate_email(value_data):
        return 'email'
    else:
        return 'string'


def counting_field_types(dict_request_args):
    """Функция подсчета типов полей"""
    dict_count_data = {'string': 0, 'email': 0, 'phone': 0, 'date': 0, }
    for key, value in dict(dict_request_args).items():
        result = check_data(value)
        if result == "email":
            dict_count_data['email'] += 1
        elif result == "phone":
            dict_count_data['phone'] += 1
        elif result == "string":
            dict_count_data['string'] += 1
        elif result == "date":
            dict_count_data['date'] += 1
    return dict_count_data


def list_name_template(db, request_args) -> dict or str:
    """Функция создания словаря в зависимости от обработки данных"""
    request_args = dict(request_args)
    dict_name_templates = {}
    dict_data_post_fields = counting_field_types(request_args)
    for template in db:
        email_count_in_db = list(template.values()).count('email')
        phone_count_in_db = list(template.values()).count('phone')
        date_count__in_db = list(template.values()).count('date')
        string_count_in_db = list(template.values()).count('string')

        if dict_data_post_fields['email'] >= email_count_in_db and \
                dict_data_post_fields['phone'] >= phone_count_in_db and \
                dict_data_post_fields['date'] >= date_count__in_db and \
                dict_data_post_fields['string'] >= string_count_in_db:
            dict_name_templates.update({template['name']: template})
    if len(dict_name_templates) <= 0:
        dict_name_templates = request_args
        for key, value in dict_name_templates.items():
            dict_name_templates.update({key: {value: check_data(value)}})
        return dict_name_templates
    else:
        return max_len_template(dict_name_templates)


def max_len_template(dicts: dict) -> str:
    """Функция для отбора самой большой из совпавших форм"""
    max_len_templates = {}
    for values in dicts.values():
        if len(values) > len(max_len_templates):
            max_len_templates = values
    return max_len_templates['name']
