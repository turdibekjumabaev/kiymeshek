from src.models.role_model import Role

import logging


def load_roles(db):
    default_roles = ["ADMIN", "VOLUNTEER", "USER"]

    for default_role in default_roles:
        role = Role.query.filter_by(role_name = default_role).first()

        if role is None:
            new_role = Role(role_name=default_role)
            db.session.add(new_role)

    db.session.commit()
    logging.info("Baslanǵısh roller qosıldı")
