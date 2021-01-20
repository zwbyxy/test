启冻消费者
cd /root/django_web/github/test/dailyfresh
 celery -A celery_tasks.tasks worker --loglevel=info      
