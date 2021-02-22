from .settings import *

# DEBUG must be false
DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    '.elasticbeanstalk.com'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ["RDS_DB_NAME"],
        'USER': os.environ["RDS_USERNAME"],
        'PASSWORD': os.environ["RDS_PASSWORD"],
        'HOST': os.environ["RDS_HOSTNAME"],
        'PORT': os.environ["RDS_PORT"],
    }
}

# configure static and media roots
AWS_LOCATION = 'static/'

# configure s3 uploads
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

# use AWS credentials, this will take from environment variables,
# however this should only be used when testing production features
# locally. For production, IAM instance roles should be used instead.
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_CUSTOM_DOMAIN = os.environ.get("AWS_S3_CUSTOM_DOMAIN")

