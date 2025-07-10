import argparse
import requests
from platforms import SITES

def check_username(username):
    print(f"[*] Checking username: {username}")
    for site, url in SITES.items():
        try:
            response = requests.get(url.format(username))
            if response.status_code == 200:
                print(f"[+] {site}: {url.format(username)}")
            else:
                print(f"[-] {site}: Not Found")
        except requests.exceptions.RequestException as e:
            print(f"[!] Error checking {site}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check for username existence on various social media platforms.")
    parser.add_argument("username", help="The username to check.")
    args = parser.parse_args()
    check_username(args.username)
