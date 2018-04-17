
create a aws lambda function on amazon webservice online
Trigger is Alexa
change the configuration handler to main.lambda_handler.

Go throught the program in this order.
1. AlexaBaseHandler:
	Basically abstract/event methods are created.

2. AlexaDeploymentHandler:
	Implements the AlexaBaseHandler abstract methods. This defines behaviour of the Alexa



3. create_deployment:
	Certain modules will be needed. so this script automatically download the necessary package files for a particular
	module and it creates a zipfile in the folder deployment to be uploaded in the lambda function online. Note you should copy AlexaBaseHandler
	AlexaDeploymentHandler into the zipfile.
	It expects there to be a deployments directory and it will create a
	deployment of the form:
	deployment_n
	where n is incremented for each deployment based on the existing deployment
	directories


4. main