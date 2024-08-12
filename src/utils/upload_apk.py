import requests

def upload_apk(file_path, username, access_key):
    url = "https://api-cloud.browserstack.com/app-automate/upload"
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, files=files, auth=(username, access_key))
    if response.status_code == 200:
        return response.json()["app_url"]
    else:
        raise Exception(f"Failed to upload APK: {response.text}")

# Example usage:
if __name__ == "__main__":
    username = "hellencheptoo_Ffbaol"
    access_key = "ppJkH5urFzdsyRZkUrxs"
    file_path = "src/utils/LocalSample.apk"  # Path to your APK file

    app_url = upload_apk(file_path, username, access_key)
    print("Uploaded APK URL:", app_url)
