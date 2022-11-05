#
#
#

import os

from environs import Env

env = Env()

#
#
#
SECRET_KEY = os.urandom(16)
USE_SESSION_FOR_NEXT=True

SQLALCHEMY_DATABASE_URI=('postgresql://'
    f"{env('POSTGRES_USER')}:{env('POSTGRES_PASSWORD')}@postgres:5432/"
    f"{env('POSTGRES_DB')}"
)
SQLALCHEMY_TRACK_MODIFICATIONS=False

CELERY={
    'broker_url': f"amqp://{env('RABBITMQ_DEFAULT_USER')}:{env('RABBITMQ_DEFAULT_PASS')}@rabbitmq:5672//",
    'result_backend': f'rpc://'
}
