# Secret Santa

This application is a micro-game designed purely around creating the social interaction of Secret Santa, but in a virtualized, online environment. All users involved in an event can send an receive an emoji gift under the guise of random mystery. What fun!



![](https://d3lw8livlfth9o.cloudfront.net/static/core/images/background_footer.png)

## How to Play
1. Jump onto the the Secret Santa Website (https://virtualsecretsanta.club)
1. Once you are registered, you can create an event. Invites are sent by specifying an email.
1. The invite will only succeed if the user holds an account with Secret Santa. If you have an account there's no rejecting an invitiation, once you're in, you're in! Feel free to edit the event as often as you would like.
1. When the creator of an event is happy with the number of participants, then can activate the event to set it in motion. There's no option to edit it after this point.
1. Now the fun begins! Users choose their emoji and personalized message of choice to their designated recipient.
1. When the big reveal occurs, users can log in and open their present, if their gift givers went MIA they'll receive coal instead :(
1. Grinches are pubically shamed, as they should be.

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


