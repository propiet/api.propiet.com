import uwsgi
from uwsgidecorators import timer
from django.utils import autoreload
 
@timer(3)
def change_code_gracefull_reload(sig):
    if autoreload.code_changed():
        uwsgi.reload()
