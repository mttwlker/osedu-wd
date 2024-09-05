import requests
import json
#import os
import base64

def lambda_handler(event, context):
    print("python lambda function begin")
    # print(event)
    
    # # Extract variables from the event
    # markdown_content = event['markdownDocument']
    # filename = event['fn']

    # Parse the JSON in the 'body' field
    body = json.loads(event['body'])

    # Extract variables from the parsed body
    markdown_content = body['markdownDocument']
    filename = body['fn']

    print(markdown_content)
    
    # GitHub repository details
    repo_owner = 'mttwlker'
    repo_name = 'osedu'
    
    #github_token = os.environ('GITHUB_TOKEN')
    github_token = 'REDACTED'

    # Create a new file in the repository
    create_file_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/databank/content/{filename}'
    
    # Encode the content to base64
    content_base64 = base64.b64encode(markdown_content.encode()).decode()

    # Build the request payload
    payload = {
        "message": "Add new file",
        "content": content_base64
    }

    # Add authentication header
    headers = {
        'Authorization': f'token {github_token}'
    }

    # Make the request to create the file
    response = requests.put(create_file_url, data=json.dumps(payload), headers=headers)

    print(response.status_code)
    print(response)

    response_data = {
        'statusCode': 201,  # You can change this status code based on your requirements
        'body': 'Hello, Lambda World!'
    }

    # Convert dictionary to JSON string
    response_json = json.dumps(response_data)

    # return response_json

    print(response_json)

    #return "hello world"

    if response.status_code == 201:
        # response = {
        #     'statusCode': 201,
        #     'body': json.dumps({'message': "File uploaded successfully!"})
        # }

        # response = {
        #     'headers':{
        #         'Content-Type': 'application/json',
        #         'statusCode': 201
        #     },
            
        #     # 'headers': {
        #     #     'Content-Type': 'application/json',
        #     #     'Access-Control-Allow-Origin': '*',
        #     #     'Access-Control-Allow-Headers': 'Content-Type',
        #     #     'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        #     # },
        #     'body': json.dumps({'message': "File uploaded successfully!"})
        # }

        response = {
            "statusCode": 200,
            "body": json.dumps({
                "message": "upload success"
                # "location": ip.text.replace("\n", "")
            })
        }

        print(json.dumps(response, indent=2)) # debugging

        testVar = '`File saved to repo successfully! <a href="${liveUrl}" target="_blank">View here!</a>`'

        return response



    else:
        print("CONSOLE FAILURE")
        return {
            'statusCode': response.status_code,
            'body': json.dumps(f'Failed to upload file. Response: {response.text}')
        }
