from ksa_hr_platform.setup.install import create_default_services, create_roles


def after_migrate():
    create_roles()
    create_default_services()
