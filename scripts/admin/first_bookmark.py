#!/usr/bin/env python
"""Handle bookmark management tasks from the cmd line for this Bookie instance

    bookmarkmgr.py --add rharding --email rharding@mitechie.com

"""
import transaction

from datetime import datetime
from ConfigParser import ConfigParser
from os import path

from bookie.models import initialize_sql


if __name__ == "__main__":
    ini = ConfigParser()
    ini_path = path.join(path.dirname(path.dirname(path.dirname(__file__))),
        'bookie.ini')

    ini.readfp(open(ini_path))
    initialize_sql(dict(ini.items("app:bookie")))

    from bookie.models import DBSession
    from bookie.models import Bmark

    bmark_us = Bmark(u'http://bmark.us',
                     u'admin',
                     desc=u'Bookie Website',
                     ext= u'Bookie Documentation Home',
                     tags = u'bookmarks')

    bmark_us.stored = datetime.now()
    bmark_us.updated = datetime.now()
    DBSession.add(bmark_us)
    DBSession.flush()
    transaction.commit()
