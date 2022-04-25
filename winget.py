import subprocess
import re

# Make it possible to debug
debug = False

# IDs of the packages you wish to ignore
ignoreIds = [
    "",
]

# Checking for upgrades and removing the first lines
toCheck = subprocess.run(["winget", "upgrade"], capture_output=True).stdout.decode('utf-8').split("\n")[2:]

# Removing the last 2 lines
toCheck.pop(len(toCheck)-1)
toCheck.pop(len(toCheck)-1)
if debug == True:
    print("Possible upgrades include:")
    print(toCheck)

# Checking for the amount of upgrades that are ready
numberOfUpgrades = len(toCheck)

# Initializing values
i = 0
upgradeable = []
skipped = []

# Going over each upgrade
while i < numberOfUpgrades:

    # Adding possible upgrade to the upgradeable list
    if debug == True:
        print("The package itself is:")
        print(str(toCheck[i]))
    package = re.findall(r'[\S]+\.[\S]+' , str(toCheck[i]))
    packageID = package[0]
    if debug == True:
        print("Package name is:")
        print(package)
        print("PackageID is:")
        print(packageID)
    if debug == True:
        print(upgradeable)

    # Upgrading if not ignored
    if packageID not in ignoreIds:
        subprocess.run(["winget", "upgrade", packageID])
        upgradeable.append(packageID)
        if debug == True:
            print("winget upgrade ", upgradeable[i])

    # Adding possible upgrade to the ignore list
    else:
        skipped.append(str(toCheck[i]).split(" ")[1])
    i += 1

# Logging/Output
print("Upgradeable: \t", upgradeable)
print("Skipped: \t", skipped)
