# Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python

"Building a Serverless Backend"


![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/63f87414ee5c6fa7b9bbb6550b0ac3c41e601704/img/Screenshot%202025-01-27%20114039.png)


## Slim the Developer

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

![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/981239d36a531f42eafd661dce2e743478c772d0/img/Screenshot%202025-01-27%20122412.png)

3.Now that the DynamoDB table is active as shown below we can now go ahead to create our Lambda Fuction

![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/21042f8b7b0ced546643287f701f4b3acc4adc14/img/Screenshot%202025-01-27%20123130.png)


## Step 2: Create Lambda functions for API methods GET, POST, PUT and DELETE

1.Search for "lambda" on your aws console home and click on create Function 

2.Choose "Author from Scratch" option and Runtime choose python "3.9

![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/69d1d882fbe3b7d02f543651550247ba8f554046/img/Screenshot%202025-01-27%20124007.png)

3.On Permission we are going to create a new lambda role with FullAccessDynamoDB and CloudWatchFullAcces and click on create new role 

select lambda as the service 

![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/85833e22cded94c2bf70f043e87cee1d40c33536/img/Screenshot%202025-01-27%20124350.png)

On add permissions choose both FullAccessDynamoDB and CloudWatchFullAcces
As you can see we have added two policies selected 

![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/6d42ba6c7f3c961279afa7248d3623edbeb6196e/img/Screenshot%202025-01-27%20124845.png)


Name your policy and then click on create 

![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/e46443050eb054e6ab8dfb9124717b106613d960/img/Screenshot%202025-01-27%20125117.png)


Now head back to your lambda function on under permission choose existing role and then proceed to create your function 

![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/a750b121d5fe7eac93398465738ed5c1668616a9/img/Screenshot%202025-01-27%20125819.png)


Now that our lambda function is created

![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/d8862df162fa6e457a92e4eec02b192f5d351e94/img/Screenshot%202025-01-27%20125843.png)




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

![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/7b3ea59cc7c1397934c0800a189b1bf6157d3ef6/img/Screenshot%202025-01-27%20130757.png)

4.After you are done pasting your code click on deploy


## Step 3: API Gateway Configuration

1.Search for "API Gateway" on your aws console home and click on create Function 

2.Select "REST API" and then click on "build"


![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/f49269403d23b71a853474214a7e0cf5bc59c101/img/Screenshot%202025-01-27%20131700.png)


3.Create API enter the name of your api leave everything as default and click create 


![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/ec78c0a273b6b9a78d9993286cf358c339787b08/img/Screenshot%202025-01-27%20131906.png)


4.Now lets create Resources /health,/product and /products  

NOTE: always enable API GATEWAY CORS for all your Resources, shown below-


![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/e8f77fd9e2350228536107ff840c94a528be7cc6/img/Screenshot%202025-01-27%20132309.png)


After you have added all three resources you should have some that look like this 


![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/97ae3b5d2f33eee31b46a5f316989f7d5b1093a7/img/Screenshot%202025-01-27%20133143.png)



Under our three resources we are going to create Methods

/health: GET
/product: GET, POST, PATCH, DELETE
/products: GET 

NOTE: always enable LAMBDA PROXY INTEGRATION

![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/3c11de60a8e73bccd68d0f873aa1ec9400e4ea58/img/Screenshot%202025-01-27%20133625.png)


After you have added all the methods you should have some that look like this 

![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/a4f8339483d27c71d6b602805c3107ca64506a58/img/Screenshot%202025-01-27%20134345.png)


5.Now let deploy the api gateway by creating new stage called "prod"

![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/eb0993f9d8a459d3991fef54908991e7745821bc/img/Screenshot%202025-01-27%20134555.png)


Now copy the URL and we will use it with Postman to query our DynamoDB table.

![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/9c00b48879511d6031ed5b4c20e110f7ed670c0e/img/Screenshot%202025-01-27%20134917.png)


## Step 4: Testing the API functionality using Postman

1.Now that the API and other resources are deployed and configured, we need to locate the unique API endpoint (URL) AWS generates before we can begin making requests. We will use this URL to test it’s functionality by simply pasting it in a web browser.

To retrieve (GET) HEALTH status for our API Gateway , head to your browser, enter the URL and make sure to add the resource “/health” at the end, as shown in the example below —

```language
https://xb0z3q5le4.execute-api.us-east-1.amazonaws.com/prod/health
```

![imaga_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/6b112059e8a438f8f59a7ff975819e6668b9bda1/img/Screenshot%202025-01-27%20140259.png)


You should see an  array/list, which verified functionality and proves we were able to receive information  "Health check successful".


2.Now, you can test all the API methods (GET, POST, PATCH and DELETE) using Postman.

To actually create an order, let’s test the POST method. Use Postman to make a POST request to the API endpoint, providing the customer’s name and coffee blend in the request body as show below —


```language

{
    "productId" : "10001",
    "color":"red",
    "price": 100
}

```

The response will be a success message with a unique ProductId of the order placed.

![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/da87142c0b12ff9165a0e827fbd5fb9482a12832/img/Screenshot%202025-01-27%20140956.png)


Verify that the new order was saved in the DynamoDB table by reviewing the items in the table —

![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/f63cdc71c8a2edaec8f4b83daf53a43fed4c3e98/img/Screenshot%202025-01-27%20141310.png)


We can add more items to our table see the example below new 2 items were added to our table


![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/a380027647c217a9fec69018f90c41d9cf3cf66e/img/Screenshot%202025-01-27%20141600.png)


Now lets test the GET Method to get a single product

productId = 10001

![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/c85e0f790859c1b2bfd7e2b244f60e1163184f9f/img/Screenshot%202025-01-27%20142232.png)



Now lets test the GET Method to get a single product not in the table 

we get a 404 error 


![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/33fb604872ce52a4a8e8f1a6da5d0cd2df83d36b/img/Screenshot%202025-01-27%20142336.png)


Now lets test the UPDATE Method for a single item in the table by modifying it 


![image_alt](https://github.com/Tatenda-Prince/Automating-the-Deployment-of-a-Serverless-CRUD-App-with-Python/blob/33fb604872ce52a4a8e8f1a6da5d0cd2df83d36b/img/Screenshot%202025-01-27%20142336.png)


You can also, verify that the productId status was updated from the DynamoDB table item.

indeed the price was changed to 1000


![image_alt]()


Now lets test the DELETE Method for a single item in the table 

productId 10002

![image_alt]()


You can also, verify that the productId was deleted from the DynamoDB table item.


![image_alt]()



Now lets test the GET Method to get all the remaining items in the table 

![image_alt]()


all the remaining items have been returned successfully 


Congratulations!

That’s it! You’ve successfully completed “Building a Serverless Backend”. We’ve utilized lambda, Python, to automate the provisioning of a serverless CRUD application using AWS’s native serverless services API Gateway, Lambda and DynamoDB!
























