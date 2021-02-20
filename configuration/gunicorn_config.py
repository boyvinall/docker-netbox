command = '/usr/bin/gunicorn'
pythonpath = '/opt/netbox/netbox'
bind = '0.0.0.0:8001'
workers = 16
errorlog = '-'
accesslog = '-'
capture_output = False
loglevel = 'warning'
timeout = 60