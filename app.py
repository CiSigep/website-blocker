import time
from datetime import datetime as dt

# hosts_location = "hosts"  # Development hosts location
hosts_location = r"C:\Windows\System32\drivers\etc\hosts"

redirect = "127.0.0.1"
websites = ["facebook.com", "www.facebook.com", "reddit.com", "www.reddit.com"]

# If inside the times, add redirects to the hosts file, else remove them
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        with open(hosts_location, "r+") as hosts:
            contents = hosts.read()
            for website in websites:
                if website in contents:
                    pass
                else:
                    hosts.write(redirect + " " + website + "\n")
                    print("Added " + website)
    else:
        with open(hosts_location, "r+") as hosts:
            contents = hosts.readlines()
            hosts.seek(0)
            for line in contents:
                if not any(website in line for website in websites):
                    hosts.write(line)
            hosts.truncate()
        print("Cleared hosts file")
    time.sleep(5)
