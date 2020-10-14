import requests
import yaml


# GET handler
def get(url):
    try:
        response = requests.get(url)
        if response.status_code >= 200 and response.status_code < 300:
            return response.json()
        print(response.text)
    except Exception as e:
        print(e)


# POST handler
def post(url, data):
    try:
        response = requests.post(url, json=data)
        if response.status_code >= 200 and response.status_code < 300:
            return response
        print(response.text)
    except Exception as e:
        print(e)


# Extract urls from yaml file
def get_urls():
    with open('config.yaml') as f:
        config = yaml.safe_load(f)
    return config


# Extract retaurants from json reponse
def extract_data(data):
    retaurants = []
    for record in data['data']:
        retaurants.append(record[8])
    return retaurants



# Main function entry point.
def main():
    config = get_urls() 
    raw_data = get(config['GET_URL'])
    data = extract_data(raw_data)
    post(config['POST_URL'], data)


if __name__ == "__main__":
    main()
