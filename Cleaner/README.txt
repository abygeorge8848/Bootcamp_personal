Run these two first

    export FLASK_ENV=development (setting it to a development mode with debugger on. Not to be used for deployment)
    export FLASK_APP=app (There's no explicit need for this since I've name the program as the default flask name)
    
Then run

     flask initdb - (this will initialise a database named SignIn and table called SignIn is made as well) - you need to have postgreSQL set up on your system for this to work though
     flask run - (this will launch the server to 127.0.0.1:5000 and you'll have the pages) 
     The pages will be at 127.0.0.1:5000/signup and at 127.0.0.1:5000/login
     
     
     I haven't really implemented anything for the log in page, only the sign up page. But I can do that too if need be. I've mentioned how I'd implement that as comments in the code.
