# restful-test-python
Rest API Services - Sample Application in Python


## Structure of the Project
#### MVC architecture
With an exception of - this doesnt use a database, instead all user and tweet data is stored in memory in hash maps

#### Controller - com.shekhar.core.TweetController.java
Contains all code for the backend. This class implements the business logic, such as <br> 
> making friend <br>
> following someone <br>
> unfollowing someone <br>
> write messages to someone <br>

#### POJO - com.shekhar.core.Tweet.java
This class is the plain old java object and describes the attributes of individual tweets

#### JAX Rest Beans - com.shekhar.restfulws.resource.MyJax*.java
These classes implements the beans of Rest api

#### JAX Rest APIS - com.shekhar.restfulws.resource.tweetaction.java
This is the main Rest API class that interacts with the APIs and calls relavant methods in the controller to get appropriate response.


# How to run

### Pre-requisites
Install
> install python, pip, Git <br>
> pip install requests <br>
> pip install Flask <br>

### Step 1: Git clone - get the code to local 
> git clone https://github.com/shekhar2010us/restful-test.git

### Step 2: Compile and create the war (web archive)
Go to the project directory (cloned from git). Using maven, compile the project. You will see restful-test-1.0.war file in the target directory if mvn runs successfully. <br>
> mvn clean install -U <br>

### Step 3: Start the Tomcat engine
> cd <TOMCAT_DIR>/bin/
> ./startup.sh

### Step 4: Copy the war file to Tomcat
> cp restful-test-1.0.war <TOMCAT_DIR>/webapp/

### Step 5: Check the application
> Open a browser and open the URLs provided in "test_cases.txt" file in the root directory of the project

*** Note: You can also watch the <b>catalina.out</b> log file in the logs directory of Tomcat, and check the log after opening each URL.