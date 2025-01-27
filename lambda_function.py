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
