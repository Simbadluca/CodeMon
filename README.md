CodeMon
=======

[Assignment 3](https://github.com/reykjavik-university/2014-T-514-VEFT/blob/master/Week12/project3.md)


##Installation guid for Mac:

Installing homebrew:

    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Install python shared objects and header files with brew:

    brew install python --framework
    
Pip(Python package manager) is installed when python --framework is installed.

Use pip to install virtualenv:

    sudo pip install virtualenv
    
    
    
###How to use virtualenv

  Create a new project folder:
  
    ➜  mkdir ~/Desktop/cinema
    
  Navigate to it:
  
	  ➜  cd ~/Desktop/cinema
	  
  Create the virtual environment:
  
	  ➜  cinema  virtualenv .venv
	  
  Activate the environment:
  
	  ➜  cinema  source .venv/bin/activate
	  
	  
###Install database

SQLAlchemy:

    pip install sqlalchemy

[SQLAlchemy demonstartion](https://github.com/reykjavik-university/2014-T-514-VEFT/blob/master/Week09/lab_assignments_for_week_9.md)
[SQLAlchemy demonstration 2](http://docs.sqlalchemy.org/en/rel_0_9/orm/tutorial.html)


###Install web framework for Python

Flask:

    pip install flask
    
[Flask quick start](http://flask.pocoo.org/docs/0.10/quickstart/#quickstart)


###Install RabbitMQ

	brew install rabbitmq
	rabbitmq-plugins enable rabbitmq_management
	
RabbitMQ needs to be added to path:

	PATH=$PATH:/usr/local/sbin
	
To run RabbitMQ

	rabbitmq-server
	
Install Pika to interact with RabbitMQ through python

	pip install pika
	
[RabbitMQ man](http://www.rabbitmq.com/man/rabbitmqctl.1.man.html)

###Install Kodemon

	pip install git+https://github.com/hlysig/kodemon-python


###Install Elasticsearch

[Elastisearch download](http://www.elasticsearch.org/overview/elkdownloads/)

Extract file to a desired location.
Navigate to elasticsearch/conf/elasticsearch.yaml
Set the name of the cluster and remove the comment:
	
	cluster.name: kodemon
	
Set the name of the node and remove the comment:
	
	node.name: "functions"
	
	pip install elasticsearch

###If we cant unit-tests

    pip install nose
    
[nose](https://nose.readthedocs.org/en/latest/)


#Running the project
In order for the project to run properly we must activate the following key components as listed.
It is wise to have one terminal window open for each component.

First navigate to the project directory (/CodeMon/)

* ##RabbitMQ
  * $ PATH=$PATH:/user/local/sbin
  * $ rabbitmq-server

* ##UDP Server
  * $ python UDPserver.py

* ##Message Listener
  * $ python messageListener.py

* ##Elastic Search
Asuming that elastic search is located in the same folder as the CodeMon directory
  * $ ./../elasticsearch-1.3.4/bin/elasticsearch

* ##Database
  * $ python data/\__init\__.py

* ##Activate the API
  * $ python api.py

* ##Activate the Frontend
  * $ python frontend/app.py

	
