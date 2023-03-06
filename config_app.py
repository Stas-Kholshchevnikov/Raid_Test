
class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password_26@localhost/raid_test'
    SQLALCHEMY_TRACK_MODIFICATIONs = False
    RESTX_JSON = {"ensure_ascii": False}
