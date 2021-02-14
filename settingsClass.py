import json

class JsonShell():

    def __init__(self, filePath=str, encoding='utf-8'):
        self.filePath = filePath
        self.encoding = encoding
        self.data = self.open()

    def open(self):
        try:
            with open(file=self.filePath, mode='r', encoding=self.encoding) as file:
                return json.load(file)
        except FileNotFoundError:
            print(f'{self.filePath} [ERROR] No such file or directory')
            return None
        except json.decoder.JSONDecodeError:
            print(f'[ERROR] Json Expecting delimiter')
            return None

    def dump(self, filePath=None):
        if filePath == None:
            filePath = self.filePath
        with open(file=filePath, mode='w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    def get(self):
        return self.data

    def put(self, data=str):
        self.data = data

'''{
    "599993492382416907": {
        "WELCOME_CHANNEL_ID": "599993493208956930",
        "WELCOME_CHANNEL_REACTION": [
            ", добро пожаловать, сенпай !",
            ", приятно познакомиться~!   ",
            ", чувствуй себя как дома!   ",
            ", осматривайся и знакомься~ "
        ],
        "RULE_MESSAGE_ID": "762339000676909066",
        "RULE_ACCEPT_EMOJI": "✅",
        "RULE_ACCEPT_ROLE": "625711440975626282",
        "ROLE_MESSAGE_ID": "770836261879545897",
        "ROLE_BY_EMOJI": {
            "🔪": "760832315466711070",
            "🔫": "738066613621882942",
            "↗️": "738005330990071858",
            "🏹": "731421506961408060",
            "🧠": "761997590068723743",
            "⚓": "761999284693368842",
            "🦿": "770834462514741258"
        },
        "EXCLUDE_ROLES": [
            600195592446017536,
            600021636942397484,
            600020445160538112,
            600020896933085304,
            600021126667698261,
            625711440975626282,
            599993492382416907
        ],
        "MAX_ROLE_PER_USER": "24",
        "ROLE_ADMIN": {
            "NAME": "Admin",
            "ID": "600021636942397484"
        }
    }
}'''