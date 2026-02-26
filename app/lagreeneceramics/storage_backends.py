from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'

    def get_object_parameters(self, name):
        """Override to ensure ACL is set for all uploaded files"""
        params = super().get_object_parameters(name)
        params['ACL'] = 'public-read'
        return params


class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False

    def get_object_parameters(self, name):
        """Override to ensure ACL is set for all uploaded files including thumbnails"""
        params = super().get_object_parameters(name)
        params['ACL'] = 'public-read'
        return params
