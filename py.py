import requests

def ban_account(username, password, target_username):
    url = "https://www.instagram.com/accounts/ban/"
    data = {
        "username": username,
        "password": password,
        "target_username": target_username
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Account banned successfully!")
    else:
        print("Failed to ban account.")

username = "your_username"
password = "your_password"
target_username = "target_username"

ban_account(username, password, target_username)
