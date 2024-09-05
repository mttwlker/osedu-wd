# import os
import base64
import requests
import csv
import boto3
from botocore.exceptions import ClientError

def get_file_contents(repo_owner, repo_name, file_path, access_token):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}'
    headers = {'Authorization': f'token {access_token}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        content = response.json().get('content', '')
        print(content)
        return content
    else:
        return None

def extract_title_from_content(content):
    decoded_content = base64.b64decode(content).decode('utf-8')
    first_line = decoded_content.split('\n')[0].strip()
    return first_line

def generate_csv(repo_owner, repo_name, access_token, output_csv):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/databank/content'
    headers = {'Authorization': f'token {access_token}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repo_contents = response.json()

        with open(output_csv, 'w', newline='', encoding='utf-8') as csv_file:
            #fieldnames = ['URL', 'Title']
            fieldnames = ['Title','Filename', 'gitURL', 'srvURL']
            
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for file_info in repo_contents:
                if file_info['type'] == 'file' and (file_info['name'].startswith('XX-') or file_info['name'].startswith('XX_')) and file_info['name'].endswith('.md'):
                    file_path = file_info['path']
                    
                    fn = file_info['name']
                    print(fn)

                    file_url = f'https://github.com/{repo_owner}/{repo_name}/blob/main/{file_path}'
                    # server_url = f'https://cci.arts.ac.uk/~mwalker/msc/osedu/apps/viewer/index-nb.html?fp={fn}' #https://cci.arts.ac.uk/~mwalker/msc/osedu/site/target.html?fp=
                    server_url = f'https://cci.arts.ac.uk/~mwalker/msc/osedu/site/target.html?fp={fn}'
                    print(file_url)
                    
                    # Fetch the file content
                    file_content = get_file_contents(repo_owner, repo_name, file_path, access_token)

                    if file_content is not None:

                        title = extract_title_from_content(file_content)

                        writer.writerow({'Title': title, 'Filename': fn, 'gitURL': file_url, 'srvURL': server_url})

def lambda_handler(event, context):
    try:
        # repository_owner = os.environ['mttwlker']
        # repository_name = os.environ['osedu']
        # github_access_token = os.environ['GITHUB_ACCESS_TOKEN']
        # output_csv_file = '/tmp/output.csv'

        repository_owner = 'mttwlker'
        repository_name = 'osedu'
        github_access_token = 'REDACTED'
        output_csv_file = '/tmp/output.csv'

        # Generate CSV file
        generate_csv(repository_owner, repository_name, github_access_token, output_csv_file)


        #s3_bucket = os.environ['S3_BUCKET']
        s3_bucket = 'cci-msc-osedu-admin-info'
        
        s3_key = 'sitemap/osedu-sitemap.csv'
        s3_client = boto3.client('s3')

        s3_client.upload_file(output_csv_file, s3_bucket, s3_key)

        return {
            'statusCode': 200,
            'body': 'CSV file generated and uploaded successfully.'
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
