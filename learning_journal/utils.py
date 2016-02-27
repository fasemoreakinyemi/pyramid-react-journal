# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pyramid.security import unauthenticated_userid
from sqlalchemy import engine_from_config
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

from .models import User

APPROVED = 'learning_journal.approved_usernames'
ADMINS = 'learning_journal.admins'


def create_session(settings):
    from sqlalchemy.orm import sessionmaker
    engine = engine_from_config(settings, 'sqlalchemy.')
    Session = sessionmaker(bind=engine)
    return Session()


def get_user(request):
    userid = unauthenticated_userid(request)
    try:
        user = User.by_username(userid)
    except (MultipleResultsFound, NoResultFound):
        user = None
    return user


def get_approved_users(request):
    raw = request.registry.settings.get(APPROVED,'')
    return set(raw.split())


def get_admin_users(request):
    raw = request.registry.settings.get(ADMINS, '')
    return set(raw.split())