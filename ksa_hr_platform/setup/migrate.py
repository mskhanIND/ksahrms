from ksa_hr_platform.setup.onboarding import create_onboarding_records
from ksa_hr_platform.setup.install import create_default_services, create_roles
from ksa_hr_platform.setup.workspace_cards import update_clickable_workspace


def after_migrate():
    create_roles()
    create_default_services()
    create_onboarding_records()
    update_clickable_workspace()
