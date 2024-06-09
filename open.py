import argparse
from utils.banner import Banner
from utils.internet_check import InternetCheck
from includes.scanning import Scanning
from includes.write_and_read import WriteAndRead

def main():
    banner = Banner("Open_Drirect")
    banner.print_ascii_banner()
    banner.print_simple_banner()
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help='URL to be processed', type=str)
    parser.add_argument('-p', '--payload', help='File location of payloads to be used', type=str)
    args = parser.parse_args()
    if not any(vars(args).values()):
        parser.print_help()
        return
    if InternetCheck.check_connection():
        print("Internet connection is active.")
    else:
        print("No internet connection.")

    # Write and read from file
    file_manager = WriteAndRead()

    # Initialize scanner
    scanner = Scanning()

    # Load payloads if file is provided
    if args.payload:
        print(f"Loading payloads from file: {args.payload}")
        scanner.add_payloads_from_file(args.payload)

    # Process URL if provided
    if args.url:
        print(f"Processing URL: {args.url}")
        scanner.add_url(args.url)
        scanner.start_scan()

    # Process file if provided
    if args.file:
        print(f"Processing file: {args.file}")
        urls = file_manager.read_from_file(args.file).splitlines()
        for url in urls:
            scanner.add_url(url)
        scanner.start_scan()

if __name__ == "__main__":
    main()
