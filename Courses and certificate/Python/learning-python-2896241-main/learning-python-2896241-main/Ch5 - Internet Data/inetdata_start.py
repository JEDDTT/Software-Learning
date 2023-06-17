#
# Example file for retrieving data from the internet
# LinkedIn Learning Python course by Joe Marini
#
import urllib.request


def main():
    pass  # this is a placeholder, do-nothing statement
    webUrl = urllib.request.urlopen("http://www.google.com")
    # print(webUrl)
    print("The result code:", webUrl.getcode())
    data = webUrl.read()
    print(data)  # It will return the google's home page


if __name__ == "__main__":
    main()
