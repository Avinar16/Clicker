from Config import config

def set_level(level_id=0):
    if level_id != config.getValue('level'):
        config.setValue('level', level_id)

def check_level():
    if config.getValue('level') == 0:
        return 0
    if config.getValue('level') == 1:
        return 1
    if config.getValue('level') == 2:
        return 2
