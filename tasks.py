from celery import Celery

app = Celery('tasks', broker='amqp://guest@localhost//')

@app.task
def myadd(x, y):
	return x + y;
