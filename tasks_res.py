from celery import Celery

app = Celery('tasks_res', backend='redis://localhost', broker='amqp://guest@localhost//')

@app.task
def myadd(x, y):
	return x + y;
