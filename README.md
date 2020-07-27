# learnKafka
Experiment with python and apache kafka.

project structure based in  [django cookiecutter](https://github.com/pydanny/cookiecutter-django)

## How to start the project with docker compose!

### Run composer
`docker-compose -f local.yml up`

### Create an administration user
` docker-compose -f local.yml exec django python  manage.py createsuperuser`

### Create topic 
`docker-compose -f local.yml exec broker kafka-topics --create --topic backend-user --bootstrap-server broker:9092 --replication-factor 1 --partitions 1`

### System url localhost
* [backend django](http://localhost:8000/)

#### More information about [Confluent Platform](https://docs.confluent.io/current/quickstart/ce-docker-quickstart.html#ce-docker-quickstart)

