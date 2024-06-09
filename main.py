import argparse
from utils.banner import Banner
from utils.internet_check import InternetCheck
from includes.scanning import Scanning
from includes.write_and_read import WriteAndRead
from includes.url_reader import URLReader

def main():
    banner = Banner("OPEN_REDIRECT")
    banner.print_simple_banner()
    banner.print_ascii_banner()
    parser = argparse.ArgumentParser(description="My Tool for Various Operations")
    parser.add_argument('-u', '--url', help='URL to be processed', type=str)
    parser.add_argument('-f', '--file', help='File location of URLs to be processed', type=str)
    parser.add_argument('-p', '--payload', help='File location of payloads to be used', type=str)
    args = parser.parse_args()
    if not any(vars(args).values()):
        parser.print_help()
        return
    if InternetCheck.check_connection():
        print("Internet connection is active.")
    else:
        print("No internet connection.")
    file_manager = WriteAndRead()
    url_reader = URLReader()
    scanner = Scanning()
    if args.url:
        print(f"Processing URL: {args.url}")
        scanner.add_url(args.url)
    if args.file:
        print(f"Processing URLs from file: {args.file}")
        url_reader.read_urls_one_by_one(args.file, scanner)
    if args.payload:
        print(f"Loading payloads from file: {args.payload}")
        file_manager.read_payloads_one_by_one(args.payload, scanner)
    else:
        scanner.start_scan()
if __name__ == "__main__":
    main()
