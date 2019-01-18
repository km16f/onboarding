import requests
import json
import sys


def checkuser(name):
    c = requests.get("https://api.github.com/users/%s" % name)
    if c.status_code == 404:
        print("Error: Invalid User")
        quit()
    elif c.status_code == 200:
        print("User Found")
        return True


def inOrg(name):
    check = requests.get("https://api.github.com/orgs/basepipe/members/%s" % name, auth=('km16f', 'kmolter3#'))
    if check.status_code == 204:
        print("User Already in Org")
        quit()
    else:
        return False


if len(sys.argv) > 1:
    user = sys.argv[1]
elif len(sys.argv) == 1:
    user = input("Enter Github Username: ")

if checkuser(user) and not inOrg(user):
    r = requests.put("https://api.github.com/orgs/basepipe/memberships/%s" % user, auth=('km16f','kmolter3#'))

if r.status_code == 200:
    print("Invitation Sent")
elif r.status_code == 404:
    print("Error: Authentication Needed")

print(r.content)

print("Testing push")
