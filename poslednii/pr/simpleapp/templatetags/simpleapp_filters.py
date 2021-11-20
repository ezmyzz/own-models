from django import template

register = template.Library()

# словарь для замены слов в статье на их цензурные аналоги)
censor_dict = {'Проект': 'П////', 'Курсы': 'К////', 'Ментор': 'М////',
               'COVID-19': 'C////'}


@register.filter(name='censor')
def censor(value):
    if isinstance(value, str):
        result = str(value)
        for key in censor_dict.keys():
            result = result.replace(key, censor_dict[key])
        return result
    else:
        raise ValueError(f'Нельзя отфильтровать тип, отличный от {type(value)}')
