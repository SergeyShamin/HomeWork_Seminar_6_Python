#Определить, присутствует ли в заданном списке строк, некоторое число

list_string = ['Мои мечты стремятся вдаль,',
'Где слышны вопли и рыданья,',
'Чужую разделить печаль',
'И муки тяжкого страданья.',
'Я там1 могу найти себе',
'Отраду в жизни, упоенье,',
'И там, наперекор судьбе,',
'Искать я буду вдохновенья.']
a = 1
print(len(list(filter(lambda text: str(a) in text, list_string))) > 0)