from .settings import *

# DEBUG must be false
DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1'
]

# configure static and media roots
MEDIA_URL = '/media/'

# configure s3 uploads
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

# use AWS credentials, this will take from enviroment varibles,
# however this should only be used when testing production features
# locally. For production, IAM instance roles should be used instead.
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
