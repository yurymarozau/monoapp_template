from decouple import config

ASGI_APPLICATION = 'config.routings.application'

CHANNEL_LAYER_DB = config('CHANNEL_LAYER_DB')
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [f"redis://{config('BROKER_HOST')}:{config('BROKER_PORT')}/{CHANNEL_LAYER_DB}"],
        },
    },
}
