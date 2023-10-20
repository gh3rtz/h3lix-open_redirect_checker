# h3lix_openredirect

h3lix_openredirect is a simple Python tool for checking Open Redirect Vulnerabilities in a list of URLs. This tool uses the `argparse`, `requests`, `art`, and `termcolor` libraries to provide an interactive command-line interface and colorful output.

## Features

- Checks a list of URLs for Open Redirect Vulnerabilities.
- Customizable payload to test for open redirect.
- Supports reading URLs from a file.
- Provides colorful output with ASCII art.

## Requirements

Ensure you have the following Python libraries installed:

- `argparse`
- `requests`
- `art`
- `termcolor`

You can install them using `pip`:

```shell
pip install -r requirements.txt
```

## How to Use

Clone or download the repository to your local machine.

Create a file containing the list of URLs you want to test. Each URL should contain the placeholder FUZZ, which will be replaced with your payload. For example:

`https://example.com/redirect?url=FUZZ`
`https://testsite.com/go?to=FUZZ`

Run the tool with the following `command`:

```shell
python openredirect.py -l <file_with_urls.txt> -p <your_payload>
```

-l or --file: Specify the file containing the list of URLs.
-p or --payload: Specify the payload to test for open redirects.

## Author

Givari Hertz
Twitter: @gh3rtz
Instagram: @givarirmdn
Feel free to reach out to the author for feedback or questions.
