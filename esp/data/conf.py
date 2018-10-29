SSID = '[ssid]'
PASSWORD = '[pass]'
CONNECT_RETRIES = 10
CONNECTION_TIME = 6.0

MQTT_SERVER = 'mqtt.gowombat.team'

ERROR_LOG_FILENAME = 'error.log'

try:
    from .local_conf import *
except ImportError:
    pass
