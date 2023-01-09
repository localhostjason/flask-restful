#!/usr/bin/env python
from flask import Blueprint
from cmds.init_data import insert_admin

db_cmd = Blueprint('db', __name__)


@db_cmd.cli.command("update_db")
def update_db():
    from flask_migrate import upgrade, migrate

    migrate()
    upgrade()


@db_cmd.cli.command("deploy")
def deploy():
    insert_admin()


@db_cmd.cli.command("upgrade")
def upgrade_db():
    from flask_migrate import upgrade

    upgrade()


@db_cmd.cli.command("init")
def init_db():
    from flask_migrate import init

    init()


@db_cmd.cli.command("migrate")
def migrate_db():
    from flask_migrate import migrate

    migrate()
