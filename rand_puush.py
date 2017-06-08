import urllib.request, webbrowser, string, random, sys

def generate_link():
    return "https://puu.sh/" + ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=5)) + "/" + "filename_doesnt_matter.png"

def get_request(url):
    return urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})

def check_link(req):
    try:
        html = urllib.request.urlopen(req).read()
        # Check if it's a usable url
        if 'That puush could not be found.' not in str(
                html) and 'You do not have access to view that puush.' not in str(html):
            return html
    except urllib.error.HTTPError:
        pass
    return False

def update_console(found, generated):
    sys.stdout.write("\r{0}".format("Found "+str(found)+" out of "+str(generated)+" links"))
    sys.stdout.flush()
    return

def open_links(links):
    for link in links:
        webbrowser.open_new_tab(link)
    return

# Check arguments
if len(sys.argv) < 2:
    n = 1
# Set amount of links to find
else:
    try:
        n = int(sys.argv[1])
    except:
        n = 1
        
i = 0 # amount of generated links
links = [] # array of found link

print("Started...")
print("Going to find "+str(n)+" link(s)...")
while len(links) < n:
    # Generate url
    url = generate_link()
    # Count++
    i += 1
    # Get request
    req = get_request(url)
    # Check
    html = check_link(req)
    # Add
    if html != False:
        links.append(url)
    # Update console
    update_console(len(links), i)
print("\nLinks:")
for x in links:
    print(x)
print("Opening links...")
open_links(links)
input("Done! Press any key to exit.\n")