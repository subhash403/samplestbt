
import configparser
config = configparser.ConfigParser()
configFilePath = r'C:\Users\Sindhushree.V\PycharmProjects\stb-tester-test-pack-charter\config\stbt.conf'
config.read(configFilePath)
Env=config.get('sst','test_env')
print (Env)