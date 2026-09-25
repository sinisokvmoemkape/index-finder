print('''
╔══════════════════════════════╗
║                              ║
║       Индекс помощник        ║
║                              ║
╚══════════════════════════════╝
''')
user_list = []
txt = ('ВСТАВЬТЕ ТЕКСТ ИЗ ВАШЕГО СПИСКА ЧЕРЕЗ ЗАПЯТУЮ' '\n' '>>> ')
user_list.extend(input(txt).split(','))



print(user_list)

variants = ('1) УЗНАТЬ ИНДЕКС ОБЬЕКТА В СПИСКЕ',
            '2) УЗНАТЬ ИНДЕКС РАСПОЛОЖЕНИЯ ОБЬЕКТА ПОСЛЕ .JOIN')
for i in variants:
    print(i)

vvod1 = int(input('Выберите Опцию (1 - 2) ' '\n' '>>> '))
if vvod1 == 1:
    print
    vvod2 = str(input('Введите название обьекта индекс которого будет выведен:' '\n' '>>> '))
    txt1 = 'Индекс - '
    indx = user_list.index(vvod2)

    print(vvod2.upper())
    print(txt1, indx)   

elif vvod1 == 2:
    inf = ','.join(user_list)
    print(inf)
    vvod2 = (input('Введите название обьекта если хотите узнать его раcположение:' '\n' '>>> '))
    vivod1 = inf.find(vvod2)
    vivod2 = vivod1 + len(vvod2)
    
    print(vvod2.upper())
    print(vivod1, ':', vivod2)

    # print(inf[6:13])
