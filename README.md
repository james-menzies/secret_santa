# Secret Santa

This application is a micro-game designed purely around creating the social interaction of Secret Santa, but in a virtualized, online environment. All users involved in an event can send an receive an emoji gift under the guise of random mystery. What fun!

## How it Works
1. Once a user is registered, they can create an event. Invites are sent by specifying an email.
2. If a user isn't registered, they'll be invited via the specified email to join up. Once registered they'll be automatically be added to the event. There's no opting out once you've joined Secret Santa, once you're in, you're in!
3. When the creator of an event is happy that everyone has joined, they can set a time for the big reveal. The gift givers and recipients are all determined and people can start giving.
4. Now the fun begins! Users will be notified that they have some gifting to do, and can choose their emoji and personalized message of choice.
5. When the big reveal happense users can log in and open their present, if their gift givers went MIA they'll receive coal instead :(
6. Grinches are pubically shamed, as they should be.

## Who is This Application For?

Anyone who's after a bit of fun! This game is probably best played amongst friends, but there's nothing that precludes strangers from playing as well. It's also designed to be a fun exercise for companies that want to create a bit of social engagement amongst their peers. 

## Tech Stack

* Python + Django: Serves as the application layer for the program. Handles everything from processing web endpoint requests, and acts as the ORM between the application and data layers.

* AWS Elastic Beanstalk: Provisions the webservers containing the Django applicaton by automatically configuring an auto-scaling group of EC2 instances. 

* S3 / Cloudfront: Where all static images and emoji gift images are served. S3 physically stores the media, and Cloudfront provisions it through making images available through caching and duplication in locations close to the user.

* Amazon Simple Email Service: Responsible for handling email communications to users. This is of particular importance for inviting new users to join, as well as notifying them when they've been added to an event, or when it's present opening time.

* Postgres / RDS: The underlying implementation of the data layer is a Postgreql database, which is provisioned by Amazon RDS, a managed database service. 

* Celery: This library is used to handle asynchronous background tasks. Celery is primarily used to handle the dispatch of mail requests whilst not locking the thread handling the user request.
