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
	
To run RabbitMQ

	sudo rabbitmq-server
	
Install Pika to interact with RabbitMQ through python

	pip install pika
	
[RabbitMQ man](http://www.rabbitmq.com/man/rabbitmqctl.1.man.html)

###Install Kodemon

	pip install git+https://github.com/hlysig/kodemon-python


###If we cant unit-tests

    pip install nose
    
[nose](https://nose.readthedocs.org/en/latest/)



	
