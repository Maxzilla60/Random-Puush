import urllib.request, webbrowser, string, random, sys, ctypes
from threading import Thread

# ----- Globals -----

global toFindCount
global generatedCount  # amount of generated links
global foundCount  # array of found links
generatedCount = 0
foundCount = 0
global endless  # endless mode


# ----- Functions -----

def task():
    global toFindCount
    global foundCount
    global generatedCount
    while True:
        url = generate_link()  # Generate url
        generatedCount += 1  # Count++
        html = check_link(url)  # Check
        # Add:
        if html is not False:
            foundCount += 1
            print("\n" + url)
            webbrowser.open_new_tab(url)
        update_console(foundCount, generatedCount)
        if endless is not True and toFindCount < foundCount:
            return


def generate_link():
    # Generate link with random string
    # https://puu.sh/[5 characters]/filename.png
    return "https://puu.sh/" + ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits,
                                                      k=5)) + "/" + "filename_doesnt_matter.png"


def check_link(url):
    # Generate request
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
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


def update_console(found, generated):
    # Cool dynamic display of found and generated foundCount
    sys.stdout.write("\r{0}".format("Found " + str(found) + " out of " + str(generated) + " links"))
    sys.stdout.flush()
    return


# ----- Main -----

# Set Windows console title
ctypes.windll.kernel32.SetConsoleTitleW("Random Puush")

# Check arguments
toFindCount = 1
threadAmount = 10

if len(sys.argv) >= 3:
    try:
        toFindCount = int(sys.argv[1])
        threadAmount = int(sys.argv[2])
    except:
        print("Error parsing arguments")
        exit()
elif len(sys.argv) is 2:
    try:
        toFindCount = int(sys.argv[1])
    except:
        print("Error parsing arguments")
        exit()

print("-- Random Puush --")
print("- by Maxzilla -")

endless = toFindCount < 0
if endless:
    print("Running endless mode (using " + str(threadAmount) + " threads). Press Ctrl+C to terminate script...")
else:
    print("Going to find at least " + str(toFindCount) + " link(s) using " + str(threadAmount) + " threads...")

# Initialize threads:
threads = []
for i in range(threadAmount):
    threads.append(Thread(target=task))
# Start threads:
for t in threads:
    t.start()
# Wait for threads:
for t in threads:
    t.join()

input("\nDone! Press enter to exit.\n")
