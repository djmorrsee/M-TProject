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

##/module/&lt;id>/ - GET
Returns a list of historical readings for the given module

##/module/&lt;id>/&lt;auth_id>/ - POST
Registers a module to the database with the given id.

Returns an m_auth_id, which is needed for the module to post data.

If a module with [id] already exists in the database, the process is aborted.

##/module/&lt;id>/&lt;auth_id>/ - DELETE
Removes the module with id from the database

Returns a success message.

##/module/post_reading/&lt;id>/&lt;m_auth_id>/ - POST
Node for module to post data. The module must know its id and m_auth_id, which is assigned at registration.

Returns a success mesage.

##/reset/&lt;auth_id>/ - DELETE
Clears All Data From The Database
