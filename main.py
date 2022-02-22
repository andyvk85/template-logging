from bar.do_sth import do_bar_stuff
from foo.do_sth import do_foo_stuff
from logger import custom_logger

logger = custom_logger(__name__)
logger.info('hello logging template!')
do_foo_stuff()
do_bar_stuff()
