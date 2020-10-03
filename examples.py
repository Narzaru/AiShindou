#DON'T IMPORT THIS FILE ANYWHERE
import discord

#Embed
# Создание переменной типа Embed https://imgur.com/a/b2nD9ST
embedVariable = discord.Embed(
    title='title',                  #Название Embed
    type='rich',                    #Тип Embed https://discord.fandom.com/ru/wiki/%D0%AD%D0%BC%D0%B1%D0%B5%D0%B4
    description='description',      #Описание Embed
    color=0xff0000,                 #Цвет полосы слева color=hex
    url='https://www.youtube.com/', #Ссылка куда ведёт Embed
    )

# Добавление нижнего колонтитула в Embed https://imgur.com/DTjUu8u
embedVariable.set_footer(
    text='footer name',                                                     #Задаёт имя нижнего колонтитула
    icon_url='https://media.giphy.com/media/wCMa5t06BdI2DUVIN9/giphy.gif'   #Задаёт изображение левее имени нижнего колонтитула
    )

# Добавление изображения к Embed https://imgur.com/a/FKGqn5a
embedVariable.set_image(
    url='https://media.giphy.com/media/wCMa5t06BdI2DUVIN9/giphy.gif'
    )

# Добавление миниатюры справа от title https://imgur.com/a/zugJskS
embedVariable.set_thumbnail(
    url='https://media.giphy.com/media/wCMa5t06BdI2DUVIN9/giphy.gif'
    )

# Добовление автора к Embed https://imgur.com/a/mUdWcno
embedVariable.set_author(
    name='author name',                                                             #Имя автора
    url='https://www.youtube.com/',                                                 #Ссылка на автора
    icon_url='https://logosklad.ru/UserFiles/image/youtube/YTLogo_old_new_1680.gif' #Сылка на картинку автора
    )

# Удаляет поле с автором https://imgur.com/a/7VTv3Pe
embedVariable.remove_author()

# Добавляет поле в Embed https://imgur.com/a/qWlrV2a
embedVariable.add_field(
    name='name0',   #Имя поля
    value='0',      #Значения, описание поля
    inline=True     #'В линию' позиционирует текст в линию (Не переносит на следующую строку, удобно для выстраивания таблиц)
)
embedVariable.add_field(
    name='name1',   #Имя поля
    value='0',      #Значения, описание поля
    inline=True     #'В линию' позиционирует текст в линию (Не переносит на следующую строку, удобно для выстраивания таблиц)
)
embedVariable.add_field(
    name='name2',   #Имя поля
    value='0',      #Значения, описание поля
    inline=True     #'В линию' позиционирует текст в линию (Не переносит на следующую строку, удобно для выстраивания таблиц)
)

# Вставляет поле на определённое место
embedVariable.insert_field_at(
    index=0,
    name='0',
    value='0',
    inline=True
)

# Модификация Embed
embedVariable.set_field_at(
    index=0,
    name='0',
    value=0,
    inline=True
)

# Удаляет поле с определённого места
embedVariable.remove_field(
    index=0
)

# Удаляет все добалвенные поля с Embed
embedVariable.clear_fields()