# Secret Santa

This application is a micro-game designed purely around creating the social interaction of Secret Santa, but in a virtualized, online environment. All users involved in an event can send an receive an emoji gift under the guise of random mystery. What fun!

## How it Works
1. Once a user is registered, they can create an event. Invites are sent by specifying an email.
2. If a user isn't registered, they'll be invited via the specified email to join up. Once registered they'll be automatically be added to the event. There's no opting out once you've joined Secret Santa, once you're in, you're in!
3. When the creator of an event is happy that everyone has joined, they can set a time for the big reveal. The gift givers and recipients are all determined and people can start giving.
4. Now the fun begins! Users will be notified that they have some gifting to do, and can choose their emoji and personalized message of choice.
5. When the big reveal occurs, users can log in and open their present, if their gift givers went MIA they'll receive coal instead :(
6. Grinches are pubically shamed, as they should be.

## Who is This Application For?

Anyone who's after a bit of fun! This game is probably best played amongst friends, but there's nothing that precludes strangers from playing as well. It's also designed to be a fun exercise for companies that want to create a bit of social engagement amongst their peers. 

## Tech Stack

* Amazon Elastic Container Service: This manages all running instances of the application into a cluster so updates can pushed out automatically.

* Github Actions: This allows me to run my unit tests on non master branches as well as push automatically to ECS when a new version of the application is added.

* S3 / Cloudfront: Where static content and user uploaded images are stored. S3 physically stores the media, and Cloudfront provisions it through caching and duplicating in edge locations close to the user.

* Postgres: The underlying implementation of the data layer is a PostgreQL database, which is provisioned by an Amazon EC2 instance.

* Docker and Docker Compose: The container technology used for the application. For local development and testing, Docker Compose is used to allow the separate elements of the application (the web server and database) to be orchestrated on a single machine.

* Python + Django: Serves as the application layer for the program. Handles everything from processing web endpoint requests, and acts as the ORM between the application and data layers.

### Django and Python Libraries

* django-storages: This allows for S3 and Cloudfront integration with minimal configuration.

* django-crispy-forms: A utility library to help render forms consistently as well as provide a more streamlined mechanism for form layouts.


## Project Management

For the delivery of the project, I've divided the development process into 4 distinct phases, read more about it [HERE](https://github.com/redbrickhut/secret_santa/wiki/Development-Roadmap)

## CI / CD Pipeline

For this application an extensive CI / CD pipeline has been devised. Read more about it [HERE](https://github.com/redbrickhut/secret_santa/wiki/CI---CD).

## Testing

The process of both automated and manual testing of the application is described [HERE](https://github.com/redbrickhut/secret_santa/wiki/Testing)


