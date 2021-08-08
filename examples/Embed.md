# DISCORD EMBED

#

## Создание Embed
```py
embed_variable = discord.Embed(
    title='title',                  # заголовок Embed
    type='rich',                    # тип Embed
    description='description',      # описание Embed
    color=0xff0000,                 # цвет в hex
    url='https://www.youtube.com/'  # ссылка Embed
)
```
##### Типы embed
* rich (типичный эмбэд, используется чаще всего ботами)
* link (обычная ссылка)
* video (обычная ссылка, например видео с youtube)

#### результат
![image](./misc/images/0644.jpg)

#

## Нижний "колонтитул"
```py
embed_variable.set_footer(
    text='footer name',                               # содержание нижнего колонтитула
    icon_url='https://jooinn.com/images/links-4.png'  # ссылка на изображение колонтитула
    )
```

#### результат
![image](./misc/images/0642.jpg)

#

## Добавление изображения к Embed
```py
embed_variable.set_image(
    url='https://img.icons8.com/cotton/2x/image--v2.png' # ссылка на изображение
    )
```

#### результат
![image](./misc/images/0646.jpg)

#

## Добавление миниатюры
```py
embed_variable.set_thumbnail(
    url='https://img.icons8.com/ios/452/image.png'
    )
```

#### результат
![image](./misc/images/0647.jpg)

#

## Добовление автора к Embed
```py
embed_variable.set_author(
    name='author name',               # имя автора
    url='https://www.youtube.com/',   # ссылка с текста
    icon_url='https://clck.ru/Wg72M'  # сылка на изображение
    )

# embed_variable.remove_author()       # удаление поля
```

#### результат
![image](./misc/images/0647.jpg)

#

## Добавление поле в Embed
```py
embed_variable.add_field(
    name='name0',          # Имя поля
    value='inline',        # Значения, описание поля
    inline=True            # 'В линию' позиционирует текст в линию (Не переносит на следующую строку, удобно для выстраивания таблиц)
)
embed_variable.add_field(
    name='name1',          # Имя поля
    value='inline',        # Значения, описание поля
    inline=True            # 'В линию' позиционирует текст в линию (Не переносит на следующую строку, удобно для выстраивания таблиц)
)
embed_variable.add_field(
    name='name2',          # Имя поля
    value='inline false',  # Значения, описание поля
    inline=False           # 'В линию' позиционирует текст в линию (Не переносит на следующую строку, удобно для выстраивания таблиц)
)
```
#

## Вставка поля по индексу
```py
embed_variable.insert_field_at(
    index=3,
    name='name00',
    value='value00',
    inline=True
)
embed_variable.insert_field_at(
    index=3,
    name='name11',
    value='value11',
    inline=True
)
```

#### результат
![image](./misc/images/0649.jpg)

#

## Модификация полей Embed
```py
embed_variable.set_field_at(
    index=0,             # позиция замены
    name='insert_0',     # заголовок
    value='insert_0',    # описание
    inline=True          # позиционирование
)
embed_variable.set_field_at(
    index=1,             # позиция замены
    name='insert_1',     # заголовок
    value='insert_1',    # описание
    inline=True          # позиционирование
)
```

#### результат
![image](./misc/images/0650.jpg)

#

## Удаление полей
```py
# удаление по индексу
embed_variable.remove_field(
    index=0
)
# очистка полей
embed_variable.clear_fields()
```
