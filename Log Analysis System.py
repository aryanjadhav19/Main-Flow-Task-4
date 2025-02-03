import re
from collections import Counter

# Function to parse log file and extract insights
def parse_log_file(file_path):
    ip_counter = Counter()
    code_counter = Counter()
    url_counter = Counter()

    try:
        # Open the log file in read mode
        with open(file_path, 'r') as file:
            # Loop through each line of the log file
            for line in file:
                # Regular expression pattern to capture IP, URL, and Response Code
                match = re.match(r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[.*\] "GET (?P<url>.+?) HTTP.*" (?P<code>\d+)', line)
                if match:
                    ip = match.group('ip')
                    url = match.group('url')
                    code = match.group('code')

                    # Increment counters for IP, URL, and Response Code
                    ip_counter[ip] += 1
                    url_counter[url] += 1
                    code_counter[code] += 1

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Display insights
    display_insights(ip_counter, url_counter, code_counter)

# Function to display insights
def display_insights(ip_counter, url_counter, code_counter):
    print("\nMost Frequent IP Addresses:")
    for ip, count in ip_counter.most_common(10):  # Display top 10 frequent IP addresses
        print(f"{ip}: {count} requests")

    print("\nMost Frequently Accessed URLs:")
    for url, count in url_counter.most_common(10):  # Display top 10 frequently accessed URLs
        print(f"{url}: {count} accesses")

    print("\nResponse Code Statistics:")
    for code, count in code_counter.items():  # Display response code stats
        print(f"Code {code}: {count} occurrences")

# Main function to check file size and parse it
def main():
    file_path = input("Enter the log file path: ")

    # Check file size and ensure it's within the limit (100 MB)
    try:
        file_size = os.path.getsize(file_path)  # Get file size in bytes
        if file_size > 100 * 1024 * 1024:  # 100 MB in bytes
            print("Error: The file size exceeds the 100 MB limit.")
            return
    except Exception as e:
        print(f"An error occurred while checking file size: {e}")
        return

    # Proceed with parsing the log file
    parse_log_file(file_path)

# Run the main function
if __name__ == "__main__":
    import os
    main()