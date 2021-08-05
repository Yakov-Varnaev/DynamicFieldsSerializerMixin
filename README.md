# DyanamicFieldsSerializerMixin

## What is it for?
This is a Mixin which allows your REST service to response with certain fields, which are requested in query parameters.

## How to use?
Just copy this code to your project and use as a regular mixin.

Then you will be able to make requests like:

api/v1/users/?filds=username,first_name,last_name
This request to your endpoint will response with username, first_name and last_name

api/v1/users/?fields!=password
This request will omit password field from the response

### NOTE: This mixin is not covered with tests, so it may contain bugs and probably might crush your project, so be careful.

## TODO:
1. Write tests for this mixin.
2. Check if it works with nested serializers.
3. Write better doc 
