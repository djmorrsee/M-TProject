#REST API Documentation

This document defines the rest api for our flask server.

Theres no way to modify data once its been posted (for now).
It's all or nothing as far as deleting module data goes.

Any method other than GET requires an authorization id.
We will have an Auth_ID for each of us, and M_Auth_ID's are assigned to the modules at registration.

## / - GET
The root directory will serve an HTML with JQPlot graphs etc.

## /all/ - GET
Serves as the root point for the REST API, since the web page takes up '/'

Will return a dictionary of all module data.

##/module/ - GET
Returns a list of available module ids



##/module/&lt;id>/ - GET, POST, DELETE

####GET
Returns a list of historical readings for the given module

####POST
Registers a module to the database.

Data is expected in the form:

	{
		"module_id":123,
		"auth_id":a1e3c83997eff1234,
	}

Both 'module_id' and 'm_auth_id' need to be recognized by the system in order
for data to be successfully posted.

Returns a Response Code

####DELETE
Deletes all data and unregisters a module

Data is expected to be of the form

	{
		"auth_id":a1e3c83997eff1234,
	}

"auth_id" must be recognized by the system for the data to be successfully deleted.

Returns a Response Code

##/module/post_reading/ - POST
Node for module to post data.

Data is expected to be of the form:

	{
		"module_id":123,
		"module_auth_id":a1e3c83997eff1234,
		"reading": {
			"temperature":4096,
			"light":4096
		}
	}

Returns a Response Code.

##/reset/ - DELETE
Clears All Data From The Database

Data is expected to be of the form:

	{
		"auth_id":a1e3c83997eff1234,
	}

Returns a Response Code
