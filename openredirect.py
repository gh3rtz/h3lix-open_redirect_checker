import argparse
import requests
from art import text2art
from termcolor import colored


# ASCII art for "Givari Hertz"
ascii_art = text2art("OPEN REDIRECT")
instagram_handle = "Twitter: @gh3rtz    Instagram: @givarirmdn"

# Print the ASCII art and Instagram handle in green color
print(colored(ascii_art, "green"))
print(colored(instagram_handle, "green"))


def check_open_redirect(url, redirect_url):
    try:
        response = requests.get(url, allow_redirects=False)
        if response.status_code == 302:
            location = response.headers['Location']
            if redirect_url in location:
                print(colored(f"[VULN] {url} -> Redirects to {location}", 'blue'))
            else:
                print(colored(f"[NOT VULN] {url} -> Redirects to {location}", 'red'))
        else:
            print(colored(f"[NOT VULN] {url}", 'red'))
    except Exception as e:
        print(f"[ERROR] {url} - {str(e)}")

def main():
    try:
        parser = argparse.ArgumentParser(description="Open Redirect Vulnerability Checker")
        parser.add_argument("-l", "--file", help="File with a list of URLs to test", required=True)
        parser.add_argument("-p", "--payload", help="URL to test for open redirect", required=True)
        args = parser.parse_args()

        with open(args.file, "r") as file:
            urls = file.read().splitlines()

        for url in urls:
            modified_url = url.replace("FUZZ", args.payload)
            check_open_redirect(modified_url, args.payload)
    except KeyboardInterrupt:
        print("Good luck, bye bye xD")

if __name__ == "__main__":
    main()
