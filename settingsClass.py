import json


class JsonShell():

    def __init__(self, filePath=str, encoding='utf-8'):
        self.filePath = filePath
        self.encoding = encoding
        self.data = self.__open()

    def __open(self):
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
        if filePath is None:
            filePath = self.filePath
        with open(file=filePath, mode='w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    def get(self):
        return self.data

    def put(self, data=str):
        self.data = data
