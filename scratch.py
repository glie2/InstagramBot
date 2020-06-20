import configparser


print("hello world")

config = configparser.ConfigParser()
config.read('config_.ini')
print(config['IG_AUTH']['USERNAME'])
print(config['IG_AUTH']['PASSWORD'])

print(config['IG_URLS']['LOGIN'])
print(config['IG_URLS']['NAV_USER'])
print(config['IG_URLS']['SEARCH_TAGS'])
print(config.sections())