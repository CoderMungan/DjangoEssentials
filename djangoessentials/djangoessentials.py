from storages.backends.s3boto3 import S3Boto3Storage


class MyS3Storage(S3Boto3Storage):
    location = "media/"  # S3'te files alt dir
    file_overwrite = False  # if have a same name about the file cant overwrite
    default_acl = "public-read"  # just can read permission
