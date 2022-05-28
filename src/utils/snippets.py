import os
import uuid


def file_name_maker(filename):
    return f"{uuid.uuid4().hex}.{filename.split('.')[-1]}".lower()


def change_file_extension_user(instance, filename):
    return os.path.join(f'static/images/user/{instance.id}', file_name_maker(filename))


def change_file_extension_profile(instance, filename):
    return os.path.join(f'static/images/profile/{instance.user.id}', file_name_maker(filename))


def change_file_extension_post(instance, filename):
    return os.path.join(f'static/images/user/{instance.user.id}/post/', file_name_maker(filename))
