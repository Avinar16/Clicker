import csv


class Config:
    def __init__(self, filename):
        self.filename = filename
        self.config = None

    def readConfig(self, index=0):
        with open(self.filename, 'r', encoding='utf-8') as config_file:
            reader = csv.DictReader(config_file, delimiter=';', quotechar='"')
            self.config = list(reader)[index]

    def saveConfig(self):
        with open(self.filename, 'w', encoding='utf-8', newline='') as config_file:
            writer = csv.DictWriter(config_file, fieldnames=self.config.keys(), delimiter=";")
            writer.writeheader()
            writer.writerow(self.config)

    def setValue(self, param_name, param_value, need_save_to_file=True):
        self.config[param_name] = param_value
        if need_save_to_file:
            self.saveConfig()

    def getValue(self, param_name, index=0):
        self.readConfig(index)
        return self.config[param_name]
