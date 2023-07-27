import email
import sys

def process_part(part):
    content_type = part.get_content_type()

    if "text/plain" in content_type:
        return part.get_payload(decode=True).decode()

    if "text/html" in content_type:
        return part.get_payload(decode=True).decode()

    if "multipart" in content_type:
        parts = part.get_payload()
        body = ""
        for p in parts:
            body += process_part(p) + "\n"
        return body

def analyze_email_header(email_data):
    try:
        msg = email.message_from_string(email_data)
        headers = msg.items()
        print("------ Email Headers ------")
        for key, value in headers:
            print(f"{key}: {value}")
        print("---------------------------")

        body = process_part(msg)
        print("------ Email Body ------")
        print(body)
        print("------------------------")

    except Exception as e:
        print(f"Error analyzing email header: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_email_header.py <path_to_email_file>")
        sys.exit(1)

    email_file = sys.argv[1]
    with open(email_file, "r") as file:
        email_data = file.read()

    analyze_email_header(email_data)
