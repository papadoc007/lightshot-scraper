import requests

base_url = "https://prnt.sc/"

# List of all possible characters for the URL
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Create a text file to write the successful links to
with open("successful_links.txt", "w") as f:
    f.write("")

# Loop through all possible 6-character combinations for the URL
for i in range(len(chars)):
    for j in range(len(chars)):
        for k in range(len(chars)):
            for l in range(len(chars)):
                for m in range(len(chars)):
                    for n in range(len(chars)):
                        url = base_url + chars[i] + chars[j] + chars[k] + chars[l] + chars[m] + chars[n]
                        try:
                            response = requests.get(url)
                            if response.status_code == 200:
                                print("SUCCESS: " + url)
                                with open("successful_links.txt", "a") as f:
                                    f.write(url + "\n")
                            else:
                                print("FAILURE: " + url + " (" + str(response.status_code) + ")")
                        except requests.exceptions.RequestException as e:
                            print("EXCEPTION: " + url + " (" + str(e) + ")")
                            continue