# ARGOSQueryTool.py
# Description: Parses a line of ARGOS tracking data 
# Created by: Erin Ansbro (erin.ansbro@duke.edu)
# Created on: Sept, 2024

#%%getting file
fileName = "Sara.txt"
fileObj = open(fileName, 'r')

#%% first line of file
lineStrings = fileObj.readlines()
print ("There are {} records in the file".format(len(lineStrings)))
# Close the file object
fileObj.close()

#%%Create dictionaries
dateDict = {}
locationDict = {}

#%%for loop
for lineString in lineStrings:
    if lineString[0] in ("#", "u"): continue

    #create list object
    lineData = lineString.split("\t")
    # Assign variables to specfic items in the list
    recordID = lineData[0]              # ARGOS tracking record ID
    obsDateTime = lineData[2]           # Observation date and time (combined)
    obsDate = obsDateTime.split()[0]    # Observation date - first item in obsDateTime list object
    obsTime = obsDateTime.split()[1]    # Observation time - second item in obsDateTime list object
    obsLC = lineData[3]                 # Observation Location Class
    obsLat = lineData[5]                # Observation Latitude
    obsLon = lineData[6]                # Observation Longitude
       
    #Filter records that get added to the dictionary
    if obsLC in ("1","2","3"):
        # Add values to dictionary
        dateDict[recordID] = obsDate
        locationDict[recordID] = (obsLat, obsLon)

#%% Ask the user for a date, specifying the format
userDate = input("Enter a date (M/D/YYYY)")

#%%Create an empty key list
keyList = []

#%% Loop through all key, value pairs in the dateDictionary
for k, v in dateDict.items():
    #See if the date (the value) matches the user date
    if v == userDate:
        keyList.append(k)

#%% Check that at least one key was returned; tell the user if not.
if len(keyList) == 0:
    print ("No observations recorded for {}".format(userDate))
else:
    # Loop through each key and report the associated date location
    for k in keyList:
        theDate = dateDict[k]
        theLocation = locationDict[k]
        theLat = theLocation[0]
        theLon = theLocation[1]
        print("Record {0}: Sara was see at {1}N-{2}W, on {3}".format(k,theLat,theLon,theDate))