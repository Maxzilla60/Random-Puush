# https://github.com/Maxzilla60/Random-Puush
import urllib.request, webbrowser, string, random, sys

# --- Functions ---

def generate_link():
	# Generate link with random string 
	# https://puu.sh/[5 characters].png
    return "https://puu.sh/" + ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=5)) + ".png"

def get_request(url):
    return urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})

def check_link(req):
    try:
    	# Fetch html from url, may throw an HTTPError (Forbidden)
        html = urllib.request.urlopen(req).read()
        # Check if it's a usable url, if so, we return it
        if 'That puush could not be found.' not in str(
                html) and 'You do not have access to view that puush.' not in str(html):
            return html
    except urllib.error.HTTPError:
        pass 
    # If it wasn't a usable url, return false
    return False

def update_console(generated):
	# Cool dynamic display of found and generated links
    sys.stdout.write("\r{0}".format("Generated "+str(generated)+" links..."))
    sys.stdout.flush()
    return

# --- Main ---

def rand_puush():
    n = 1 # amount of to be generated links
    i = 0 # amount of generated links
    html = False # link to return

    print("Started...")
    while html == False:
        # Generate url
        url = generate_link()
        # Count++
        i += 1
        # Check
        html = check_link(get_request(url))
        # Update console
        update_console(i)
    print("\nLink found: "+url)
    return url