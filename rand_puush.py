import urllib.request, webbrowser, string, random, sys, ctypes, argparse
from threading import Thread

# ----- Globals -----

global args
global toFindCount
global generatedCount  # amount of generated links
global foundCount  # array of found links
generatedCount = 0
foundCount = 0
global endless  # endless mode


# ----- Functions -----

def task():
    global args
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
            if args.output_urls_only:
                print(url)
            else:
                print('\n' + url)
            if not args.no_auto_open:
                webbrowser.open_new_tab(url)
        if not args.output_urls_only:
            update_console(foundCount, generatedCount)
        if args.endless is not True and foundCount >= toFindCount:
            return


def generate_link():
    # Generate link with random string
    # https://puu.sh/[5 characters]/filename.png
    return "https://puu.sh/" + ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits,
                                                      k=5)) + "/" + "random.png"


def check_link(url):
    # Generate request
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        # Fetch html from url, may throw an HTTPError (Forbidden)
        html = urllib.request.urlopen(req).read()
        # Check if it's a usable url, if so, we return it
        if 'That puush could not be found.' not in str(html) and 'You do not have access to view that puush.' not in str(html):
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

def parse_args():
    parser = argparse.ArgumentParser(description="Random Puush - Opens a (or multiple) random public Puush.me links!", epilog="https://github.com/Maxzilla60/Random-Puush")
    parser.add_argument("-a", "--amount", type=int, help="amount of Puush links to find, default is 1", default=1)
    parser.add_argument("-th", "--threadcount", action="store", type=int, help="amount of threads to use, default is 10", default=10)
    parser.add_argument("-s", "--output-urls-only", action="store_true", help="print out only the found links, default is False")
    parser.add_argument("-e", "--endless", action="store_true", help="enable endless mode, opening links as it finds them, default is False")
    parser.add_argument("-no", "--no-auto-open", action="store_true", help="disable automatically opening found links in browser, default is False")
    return parser.parse_args()

# ----- Main -----

# Set Windows console title
ctypes.windll.kernel32.SetConsoleTitleW("Random Puush")

# Parse arguments
args = parse_args()
toFindCount = args.amount
threadAmount = args.threadcount

# Amount of threads validation
if threadAmount <= 0:
    threadAmount = 10

if not args.output_urls_only:
    print("-- Random Puush --")
    print("- by Maxzilla -")

# Check for endless mode:
if not args.output_urls_only:
    if args.endless:
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