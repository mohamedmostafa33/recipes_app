from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """
    Storage backend for static files (CSS, JS, images from staticfiles)
    """
    location = 'staticfiles'
    default_acl = None  # استخدام bucket policy بدل ACL
    file_overwrite = True


class MediaStorage(S3Boto3Storage):
    """
    Storage backend for media files (user uploaded files like recipe images)
    """
    location = 'media'
    default_acl = None  # استخدام bucket policy بدل ACL
    file_overwrite = False
