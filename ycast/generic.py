import logging
import os

USER_AGENT = 'YCast'
VAR_PATH = os.path.expanduser("~") + '/.ycast'
CACHE_PATH = VAR_PATH + '/cache'

STATIONID_LEN = 8
PREFIX_LEN = 1

class Directory:
    def __init__(self, name, item_count):
        self.name = name
        self.item_count = item_count


def generate_stationid_with_prefix(uid, prefix):
    if not prefix or len(prefix) != PREFIX_LEN:
        logging.error("Invalid station prefix length (must be {:d})".format(PREFIX_LEN))
        return None
    if not uid:
        logging.error("Missing station id for full station id generation")
        return None
    fmt = '{:0' + str(STATIONID_LEN) + 'd}'
    return str(prefix) + fmt.format(int(uid))


def get_stationid_prefix(uid):
    if len(uid) < PREFIX_LEN + 1:
        logging.error("Could not extract stationid (Invalid station id length)")
        return None
    return uid[:PREFIX_LEN]


def get_stationid_without_prefix(uid):
    if len(uid) < PREFIX_LEN + 1:
        logging.error("Could not extract stationid (Invalid station id length)")
        return None
    return uid[PREFIX_LEN:].lstrip('0')


def get_cache_path(cache_name):
    cache_path = CACHE_PATH + '/' + cache_name
    try:
        os.makedirs(cache_path)
    except FileExistsError:
        pass
    except PermissionError:
        logging.error("Could not create cache folders (%s) because of access permissions", cache_path)
        return None
    return cache_path
