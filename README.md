# Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python

"Building a Serverless Backend"


![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/63f87414ee5c6fa7b9bbb6550b0ac3c41e601704/img/Screenshot%202025-01-27%20114039.png)


# Slim the Developer

Introducing Slim, the developer who has now mastered the basics of AWS Lambda! But his interest has been sparked much more. He considers a personal project that would challenge his abilities and appeal to his experience in software development, using his newly acquired understanding of serverless architectures on AWS. He also longs to learn more about Amazon API Gateway and Amazon DynamoDB, two more potent serverless services. The scene in now set for “Slim the Developer” to take center stage once again.


## What is the Backend

When it comes to web application development, the BACKEND is the engine behind the scenes that makes the web application function. It is responsible for data storage, business logic and handling user requests.
It differs from the FRONTEND, which is the user-facing part that allows users to interact with and use the application directly in their web browsers, as the backend is responsible for managing and serving the relevant data to the frontend.Both FRONTEND and BACKEND work together to create a web application.

# Background Concepts

## Application Protocol Interface (API)

An Application Protocol Interface (API), is a set of rules and protocols that allow different software applications to communicate and interact with each other. It defines the methods and data formats that applications can use to request and exchange information for seamless integration and data sharing between diverse systems.

## HTTP methods

HTTP methods or request methods, are a critical component of web services and APIs which indicate the desired action to be performed on a resource in a given request URL. The most commonly used methods in RESTful APIs are GET, used to retrieve data from a server, POST, which sends data, included in the body of the request, to create or update a resource, PUT, which updates or replaces an existing resource or creates a new resource if it doesn’t exist and DELETE, which deletes the specified data from the server

## Amazon API Gateway

Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor and secure APIs at scale. It acts as an entry point for multiple APIs, managing and controlling the interactions between clients (such as web or mobile applications) and backend services providing various functions, including request routing, security, authentication, caching and rate limiting, to simplify the management and deployment of APIs.

## Amazon DynamoDB

DynamoDB is a fully managed NoSQL database service designed for high scalability, low latency and replication of data across multiple regions. DynamoDB stores data in a schema-less format, allowing for flexible and fast storage and retrieval of structured and semi-structured data. It is commonly used for building scalable and responsive applications in cloud-based environments.

## Serverless CRUD application

In a serverless CRUD application using API Gateway, Lambda and DynamoDB, CRUD refers to the usual meaning of Create, Read, Update and Delete, but the architecture and components involved differ from traditional server-based applications. Create involves adding new entries to a DynamoDB table. The Read operation retrieves data from a DynamoDB table. Update updates existing data in DynamoDB and the Delete operation deletes data from DynamoDB.

## Postman

Postman is a popular collaboration platform that simplifies the process of designing, testing and documenting APIs. It offers a user-friendly interface for developers to create and send HTTP requests, test API endpoints and automate testing workflows.

# Prerequisites

1.WS Account with an IAM User with administrative privileges

2.Basic knowledge of the Python programming language and AWS SDK Boto3

3.Familiarity with an Interactive Development Environment (IDE)

4.AWS Command Line Interface (CLI) installed and configured on your local machine

5.Basic knowledge and use of Linux fundamental commands

# Objectives

Slim’s main objectives are to automate the entire set up of the serverless CRUD Book store application and verify its functionality. He decided to test the endpoints directly using Postman. The following are his broken down objectives —

1.Create a DynamoDB Table to store book order details

2.Develop HTTP method Lambda Functions with necessary permissions

3.Create book API using API Gateway

4.Integrate API Gateway to Lambda Functions

5.Test the API using Postman

Before we dive into the code, make sure to fork the project’s repository from Slim’s GitHub. You can make necessary edits to the files to personalize them as we progress:https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python.git

## Step 1: Create a DynamoDB Table to store coffee order details

1.Navigate to your AWS Console and search for "DynamoDB" and click on create table

2.Enter yout table and the Partition Key as "ProductId" and leave everything as default, click on create table 

![image_alt]()

3.Now that the DynamoDB table is active as shown below we can now go ahead to create our Lambda Fuction

![image_alt]()


## Step 2: Create Lambda functions for API methods GET, POST, PUT and DELETE

1.Search for "lambda" on your aws console home and click on create Function 

2.Choose "Author from Scratch" option and Runtime choose python "3.9

![image_alt]()

3.On Permission we are going to create a new lambda role with FullAccessDynamoDB and CloudWatchFullAcces and click on create new role 

select lambda as the service 

![image_alt]()

On add permissions choose both FullAccessDynamoDB and CloudWatchFullAcces
As you can see we have to policies selected 

![image_alt]()


Name your policy and then click on create 

![image_alt]()


Now head back to your lambda function on under permission choose existing role and then proceed to create your function 

![image_alt]()


Now that our lambda function is created

![image_alt]()




copy and paste the code below, delete the default code and paste the one below 

```python
import boto3
import json
from custom_encoder import CustomEncoder
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodbTableName = 'product-inventory'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(dynamodbTableName)

getMethod = 'GET'
postMethod = 'POST'
patchMethod = 'PATCH'
deleteMethod = 'DELETE'
healthPath = '/health'
productPath = '/product'
productsPath = '/products'


def lambda_handler(event, context):
    logger.info(event)
    httpMethod = event['httpMethod']
    path = event['path']
    
    if httpMethod == getMethod and path == healthPath:
        response = buildResponse(200, {"message": "Health check successful"})
    elif httpMethod == getMethod and path == productPath:
        productId = event['queryStringParameters'].get('productId') if event.get('queryStringParameters') else None
        if productId:
            response = getProduct(productId)
        else:
            response = buildResponse(400, {"error": "Missing productId in query string"})
    elif httpMethod == getMethod and path == productsPath:
        response = getProducts()
    elif httpMethod == postMethod and path == productPath:
        response = saveProducts(json.loads(event['body']))
    elif httpMethod == patchMethod and path == productPath:
        requestBody = json.loads(event['body'])
        response = modifyProduct(requestBody['productId'], requestBody['updateKey'], requestBody['updateValue'])
    elif httpMethod == deleteMethod and path == productPath:
        requestBody = json.loads(event['body'])
        response = deleteProduct(requestBody['productId'])
    else:
        response = buildResponse(404, {"error": "Not Found"})
        
    return response


def getProduct(productId):
    try:
        response = table.get_item(
            Key={
                'productId': productId
            }
        )
        if 'Item' in response:
            return buildResponse(200, response['Item'])
        else:
            return buildResponse(404, {'error': f'ProductId {productId} not found'})
    except Exception as e:
        logger.exception("Error retrieving product")
        return buildResponse(500, {'error': str(e)})


def getProducts():
    try:
        response = table.scan()
        result = response['Items']
        
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            result.extend(response['Items'])
        
        body = {
            'products': result
        }
        return buildResponse(200, body)
    except Exception as e:
        logger.exception("Error retrieving products")
        return buildResponse(500, {'error': str(e)})


def saveProducts(requestBody):
    try:
        table.put_item(Item=requestBody)
        body = {
            'operation': 'SAVE',
            'message': 'SUCCESS',
            'item': requestBody
        }
        return buildResponse(200, body)
    except Exception as e:
        logger.exception("Error saving product")
        return buildResponse(500, {'error': str(e)})


def modifyProduct(productId, updateKey, updateValue):
    try:
        response = table.update_item(
            Key={
                'productId': productId
            },
            UpdateExpression=f'set {updateKey} = :value',
            ExpressionAttributeValues={
                ':value': updateValue
            },
            ReturnValues='UPDATED_NEW'
        )
        
        body = {
            'operation': 'UPDATE',
            'message': 'SUCCESS',
            'updatedAttributes': response['Attributes']
        }
        return buildResponse(200, body)
    except Exception as e:
        logger.exception("Error updating product")
        return buildResponse(500, {'error': str(e)})


def deleteProduct(productId):
    try:
        response = table.delete_item(
            Key={
                'productId': productId
            },
            ReturnValues='ALL_OLD'
        )
        
        if 'Attributes' in response:
            body = {
                'operation': 'DELETE',
                'message': 'SUCCESS',
                'deletedItem': response['Attributes']
            }
            return buildResponse(200, body)
        else:
            return buildResponse(404, {'error': f'ProductId {productId} not found'})
    except Exception as e:
        logger.exception("Error deleting product")
        return buildResponse(500, {'error': str(e)})


def buildResponse(statusCode, body=None):
    response = {
        'statusCode': statusCode,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
    if body is not None:
        response['body'] = json.dumps(body, cls=CustomEncoder)
    return response
```

under lambda code block create a new python file and name it custom_encoder.py 

again copy the code below and paste it on your new file

```python
import json

from decimal import Decimal


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float()
        
        return json.JSONEncoder.default(self,obj)
```

The output should like the image shown below

![image_alt]()

4.After you are done pasting your code click on deploy











