# Dynamic Feed in the Blog

Hi! This is s demo of Redis PubSub model using Python. 

## Setup

**Setup a local Redis Server using Docker**
Pull the latest redis image from dockerhub
    
    docker pull redis

create an internal bridge

    docker network create redis

create the redis container

    docker run --name redis-docker --network redis --detach --publish 16379:6379 redis:latest redis-server

The port 6379 of the container has been mapped to 16379 of your system to avoid port conflicts.
**Creating a virtual environment**

    python -m venv <name of the virtual environment>
**Installing the dependencies**

    pip install -r requirements.txt
**To  play around**
- Open 4 or more CMD instances on your local. The 4 instances will represent 2 publishers and 2 subscribers.
- Activate the virtual environment in all the instances (for Windows users given below)
	- `<name of your virtual environment>\Scripts\activate `
	
**Publisher CODE**

    from rpublisher import Publisher
    # creating a publisher instance
    pub1 = Publisher('python')
    # create a channel
    pub1.createChannel()
    # pub1.publishMessage('List are a line...')
	
	# creating another publisher instance
    pub1 = Publisher('database')
    # create a channel
    pub1.createChannel()
    # pub1.publishMessage('Indexing may lead to write amplification...')

*Note: Only messages published after subscribers have subscribed to the respective channels will be shown to the subscriber nothing before that. Make sure you subscribe a channel with the method shown below before using publishMessage method*

**Subscriber CODE**

    from rsubscriber import Subscriber
    # creating a subscriber instance
    s2 = Subscriber('James')
    # adding subscription to database channel
    s2.addSubscription('database')
    # adding subscription to python channel
    s2.addSubscription('python')
    # getting the topics as per the channels you subscribed
    s2.getNewMessages()
	
	# creating another subscriber instance
	s1 = Subscriber('John')
    # adding subscription to python channel
    s1.addSubscription('python')
    # getting the topics as per the channels you subscribed
    s1.getNewMessages()
   
   As you will observe s2 will get messages from both 'python' and 'database' channels while s1 will get messages from 'python' channel' only.
   
To see the results checkout this LinkedIn post:-https://www.linkedin.com/posts/auroshisray_redis-pubsub-eazyhacks-activity-6946062995152068608-jmCA?utm_source=linkedin_share&utm_medium=member_desktop_web