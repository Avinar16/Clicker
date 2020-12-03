import csv


class Config:
    def __init__(self):
        self.filename = 'config.csv'
        self.config = None
        self.readConfig()

    def readConfig(self):
        with open(self.filename, 'r', encoding='utf-8') as config_file:
            reader = csv.DictReader(config_file, delimiter=';', quotechar='"')
            self.config = list(reader)[0]

    def saveConfig(self):
        with open(self.filename, 'w', encoding='utf-8', newline='') as config_file:
            writer = csv.DictWriter(config_file, fieldnames=self.config.keys(), delimiter=";")
            writer.writeheader()
            writer.writerow(self.config)

    def setValue(self, param_name, param_value, need_save_to_file=True):
        self.config[param_name] = param_value
        if need_save_to_file:
            self.saveConfig()

    def getValue(self, param_name):
        return self.config[param_name]
