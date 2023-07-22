import requests

def download_weather():
    url = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization=rdec-key-123-45678-011121314&format=JSON'
    response = requests.get(url)
    if response.status_code

def main():
    print("main function執行")
if __name__=="__main__":
    main()