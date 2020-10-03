#Канал приветсвия
# ID канала для приветсвия новых участников гильдии (сервера)
WELCOME_CHANNEL_ID = 599993493208956930
# Случайные приветсвия. @Name+'description'
WELCOME_REACTION = [
            '. добро пожаловать, сенпай !',
            ', приятно познакомиться~!',
            '. чувствуй себя как дома!',
            ', осматривайся и знакомся~'
        ]

#Настройка канала с правилами
# ID сообщения с правилами
RULE_MESSAGE_ID = 749871626849484831
# Emoji согласия с правилами
RULE_ACCEPT_EMOJI = '✅'
# Роль выдаваемая при согласии с правилами
RULE_ACCEPT_ROLE = 625711440975626282

#Настройка автоматической выдачи ролей по emoji
# ID сообщения с реакциями
ROLE_MESSAGE_ID = 761982318927020052
# Список ролей и их аналог в виде emoji
ROLE_EMOJI_ROLE = {
    '🔪' : 760832315466711070, #Among As
    '🔫' : 738066613621882942, #CS:GO
    '↗️' : 738005330990071858, #Dota 2
    '🏹' : 731421506961408060, #Valorant
    '🧠' : 761997590068723743, #minecraft
    '⚓' : 761999284693368842 #Azur Lane
    }
# Максимальное возможное количество ролей на одного участника гильдии (сервера)
ROLE_MAX_NUMBER_ROLE_PER_USER = 24
# Роли не используемые при счёте максимального количества ролей
ROLE_EXCEPTION = (

)

#Остальные роли
# Роль админов
ROLE_ADMIN = 'Role'
# Роль модераторов
ROLE_MODERATOR = 'Role'