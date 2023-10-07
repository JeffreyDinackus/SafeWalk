from flask import Flask, render_template


app = Flask(__name__)


data = [
 {
   "FIELD1": "Case\n Number",
   "FIELD2": "Nature\n Classification",
   "FIELD3": "Date/Time\n Reported",
   "FIELD4": "Date/Time\n Occurred",
   "FIELD5": "General\n Location",
   "FIELD6": "Campus",
   "FIELD7": "Disposition",
   "FIELD8": "Description"
 },
 {
   "FIELD1": "2023-000243",
   "FIELD2": "Police Service",
   "FIELD3": "10-5-2023\n 1742",
   "FIELD4": "10-5-2023\n 0540",
   "FIELD5": "Pender 4",
   "FIELD6": "PN",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of  someone attempting to get into the building"
 },
 {
   "FIELD1": "2023-000242",
   "FIELD2": "Drug Violation",
   "FIELD3": "10-5-2023\n 1635",
   "FIELD4": "10-5-2023\n 1635",
   "FIELD5": "Parking Garage",
   "FIELD6": "AN",
   "FIELD7": "Report Taken Summons Issued 2X Referred to Student Conduct",
   "FIELD8": "Individual under 21 possessing marijuana and drug paraphernalia"
 },
 {
   "FIELD1": "2023-000241",
   "FIELD2": "Police Service",
   "FIELD3": "10-5-2023\n 1521",
   "FIELD4": "Between 10-4-2023 at 2200 and 10-5-2023 at 0800",
   "FIELD5": "Not on NOVA’s Clery Geography",
   "FIELD6": "MA",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a NOVA laptop stolen off campus"
 },
 {
   "FIELD1": "2023-000239",
   "FIELD2": "Welfare Check",
   "FIELD3": "10-5-2023\n 1123",
   "FIELD4": "10-5-2023\n 1123",
   "FIELD5": "LHEC Building",
   "FIELD6": "LO",
   "FIELD7": "Report Taken NOVACares Notified",
   "FIELD8": "Welfare check request for a student on campus"
 },
 {
   "FIELD1": "2023-000237",
   "FIELD2": "Weapons Violation",
   "FIELD3": "10-4-23\n 1623",
   "FIELD4": "Unknown",
   "FIELD5": "Soccer Field near Lot LO7",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of rusted old bullet hole damage to a soccer field storage box"
 },
 {
   "FIELD1": "2310040031",
   "FIELD2": "Suspicious Vehicle",
   "FIELD3": "10-4-2023\n 1129",
   "FIELD4": "10-4-2023\n 129",
   "FIELD5": "Lot AN3",
   "FIELD6": "AN",
   "FIELD7": "Assisted",
   "FIELD8": "Report of a disabled and wrecked vehicle parked in Lot AN3"
 },
 {
   "FIELD1": "2023-000236",
   "FIELD2": "Threats\n (Stalking)\n (Dating Violence)",
   "FIELD3": "10-4-2023\n 0951",
   "FIELD4": "10-4-2023\n 0951",
   "FIELD5": "5000 Dawes Ave",
   "FIELD6": "AL",
   "FIELD7": "Report Taken Title IX and Student Conduct notified",
   "FIELD8": "Report of an ex-partner  threatening to send nude photos of complainant and stalking them"
 },
 {
   "FIELD1": "2023-000235",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "10-3-2023\n 1421",
   "FIELD4": "9-28-2023\n 0946",
   "FIELD5": "CT Building",
   "FIELD6": "AN",
   "FIELD7": "Report Taken NOVACares Notified",
   "FIELD8": "Report of an individual writing suspicious things"
 },
 {
   "FIELD1": "2023-000234",
   "FIELD2": "Hit & Run",
   "FIELD3": "10-3-2023\n 1241",
   "FIELD4": "10-3-2023\n 1030-1220",
   "FIELD5": "Parking Garage",
   "FIELD6": "AN",
   "FIELD7": "Report Taken Unfounded",
   "FIELD8": "Report of a hit and run and later discovered it did not take place on campus"
 },
 {
   "FIELD1": "2023-000233\n (Related to 2023-000232)",
   "FIELD2": "Assault",
   "FIELD3": "10-2-2023\n 2122",
   "FIELD4": "10-2-2023\n 2122",
   "FIELD5": "LHEC Building",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a simple assault of 3 individuals by the individual  from case 2023-000232"
 },
 {
   "FIELD1": "2023-000231",
   "FIELD2": "EMS",
   "FIELD3": "10-2-2023\n 1417",
   "FIELD4": "10-2-2023\n 1417",
   "FIELD5": "CC Building",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of individual having a medical issue"
 },
 {
   "FIELD1": "2023-000232",
   "FIELD2": "Assault",
   "FIELD3": "10-2-2023\n 1414",
   "FIELD4": "10-2-2023\n 1414",
   "FIELD5": "LC Building",
   "FIELD6": "LO",
   "FIELD7": "Report Taken Cleared by arrest No Trespass Order Issued",
   "FIELD8": "Report of simple assault by an identified male"
 },
 {
   "FIELD1": "2310010008",
   "FIELD2": "Welfare Check",
   "FIELD3": "10-1-23\n 1610",
   "FIELD4": "10-1-23\n 1610",
   "FIELD5": "Behind Beauregard Parking Garage",
   "FIELD6": "AL",
   "FIELD7": "No Police Action",
   "FIELD8": "Unit observed a homeless individual lying in the grass area"
 }
]

# print(data)


logsof2022 = [
 {
   "FIELD1": "Case\n Number",
   "FIELD2": "Nature\n Classification",
   "FIELD3": "Date/Time\n Reported",
   "FIELD4": "Date/Time\n Occurred",
   "FIELD5": "General\n Location",
   "FIELD6": "Campus",
   "FIELD7": "Disposition",
   "FIELD8": "Description"
 },
 {
   "FIELD1": "2022-000257",
   "FIELD2": "Domestic",
   "FIELD3": "12-29-22\n 1859",
   "FIELD4": "12-29-22\n 1859",
   "FIELD5": "B10 Lot\n (Not on Clery Geography)",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complaint of an argument in the parking lot"
 },
 {
   "FIELD1": "2022-000256",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "12-19-22\n 0702",
   "FIELD4": "12-19-22\n 0702",
   "FIELD5": "Greenhouse",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported hearing screaming from a women walking towards the CS building"
 },
 {
   "FIELD1": "2022-000255",
   "FIELD2": "Vandalism",
   "FIELD3": "12-17-22\n 1405",
   "FIELD4": "Unknown",
   "FIELD5": "4th Floor Bisdorf",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Unit observed damage to a window near 454-A"
 },
 {
   "FIELD1": "2212160001",
   "FIELD2": "Suspicious Vehicle",
   "FIELD3": "12-16-22\n 0745",
   "FIELD4": "12-16-22\n 0745",
   "FIELD5": "B1 Lot",
   "FIELD6": "AL",
   "FIELD7": "Advised TOT Parking Services",
   "FIELD8": "Report of a camper parked in the lot for days"
 },
 {
   "FIELD1": "2022-000254",
   "FIELD2": "Larceny",
   "FIELD3": "12-13-22\n 1443",
   "FIELD4": "12-12-22\n Between\n 1100-1700",
   "FIELD5": "B1 Lot",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported someone stole the license plate off of their vehicle"
 },
 {
   "FIELD1": "2212120030",
   "FIELD2": "Suspicious Vehicle",
   "FIELD3": "12-12-22\n 1802",
   "FIELD4": "12-12-22\n 1802",
   "FIELD5": "Parking Garage",
   "FIELD6": "AL",
   "FIELD7": "Advised",
   "FIELD8": "Unit out with a suspicious vehicle at the location"
 },
 {
   "FIELD1": "2022-000253",
   "FIELD2": "Suspicious Item",
   "FIELD3": "12-12-22\n 1203",
   "FIELD4": "12-12-22\n 1203",
   "FIELD5": "Bisdorf 352",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported receiving an unwanted unexpected gift from a former student"
 },
 {
   "FIELD1": "2022-000252",
   "FIELD2": "Threats\n (Hate Crime)\n (Intimidation)\n (National Origin)",
   "FIELD3": "12-12-22\n 1141",
   "FIELD4": "12-7-22\n or\n 12-8-22\n Unknown",
   "FIELD5": "AN",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported a person threatened to kill them if they did not remove a Israel flag"
 },
 {
   "FIELD1": "2022-000251",
   "FIELD2": "Suspicious Vehicle",
   "FIELD3": "12-12-22\n 1116",
   "FIELD4": "12-12-22\n 1116",
   "FIELD5": "Parking Garage",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a suspicious vehicle parked at the location with TX plates parked for extended periods of time"
 },
 {
   "FIELD1": "2022-000250",
   "FIELD2": "Suspicious Activity\n (Drug Investigation)",
   "FIELD3": "12-10-22\n 0918",
   "FIELD4": "12-1-22\n Unknown",
   "FIELD5": "Parking Garage",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported a group of students smoking marijuana at the location"
 },
 {
   "FIELD1": "2022-000249",
   "FIELD2": "Police Service\n (Suspicious Person)",
   "FIELD3": "12-9-22\n 1318",
   "FIELD4": "12-9-22\n Between\n 0930-1000",
   "FIELD5": "Brault",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Unknown female at the location was inquiring about her missing juvenile son"
 },
 {
   "FIELD1": "2022-000248",
   "FIELD2": "Larceny",
   "FIELD3": "12-8-22\n 1223",
   "FIELD4": "12-5-22\n Between\n 1630-1800",
   "FIELD5": "CFH 206",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported missing money from her wallet at the location"
 },
 {
   "FIELD1": "2022-000247",
   "FIELD2": "Hit & Run",
   "FIELD3": "12-8-22\n 0958",
   "FIELD4": "12-8-22\n 0958",
   "FIELD5": "B6 Lot",
   "FIELD6": "AN",
   "FIELD7": "Report Taken Info Exchanged",
   "FIELD8": "Complainant reported observing a hit and run"
 },
 {
   "FIELD1": "2212070035",
   "FIELD2": "Police Service",
   "FIELD3": "12-7-22\n 1408",
   "FIELD4": "12-7-22\n Between\n 1000-1400",
   "FIELD5": "Parking Garage",
   "FIELD6": "AN",
   "FIELD7": "Assisted",
   "FIELD8": "Complainant reported all of the vehicles were open upon returning to where it was parked"
 },
 {
   "FIELD1": "2022-000246",
   "FIELD2": "Larceny",
   "FIELD3": "12-7-22\n 1252",
   "FIELD4": "12-7-22\n 1252",
   "FIELD5": "Pender 4",
   "FIELD6": "Fairfax",
   "FIELD7": "Report Taken\n Unfounded",
   "FIELD8": "person on the roof stealing HVAC equipment"
 },
 {
   "FIELD1": "2022-000245",
   "FIELD2": "Harassment",
   "FIELD3": "12-6-22\n 2053",
   "FIELD4": "12-6-22\n Between\n 1730-1800",
   "FIELD5": "Library",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported that another student made inappropriate sexual related comments towards her"
 },
 {
   "FIELD1": "2212060038",
   "FIELD2": "Vandalism",
   "FIELD3": "12-6-22\n 1406",
   "FIELD4": "12-6-22\n 1406",
   "FIELD5": "WAS",
   "FIELD6": "WO",
   "FIELD7": "Unfounded",
   "FIELD8": "Report of a lockbox being tampered with and pulled from the wall"
 },
 {
   "FIELD1": "2212050041",
   "FIELD2": "Suspicious Item",
   "FIELD3": "12-5-22\n 1826",
   "FIELD4": "12-5-22\n 1826",
   "FIELD5": "LR Bench",
   "FIELD6": "LO",
   "FIELD7": "Unfounded",
   "FIELD8": "Bag left at the location"
 },
 {
   "FIELD1": "2022-000244",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "12-5-22\n 1107",
   "FIELD4": "12-3-22\n 2115",
   "FIELD5": "CE",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of concerning behavior involving young children"
 },
 {
   "FIELD1": "2212040006",
   "FIELD2": "Assist other agency\n (Hit & Run)",
   "FIELD3": "12-4-22\n 2104",
   "FIELD4": "12-4-22\n 2104",
   "FIELD5": "S. Cottage and Potomac View",
   "FIELD6": "LO",
   "FIELD7": "Assisted",
   "FIELD8": "Report that LOCSO is looking for a vehicle in the area involved in a hit and run"
 },
 {
   "FIELD1": "2022-000243",
   "FIELD2": "Police Service\n (Extortion)",
   "FIELD3": "12-1-22\n 1250",
   "FIELD4": "11-30-22\n unknown",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported being threatened to release videos if they did not pay"
 },
 {
   "FIELD1": "2212010026",
   "FIELD2": "Police Service\n (Theft)",
   "FIELD3": "12-1-22\n 1157",
   "FIELD4": "12-1-22\n 1157",
   "FIELD5": "CA 105",
   "FIELD6": "AN",
   "FIELD7": "Assisted",
   "FIELD8": "Complaint of a toddler stealing items from the location"
 },
 {
   "FIELD1": "2212010024",
   "FIELD2": "Public Service\n (Drug Investigation)",
   "FIELD3": "12-1-22\n 1040",
   "FIELD4": "12-1-22\n 1040",
   "FIELD5": "B8 Lot\n Parking Garage",
   "FIELD6": "AL",
   "FIELD7": "GOA",
   "FIELD8": "Complainant reported 4 students smoking marijuana at the location"
 },
 {
   "FIELD1": "2022-000242",
   "FIELD2": "Larceny",
   "FIELD3": "11-30-22\n 1720",
   "FIELD4": "11-30-22\n After\n 1500",
   "FIELD5": "LS 103\n or\n LS 121A",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a stolen laptop computer at the location"
 },
 {
   "FIELD1": "2022-000240",
   "FIELD2": "Threats\n (ESRO)",
   "FIELD3": "11-30-22\n 1351",
   "FIELD4": "Previous",
   "FIELD5": "AN",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Unit conducted an ESRO investigation"
 },
 {
   "FIELD1": "2022-000241",
   "FIELD2": "EMS",
   "FIELD3": "11-30-22\n 1231",
   "FIELD4": "11-30-22\n 1231",
   "FIELD5": "CE/CF",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a student having a panic attack at the location"
 },
 {
   "FIELD1": "2211290033",
   "FIELD2": "Disorderly Conduct",
   "FIELD3": "11-29-22\n 1432",
   "FIELD4": "11-29-22\n 1432",
   "FIELD5": "WAS",
   "FIELD6": "WO",
   "FIELD7": "NPA",
   "FIELD8": "Report of a male and female arguing loudly and shoving each other at the location"
 },
 {
   "FIELD1": "2211290031",
   "FIELD2": "Threat Assessment",
   "FIELD3": "11-29-22\n 1414",
   "FIELD4": "11-29-22\n 1414",
   "FIELD5": "Brault",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Unit conducted a threat assessment upon an individual"
 },
 {
   "FIELD1": "2211290004",
   "FIELD2": "Suspicious Person",
   "FIELD3": "11-29-22\n 0706",
   "FIELD4": "11-29-22\n 0706",
   "FIELD5": "B2 Lot",
   "FIELD6": "WO",
   "FIELD7": "GOA",
   "FIELD8": "Report of a person defecating in the parking lot"
 },
 {
   "FIELD1": "2211280037",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "11-28-22\n 1858",
   "FIELD4": "11-28-22\n 1858",
   "FIELD5": "Parking Garage",
   "FIELD6": "AN",
   "FIELD7": "Advised",
   "FIELD8": "Report of two people squatting in the area"
 },
 {
   "FIELD1": "2211280036",
   "FIELD2": "Suspicious Item",
   "FIELD3": "11-28-22\n 1841",
   "FIELD4": "11-28-22\n 1841",
   "FIELD5": "CH",
   "FIELD6": "AN",
   "FIELD7": "Assisted",
   "FIELD8": "Report of a package left at the location"
 },
 {
   "FIELD1": "2211280029",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "11-28-22\n 1630",
   "FIELD4": "11-28-22\n 1630",
   "FIELD5": "WFA Info Desk",
   "FIELD6": "WO",
   "FIELD7": "GOA",
   "FIELD8": "Report someone wrote and left a disturbing message"
 },
 {
   "FIELD1": "221124004",
   "FIELD2": "Traffic Complaint",
   "FIELD3": "11-24-22\n 1330",
   "FIELD4": "11-24-22\n 1330",
   "FIELD5": "B1 Lot",
   "FIELD6": "LO",
   "FIELD7": "GOA",
   "FIELD8": "Report of a vehicle doing burn outs at the location"
 },
 {
   "FIELD1": "2211230016",
   "FIELD2": "Suspicious Person",
   "FIELD3": "11-23-22\n 1205",
   "FIELD4": "11-23-22\n 1205",
   "FIELD5": "Parking Garage",
   "FIELD6": "AN",
   "FIELD7": "GOA",
   "FIELD8": "Complainant reported somebody started screaming at them at the location"
 },
 {
   "FIELD1": "2022-000239",
   "FIELD2": "Larceny",
   "FIELD3": "11-22-22\n 1007",
   "FIELD4": "11-17-22\n Unknown",
   "FIELD5": "227",
   "FIELD6": "MEC",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported stolen supplies from the location"
 },
 {
   "FIELD1": "2022-000238",
   "FIELD2": "Suspicious Person",
   "FIELD3": "11-21-22\n 1820",
   "FIELD4": "11-21-22\n 1820",
   "FIELD5": "Café",
   "FIELD6": "AL",
   "FIELD7": "Report Taken Assisted",
   "FIELD8": "Homeless individual escorted off campus"
 },
 {
   "FIELD1": "2022-000237",
   "FIELD2": "911 Hang-Up",
   "FIELD3": "11-21-22\n 1631",
   "FIELD4": "11-21-22\n 1631",
   "FIELD5": "Phone",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a person wanting to harm themselves"
 },
 {
   "FIELD1": "2211210016\n 2022-000236",
   "FIELD2": "Follow-Up\n to\n 2211210001",
   "FIELD3": "11-21-22\n 0056",
   "FIELD4": "Previous",
   "FIELD5": "Email",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported a student making threats via video"
 },
 {
   "FIELD1": "2211210001",
   "FIELD2": "Threats",
   "FIELD3": "11-21-22\n 0056",
   "FIELD4": "Previous",
   "FIELD5": "Email",
   "FIELD6": "AN",
   "FIELD7": "TOT",
   "FIELD8": "Complainant reported a student making threats via video"
 },
 {
   "FIELD1": "2022-000235",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "11-18-22\n 1244",
   "FIELD4": "Previous",
   "FIELD5": "MEC",
   "FIELD6": "MEC",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a student concerned about being sent home from clinical"
 },
 {
   "FIELD1": "2022-000234",
   "FIELD2": "Police Service",
   "FIELD3": "11-17-22\n 1453",
   "FIELD4": "11-2-22\n 0155",
   "FIELD5": "Facebook",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Professor wanted to report an incident with a former student that occurred on Facebook"
 },
 {
   "FIELD1": "2211170041",
   "FIELD2": "Police Service",
   "FIELD3": "11-17-22\n 1347",
   "FIELD4": "11-17-22\n 1347",
   "FIELD5": "Bench in front of AA 194",
   "FIELD6": "AL",
   "FIELD7": "Advised",
   "FIELD8": "Complaint of a person sleeping on the bench who was just resting to get out of the cold"
 },
 {
   "FIELD1": "2022-000233",
   "FIELD2": "Larceny",
   "FIELD3": "11-15-22\n 1606",
   "FIELD4": "11-14-22\n Between\n 1851-2200",
   "FIELD5": "AA354",
   "FIELD6": "AL",
   "FIELD7": "Report Taken\n Unfounded",
   "FIELD8": "Complaint of a missing laptop which was later returned as missing property"
 },
 {
   "FIELD1": "2022-000232",
   "FIELD2": "Assist Other Agency\n (Missing Person)",
   "FIELD3": "11-15-22\n 1017",
   "FIELD4": "Previous",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "MA",
   "FIELD7": "Report Taken",
   "FIELD8": "Unit assisted another agency with a missing person"
 },
 {
   "FIELD1": "2211140046",
   "FIELD2": "Animal Complaint",
   "FIELD3": "11-14-22\n 1544",
   "FIELD4": "11-14-22\n 1544",
   "FIELD5": "B2 Lot",
   "FIELD6": "LO",
   "FIELD7": "Advised",
   "FIELD8": "Complaint of a dog left in a vehicle"
 },
 {
   "FIELD1": "2022-000231",
   "FIELD2": "Mental",
   "FIELD3": "11-14-22\n 1214",
   "FIELD4": "11-14-22\n 1214",
   "FIELD5": "2nd Floor Library",
   "FIELD6": "AL",
   "FIELD7": "Report Taken TOT\n Alexandria City Police",
   "FIELD8": "Complaint of a student in a mental health crisis on the phone with crisis care"
 },
 {
   "FIELD1": "2211140025",
   "FIELD2": "Hit & Run",
   "FIELD3": "11-14-22\n 1029",
   "FIELD4": "11-14-22\n Previous",
   "FIELD5": "B1",
   "FIELD6": "MA",
   "FIELD7": "Info",
   "FIELD8": "Complainant reported her vehicle was hit while parked in the lot"
 },
 {
   "FIELD1": "2022-000230",
   "FIELD2": "Police Service",
   "FIELD3": "11-14-22\n 1004",
   "FIELD4": "Previous",
   "FIELD5": "AL",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Unit assisted the USSS with an information request"
 },
 {
   "FIELD1": "2022-000229",
   "FIELD2": "Police Service\n (Missing Person)",
   "FIELD3": "11-12-22\n 1440",
   "FIELD4": "Previous",
   "FIELD5": "AN",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported not being able to contact or communicate with a friend for several days"
 },
 {
   "FIELD1": "2211110024",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "11-11-22\n 1358",
   "FIELD4": "11-11-22\n 1358",
   "FIELD5": "113 Founders Hall",
   "FIELD6": "AN",
   "FIELD7": "NPA",
   "FIELD8": "Complaint about a door being unlocked"
 },
 {
   "FIELD1": "2211100056",
   "FIELD2": "Be on the Lookout",
   "FIELD3": "11-10-22\n 1820",
   "FIELD4": "11-10-22\n 1820",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AL",
   "FIELD7": "Assisted",
   "FIELD8": "Report from Alexandria City Police about a missing elderly person"
 },
 {
   "FIELD1": "2211100025",
   "FIELD2": "Suspicious Vehicle",
   "FIELD3": "11-10-22\n 1022",
   "FIELD4": "11-10-22\n 1022",
   "FIELD5": "Level 4 Parking Garage",
   "FIELD6": "AN",
   "FIELD7": "Advised",
   "FIELD8": "Report of a vehicle with it’s doors left open"
 },
 {
   "FIELD1": "2022-000228",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "11-9-22\n 1330",
   "FIELD4": "11-9-22\n Between\n 1110-1230",
   "FIELD5": "Victual Class",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Complaint of inappropriate text communication during a zoom class was posted"
 },
 {
   "FIELD1": "2211090024",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "11-9-22\n 1117",
   "FIELD4": "Previous Week",
   "FIELD5": "Café",
   "FIELD6": "AL",
   "FIELD7": "GOA",
   "FIELD8": "Report of a empty beer bottle at the location"
 },
 {
   "FIELD1": "2022-000226",
   "FIELD2": "Stalking",
   "FIELD3": "11-7-22\n 1000",
   "FIELD4": "Various",
   "FIELD5": "On and Off Campus",
   "FIELD6": "WO",
   "FIELD7": "Report Taken Title IX Notified",
   "FIELD8": "Complainant reported to being followed around by a fellow student"
 },
 {
   "FIELD1": "2022-000227",
   "FIELD2": "Stalking",
   "FIELD3": "11-7-22\n 1515",
   "FIELD4": "Various",
   "FIELD5": "Various",
   "FIELD6": "AN",
   "FIELD7": "Report Taken Title IX Notified",
   "FIELD8": "Complainant reported to being followed and having her photo taken and video taken by another student without her permission"
 },
 {
   "FIELD1": "2022-000225",
   "FIELD2": "Police Service\n (Stalking)",
   "FIELD3": "11-7-22\n 1318",
   "FIELD4": "11-6-22\n 2348",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AL",
   "FIELD7": "Report Taken TOT Alexandria City Police",
   "FIELD8": "Complainant reported a former boyfriend threatened to release information without permission"
 },
 {
   "FIELD1": "2211070047",
   "FIELD2": "Suspicious Item",
   "FIELD3": "11-7-22\n 1234",
   "FIELD4": "11-7-22\n 1234",
   "FIELD5": "Bathroom",
   "FIELD6": "AL",
   "FIELD7": "Unfounded",
   "FIELD8": "Report of a black box at the location since this morning"
 },
 {
   "FIELD1": "2022-000224",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "11-7-22\n 1058",
   "FIELD4": "11-7-22\n 0830",
   "FIELD5": "252",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported an unknown male acting weird at the location"
 },
 {
   "FIELD1": "2022-000222",
   "FIELD2": "Fraud",
   "FIELD3": "11-7-22\n 1032",
   "FIELD4": "Spring 2022",
   "FIELD5": "On-Line",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported someone used his personal information to attend NOVA without his knowledge"
 },
 {
   "FIELD1": "2022-000221",
   "FIELD2": "Larceny",
   "FIELD3": "11-7-22\n 0939",
   "FIELD4": "11-7-22\n 0939",
   "FIELD5": "Bookstore",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Student observed stealing from the bookstore"
 },
 {
   "FIELD1": "2211050015",
   "FIELD2": "Be on the Lookout",
   "FIELD3": "11-5-22\n 1708",
   "FIELD4": "11-5-22\n 1708",
   "FIELD5": "Wakefield Chapel Rd.\n &\n Chapel Dr.",
   "FIELD6": "AN",
   "FIELD7": "Assisted",
   "FIELD8": "Report of two missing juveniles in the area"
 },
 {
   "FIELD1": "2211050008",
   "FIELD2": "Suspicious Person",
   "FIELD3": "11-5-22\n 1002",
   "FIELD4": "11-5-22\n 1002",
   "FIELD5": "Schlesinger",
   "FIELD6": "AL",
   "FIELD7": "GOA",
   "FIELD8": "Report of a person acting strange in the area"
 },
 {
   "FIELD1": "2211030053",
   "FIELD2": "Noise Complaint",
   "FIELD3": "11-3-22\n 1510",
   "FIELD4": "11-3-22\n 1510",
   "FIELD5": "Arts and Science 338",
   "FIELD6": "WO",
   "FIELD7": "Assisted",
   "FIELD8": "Report of a group in the hallway being very loud"
 },
 {
   "FIELD1": "2022-000218",
   "FIELD2": "Larceny",
   "FIELD3": "11-3-22\n 1400",
   "FIELD4": "Between\n 11-2-22\n 2100\n &\n 11-3-22\n Morning",
   "FIELD5": "218 HEC",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a missing dell charger from the quad room"
 },
 {
   "FIELD1": "2022-000220",
   "FIELD2": "Suicide Attempt",
   "FIELD3": "11-3-22\n 1316",
   "FIELD4": "11-3-22\n 1316",
   "FIELD5": "CA",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a student wanted to commit self harm"
 },
 {
   "FIELD1": "2022-000219",
   "FIELD2": "Suicide Attempt",
   "FIELD3": "11-3-22\n 1303",
   "FIELD4": "11-3-22\n 1303",
   "FIELD5": "202",
   "FIELD6": "MEC",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a student wanted to commit self harm"
 },
 {
   "FIELD1": "2022-000217",
   "FIELD2": "Fraud",
   "FIELD3": "11-3-22\n 1112",
   "FIELD4": "Fall of 2018",
   "FIELD5": "On-Line",
   "FIELD6": "WO",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported someone obtained fraudulent funds while attending NOVA in his name"
 },
 {
   "FIELD1": "2211020057",
   "FIELD2": "Suspicious Vehicle",
   "FIELD3": "11-2-22\n 2145",
   "FIELD4": "11-2-22\n 2145",
   "FIELD5": "Lot",
   "FIELD6": "LO",
   "FIELD7": "Advised",
   "FIELD8": "Report of a vehicle with no tags and someone sleeping within the vehicle"
 },
 {
   "FIELD1": "2022-000216",
   "FIELD2": "Hit & Run",
   "FIELD3": "11-2-22\n 1403",
   "FIELD4": "11-2-22\n Between\n 0850-1400",
   "FIELD5": "B Lot",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported damage to their parked vehicle"
 },
 {
   "FIELD1": "2211020023",
   "FIELD2": "Assault",
   "FIELD3": "11-2-22\n 1054",
   "FIELD4": "11-2-22\n 1054",
   "FIELD5": "HEC",
   "FIELD6": "LO",
   "FIELD7": "Unknown",
   "FIELD8": "No Information Available"
 },
 {
   "FIELD1": "2211020021",
   "FIELD2": "Suspicious Vehicle",
   "FIELD3": "11-2-22\n 1036",
   "FIELD4": "11-2-22\n 1036",
   "FIELD5": "B3 Lot",
   "FIELD6": "LO",
   "FIELD7": "Assisted",
   "FIELD8": "Report of a vehicle in the lot without any license plates"
 },
 {
   "FIELD1": "2022-000215",
   "FIELD2": "Hit & Run",
   "FIELD3": "10-31-22\n 1123",
   "FIELD4": "10-31-22\n 1123",
   "FIELD5": "B2 Lot",
   "FIELD6": "AN",
   "FIELD7": "Info Exchange",
   "FIELD8": "Unit out with a hit and run at the location"
 },
 {
   "FIELD1": "2210300012",
   "FIELD2": "Be on the Lookout",
   "FIELD3": "10-30-22\n 1649",
   "FIELD4": "10-30-22\n 1649",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AL",
   "FIELD7": "Advised",
   "FIELD8": "Alexandria PD advised they were looking for a suspect involved in a shooting in the area"
 },
 {
   "FIELD1": "2022-000214",
   "FIELD2": "Drunk In Public (Not Clery)",
   "FIELD3": "10-28-22\n 2321",
   "FIELD4": "10-28-22\n 2321",
   "FIELD5": "AFA",
   "FIELD6": "AL",
   "FIELD7": "Report Taken TOT Alexandria City Police Cleared by Arrest",
   "FIELD8": "Unit observed an individual who was later arrested for drunk in public"
 },
 {
   "FIELD1": "2210280020",
   "FIELD2": "Vehicle Theft\n (Recovery)",
   "FIELD3": "10-28-22\n 1036",
   "FIELD4": "10-28-22\n 1036",
   "FIELD5": "Fillmore Ave",
   "FIELD6": "AL",
   "FIELD7": "TOT\n Alexandria City Police",
   "FIELD8": "Stolen Vehicle pinged in area"
 },
 {
   "FIELD1": "2022-000211",
   "FIELD2": "Welfare Check",
   "FIELD3": "10-27-22\n 1300",
   "FIELD4": "10-27-22\n 1015",
   "FIELD5": "Trailside",
   "FIELD6": "MA",
   "FIELD7": "Report Taken NOVACares Report",
   "FIELD8": "Professor reported a student reported wanting to commit suicide"
 },
 {
   "FIELD1": "2022-000209",
   "FIELD2": "Harassment",
   "FIELD3": "10-27-22\n 0700",
   "FIELD4": "9-6-22\n 1700",
   "FIELD5": "134",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported a deliver person making her feel uncomfortable during a delivery of product"
 },
 {
   "FIELD1": "2022-000208",
   "FIELD2": "Police Service",
   "FIELD3": "10-26-22\n 1350",
   "FIELD4": "10-26-22\n 1350",
   "FIELD5": "102",
   "FIELD6": "MEC",
   "FIELD7": "Report Taken",
   "FIELD8": "Complaint about a disagreement between two people coming through the doorway"
 },
 {
   "FIELD1": "2022-000206",
   "FIELD2": "Fraud",
   "FIELD3": "10-26-22\n 0807",
   "FIELD4": "Spring 2022",
   "FIELD5": "On-Line",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant from out of state reported someone using their personal information to attend NOVA"
 },
 {
   "FIELD1": "2022-000205",
   "FIELD2": "Vandalism",
   "FIELD3": "10-25-22\n 1330",
   "FIELD4": "10-25-22\n Between\n 1100-1320",
   "FIELD5": "B1 Lot",
   "FIELD6": "AL",
   "FIELD7": "Report Taken\n Unfounded",
   "FIELD8": "Complainant reported scratches on their vehicle and wheel lock malfunction"
 },
 {
   "FIELD1": "2022-000204",
   "FIELD2": "Disorderly Conduct",
   "FIELD3": "10-25-22\n 1200",
   "FIELD4": "10-24-22\n 1040",
   "FIELD5": "105",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a former student disrupting a class with other people"
 },
 {
   "FIELD1": "2022-000202",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "10-25-22\n 1001",
   "FIELD4": "10-24-22\n 1402",
   "FIELD5": "Zoom Class",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Complaint of an unknown person in the zoom class pointing a gun"
 },
 {
   "FIELD1": "2022-000201",
   "FIELD2": "Fraud",
   "FIELD3": "10-25-22\n 1009",
   "FIELD4": "Previous",
   "FIELD5": "On-Line",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported potential stolen credit cards used to pay for tuition"
 },
 {
   "FIELD1": "2210240042",
   "FIELD2": "Police Service",
   "FIELD3": "10-24-22\n 1635",
   "FIELD4": "10-24-22\n 1635",
   "FIELD5": "Parking Garage",
   "FIELD6": "AN",
   "FIELD7": "Advised",
   "FIELD8": "Units observed two vehicles and individuals hanging out at the location"
 },
 {
   "FIELD1": "2022-000200",
   "FIELD2": "Disorderly Conduct",
   "FIELD3": "10-24-22\n 1319",
   "FIELD4": "10-24-22\n 1319",
   "FIELD5": "CA 114",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complaint of a disorderly student at the location"
 },
 {
   "FIELD1": "2022-000199",
   "FIELD2": "Welfare Check",
   "FIELD3": "10-24-22\n 0951",
   "FIELD4": "10-24-22\n 0951",
   "FIELD5": "MH",
   "FIELD6": "MA",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported a student who expressed suicidal ideations"
 },
 {
   "FIELD1": "2210240014",
   "FIELD2": "Animal Complaint",
   "FIELD3": "10-24-22\n 0940",
   "FIELD4": "10-24-22\n 0940",
   "FIELD5": "B2 Lot",
   "FIELD6": "AN",
   "FIELD7": "Advised",
   "FIELD8": "Report of a person with a dog that is not on a lease acting aggressive"
 },
 {
   "FIELD1": "2210240011",
   "FIELD2": "Public Service\n (Unauthorized Use)",
   "FIELD3": "10-24-22\n 0930",
   "FIELD4": "10-24-22\n 0930",
   "FIELD5": "LR",
   "FIELD6": "LO",
   "FIELD7": "Assisted",
   "FIELD8": "Complainant reported their child  took their vehicle without permission"
 },
 {
   "FIELD1": "2022-000198",
   "FIELD2": "Hit & Run",
   "FIELD3": "10-20-22\n 1507",
   "FIELD4": "10-20-22\n Between\n 1100-1330",
   "FIELD5": "B1",
   "FIELD6": "AL",
   "FIELD7": "Report Taken\n Unfounded",
   "FIELD8": "Complainant reported damage to their vehicle which was found to not have occurred on NOVA property"
 },
 {
   "FIELD1": "2022-000197\n Related to\n 2022-000192",
   "FIELD2": "Threats of Suicide",
   "FIELD3": "10-20-22\n 1202",
   "FIELD4": "10-19-22\n Morning",
   "FIELD5": "LO",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a student making threats"
 },
 {
   "FIELD1": "2022-000196",
   "FIELD2": "Vandalism",
   "FIELD3": "10-20-22\n 1141",
   "FIELD4": "Unknown",
   "FIELD5": "AFA 1st Floor and 2nd Floor",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported graffiti written on the walls in black marker"
 },
 {
   "FIELD1": "221020019",
   "FIELD2": "Threat Assessment",
   "FIELD3": "10-20-22\n 0947",
   "FIELD4": "10-20-22\n 0947",
   "FIELD5": "Brault",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Unit conducted a threat assessment upon an individual"
 },
 {
   "FIELD1": "2022-000195",
   "FIELD2": "Larceny",
   "FIELD3": "10-20-22\n 0854",
   "FIELD4": "Between\n 10-17-22\n 1200\n 10-19-22\n 1300",
   "FIELD5": "CM342",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a missing IPad from the location"
 },
 {
   "FIELD1": "2210190054",
   "FIELD2": "Suspicious Item",
   "FIELD3": "10-19-22\n 1802",
   "FIELD4": "10-19-22\n 1802",
   "FIELD5": "Lower level plaza",
   "FIELD6": "AN",
   "FIELD7": "Unfounded",
   "FIELD8": "Report if an unattended suitcase at the location"
 },
 {
   "FIELD1": "2022-000194",
   "FIELD2": "Police Service\n (Reckless Operation)",
   "FIELD3": "10-19-22\n 1645",
   "FIELD4": "10-19-22\n 1425",
   "FIELD5": "B16 Lot",
   "FIELD6": "AN",
   "FIELD7": "Report Taken\n Student Conduct Notified",
   "FIELD8": "Complainant reported unsafe driving from a person leaving campus earlier in the day"
 },
 {
   "FIELD1": "2022-000193",
   "FIELD2": "Traffic Stop\n (Reckless Operation)",
   "FIELD3": "10-19-22\n 1625",
   "FIELD4": "10-19-22\n 1625",
   "FIELD5": "B12 Lot",
   "FIELD6": "AN",
   "FIELD7": "Report  Taken TOT Student Conduct",
   "FIELD8": "Unit observed a student on top of a vehicle while it was being driven"
 },
 {
   "FIELD1": "2022-000192",
   "FIELD2": "Welfare Check",
   "FIELD3": "10-19-22\n 1130",
   "FIELD4": "10-19-22\n Morning",
   "FIELD5": "LO",
   "FIELD6": "LO",
   "FIELD7": "Report Taken Fairfax Police Notified NOVACares Report",
   "FIELD8": "Complainants reported a fellow classmate made concerning remarks about harming themselves and others"
 },
 {
   "FIELD1": "2210190016",
   "FIELD2": "Traffic Complaint",
   "FIELD3": "10-19-22\n 1017",
   "FIELD4": "10-19-22\n 1017",
   "FIELD5": "Parking Garage",
   "FIELD6": "AN",
   "FIELD7": "Advised\n TOT Student Conduct",
   "FIELD8": "Unit observed a vehicle doing donuts while operating a vehicle"
 },
 {
   "FIELD1": "2022-000191",
   "FIELD2": "Child Pornography",
   "FIELD3": "10-17-22\n 1542",
   "FIELD4": "9-21-22\n Unknown",
   "FIELD5": "AL",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported a student possibly possessing child pornography"
 },
 {
   "FIELD1": "2022-000190",
   "FIELD2": "Larceny",
   "FIELD3": "10-14-22\n 1457",
   "FIELD4": "10-14-22\n Between\n 1241-1317",
   "FIELD5": "Bisdorf 252",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported her credit card unauthorized use at various stores"
 },
 {
   "FIELD1": "2210140018",
   "FIELD2": "Attempted Suicide\n (Mental Health)",
   "FIELD3": "10-14-22\n 1328",
   "FIELD4": "10-14-22\n 1328",
   "FIELD5": "Parking Garage",
   "FIELD6": "AN",
   "FIELD7": "Unfounded",
   "FIELD8": "Report of a female threatening to commit suicide"
 },
 {
   "FIELD1": "2210120044",
   "FIELD2": "Hit & Run",
   "FIELD3": "10-12-22\n 2111",
   "FIELD4": "10-12-22\n 2111",
   "FIELD5": "B3 Lot",
   "FIELD6": "MA",
   "FIELD7": "Assisted Unfounded",
   "FIELD8": "Complaint of a hit and run which turned out to be a prank"
 },
 {
   "FIELD1": "2022-000189",
   "FIELD2": "Alarm Fire\n (Drug Investigation)",
   "FIELD3": "10-11-22\n 1341",
   "FIELD4": "10-11-22\n 1341",
   "FIELD5": "Founders Hall",
   "FIELD6": "AN",
   "FIELD7": "Report Taken\n TOT Student Conduct",
   "FIELD8": "Fire alarm activated from an individual vaping THC"
 },
 {
   "FIELD1": "2022-000188",
   "FIELD2": "Shoplifting",
   "FIELD3": "10-11-22\n 1242",
   "FIELD4": "10-11-22\n 1242",
   "FIELD5": "Café",
   "FIELD6": "AN",
   "FIELD7": "Report Taken Cleared by Summons Student Conduct Notified",
   "FIELD8": "Unit observed a student steal an item from the store without paying"
 },
 {
   "FIELD1": "2022-000187",
   "FIELD2": "Fraud",
   "FIELD3": "10-11-22\n 1038",
   "FIELD4": "Previous",
   "FIELD5": "On-Line",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of an on-line fraud ring operating out of MD and DC"
 },
 {
   "FIELD1": "2210090002",
   "FIELD2": "Suspicious Item",
   "FIELD3": "10-9-22\n 1001",
   "FIELD4": "10-9-22\n 1001",
   "FIELD5": "Vestibule",
   "FIELD6": "AL",
   "FIELD7": "Unfounded",
   "FIELD8": "Complaint of coffee and food left at the location"
 },
 {
   "FIELD1": "2210070035",
   "FIELD2": "Suspicious Item",
   "FIELD3": "10-7-22\n 1728",
   "FIELD4": "10-7-22\n 1728",
   "FIELD5": "1A1 Entrance",
   "FIELD6": "AL",
   "FIELD7": "Assisted",
   "FIELD8": "Report of two unattended backpacks at the location"
 },
 {
   "FIELD1": "2022-000186",
   "FIELD2": "Hit & Run",
   "FIELD3": "10-6-22\n 1645",
   "FIELD4": "10-6-22\n 1435",
   "FIELD5": "A1 Lot",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a vehicle striking a telecom box in the lot"
 },
 {
   "FIELD1": "2022-000185",
   "FIELD2": "Larceny",
   "FIELD3": "10-6-22\n 1300",
   "FIELD4": "Between\n 10-3-22\n &\n 10-6-22",
   "FIELD5": "211",
   "FIELD6": "MEC",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a hard drive stolen from one of the computers"
 },
 {
   "FIELD1": "2022-000183",
   "FIELD2": "Suspicious Person",
   "FIELD3": "10-5-22\n 1736",
   "FIELD4": "10-5-22\n 1736",
   "FIELD5": "Science Building",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported someone bleeding in the bathroom and possibly needing assistance"
 },
 {
   "FIELD1": "2022-000182",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "10-5-22\n 1719",
   "FIELD4": "10-3-22\n 1735",
   "FIELD5": "B2 Lot",
   "FIELD6": "LO",
   "FIELD7": "Report Taken Unfounded",
   "FIELD8": "Complainant reported being followed by a vehicle"
 },
 {
   "FIELD1": "2022-000180",
   "FIELD2": "Harassment (Threats)",
   "FIELD3": "10-5-22\n 1452",
   "FIELD4": "10-5-22\n 1452",
   "FIELD5": "Game Room",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported being harassed"
 },
 {
   "FIELD1": "2022-000181",
   "FIELD2": "Alarm Fire\n (Arson)",
   "FIELD3": "10-5-22\n 1406",
   "FIELD4": "10-5-22\n 1403",
   "FIELD5": "Tyler",
   "FIELD6": "AL",
   "FIELD7": "Report Taken TOT Student Conduct",
   "FIELD8": "Fire alarm activated from discharge of fire extinguisher and burned booked observed near by"
 },
 {
   "FIELD1": "2022-000179",
   "FIELD2": "EMS",
   "FIELD3": "10-4-22\n 1715",
   "FIELD4": "10-4-22\n 1715",
   "FIELD5": "Reynolds",
   "FIELD6": "LO",
   "FIELD7": "Report Taken BIT Report",
   "FIELD8": "Report of an injury to a student who was transported to the hospital"
 },
 {
   "FIELD1": "2022-000177\n Related to\n 2022-000175",
   "FIELD2": "Harassment",
   "FIELD3": "10-3-22\n 1332",
   "FIELD4": "10-3-22\n 1146",
   "FIELD5": "B14 Lot",
   "FIELD6": "AN",
   "FIELD7": "Report Taken TOT Student Conduct",
   "FIELD8": "Carryover from 2022-000175"
 },
 {
   "FIELD1": "221020007",
   "FIELD2": "Police Service\n (Reckless Driving)",
   "FIELD3": "10-2-22\n 2005",
   "FIELD4": "10-2-22\n 2005",
   "FIELD5": "B13 Lot",
   "FIELD6": "AN",
   "FIELD7": "Advised\n Released to Parents",
   "FIELD8": "Unit observed two vehicles being operated recklessly and released the drivers to their parents"
 },
 {
   "FIELD1": "2022-000175",
   "FIELD2": "Property Damage Non-Criminal",
   "FIELD3": "9-30-22\n 1208",
   "FIELD4": "9/30/2022",
   "FIELD5": "A2 Lot",
   "FIELD6": "AN",
   "FIELD7": "Report Taken Info Exchanged",
   "FIELD8": "Complainant was upset about receiving a parking ticket and damage on their vehicle"
 },
 {
   "FIELD1": "2022-000174",
   "FIELD2": "Police Service",
   "FIELD3": "9-29-22\n 1818",
   "FIELD4": "9-29-22\n 1818",
   "FIELD5": "LC 215",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Complaint of individuals running in the hallway and looking into classrooms"
 },
 {
   "FIELD1": "2022-000173",
   "FIELD2": "Hit & Run",
   "FIELD3": "9-29-22\n 1708",
   "FIELD4": "unknown",
   "FIELD5": "Unknown",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported damage to their parked vehicle"
 },
 {
   "FIELD1": "2209290038",
   "FIELD2": "Police Service",
   "FIELD3": "9-29-22\n 1330",
   "FIELD4": "9-29-22\n 1330",
   "FIELD5": "Seefeldt",
   "FIELD6": "WO",
   "FIELD7": "Assisted",
   "FIELD8": "Unit checking status of a bike left in the area"
 },
 {
   "FIELD1": "2209290024",
   "FIELD2": "Suspicious Vehicle",
   "FIELD3": "9-29-22\n 1026",
   "FIELD4": "9-29-22\n 1026",
   "FIELD5": "A2 Lot",
   "FIELD6": "AN",
   "FIELD7": "Advised",
   "FIELD8": "unregistered vehicle in the lot"
 },
 {
   "FIELD1": "2022-000172",
   "FIELD2": "Larceny",
   "FIELD3": "9-29-22\n 0830",
   "FIELD4": "9-29-22\n 0830",
   "FIELD5": "Reynolds",
   "FIELD6": "LO",
   "FIELD7": "Report Taken Unfounded",
   "FIELD8": "Complainant reported a chain left in the bathroom was stolen"
 },
 {
   "FIELD1": "2022-000170",
   "FIELD2": "Police Service (Drug Investigation)",
   "FIELD3": "9-28-22\n 1109",
   "FIELD4": "9-28-22\n 1109",
   "FIELD5": "Parking Garage",
   "FIELD6": "AN",
   "FIELD7": "Report Taken TOT Student Conduct",
   "FIELD8": "Complaint of two students smoking marijuana in the area"
 },
 {
   "FIELD1": "2022-000169",
   "FIELD2": "Hit & Run",
   "FIELD3": "9-27-22\n 1730",
   "FIELD4": "9-27-22\n Between\n 1550-1630",
   "FIELD5": "A1 Lot",
   "FIELD6": "LO",
   "FIELD7": "Report Taken Unfounded",
   "FIELD8": "Complainant reported damage to their parked vehicle which did not occur on NOVA’s property"
 },
 {
   "FIELD1": "2022-000168",
   "FIELD2": "Hit & Run",
   "FIELD3": "9-26-22\n 2110",
   "FIELD4": "9-26-22\n 1805",
   "FIELD5": "B1 Lot",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported damage to their parked vehicle upon returning to where it was parked in the lot"
 },
 {
   "FIELD1": "2209260048",
   "FIELD2": "Be on the Lookout",
   "FIELD3": "9-26-22\n 1743",
   "FIELD4": "9-26-22\n 1743",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AN",
   "FIELD7": "Advised",
   "FIELD8": "Report of a Senior Alert in the area"
 },
 {
   "FIELD1": "2022-000167",
   "FIELD2": "Shoplifting",
   "FIELD3": "9-26-22\n 1312",
   "FIELD4": "9-26-22\n unknown",
   "FIELD5": "Café",
   "FIELD6": "AN",
   "FIELD7": "Report Taken Cleared by Summons TOT Student Conduct",
   "FIELD8": "Two students observed shoplifting from the café"
 },
 {
   "FIELD1": "2209230025",
   "FIELD2": "Domestic in Progress",
   "FIELD3": "9-23-22\n 1325",
   "FIELD4": "9-23-22\n 1325",
   "FIELD5": "Lot between CS & CN",
   "FIELD6": "AN",
   "FIELD7": "GOA",
   "FIELD8": "Complaint of a male and female arguing in the parking lot"
 },
 {
   "FIELD1": "2022-000166",
   "FIELD2": "Police Service\n (Property Damage)",
   "FIELD3": "9-23-22\n 0819",
   "FIELD4": "Unknown",
   "FIELD5": "B8 Lot",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of scratches on a state vehicle parked in the lot"
 },
 {
   "FIELD1": "2022-000163",
   "FIELD2": "Hit & Run",
   "FIELD3": "9-22-22\n 1538",
   "FIELD4": "9-22-22\n Between\n 0900-1513",
   "FIELD5": "CF Loading Dock",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported damage to their vehicle upon returning to where it was parked"
 },
 {
   "FIELD1": "2022-000164",
   "FIELD2": "Suspicious Person (Shoplifting)",
   "FIELD3": "9-22-22\n 1510",
   "FIELD4": "9-22-22\n 1510",
   "FIELD5": "Café",
   "FIELD6": "AN",
   "FIELD7": "Report Taken Cleared by Arrest",
   "FIELD8": "Report of a suspicious person who was found to have shoplifted and have a warrant"
 },
 {
   "FIELD1": "2022-000165",
   "FIELD2": "Police Service",
   "FIELD3": "9-22-22\n 1415",
   "FIELD4": "9-22-22\n 1415",
   "FIELD5": "LW",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Person attending a club event showed behavioral concerns"
 },
 {
   "FIELD1": "2022-000162",
   "FIELD2": "Larceny",
   "FIELD3": "9-22-22\n 1345",
   "FIELD4": "Unknown",
   "FIELD5": "223",
   "FIELD6": "MEC",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of missing radiology goggles"
 },
 {
   "FIELD1": "2022-000161",
   "FIELD2": "Suspicious Person",
   "FIELD3": "9-22-22\n 0847",
   "FIELD4": "9-22-22\n 0700",
   "FIELD5": "Pender 4",
   "FIELD6": "Fairfax",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported an unknown male yelling and screaming at the location"
 },
 {
   "FIELD1": "2022-000160",
   "FIELD2": "Disorderly Conduct",
   "FIELD3": "9-21-22\n 1637",
   "FIELD4": "9-21-22\n 1637",
   "FIELD5": "CT 312",
   "FIELD6": "AN",
   "FIELD7": "Report Taken TOT HR",
   "FIELD8": "Complaint of a disruptive student in a classroom that felt targeted"
 },
 {
   "FIELD1": "2022-000158",
   "FIELD2": "Police Service\n (Larceny)",
   "FIELD3": "9-19-22\n 1557",
   "FIELD4": "9-19-22\n Between\n 0900-1535",
   "FIELD5": "Soccer Fields",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported their bike was not where they left it upon returning"
 },
 {
   "FIELD1": "2209190046\n Related to\n 2022-000159",
   "FIELD2": "Police Service",
   "FIELD3": "9-19-22\n 1500",
   "FIELD4": "9-19-22\n 1500",
   "FIELD5": "Provost Office",
   "FIELD6": "LO",
   "FIELD7": "Assisted",
   "FIELD8": "Complainant wanted to report an abduction or a missing student after observing an argument between the student and parent"
 },
 {
   "FIELD1": "2022-000159",
   "FIELD2": "Welfare Check",
   "FIELD3": "9-19-22\n 1421",
   "FIELD4": "9-19-22\n 1421",
   "FIELD5": "Tutoring Center",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported they are having trouble locate their disabled sister"
 },
 {
   "FIELD1": "2022-000157",
   "FIELD2": "Weapons Violation (Not Clery Related)",
   "FIELD3": "9-19-22\n 1403",
   "FIELD4": "9-15-22\n Between\n 1700-0040",
   "FIELD5": "CE",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complaint of a weapon being used during a show at the Ernst Center"
 },
 {
   "FIELD1": "2022-000156",
   "FIELD2": "Larceny",
   "FIELD3": "9-19-22\n 1234",
   "FIELD4": "Unknown",
   "FIELD5": "Café",
   "FIELD6": "WO",
   "FIELD7": "Report Taken",
   "FIELD8": "Complaint of a petit larceny that past occurred"
 },
 {
   "FIELD1": "2022-000155",
   "FIELD2": "Motor Assist Mental Health",
   "FIELD3": "9-19-22\n 1137",
   "FIELD4": "9-19-22\n 1137",
   "FIELD5": "B1 Lot",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant requested a motor assist and displayed mental/ emotional distress"
 },
 {
   "FIELD1": "2022-000154",
   "FIELD2": "Mental Health",
   "FIELD3": "9-19-22\n 0947",
   "FIELD4": "9-19-22\n 0947",
   "FIELD5": "CA",
   "FIELD6": "AN",
   "FIELD7": "Report Taken NOVACares Report",
   "FIELD8": "Student Requested assistance with family notification"
 },
 {
   "FIELD1": "2209150072",
   "FIELD2": "Welfare Check",
   "FIELD3": "9-15-22\n 2304",
   "FIELD4": "9-15-22\n 2304",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "WO",
   "FIELD7": "TOT\n Local Law Enforcement",
   "FIELD8": "Received a phone call about a suicidal student not on campus"
 },
 {
   "FIELD1": "2209150071",
   "FIELD2": "Be On the Lookout",
   "FIELD3": "9-15-22\n 2118",
   "FIELD4": "9-15-22\n 2118",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "MA",
   "FIELD7": "Assisted",
   "FIELD8": "Received information about an armed person in the area"
 },
 {
   "FIELD1": "2022-000153",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "9-15-22\n 1650",
   "FIELD4": "9-12-22\n Between\n 1200-1230",
   "FIELD5": "Café",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported overhearing individuals talking about firearms at the café and making concerning motions"
 },
 {
   "FIELD1": "2209150054",
   "FIELD2": "Assist Other Agency",
   "FIELD3": "9-15-22\n 1526",
   "FIELD4": "9-15-22\n 1526",
   "FIELD5": "WS",
   "FIELD6": "WO",
   "FIELD7": "TOT Prince William County Police NOVACares Report",
   "FIELD8": "Prince William County Police on location with a suicidal student"
 },
 {
   "FIELD1": "2022-000152",
   "FIELD2": "Shoplifting",
   "FIELD3": "9-15-22\n 1205",
   "FIELD4": "9-15-22\n 1205",
   "FIELD5": "CA",
   "FIELD6": "AN",
   "FIELD7": "Report Taken TOT Student Conduct",
   "FIELD8": "Complaint of a student shoplifting from the café"
 },
 {
   "FIELD1": "2209140050",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "9-14-22\n 1432",
   "FIELD4": "9-14-22\n 1432",
   "FIELD5": "Seefeldt",
   "FIELD6": "WO",
   "FIELD7": "Unfounded",
   "FIELD8": "Complainant reported another person was walking slowly in the area and making them feel uncomfortable"
 },
 {
   "FIELD1": "2209140020",
   "FIELD2": "Suspicious Person",
   "FIELD3": "9-14-22\n 0947",
   "FIELD4": "9-14-22\n 0947",
   "FIELD5": "Reynolds",
   "FIELD6": "LO",
   "FIELD7": "Unfounded",
   "FIELD8": "Complaint of a person taking video at the location"
 },
 {
   "FIELD1": "2022-000151",
   "FIELD2": "Larceny",
   "FIELD3": "9-13-22\n 1900",
   "FIELD4": "Unknown",
   "FIELD5": "CN 225",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported leaving his property and upon returning discovered missing property"
 },
 {
   "FIELD1": "2022-000150",
   "FIELD2": "Assist other Agency",
   "FIELD3": "9-13-22\n 0828",
   "FIELD4": "Previous",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Unit assisted FFX PD with identification of suspects"
 },
 {
   "FIELD1": "2209120070",
   "FIELD2": "Welfare Check",
   "FIELD3": "9-12-22\n 2254",
   "FIELD4": "9-12-22\n 2254",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AN",
   "FIELD7": "TOT\n Local Law Enforcement",
   "FIELD8": "Complainant reported a suicidal student living off campus. Advised to call local police"
 },
 {
   "FIELD1": "2022-000149",
   "FIELD2": "Suspicious Activity\n (Computer Trespass)",
   "FIELD3": "9-12-22\n 1722",
   "FIELD4": "Unknown",
   "FIELD5": "On-Line Class",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported two other people have access to his on-line accounts"
 },
 {
   "FIELD1": "2022-000147",
   "FIELD2": "Police Service",
   "FIELD3": "9-12-22\n 1130",
   "FIELD4": "9-12-22\n 1115",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "WO",
   "FIELD7": "Report Taken",
   "FIELD8": "Received information about an active situation happening across the street at the county high school"
 },
 {
   "FIELD1": "2209120020",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "9-12-22\n 0956",
   "FIELD4": "9-12-22\n 0956",
   "FIELD5": "Parking Garage",
   "FIELD6": "AN",
   "FIELD7": "Assisted",
   "FIELD8": "Complaint of people throwing sticks off the roof"
 },
 {
   "FIELD1": "2022-000146",
   "FIELD2": "Hit & Run",
   "FIELD3": "9-9-22\n 1600",
   "FIELD4": "Unknown",
   "FIELD5": "B6 Lot",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported damage to their vehicle while parked in the lot"
 },
 {
   "FIELD1": "2209090012",
   "FIELD2": "Welfare Check",
   "FIELD3": "9-9-22\n 0826",
   "FIELD4": "9-9-22\n 0826",
   "FIELD5": "MA",
   "FIELD6": "MA",
   "FIELD7": "Assisted",
   "FIELD8": "LOSO requested assistance with a welfare check on a Manassas virtual student"
 },
 {
   "FIELD1": "2022-000145",
   "FIELD2": "Hit & Run",
   "FIELD3": "9-8-22\n 1230",
   "FIELD4": "9-7-22\n 2345",
   "FIELD5": "B6 Lot",
   "FIELD6": "AN",
   "FIELD7": "Report Taken (Info Exchange)",
   "FIELD8": "Complaint of a vehicle hitting a tree in the lot"
 },
 {
   "FIELD1": "2022-000144",
   "FIELD2": "Fraud",
   "FIELD3": "9-8-22\n 1349",
   "FIELD4": "4-12-22\n Unknown",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AN",
   "FIELD7": "Report Taken TOT Local Law Enforcement",
   "FIELD8": "Complainant reported a financial aid check had been cashed"
 },
 {
   "FIELD1": "2209080038",
   "FIELD2": "Vehicle Tampering",
   "FIELD3": "9-8-22\n 1237",
   "FIELD4": "Unknown",
   "FIELD5": "Unknown",
   "FIELD6": "LO",
   "FIELD7": "Cancelled",
   "FIELD8": "Complainant reported someone tampered with the vehicle’s gas tank"
 },
 {
   "FIELD1": "220908032",
   "FIELD2": "Public Service\n (Vandalism)",
   "FIELD3": "9-8-22\n 1153",
   "FIELD4": "Unknown",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AN",
   "FIELD7": "TOT\n Fairfax County PD",
   "FIELD8": "Complainant reported vandalism to their vehicle"
 },
 {
   "FIELD1": "220908008",
   "FIELD2": "Suspicious Person",
   "FIELD3": "9-8-22\n 0747",
   "FIELD4": "9-8-22\n 0747",
   "FIELD5": "CH",
   "FIELD6": "AN",
   "FIELD7": "NPA",
   "FIELD8": "Report of a suspicious person walking around CH"
 },
 {
   "FIELD1": "2022-000143",
   "FIELD2": "Police Service",
   "FIELD3": "9-7-22\n 1612",
   "FIELD4": "9-7-22\n 1612",
   "FIELD5": "MH",
   "FIELD6": "MA",
   "FIELD7": "Report Taken",
   "FIELD8": "Student reported conflict with parents"
 },
 {
   "FIELD1": "2022-000142",
   "FIELD2": "Police Service",
   "FIELD3": "9-6-22\n 1043",
   "FIELD4": "After\n 9-1-22\n 1500",
   "FIELD5": "219B",
   "FIELD6": "MEC",
   "FIELD7": "Report Taken",
   "FIELD8": "Faculty advised they could not find several items from her locked office"
 },
 {
   "FIELD1": "2022-000141",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "9-1-22\n 1257",
   "FIELD4": "Unknown",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Unit contacted by another agency regarding an on-line comment"
 },
 {
   "FIELD1": "2022-000140",
   "FIELD2": "Traffic Stop\n (Warrant Service)",
   "FIELD3": "8-31-22\n 1135",
   "FIELD4": "8-31-22\n 1135",
   "FIELD5": "Potomac View",
   "FIELD6": "LO",
   "FIELD7": "Report Taken Cleared by Arrest",
   "FIELD8": "Unit conducted a traffic stop which turned into a warrant service"
 },
 {
   "FIELD1": "2208270007\n 2022-000139",
   "FIELD2": "Trespassing",
   "FIELD3": "8-27-22\n 1134",
   "FIELD4": "8-27-22\n 1134",
   "FIELD5": "Bisdorf 293",
   "FIELD6": "AL",
   "FIELD7": "Supplemental Report Summons Issued",
   "FIELD8": "Unit observed an individual whom had been no trespassed previously"
 },
 {
   "FIELD1": "2022-000139\n Related to\n 2022-000138\n 2022-000137",
   "FIELD2": "Trespassing",
   "FIELD3": "8-26-22\n 0816",
   "FIELD4": "8-26-22\n 0816",
   "FIELD5": "Bisdorf",
   "FIELD6": "AL",
   "FIELD7": "Report Taken No Trespass Order Issued",
   "FIELD8": "Units observed an individual involved in multiple cases and issued a no trespass warning"
 },
 {
   "FIELD1": "2022-000138",
   "FIELD2": "Harassment",
   "FIELD3": "8-25-22\n 2015",
   "FIELD4": "8-24-22\n 1730",
   "FIELD5": "AFA",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported being harassed at the location with a concerning conversation"
 },
 {
   "FIELD1": "2022-000137\n Related to\n 2208240049",
   "FIELD2": "Police Service",
   "FIELD3": "8-24-22\n 1632",
   "FIELD4": "8-18-22\n 1400",
   "FIELD5": "Parking Garage\n Via Text",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Professor reported that a student reported she was being stalked"
 },
 {
   "FIELD1": "2022-000136",
   "FIELD2": "Police Service\n (Stalking)",
   "FIELD3": "8-24-22\n 1740",
   "FIELD4": "8-18-22\n 1400",
   "FIELD5": "Parking Garage",
   "FIELD6": "MEC",
   "FIELD7": "Report Taken",
   "FIELD8": "Professor reported that a student reported she was being stalked"
 },
 {
   "FIELD1": "2022-000135",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "8-24-22\n 1323",
   "FIELD4": "8-23-22\n 2245",
   "FIELD5": "Library Bathroom",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported receiving a phone call because their number was  on the bathroom wall"
 },
 {
   "FIELD1": "2208240049\n 2208240068",
   "FIELD2": "Police Service\n (Suspicious Person)\n (Person Stop)",
   "FIELD3": "8-24-22\n 1302",
   "FIELD4": "8-24-22\n 1302",
   "FIELD5": "Main Entrance\n AA",
   "FIELD6": "AL",
   "FIELD7": "Field Interview",
   "FIELD8": "Report of a suspicious person at the location"
 },
 {
   "FIELD1": "2022-000134",
   "FIELD2": "Hit & Run",
   "FIELD3": "8-24-22\n 1158",
   "FIELD4": "8-24-22\n Between\n 0930-1100",
   "FIELD5": "B1 Lot",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported damage to their vehicle upon returning to where they had parked in the lot"
 },
 {
   "FIELD1": "2208240010",
   "FIELD2": "Public Service",
   "FIELD3": "8-24-22\n 0842",
   "FIELD4": "8-24-22\n 0842",
   "FIELD5": "Workforce",
   "FIELD6": "WO",
   "FIELD7": "GOA",
   "FIELD8": "Report of a homeless person using the flower beds as a bathroom"
 },
 {
   "FIELD1": "2022-000133",
   "FIELD2": "Hit & Run",
   "FIELD3": "8-23-22\n 1235",
   "FIELD4": "8-23-22\n Between\n 1050-1230",
   "FIELD5": "B1 Lot",
   "FIELD6": "LO",
   "FIELD7": "Report Taken Un founded",
   "FIELD8": "Complainant reported damage to their parked vehicle that was found to not have occurred on campus"
 },
 {
   "FIELD1": "2208230029",
   "FIELD2": "Threats",
   "FIELD3": "8-23-22\n 1045",
   "FIELD4": "8-23-22\n Previous",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AN",
   "FIELD7": "Unfounded",
   "FIELD8": "Complaint of a voice message threat"
 },
 {
   "FIELD1": "2022-000130",
   "FIELD2": "Welfare Check",
   "FIELD3": "8-19-22\n 1700",
   "FIELD4": "8-19-22\n 1700",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AL",
   "FIELD7": "Report Taken TOT Fairfax County Police",
   "FIELD8": "Complainant reported receiving an email from a faculty member about hearing voices and wanting to harm themselves"
 },
 {
   "FIELD1": "2022-000129",
   "FIELD2": "Hit & Run",
   "FIELD3": "8-19-22\n 1512",
   "FIELD4": "8-11-22\n 1911",
   "FIELD5": "A-1 Lot",
   "FIELD6": "WO",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported damage to their vehicle upon returning to where it was parked in the lot"
 },
 {
   "FIELD1": "2022-000128",
   "FIELD2": "Police Service\n (Mental Health)",
   "FIELD3": "8-18-22\n 0024",
   "FIELD4": "8-18-22\n 0024",
   "FIELD5": "Parking Garage",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Unit observed concerning behavior of a person at the parking garage"
 },
 {
   "FIELD1": "2208170034",
   "FIELD2": "Disorderly Conduct Mental Health",
   "FIELD3": "8-17-22\n 1437",
   "FIELD4": "8-17-22\n 1437",
   "FIELD5": "Maintenance Building",
   "FIELD6": "WO",
   "FIELD7": "TOT Prince William County Police",
   "FIELD8": "Complaint of someone being disruptive at the location that left NOVA’s property"
 },
 {
   "FIELD1": "2022-000127",
   "FIELD2": "Mental Health",
   "FIELD3": "8-17-22\n 1436",
   "FIELD4": "8-17-22\n 1436",
   "FIELD5": "CT",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported an issue with another employee and needing mental health assistance"
 },
 {
   "FIELD1": "2022-000126",
   "FIELD2": "Threats\n (Aggravated Assault)\n (Weapons Arrest)",
   "FIELD3": "8-15-22\n 1720",
   "FIELD4": "8-15-22\n 1700",
   "FIELD5": "A2 Lot",
   "FIELD6": "AL",
   "FIELD7": "Report Taken Cleared by Arrest",
   "FIELD8": "Complainant reported being threatened by a person with a knife"
 },
 {
   "FIELD1": "2022-000125",
   "FIELD2": "Vandalism",
   "FIELD3": "8-12-22\n 1405",
   "FIELD4": "Unknown",
   "FIELD5": "Beauregard Parking Garage",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a graffiti cross at the location"
 },
 {
   "FIELD1": "2022-000124",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "8-12-22\n 1234",
   "FIELD4": "8-12-22\n 1119",
   "FIELD5": "Via Phone\n Barnes and Noble",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported receiving a concerning phone call with in appropriate questions and statements made"
 },
 {
   "FIELD1": "2208060007\n 2208060008",
   "FIELD2": "Public Service\n (Loud Music)",
   "FIELD3": "8-6-22\n 2200",
   "FIELD4": "8-6-22\n 2156",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AN",
   "FIELD7": "TOT Fairfax County Police Department",
   "FIELD8": "Report of music coming from the neighborhood near the B1 Lot"
 },
 {
   "FIELD1": "2022-000123",
   "FIELD2": "Domestic",
   "FIELD3": "8-6-22\n 2127",
   "FIELD4": "8-6-22\n 2127",
   "FIELD5": "CH Parking Lot",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Male cursing loudly at the location"
 },
 {
   "FIELD1": "2022-000120",
   "FIELD2": "Trespassing",
   "FIELD3": "8-4-22\n 1151",
   "FIELD4": "8-4-22\n 1151",
   "FIELD5": "Soccer Fields",
   "FIELD6": "AN",
   "FIELD7": "Report Taken Cleared By Arrest",
   "FIELD8": "Unit observed an individual who had been previously no trespassed"
 },
 {
   "FIELD1": "2022-000119",
   "FIELD2": "Larceny",
   "FIELD3": "8-2-22\n 1522",
   "FIELD4": "7-11-22\n 1120",
   "FIELD5": "Loading Dock",
   "FIELD6": "AL",
   "FIELD7": "Report Taken Unfounded",
   "FIELD8": "Report of a dell monitor missing from the shipping area"
 },
 {
   "FIELD1": "2022-000118",
   "FIELD2": "Vandalism",
   "FIELD3": "7-29-22\n 1457",
   "FIELD4": "7-28-22\n prior to 1400",
   "FIELD5": "AFA 115",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Complaint of damages and used items within the space"
 },
 {
   "FIELD1": "2022-000117",
   "FIELD2": "Police Service",
   "FIELD3": "7-26-22\n 1730",
   "FIELD4": "3-30-21\n Unknown",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AN",
   "FIELD7": "Report Taken\n TOT Fairfax County and LCSO",
   "FIELD8": "Complainant reported an assault"
 },
 {
   "FIELD1": "2022-000116",
   "FIELD2": "Police Service",
   "FIELD3": "7-26-22\n 1425",
   "FIELD4": "7-26-22\n 1425",
   "FIELD5": "Via Phone",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported receiving repeated phone calls from relatives"
 },
 {
   "FIELD1": "2207250010",
   "FIELD2": "Suspicious Vehicle",
   "FIELD3": "7-25-22\n 0901",
   "FIELD4": "7-25-22\n 0901",
   "FIELD5": "Parking Garage",
   "FIELD6": "AN",
   "FIELD7": "NPA",
   "FIELD8": "Report of an individual working on their vehicle in the garage"
 },
 {
   "FIELD1": "2207230010",
   "FIELD2": "Public Service",
   "FIELD3": "7-23-22\n 1750",
   "FIELD4": "7-23-22\n 1750",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AN",
   "FIELD7": "Referred to Fairfax County Police",
   "FIELD8": "Caller inquired about mental health assistance"
 },
 {
   "FIELD1": "2022-000115",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "7-22-22\n 1137",
   "FIELD4": "7-22-22\n 1137",
   "FIELD5": "Via Phone",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Caller inquiring about closing times at the campus"
 },
 {
   "FIELD1": "2207210044",
   "FIELD2": "Police Service\n (Aggravated Assault)",
   "FIELD3": "7-21-22\n 1933",
   "FIELD4": "7-21-22\n 1933",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "WO",
   "FIELD7": "TOT Prince William County Police",
   "FIELD8": "Caller reported accidental shooting of a relative"
 },
 {
   "FIELD1": "2022-000113",
   "FIELD2": "Hit & Run",
   "FIELD3": "7-21-22\n 1606",
   "FIELD4": "7-21-22\n 1606",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AN",
   "FIELD7": "Unfounded",
   "FIELD8": "Report of a hit and run that did not occur  on NOVA’s Clery geography"
 },
 {
   "FIELD1": "2022-000114",
   "FIELD2": "Police Service",
   "FIELD3": "7-21-22\n 1522",
   "FIELD4": "7-21-22\n 1522",
   "FIELD5": "Parking Garage",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a juvenile running around and refusing to follow directions"
 },
 {
   "FIELD1": "2207210023",
   "FIELD2": "Police Service",
   "FIELD3": "7-21-22\n 0933",
   "FIELD4": "7-21-22\n 0933",
   "FIELD5": "CS",
   "FIELD6": "AN",
   "FIELD7": "Assisted",
   "FIELD8": "Report of a homeless person asleep in the building"
 },
 {
   "FIELD1": "2022-000112",
   "FIELD2": "Disorderly Conduct\n (Suspicious Person)",
   "FIELD3": "7-20-22\n 1057",
   "FIELD4": "7-20-22\n 1057",
   "FIELD5": "AA194",
   "FIELD6": "AL",
   "FIELD7": "Report Taken Student Conduct Notified",
   "FIELD8": "Report of a student being loud and disorderly at the location"
 },
 {
   "FIELD1": "2022-000111",
   "FIELD2": "Welfare Check",
   "FIELD3": "7-20-22\n 0845",
   "FIELD4": "7-19-22\n 1400",
   "FIELD5": "MA",
   "FIELD6": "MA",
   "FIELD7": "Report Taken",
   "FIELD8": "Professor reported a student that threatened to commit suicide"
 },
 {
   "FIELD1": "2022-000109",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "7-14-22\n 0908",
   "FIELD4": "7-13-22\n 0908",
   "FIELD5": "Via Telephone",
   "FIELD6": "MA",
   "FIELD7": "Report Taken",
   "FIELD8": "Suspicious phone call asking about multiple members of staffing"
 },
 {
   "FIELD1": "2022-0000108",
   "FIELD2": "Suspicious Vehicle",
   "FIELD3": "7-13-22\n 1717",
   "FIELD4": "7-13-22\n 1717",
   "FIELD5": "B-15 Lot",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Unit observed a suspicious vehicle at the location"
 },
 {
   "FIELD1": "2022-000107",
   "FIELD2": "Welfare Check",
   "FIELD3": "7-13-22\n 1505",
   "FIELD4": "7-12-22\n 1700",
   "FIELD5": "Lab",
   "FIELD6": "MA",
   "FIELD7": "Report Taken\n Care Report",
   "FIELD8": "Professor reported a student that wanted to kill themselves"
 },
 {
   "FIELD1": "2022-000106",
   "FIELD2": "Noise Complaint",
   "FIELD3": "7-12-22\n 0928",
   "FIELD4": "7-12-22\n 0928",
   "FIELD5": "Bisdorf",
   "FIELD6": "AL",
   "FIELD7": "Report Taken TOT Student Conduct",
   "FIELD8": "Unit called to a loud noise complaint found a student vaping in the building"
 },
 {
   "FIELD1": "2022-000105",
   "FIELD2": "Assist other Agency\n (Criminal Damage to Property)",
   "FIELD3": "7-9-22\n 1605",
   "FIELD4": "7-9-22\n 1600",
   "FIELD5": "Bus Stop",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "LO Unit called to report someone had thrown rocks at the bus stop shelter and damaged it"
 },
 {
   "FIELD1": "2207080023",
   "FIELD2": "Suspicious Person",
   "FIELD3": "7-8-22\n 1419",
   "FIELD4": "7-8-22\n 1419",
   "FIELD5": "Traffic Circle",
   "FIELD6": "MA",
   "FIELD7": "GOA",
   "FIELD8": "Report of an unknown person walking with a rock near the police unit"
 },
 {
   "FIELD1": "2022-000104",
   "FIELD2": "Suspicious Item\n (Bomb Threat)",
   "FIELD3": "7-8-22\n 1145",
   "FIELD4": "7-8-22\n 1140",
   "FIELD5": "Via Phone",
   "FIELD6": "MA",
   "FIELD7": "Report Taken TOT PWCP",
   "FIELD8": "Report of a bomb threat made through the 911 telephone system"
 },
 {
   "FIELD1": "2207070016",
   "FIELD2": "Suspicious Item",
   "FIELD3": "7-7-22\n 0933",
   "FIELD4": "7-7-22\n 0933",
   "FIELD5": "Brault",
   "FIELD6": "AN",
   "FIELD7": "Assisted",
   "FIELD8": "Report of a suspicious black box item in the mulch"
 },
 {
   "FIELD1": "2207060015",
   "FIELD2": "Assist Other Agency",
   "FIELD3": "7-6-22\n 1017",
   "FIELD4": "7-6-22\n 1017",
   "FIELD5": "Bench on Campus",
   "FIELD6": "LO",
   "FIELD7": "Assisted TOT LCSO",
   "FIELD8": "Report of a suicidal person on a bench on campus, person found off campus"
 },
 {
   "FIELD1": "2022-000103",
   "FIELD2": "Shoplifting",
   "FIELD3": "7-6-22\n 0918",
   "FIELD4": "7-6-22\n 0918",
   "FIELD5": "Bookstore",
   "FIELD6": "AN",
   "FIELD7": "Report Taken TOT Student Conduct",
   "FIELD8": "Student observed stealing from the bookstore"
 },
 {
   "FIELD1": "2207050028",
   "FIELD2": "Police Service",
   "FIELD3": "7-5-22\n 1145",
   "FIELD4": "7-5-22\n 1145",
   "FIELD5": "Bisdorf",
   "FIELD6": "AL",
   "FIELD7": "Unfounded",
   "FIELD8": "Facilities observed an individual riding a scooter in AA"
 },
 {
   "FIELD1": "2207050025",
   "FIELD2": "Animal Complaint",
   "FIELD3": "7-5-22\n 1109",
   "FIELD4": "7-5-22\n 1109",
   "FIELD5": "Near Pond",
   "FIELD6": "LO",
   "FIELD7": "GOA",
   "FIELD8": "Report of a dog off leash acting aggressive towards students"
 },
 {
   "FIELD1": "2022-000102",
   "FIELD2": "Mental Health",
   "FIELD3": "7-5-22\n 0654",
   "FIELD4": "7-5-22\n 0654",
   "FIELD5": "Center Dr.",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Unit observed an elderly lost individual who was picked up by her husband"
 },
 {
   "FIELD1": "2022-000100",
   "FIELD2": "Hit & Run",
   "FIELD3": "6-27-22\n 1145",
   "FIELD4": "6-27-22\n 1140",
   "FIELD5": "Metered Lot",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Unit observed a hit in run in the lot and issued a citation"
 },
 {
   "FIELD1": "2206230023",
   "FIELD2": "Police Service\n (Weapons Violation)",
   "FIELD3": "6-23-22\n 1338",
   "FIELD4": "6-23-22\n 1338",
   "FIELD5": "Café",
   "FIELD6": "LO",
   "FIELD7": "Advised\n (Unfounded)",
   "FIELD8": "Complainant reported an unknown male sitting in the café with a large knife"
 },
 {
   "FIELD1": "220623002",
   "FIELD2": "Suspicious Activity\n (Drug Investigation)",
   "FIELD3": "6-23-22\n 0715",
   "FIELD4": "6-23-22\n 0715",
   "FIELD5": "B1 Lot",
   "FIELD6": "AL",
   "FIELD7": "GOA",
   "FIELD8": "Complainant reported an unknown male at the location smoking marijuana"
 },
 {
   "FIELD1": "2206210017",
   "FIELD2": "Police Service",
   "FIELD3": "6-21-22\n 1005",
   "FIELD4": "6-21-22\n 1005",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AN",
   "FIELD7": "Advised\n TOT\n FFX County",
   "FIELD8": "Complainant wished to speak to an officer about an ex-girlfriend and obtaining a restraining order"
 },
 {
   "FIELD1": "2206210014",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "6-21-22\n 0910",
   "FIELD4": "6-21-22\n 0910",
   "FIELD5": "A8 Lot",
   "FIELD6": "AL",
   "FIELD7": "GOA",
   "FIELD8": "Complainant reported suspicious activity involving a van in the lot"
 },
 {
   "FIELD1": "220620019",
   "FIELD2": "Traffic Stop",
   "FIELD3": "6-20-22\n 2030",
   "FIELD4": "6-20-22\n 2030",
   "FIELD5": "Parking Garage",
   "FIELD6": "AN",
   "FIELD7": "Advised",
   "FIELD8": "Unit observed a male and female having sex in a vehicle"
 },
 {
   "FIELD1": "2206200018",
   "FIELD2": "Littering/ Dumping",
   "FIELD3": "6-20-22\n 1957",
   "FIELD4": "6-20-22\n 1957",
   "FIELD5": "Parking Garage",
   "FIELD6": "AN",
   "FIELD7": "Advised Released to parents",
   "FIELD8": "Unit observed children throw items over the parking garage wall."
 },
 {
   "FIELD1": "2022-000099",
   "FIELD2": "Mulch Fire",
   "FIELD3": "6-20-22\n 1935",
   "FIELD4": "6-20-22\n 1933",
   "FIELD5": "Filmore Ave & Bisdorf Dr.\n Brush near the stairwell",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a mulch fire at the location from a cigarette"
 },
 {
   "FIELD1": "2022-000098",
   "FIELD2": "Police Service",
   "FIELD3": "6-19-22\n 1618",
   "FIELD4": "Unknown",
   "FIELD5": "Via Email",
   "FIELD6": "WO",
   "FIELD7": "Report Taken",
   "FIELD8": "Professor received an email from a student about their welfare"
 },
 {
   "FIELD1": "2022-000097",
   "FIELD2": "Suspicious Person",
   "FIELD3": "6-17-22\n 2200",
   "FIELD4": "6-17-22\n 1700",
   "FIELD5": "Bisdorf 469",
   "FIELD6": "AL",
   "FIELD7": "Report Taken TOT Student Conduct",
   "FIELD8": "Complaint of a student in a classroom with their pants off"
 },
 {
   "FIELD1": "2022-000096",
   "FIELD2": "Police Service",
   "FIELD3": "6-17-22\n 1157",
   "FIELD4": "Unknown",
   "FIELD5": "Brault",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant wanted to speak with an officer regarding government activities"
 },
 {
   "FIELD1": "2022-000095",
   "FIELD2": "Hate Crime\n Intimidation\n Racial",
   "FIELD3": "6-16-22\n 1417",
   "FIELD4": "Unknown",
   "FIELD5": "Brault 1st Floor Hallway",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Unit observed a racial epithet written on a box for disposal"
 },
 {
   "FIELD1": "2206140024",
   "FIELD2": "Suspicious Vehicle",
   "FIELD3": "6-14-22\n 1039",
   "FIELD4": "6-14-22\n 1039",
   "FIELD5": "B4 Lot",
   "FIELD6": "LO",
   "FIELD7": "GOA",
   "FIELD8": "Complaint of a vehicle in the lot without a plate and covered VIN"
 },
 {
   "FIELD1": "2206130008",
   "FIELD2": "Suspicious Vehicle",
   "FIELD3": "6-13-22\n 0849",
   "FIELD4": "6-13-22\n 0849",
   "FIELD5": "A4 Lot",
   "FIELD6": "AL",
   "FIELD7": "Assisted",
   "FIELD8": "Report of a vehicle with its door ajar"
 },
 {
   "FIELD1": "2022-000094",
   "FIELD2": "Disorderly Conduct",
   "FIELD3": "6-10-22\n 1528",
   "FIELD4": "6-10-22\n 1528",
   "FIELD5": "CH",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported an individual yelling and screaming at the location"
 },
 {
   "FIELD1": "2022-000093",
   "FIELD2": "Police Service",
   "FIELD3": "6-10-22\n 1002",
   "FIELD4": "6-10-22\n 1002",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported an incident which occurred off campus"
 },
 {
   "FIELD1": "220610001",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "6-10-22\n 0404",
   "FIELD4": "6-10-22\n 0404",
   "FIELD5": "CA",
   "FIELD6": "AN",
   "FIELD7": "Unfounded",
   "FIELD8": "Unit observed the door wide open and unsecured"
 },
 {
   "FIELD1": "2022-000092",
   "FIELD2": "Hit & Run",
   "FIELD3": "6-9-22\n 1738",
   "FIELD4": "Unknown",
   "FIELD5": "Dawes Ave & Bisdorf Dr.",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a stop sign knocked down by a semi truck"
 },
 {
   "FIELD1": "2022-000091",
   "FIELD2": "Bomb Threat",
   "FIELD3": "6-8-22\n 0756",
   "FIELD4": "6-8-22\n 0730",
   "FIELD5": "Via Chat",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a bomb threat made through the chat system"
 },
 {
   "FIELD1": "2022-000090",
   "FIELD2": "Littering/ Dumping",
   "FIELD3": "6-7-22\n 0924",
   "FIELD4": "Unknown",
   "FIELD5": "A4 Lot",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Boxes of items discarded on the grass area"
 },
 {
   "FIELD1": "2022-000089",
   "FIELD2": "Police Service",
   "FIELD3": "6-6-22\n 0638",
   "FIELD4": "6-6-22\n 0638",
   "FIELD5": "Science Building",
   "FIELD6": "LO",
   "FIELD7": "Field Interview",
   "FIELD8": "Report of a person sleeping in the building"
 },
 {
   "FIELD1": "2206050004",
   "FIELD2": "Suspicious Person",
   "FIELD3": "6-5-22\n 1439",
   "FIELD4": "6-5-22\n 1439",
   "FIELD5": "Ernst Center",
   "FIELD6": "AL",
   "FIELD7": "Advised",
   "FIELD8": "Report of a suspicious person in the dressing room"
 },
 {
   "FIELD1": "2022-000088",
   "FIELD2": "EMS",
   "FIELD3": "6-2-22\n 1414",
   "FIELD4": "6-2-22\n 1414",
   "FIELD5": "CP,CE,CF",
   "FIELD6": "AN",
   "FIELD7": "Report Taken No Trespass Order Issued",
   "FIELD8": "Report of a person jumping off the garage in order to make a music video"
 },
 {
   "FIELD1": "2022-000087",
   "FIELD2": "Hit & Run",
   "FIELD3": "6-1-22\n 2049",
   "FIELD4": "6-1-22\n Between\n 1800-2040",
   "FIELD5": "B2",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported damage to their parked vehicle"
 },
 {
   "FIELD1": "2022-000086",
   "FIELD2": "EMS",
   "FIELD3": "6-1-22\n 1705",
   "FIELD4": "6-1-22\n 1705",
   "FIELD5": "LW",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Student fell and medics were requested"
 },
 {
   "FIELD1": "2022-000085",
   "FIELD2": "Police Service\n (Domestic Violence)",
   "FIELD3": "6-1-22\n 1128",
   "FIELD4": "6-31-22\n 0000",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AL",
   "FIELD7": "Report Taken TOT Fairfax County Police Title IX Notified",
   "FIELD8": "Complainant reported an altercation with her husband"
 },
 {
   "FIELD1": "2205310027\n Related to\n 2022-000075",
   "FIELD2": "Mental Health",
   "FIELD3": "5-31-22\n 1209",
   "FIELD4": "5-31-22\n 1209",
   "FIELD5": "CT-226",
   "FIELD6": "AN",
   "FIELD7": "Supplemental Report Taken",
   "FIELD8": "Mental Health assistance was requested"
 },
 {
   "FIELD1": "2021134301",
   "FIELD2": "Stalking Dating Violence",
   "FIELD3": "5-18-22\n 0856",
   "FIELD4": "4-6-22\n Unknown",
   "FIELD5": "Parking lot/ Various",
   "FIELD6": "AN",
   "FIELD7": "Reported to Title IX",
   "FIELD8": "Complainant reported being followed and having their vehicle threatened with a key"
 },
 {
   "FIELD1": "2205190021",
   "FIELD2": "Traffic Complaint",
   "FIELD3": "5-19-22\n 1319",
   "FIELD4": "5-19-22\n 1319",
   "FIELD5": "Parking Garage",
   "FIELD6": "AL",
   "FIELD7": "Advised",
   "FIELD8": "Report of a person at the location learning to drive"
 },
 {
   "FIELD1": "2205190018",
   "FIELD2": "Threat Assessment",
   "FIELD3": "5-19-22\n 1240",
   "FIELD4": "5-19-22\n 1240",
   "FIELD5": "Brault",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Unit conducted a threat assessment upon an individual"
 },
 {
   "FIELD1": "2022-000081",
   "FIELD2": "Larceny",
   "FIELD3": "5-18-22\n 1100",
   "FIELD4": "5-13-22\n 1342",
   "FIELD5": "Bisdorf Loading Dock",
   "FIELD6": "AL",
   "FIELD7": "Report Taken Unfounded",
   "FIELD8": "Report of missing packages delivered by FedEx"
 },
 {
   "FIELD1": "2022-000080",
   "FIELD2": "Suspicious Person",
   "FIELD3": "5-17-22\n 2205",
   "FIELD4": "2-17-22\n 1605",
   "FIELD5": "116",
   "FIELD6": "MEC",
   "FIELD7": "Report Taken Title IX Notified",
   "FIELD8": "Report that a person made another person feel uncomfortable within a conversation"
 },
 {
   "FIELD1": "2205160023",
   "FIELD2": "Police Service",
   "FIELD3": "5-16-22\n 2046",
   "FIELD4": "5-16-22\n 2046",
   "FIELD5": "WAS",
   "FIELD6": "WO",
   "FIELD7": "GOA",
   "FIELD8": "Report of an unknown female at the location asking people for rides home"
 },
 {
   "FIELD1": "2022-000077",
   "FIELD2": "Traffic Stop",
   "FIELD3": "5-13-22\n 1650",
   "FIELD4": "5-13-22\n 1650",
   "FIELD5": "Parking lot",
   "FIELD6": "AN",
   "FIELD7": "Report Taken Cleared by Summons",
   "FIELD8": "Unit observed an underage unlicensed driver operating a vehicle"
 },
 {
   "FIELD1": "2022-000076",
   "FIELD2": "Welfare Check",
   "FIELD3": "5-13-22\n 1336",
   "FIELD4": "5-13-22\n 1336",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AN",
   "FIELD7": "Report Taken TOT Fairfax County Police",
   "FIELD8": "Report of concerning behavior and concerns for personal safety"
 },
 {
   "FIELD1": "2021126701",
   "FIELD2": "Stalking",
   "FIELD3": "5-13-22\n 1207",
   "FIELD4": "4-26-22\n Previous",
   "FIELD5": "In class, On campus, at home",
   "FIELD6": "AN",
   "FIELD7": "Maxient Report to Title IX",
   "FIELD8": "Complainant reported being stalked by an individual in class, on campus, and at home"
 },
 {
   "FIELD1": "2022-000075",
   "FIELD2": "Mental Health",
   "FIELD3": "5-12-22\n 1911",
   "FIELD4": "5-12-22\n 1911",
   "FIELD5": "CA",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported she could hear someone talking through her ears and see through her eyes while across the country"
 },
 {
   "FIELD1": "2021132001",
   "FIELD2": "Stalking",
   "FIELD3": "5-11-22\n 1252",
   "FIELD4": "4-28-22\n Evening",
   "FIELD5": "Parking Garage",
   "FIELD6": "AN",
   "FIELD7": "Maxient Report to Title IX",
   "FIELD8": "Report of an unknown male stalking a student with a phone tracker"
 },
 {
   "FIELD1": "2205110018",
   "FIELD2": "Disorderly Conduct",
   "FIELD3": "5-11-22\n 1448",
   "FIELD4": "5-11-22\n 1448",
   "FIELD5": "2nd Floor Elevator\n Bisdorf",
   "FIELD6": "AL",
   "FIELD7": "GOA",
   "FIELD8": "Report of an unknown female at the location yelling at people"
 },
 {
   "FIELD1": "220510038",
   "FIELD2": "Animal Complaint",
   "FIELD3": "5-10-22\n 1710",
   "FIELD4": "5-10-22\n 1710",
   "FIELD5": "CE 202",
   "FIELD6": "AN",
   "FIELD7": "TOT Maintenance",
   "FIELD8": "Report of a mouse at the location"
 },
 {
   "FIELD1": "2205100028",
   "FIELD2": "Assist Other Agency\n (Elder Abuse)",
   "FIELD3": "5-10-22\n 1412",
   "FIELD4": "5-10-22\n 1412",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AN",
   "FIELD7": "TOT Fairfax County Police Department",
   "FIELD8": "Report of elderly abuse in a local shelter"
 },
 {
   "FIELD1": "2022-000073",
   "FIELD2": "Assist Other Agency\n (DUI)",
   "FIELD3": "5-7-22\n 0803",
   "FIELD4": "5-5-22\n 1840",
   "FIELD5": "Campus Dr. and Route 7",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "NOVA Unit assisted a LO Deputy with a DUI arrest"
 },
 {
   "FIELD1": "2205060037",
   "FIELD2": "Suspicious Person",
   "FIELD3": "5-6-22\n 2002",
   "FIELD4": "5-6-22\n 2002",
   "FIELD5": "Workforce",
   "FIELD6": "WO",
   "FIELD7": "GOA",
   "FIELD8": "Female asking people for a ride at the location"
 },
 {
   "FIELD1": "2205050002",
   "FIELD2": "Suspicious Person",
   "FIELD3": "5-5-22\n 0316",
   "FIELD4": "5-5-22\n 0316",
   "FIELD5": "CM",
   "FIELD6": "AN",
   "FIELD7": "GOA",
   "FIELD8": "Person in the area observed stumbling and kicking objects"
 },
 {
   "FIELD1": "2022-000072",
   "FIELD2": "Police Service\n (Welfare Check)",
   "FIELD3": "4-30-22\n 1923",
   "FIELD4": "4-30-22\n 1923",
   "FIELD5": "Via Email",
   "FIELD6": "MA",
   "FIELD7": "Report Taken TOT Student Conduct",
   "FIELD8": "Professor received concerning email from student"
 },
 {
   "FIELD1": "2022000071",
   "FIELD2": "Suspicious Person",
   "FIELD3": "4-29-22\n 1916",
   "FIELD4": "4-29-22\n 1916",
   "FIELD5": "Parking Garage",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Unit observed a suspicious person in a vehicle at the location"
 },
 {
   "FIELD1": "2204280045",
   "FIELD2": "Animal Complaint",
   "FIELD3": "4-28-22\n 1932",
   "FIELD4": "4-28-22\n 1932",
   "FIELD5": "B9 Lot",
   "FIELD6": "AN",
   "FIELD7": "TOT Fairfax County Animal Control",
   "FIELD8": "Complaint of a sick fox at the location"
 },
 {
   "FIELD1": "2022-000070",
   "FIELD2": "Hit & Run",
   "FIELD3": "4-25-22\n 1632",
   "FIELD4": "4-25-22\n Between\n 0915-1630",
   "FIELD5": "B-6 Lot",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported damage to their vehicle upon returning to where it was parked in the lot"
 },
 {
   "FIELD1": "2204250014",
   "FIELD2": "Suspicious Person",
   "FIELD3": "4-25-22\n 1024",
   "FIELD4": "4-25-22\n 1024",
   "FIELD5": "CN 128",
   "FIELD6": "AN",
   "FIELD7": "GOA",
   "FIELD8": "Report of a person trying to gain access without having proper ID"
 },
 {
   "FIELD1": "2204240004",
   "FIELD2": "Suspicious Vehicle",
   "FIELD3": "4-24-22\n 1306",
   "FIELD4": "4-24-22\n 1306",
   "FIELD5": "B13 Lot",
   "FIELD6": "AN",
   "FIELD7": "GOA",
   "FIELD8": "Report of two individuals jumping out of a moving white van"
 },
 {
   "FIELD1": "2204240001",
   "FIELD2": "Be on the Lookout",
   "FIELD3": "4-24-22\n 0155",
   "FIELD4": "4-24-22\n 0155",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "MA",
   "FIELD7": "NPA",
   "FIELD8": "Notification of a sexual assault suspect in the area"
 },
 {
   "FIELD1": "2204210034",
   "FIELD2": "Police Service",
   "FIELD3": "4-21-22\n 1547",
   "FIELD4": "4-21-22\n 1547",
   "FIELD5": "CM/CA",
   "FIELD6": "AN",
   "FIELD7": "Advised",
   "FIELD8": "Report of a scammer inquiring about gas money"
 },
 {
   "FIELD1": "2022-000069",
   "FIELD2": "Harassment\n (Stalking)",
   "FIELD3": "4-21-22\n 1236",
   "FIELD4": "Previous",
   "FIELD5": "On-Line\n &\n Café",
   "FIELD6": "WO",
   "FIELD7": "Report Taken Title IX Notified Student Conduct Notified",
   "FIELD8": "Complainant reported being made to feel uncomfortable by another student at the café, on-line, and in class"
 },
 {
   "FIELD1": "2022-000067",
   "FIELD2": "Hit & Run",
   "FIELD3": "4-19-22\n 1430",
   "FIELD4": "4-19-22\n 1407",
   "FIELD5": "B-3 Lot",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a vehicle struck at the location"
 },
 {
   "FIELD1": "2022-000068",
   "FIELD2": "Bomb Threat\n (Hate Crime)\n (Race)\n (Intimidation)",
   "FIELD3": "4-19-22\n 1213",
   "FIELD4": "4-19-22\n 1202",
   "FIELD5": "On-Line",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of an on-line bomb threat"
 },
 {
   "FIELD1": "2022-000066",
   "FIELD2": "Hit & Run",
   "FIELD3": "4-18-22\n 2045",
   "FIELD4": "4-18-22\n 2045",
   "FIELD5": "B-3 Lot",
   "FIELD6": "LO",
   "FIELD7": "Report Taken Info Exchanged",
   "FIELD8": "Report of a hit and run at the location"
 },
 {
   "FIELD1": "2022-000065",
   "FIELD2": "Shoplifting",
   "FIELD3": "4-18-22\n 1100",
   "FIELD4": "4-18-22\n 1100",
   "FIELD5": "Café",
   "FIELD6": "AL",
   "FIELD7": "Report Taken\n Cleared by Arrest",
   "FIELD8": "Person stole merchandise from the café without paying"
 },
 {
   "FIELD1": "2022-000064",
   "FIELD2": "Crash Property Damage\n (Hit & Run)",
   "FIELD3": "4-17-22\n 0715",
   "FIELD4": "4-16-22\n 1916",
   "FIELD5": "B-1 Lot",
   "FIELD6": "MA",
   "FIELD7": "Report Taken",
   "FIELD8": "Unit observed damage to the construction fence caused by a vehicle"
 },
 {
   "FIELD1": "2022-000063",
   "FIELD2": "EMS",
   "FIELD3": "4-15-22\n 1243",
   "FIELD4": "4-15-22\n 1243",
   "FIELD5": "Metro Bus",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of two people needing EMS at the bus"
 },
 {
   "FIELD1": "2022-000062",
   "FIELD2": "Disorderly Conduct",
   "FIELD3": "4-14-22\n 1545",
   "FIELD4": "4-14-22\n 1545",
   "FIELD5": "AFA 342",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Complaint of an irate student at the location"
 },
 {
   "FIELD1": "2204140022",
   "FIELD2": "Be on the Look Out (Reckless Driving)",
   "FIELD3": "4-14-22\n 1046",
   "FIELD4": "4-14-22\n 1046",
   "FIELD5": "Campus Dr.",
   "FIELD6": "LO",
   "FIELD7": "GOA",
   "FIELD8": "Report of a dark green Ford driving recklessly"
 },
 {
   "FIELD1": "2022-000061",
   "FIELD2": "Police Service",
   "FIELD3": "4-14-22\n 0733",
   "FIELD4": "Previous",
   "FIELD5": "LC",
   "FIELD6": "LO",
   "FIELD7": "Report Taken Title IX",
   "FIELD8": "Complainant reported feeling unsafe because of another student which was already reported to Title IX"
 },
 {
   "FIELD1": "2204130025",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "4-13-22\n 1319",
   "FIELD4": "4-13-22\n 1319",
   "FIELD5": "LS",
   "FIELD6": "LO",
   "FIELD7": "GOA",
   "FIELD8": "Report of a person in the bathroom that is talking loud and sound intoxicated"
 },
 {
   "FIELD1": "2204120024",
   "FIELD2": "Police Service\n (Robbery)",
   "FIELD3": "4-12-22\n 1449",
   "FIELD4": "Yesterday",
   "FIELD5": "Unknown",
   "FIELD6": "AN",
   "FIELD7": "Unfounded (Civil Matter)",
   "FIELD8": "Complainant reported giving someone money for gas that has not been paid back"
 },
 {
   "FIELD1": "2022-000059",
   "FIELD2": "Aggravated Assault Dating Violence",
   "FIELD3": "4-12-22\n 0700",
   "FIELD4": "4-11-22\n Between\n 2130-2345",
   "FIELD5": "Parking Garage",
   "FIELD6": "AN",
   "FIELD7": "Report Taken Title IX Notified",
   "FIELD8": "Complaint of an aggravated assault in the parking garage"
 },
 {
   "FIELD1": "2022-000058",
   "FIELD2": "Suspicious Person",
   "FIELD3": "4-11-22\n 1857",
   "FIELD4": "4-11-22\n 1857",
   "FIELD5": "Bisdorf",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Complaint of an unknown male at the location yelling and complaining about financial aid"
 },
 {
   "FIELD1": "2204110037",
   "FIELD2": "Hit & Run",
   "FIELD3": "4-11-22\n 1513",
   "FIELD4": "4-11-22\n Between\n 1100-1500",
   "FIELD5": "B1 Lot",
   "FIELD6": "WO",
   "FIELD7": "Unfounded",
   "FIELD8": "Complainant reported damage to their vehicle upon returning to where they had parked it in the lot"
 },
 {
   "FIELD1": "2022-000057",
   "FIELD2": "Person Stop",
   "FIELD3": "4-11-22\n 1405",
   "FIELD4": "4-11-22\n 1405",
   "FIELD5": "Parking Lot",
   "FIELD6": "LO",
   "FIELD7": "Report Taken Field Interview",
   "FIELD8": "Complaint of a male taking photos of females while on campus"
 },
 {
   "FIELD1": "2204090012",
   "FIELD2": "Suspicious Item",
   "FIELD3": "4-9-22\n 1004",
   "FIELD4": "4-9-22\n 1004",
   "FIELD5": "Bisdorf",
   "FIELD6": "AL",
   "FIELD7": "Unfounded",
   "FIELD8": "Unit out with an unattended suitcase"
 },
 {
   "FIELD1": "2022-000056",
   "FIELD2": "Welfare Check",
   "FIELD3": "4-8-22\n 1030",
   "FIELD4": "4-8-22\n 1030",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "LO",
   "FIELD7": "Report Taken TOT Herndon PD",
   "FIELD8": "A concerned parent reported his daughter missing"
 },
 {
   "FIELD1": "2022-000055",
   "FIELD2": "Hit & Run",
   "FIELD3": "4-7-22\n 1915",
   "FIELD4": "4-7-22\n Between\n 1430-1556",
   "FIELD5": "B-3 Lot",
   "FIELD6": "AN",
   "FIELD7": "Report Taken\n Unfounded",
   "FIELD8": "Complainant reported damage to their parked vehicle which did not occur on NOVA’s property"
 },
 {
   "FIELD1": "2204060048",
   "FIELD2": "Police Service",
   "FIELD3": "4-6-22\n 1758",
   "FIELD4": "4-6-22\n 1758",
   "FIELD5": "CT",
   "FIELD6": "AN",
   "FIELD7": "Assisted",
   "FIELD8": "Report of a person angry with the vending machine being loud and aggressive"
 },
 {
   "FIELD1": "2022-000054",
   "FIELD2": "Attempted Suicide\n (Mental Health)",
   "FIELD3": "4-6-22\n 1551",
   "FIELD4": "4-6-22\n 1551",
   "FIELD5": "CN",
   "FIELD6": "AN",
   "FIELD7": "Report Taken Voluntary Commitment",
   "FIELD8": "Report of a potentially suicidal student at the location"
 },
 {
   "FIELD1": "2204060016",
   "FIELD2": "Police Service",
   "FIELD3": "4-6-22\n 0944",
   "FIELD4": "4-6-22\n 0944",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AN",
   "FIELD7": "Advised\n TOT\n Fairfax County Police",
   "FIELD8": "Complainant reported paying through Western Union for an on-line class at an unknown college and wanted the degree or the money back"
 },
 {
   "FIELD1": "2204010004",
   "FIELD2": "Suspicious Vehicle",
   "FIELD3": "4-1-22\n 0726",
   "FIELD4": "4-1-22\n 0726",
   "FIELD5": "6th Floor Parking Garage",
   "FIELD6": "AN",
   "FIELD7": "Advised",
   "FIELD8": "2 teenagers hanging out at the location"
 },
 {
   "FIELD1": "2022-000052",
   "FIELD2": "Property Damage",
   "FIELD3": "3-31-22\n 1812",
   "FIELD4": "3/31/2022",
   "FIELD5": "Provost Office",
   "FIELD6": "MEC",
   "FIELD7": "Report Taken Unfounded",
   "FIELD8": "Report of veneer knocked off the door"
 },
 {
   "FIELD1": "2203310034",
   "FIELD2": "Animal Complaint",
   "FIELD3": "3-31-22\n 1326",
   "FIELD4": "3-31-22\n 1326",
   "FIELD5": "Lake",
   "FIELD6": "WO",
   "FIELD7": "Assisted",
   "FIELD8": "Report of a lost dog in the area"
 },
 {
   "FIELD1": "2203310033",
   "FIELD2": "Animal Complaint",
   "FIELD3": "3-31-22\n 1324",
   "FIELD4": "3-31-22\n 1324",
   "FIELD5": "Between MH & MC",
   "FIELD6": "MA",
   "FIELD7": "Assisted",
   "FIELD8": "Report of a snake at the location"
 },
 {
   "FIELD1": "2203310014",
   "FIELD2": "Suspicious Vehicle",
   "FIELD3": "3-31-22\n 1021",
   "FIELD4": "3-31-22\n 1021",
   "FIELD5": "B7 Lot",
   "FIELD6": "WO",
   "FIELD7": "GOA",
   "FIELD8": "Report of 2 people having sex in a vehicle"
 },
 {
   "FIELD1": "2203300038",
   "FIELD2": "Mental Health",
   "FIELD3": "3-30-22\n 1520",
   "FIELD4": "3-30-22\n 1520",
   "FIELD5": "Reston Center",
   "FIELD6": "Reston",
   "FIELD7": "TOT\n Fairfax County PD",
   "FIELD8": "Report of a female wandering in the area with mental health concerns"
 },
 {
   "FIELD1": "2203300034",
   "FIELD2": "Suspicious Vehicle",
   "FIELD3": "3-30-22\n 1347",
   "FIELD4": "3-30-22\n 1347",
   "FIELD5": "B7 Lot",
   "FIELD6": "AN",
   "FIELD7": "TRAF",
   "FIELD8": "Unit out with a vehicle with no plates"
 },
 {
   "FIELD1": "2203290026",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "3-29-22\n 1400",
   "FIELD4": "3-29-22\n 1400",
   "FIELD5": "B6 Lot",
   "FIELD6": "AN",
   "FIELD7": "CBO",
   "FIELD8": "Report of a student attempting to gain access to their own vehicle with keys locked within"
 },
 {
   "FIELD1": "2203290025",
   "FIELD2": "Bomb Threat\n (Hate Crime Intimidation Sexual Orientation/)",
   "FIELD3": "3-29-22\n 1537",
   "FIELD4": "3-29-22\n 1413",
   "FIELD5": "AL",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of an on-line bomb threat"
 },
 {
   "FIELD1": "2022-000051",
   "FIELD2": "Bomb Threat\n (Hate Crime Intimidation Race/Sexual Orientation/ Religion)",
   "FIELD3": "3-29-22\n 1013",
   "FIELD4": "3-29-22\n 0939",
   "FIELD5": "AN",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of an on-line bomb threat"
 },
 {
   "FIELD1": "2022-000050",
   "FIELD2": "Bomb Threat",
   "FIELD3": "3-29-22\n 0350",
   "FIELD4": "3-29-22\n 0230",
   "FIELD5": "AL",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of an on-line bomb threat"
 },
 {
   "FIELD1": "2203280018",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "3-28-22\n 1131",
   "FIELD4": "3-28-22\n 1131",
   "FIELD5": "Parking Garage",
   "FIELD6": "AN",
   "FIELD7": "Unfounded",
   "FIELD8": "Complainant reported hearing a man and woman screaming at the location"
 },
 {
   "FIELD1": "2203280014",
   "FIELD2": "Maintenance",
   "FIELD3": "3-28-22\n 1020",
   "FIELD4": "3-28-22\n 1020",
   "FIELD5": "CS",
   "FIELD6": "AN",
   "FIELD7": "TOT\n Maintenance",
   "FIELD8": "Construction crew at the location removing asbestos"
 },
 {
   "FIELD1": "2022-000049",
   "FIELD2": "Mental Health",
   "FIELD3": "2-25-22\n 1308",
   "FIELD4": "2-25-22\n 1308",
   "FIELD5": "LM",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Student requested assistance with mental health"
 },
 {
   "FIELD1": "2203230049",
   "FIELD2": "Assist Other Agency\n (DUI)",
   "FIELD3": "3-23-22\n 2142",
   "FIELD4": "3-23-22\n 2142",
   "FIELD5": "7 Eleven",
   "FIELD6": "LO",
   "FIELD7": "Assist LOSO",
   "FIELD8": "Unit assisted a LO unit with a DUI at Anchor Shop and A3 Lot which originated off campus"
 },
 {
   "FIELD1": "2203220032",
   "FIELD2": "Police Service",
   "FIELD3": "3-22-22\n 1448",
   "FIELD4": "3-22-22\n 1448",
   "FIELD5": "Lake",
   "FIELD6": "AN",
   "FIELD7": "Advised",
   "FIELD8": "Group of men fishing in the lake"
 },
 {
   "FIELD1": "2203220024",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "3-22-22\n 1219",
   "FIELD4": "3-22-22\n 1219",
   "FIELD5": "LS",
   "FIELD6": "LO",
   "FIELD7": "GOA",
   "FIELD8": "Report of a person yelling and talking loudly in the men’s room"
 },
 {
   "FIELD1": "2203220012",
   "FIELD2": "Threat Assessment",
   "FIELD3": "3-22-22\n 0904",
   "FIELD4": "3-22-22\n 0904",
   "FIELD5": "Brault",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Unit conducted a threat assessment upon an individual"
 },
 {
   "FIELD1": "2022-000044",
   "FIELD2": "Fire Mulch\n (Arson)",
   "FIELD3": "3-21-22\n 1730",
   "FIELD4": "3-21-22\n 1730",
   "FIELD5": "Soccer Fields",
   "FIELD6": "LO",
   "FIELD7": "Report Taken TOT\n State Fire Marshal",
   "FIELD8": "Complaint of a small fire in the area that was put out"
 },
 {
   "FIELD1": "2203210022",
   "FIELD2": "Hit & Run",
   "FIELD3": "321-22\n 1253",
   "FIELD4": "3-14-22\n 0745-1245",
   "FIELD5": "B1 Lot",
   "FIELD6": "AN",
   "FIELD7": "Unfounded",
   "FIELD8": "Complainant reported damaged to their parked vehicle"
 },
 {
   "FIELD1": "2022-000043",
   "FIELD2": "Hit & Run",
   "FIELD3": "3-18-22\n 1103",
   "FIELD4": "3-17-22\n 1245-1430",
   "FIELD5": "B2 or B13 Lots",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported damage to their parked vehicle"
 },
 {
   "FIELD1": "2022-000041",
   "FIELD2": "Suspicious Person",
   "FIELD3": "3-17-22\n 1401",
   "FIELD4": "Previous",
   "FIELD5": "WAS 362",
   "FIELD6": "WO",
   "FIELD7": "Report Taken\n TOT\n Student Conduct",
   "FIELD8": "Complaint of a former student involving class and another student current"
 },
 {
   "FIELD1": "2022-000040",
   "FIELD2": "Hit & Run",
   "FIELD3": "3-17-22\n 1216",
   "FIELD4": "3-14-22\n 1250\n 3-15-22\n 1530",
   "FIELD5": "B7 Lot\n or\n B6 lot",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported damage to their parked vehicle"
 },
 {
   "FIELD1": "2022-000039",
   "FIELD2": "Suspicious Person",
   "FIELD3": "3-17-22\n 0824",
   "FIELD4": "3-16-22\n 1303",
   "FIELD5": "B1 Lot",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Follow-up on the homeless camp in the woods"
 },
 {
   "FIELD1": "2203160034",
   "FIELD2": "Follow-Up",
   "FIELD3": "3-16-22\n 1905",
   "FIELD4": "3-16-22\n 1905",
   "FIELD5": "B1 Lot",
   "FIELD6": "AL",
   "FIELD7": "NPA",
   "FIELD8": "Follow-up on the homeless camp in the woods"
 },
 {
   "FIELD1": "2203160028",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "3-16-22\n 1620",
   "FIELD4": "3-16-22\n 1620",
   "FIELD5": "Loading Dock",
   "FIELD6": "AL",
   "FIELD7": "GOA",
   "FIELD8": "Report of 2 males in vehicle throwing trash on the ground"
 },
 {
   "FIELD1": "2203160027",
   "FIELD2": "Suspicious Person",
   "FIELD3": "3-16-22\n 1615",
   "FIELD4": "3-16-22\n 1615",
   "FIELD5": "B1 Lot",
   "FIELD6": "AL",
   "FIELD7": "GOA",
   "FIELD8": "Homeless camp in the woods"
 },
 {
   "FIELD1": "2203160023",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "3-16-22\n 1303",
   "FIELD4": "3-16-22\n 1303",
   "FIELD5": "B1 Lot",
   "FIELD6": "AL",
   "FIELD7": "Assisted",
   "FIELD8": "AL PD reported a homeless camp in the woods"
 },
 {
   "FIELD1": "2203160017",
   "FIELD2": "Traffic Stop",
   "FIELD3": "3-16-22\n 1236",
   "FIELD4": "3-16-22\n 1236",
   "FIELD5": "Lake Dr.",
   "FIELD6": "AN",
   "FIELD7": "Assisted Cleared by Arrest",
   "FIELD8": "Unit conducted a traffic stop"
 },
 {
   "FIELD1": "2022000038",
   "FIELD2": "Domestic Violence\n (Dating Violence)",
   "FIELD3": "3-15-22\n 1316",
   "FIELD4": "3-15-22\n 1316",
   "FIELD5": "B-9 Lot",
   "FIELD6": "AN",
   "FIELD7": "Report Taken\n Title IX Notified\n TOT\n Student Conduct",
   "FIELD8": "Report of a male hitting his girlfriend in a parked vehicle in the lot"
 },
 {
   "FIELD1": "2203150027",
   "FIELD2": "Threat Assessment",
   "FIELD3": "3-15-22\n 1215",
   "FIELD4": "3-15-22\n 1215",
   "FIELD5": "Brault",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Unit conducted a threat assessment upon an individual"
 },
 {
   "FIELD1": "2022-000037",
   "FIELD2": "Suspicious Person",
   "FIELD3": "3-15-22\n 1034",
   "FIELD4": "3-15-22\n 1034",
   "FIELD5": "Café",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Complaint of a suspicious person at the location throwing rocks and talking with themselves"
 },
 {
   "FIELD1": "220350001",
   "FIELD2": "Person Stop",
   "FIELD3": "3-15-22\n 0059",
   "FIELD4": "3-15-22\n 0059",
   "FIELD5": "CS",
   "FIELD6": "AN",
   "FIELD7": "Field Interview",
   "FIELD8": "Unit  observed homeless student within the building"
 },
 {
   "FIELD1": "2203120005",
   "FIELD2": "Suspicious Person",
   "FIELD3": "3-12-22\n 2202",
   "FIELD4": "3-12-22\n 2202",
   "FIELD5": "MEC",
   "FIELD6": "MEC",
   "FIELD7": "GOA\n TOT\n Fairfax County PD",
   "FIELD8": "Report of an unknown person wearing a hoodie walking around campus"
 },
 {
   "FIELD1": "2022-000036",
   "FIELD2": "Animal Complaint",
   "FIELD3": "3-10-22\n 1314",
   "FIELD4": "3-7-22\n 1930",
   "FIELD5": "NOVA Ct. and Battleview Parkway",
   "FIELD6": "MA",
   "FIELD7": "Report Taken\n TOT\n PWC Animal Control",
   "FIELD8": "Report of a deceased dog found in a plastic bag in the woods"
 },
 {
   "FIELD1": "2203070020",
   "FIELD2": "Traffic Complaint",
   "FIELD3": "3-7-22\n 1455",
   "FIELD4": "3-7-22\n 1455",
   "FIELD5": "B10 Lot",
   "FIELD6": "AN",
   "FIELD7": "Advised",
   "FIELD8": "Complainant reported a vehicle doing donuts in the parking lot"
 },
 {
   "FIELD1": "2022-000035",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "3-3-22\n 1215",
   "FIELD4": "3-1-22\n 0751",
   "FIELD5": "AFA Loading Dock",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a vehicle driving on the grassy area causing tire marks"
 },
 {
   "FIELD1": "2022-000034",
   "FIELD2": "Hit & Run",
   "FIELD3": "3-3-22\n 0949",
   "FIELD4": "2-27-22\n 1100",
   "FIELD5": "B-7 Lot",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a student driver striking a fence"
 },
 {
   "FIELD1": "2022-000033",
   "FIELD2": "Larceny",
   "FIELD3": "3-2-22\n 1359",
   "FIELD4": "Prior to\n 1-19-22",
   "FIELD5": "B-3 Lot",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported hubcaps stolen from an NVCC van"
 },
 {
   "FIELD1": "2022-000031",
   "FIELD2": "Hit & Run",
   "FIELD3": "3-2-22\n 1009",
   "FIELD4": "3-2-22\n Between\n 0800-1000",
   "FIELD5": "B-2 Lot",
   "FIELD6": "MA",
   "FIELD7": "Report Taken\n Unfounded",
   "FIELD8": "Complainant reported damage to their vehicle upon returning to where it was parked in the lot"
 },
 {
   "FIELD1": "2203010011",
   "FIELD2": "Traffic Complaint",
   "FIELD3": "3-1-22\n 0859",
   "FIELD4": "3-1-22\n 0859",
   "FIELD5": "B3 Lot",
   "FIELD6": "MA",
   "FIELD7": "Advised",
   "FIELD8": "Complainant reported a vehicle doing donuts and burnouts in the parking lot"
 },
 {
   "FIELD1": "2022-000030",
   "FIELD2": "Hit & Run",
   "FIELD3": "2-28-22\n 1300",
   "FIELD4": "2-28-22\n Between\n 1100-1235",
   "FIELD5": "Parking Garage",
   "FIELD6": "AN",
   "FIELD7": "Report Taken\n Unfounded",
   "FIELD8": "Complainant reported damage to their vehicle upon returning to where it was parked"
 },
 {
   "FIELD1": "2202260002",
   "FIELD2": "Animal Complaint",
   "FIELD3": "2-26-22\n 0846",
   "FIELD4": "2-26-22\n 0846",
   "FIELD5": "Trailside",
   "FIELD6": "MA",
   "FIELD7": "Assisted",
   "FIELD8": "Report of a snake at the location"
 },
 {
   "FIELD1": "2202250032",
   "FIELD2": "Civil Dispute",
   "FIELD3": "2-25-22\n 2235",
   "FIELD4": "2-25-22\n 2235",
   "FIELD5": "Schlesinger",
   "FIELD6": "AL",
   "FIELD7": "Field Interview",
   "FIELD8": "Report of a verbal dispute at the location"
 },
 {
   "FIELD1": "2202230044",
   "FIELD2": "Disorderly Conduct",
   "FIELD3": "2-23-22\n 1418",
   "FIELD4": "2-23-22\n 1418",
   "FIELD5": "CF",
   "FIELD6": "AN",
   "FIELD7": "GOA",
   "FIELD8": "Report of a group of males carrying on and wrestling at the location"
 },
 {
   "FIELD1": "2022-000028",
   "FIELD2": "Welfare Check",
   "FIELD3": "2-23-22\n 1333",
   "FIELD4": "2-23-22\n 1333",
   "FIELD5": "CM",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Parent concerned for their 19 year old daughters safety"
 },
 {
   "FIELD1": "2020-000027",
   "FIELD2": "Suspicious Person",
   "FIELD3": "2-23-22\n 1127",
   "FIELD4": "2-23-22\n 1127",
   "FIELD5": "CF",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complain of an unknown male walking around talking with girls at the location"
 },
 {
   "FIELD1": "2202230020",
   "FIELD2": "Traffic Complaint",
   "FIELD3": "2-23-22\n 1007",
   "FIELD4": "2-23-22\n 1007",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AN",
   "FIELD7": "Advised",
   "FIELD8": "Complainant reported a distracted driver on I495"
 },
 {
   "FIELD1": "2202230003",
   "FIELD2": "Public Service",
   "FIELD3": "2-23-22\n 0700",
   "FIELD4": "2-23-22\n 0700",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AN",
   "FIELD7": "TOT Fairfax Police",
   "FIELD8": "Complainant reported another care almost collided with her car on Route 50"
 },
 {
   "FIELD1": "2022-000026",
   "FIELD2": "Welfare Check",
   "FIELD3": "2-22-22\n 1115",
   "FIELD4": "2-22-22\n 1115",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "MEC",
   "FIELD7": "Report Taken Wellness Referral Form",
   "FIELD8": "Report of a student possibly needing assistance"
 },
 {
   "FIELD1": "2022-000025",
   "FIELD2": "Police Service",
   "FIELD3": "2-21-22\n 1200",
   "FIELD4": "2-21-22\n 1200",
   "FIELD5": "Café",
   "FIELD6": "MA",
   "FIELD7": "Report Taken",
   "FIELD8": "Report that a current boyfriend of an ex-girlfriend told him to stay off her twitter account"
 },
 {
   "FIELD1": "2022-000024",
   "FIELD2": "Drug Violation",
   "FIELD3": "2-21-22\n 0800",
   "FIELD4": "2-21-22\n 0800",
   "FIELD5": "CF",
   "FIELD6": "AN",
   "FIELD7": "Report Taken TOT Student Conduct",
   "FIELD8": "Report of a fire alarm going off because of a student smoking marijuana in the bathroom"
 },
 {
   "FIELD1": "2202200010",
   "FIELD2": "Suspicious Vehicle",
   "FIELD3": "2-20-22\n 1749",
   "FIELD4": "2-20-22\n 1749",
   "FIELD5": "Brault",
   "FIELD6": "AN",
   "FIELD7": "Advised",
   "FIELD8": "Report of a suspicious vehicle parked at the location"
 },
 {
   "FIELD1": "2202180013",
   "FIELD2": "Suspicious Item",
   "FIELD3": "2-18-22\n 0839",
   "FIELD4": "2-18-22\n 0839",
   "FIELD5": "Ernst Center",
   "FIELD6": "AN",
   "FIELD7": "Assisted",
   "FIELD8": "Report of a suspicious backpack a the location"
 },
 {
   "FIELD1": "2022-000023",
   "FIELD2": "Harassment\n (Stalking)",
   "FIELD3": "2-17-22\n 1918",
   "FIELD4": "2-17-22\n Previous",
   "FIELD5": "Trailside",
   "FIELD6": "MA",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported an ex-girlfriend would not leave him alone after breaking up six weeks ago who then showed up at the college looking for him"
 },
 {
   "FIELD1": "2022-000022",
   "FIELD2": "Suspicious Vehicle",
   "FIELD3": "2-17-22\n 1530",
   "FIELD4": "2-17-22\n 1530",
   "FIELD5": "B6 Lot",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a vehicle failing to display  registration information"
 },
 {
   "FIELD1": "2202170018",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "2-17-22\n 1152",
   "FIELD4": "2-17-22\n 1152",
   "FIELD5": "A3 Lot",
   "FIELD6": "AL",
   "FIELD7": "Unfounded",
   "FIELD8": "Report of individuals trying door handles of vehicles in the parking lot"
 },
 {
   "FIELD1": "2022-000021\n Related to\n 2202110018\n 220210025",
   "FIELD2": "Police Service\n (Civil Dispute)",
   "FIELD3": "2-16-22\n 1816",
   "FIELD4": "2-11-22\n 1156",
   "FIELD5": "AL",
   "FIELD6": "AL",
   "FIELD7": "Report Taken\n TOT\n Student Conduct",
   "FIELD8": "Dispute between a mother of a student and the professor"
 },
 {
   "FIELD1": "2022-000020",
   "FIELD2": "Fraud",
   "FIELD3": "2-15-22\n 1535",
   "FIELD4": "January\n February\n 2022",
   "FIELD5": "On-Line",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of fraud involving students financial aid"
 },
 {
   "FIELD1": "2022-000018",
   "FIELD2": "Assault",
   "FIELD3": "2-12-22\n 2248",
   "FIELD4": "2-12-22\n 1955",
   "FIELD5": "Schlesinger",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported being assaulted for not wearing a mask"
 },
 {
   "FIELD1": "2202120016",
   "FIELD2": "Suspicious Person",
   "FIELD3": "2-12-22\n 1234",
   "FIELD4": "2-12-22\n 1234",
   "FIELD5": "Bisdorf",
   "FIELD6": "AL",
   "FIELD7": "Unfounded",
   "FIELD8": "Complaint of an individual with luggage and a dog in the building"
 },
 {
   "FIELD1": "220211026",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "2-11-22\n 1419",
   "FIELD4": "2-11-22\n 1419",
   "FIELD5": "CF",
   "FIELD6": "AN",
   "FIELD7": "Advised",
   "FIELD8": "Complaint of an unknown person climbing onto the roof of the building"
 },
 {
   "FIELD1": "2202110018",
   "FIELD2": "Civil Dispute",
   "FIELD3": "2-11-22\n 1156",
   "FIELD4": "2-11-22\n 1156",
   "FIELD5": "AL",
   "FIELD6": "AL",
   "FIELD7": "TOT Student Conduct",
   "FIELD8": "Dispute between a mother of a student and the professor"
 },
 {
   "FIELD1": "2022-000017",
   "FIELD2": "Harassment",
   "FIELD3": "2-10-22\n 1257",
   "FIELD4": "Previous",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported being harassed multiple times by an unknown male via social media and phone"
 },
 {
   "FIELD1": "2022-000016",
   "FIELD2": "Indecent Exposure",
   "FIELD3": "2-10-22\n 0854",
   "FIELD4": "2-9-22\n 1515",
   "FIELD5": "Library",
   "FIELD6": "AN",
   "FIELD7": "Report Taken Title IX Notified Student Conduct Notified",
   "FIELD8": "Complainant reported an unknown male masturbating in the library"
 },
 {
   "FIELD1": "2022-000015",
   "FIELD2": "Hit & Run",
   "FIELD3": "2-10-22\n 0839",
   "FIELD4": "2-7-22\n Unknown",
   "FIELD5": "B1 Lot",
   "FIELD6": "MA",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported that upon returning to where their vehicle was parked in the lot they observed damage to the vehicle"
 },
 {
   "FIELD1": "2022-000013",
   "FIELD2": "Suspicious Person (Weapons Violation) Not Clery ASR Reportable",
   "FIELD3": "2-7-22\n 1132",
   "FIELD4": "2-7-22\n 1132",
   "FIELD5": "Parking Lot",
   "FIELD6": "AL",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a student with an empty holster in class and a weapon not safely secured within a vehicle"
 },
 {
   "FIELD1": "2022-000012",
   "FIELD2": "Drunk In Public",
   "FIELD3": "2-4-22\n 0907",
   "FIELD4": "2-4-22\n 0907",
   "FIELD5": "Bust Stop",
   "FIELD6": "AN",
   "FIELD7": "Report Taken Cleared by Arrest Not Clery ASR Reportable",
   "FIELD8": "Complaint of a person being disorderly at the location"
 },
 {
   "FIELD1": "2202030032",
   "FIELD2": "Noise Complaint",
   "FIELD3": "2-3-22\n 1741",
   "FIELD4": "2-3-22\n 1741",
   "FIELD5": "Parking Garage",
   "FIELD6": "AL",
   "FIELD7": "Unfounded",
   "FIELD8": "Complaint of a vehicle screeching tires"
 },
 {
   "FIELD1": "2022-000011",
   "FIELD2": "Hit & Run",
   "FIELD3": "2-2-22\n 1100",
   "FIELD4": "2-1-22\n Between\n 0730-1530",
   "FIELD5": "Brault Parking Lot",
   "FIELD6": "AN",
   "FIELD7": "Report Taken\n Unfounded",
   "FIELD8": "Complainant reported damage to their vehicle upon returning to where it was parked in the lot"
 },
 {
   "FIELD1": "2202020004",
   "FIELD2": "Property Damage",
   "FIELD3": "2-2-22\n 0712",
   "FIELD4": "2-2-22\n 0712",
   "FIELD5": "WAS",
   "FIELD6": "WO",
   "FIELD7": "Unfounded",
   "FIELD8": "Reader on the wall separated and hanging"
 },
 {
   "FIELD1": "2022-000010",
   "FIELD2": "Police Service\n (Threats)",
   "FIELD3": "2-1-22\n 0450",
   "FIELD4": "1-31-22\n 1845",
   "FIELD5": "LC",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported concerning behavior of a fellow student"
 },
 {
   "FIELD1": "2201310023",
   "FIELD2": "Police Service",
   "FIELD3": "1-31-22\n 1331",
   "FIELD4": "1-31-22\n 1331",
   "FIELD5": "B1 Lot",
   "FIELD6": "AL",
   "FIELD7": "Unfounded",
   "FIELD8": "Complainant reported a homeless person camping in the stairwell"
 },
 {
   "FIELD1": "2201270016",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "1-27-22\n 1005",
   "FIELD4": "1-27-22\n 1005",
   "FIELD5": "4th Floor Parking Garage",
   "FIELD6": "AN",
   "FIELD7": "Unfounded",
   "FIELD8": "Report that someone took something from the fire extinguisher box"
 },
 {
   "FIELD1": "2201260028",
   "FIELD2": "Police Service\n (Criminal Damage)",
   "FIELD3": "1-26-22\n 1550",
   "FIELD4": "1-26-22\n 0800",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "LO",
   "FIELD7": "Assisted",
   "FIELD8": "Complainant reported their vehicle was keyed"
 },
 {
   "FIELD1": "2201250039",
   "FIELD2": "Police Service",
   "FIELD3": "1-25-22\n 2207",
   "FIELD4": "1-25-22\n 2207",
   "FIELD5": "WS",
   "FIELD6": "WO",
   "FIELD7": "Advised",
   "FIELD8": "Unit found a student sleeping in the storage shed"
 },
 {
   "FIELD1": "2022-000009",
   "FIELD2": "Shoplifting",
   "FIELD3": "1-25-22\n 1210",
   "FIELD4": "1-25-22\n 1210",
   "FIELD5": "Bookstore",
   "FIELD6": "MA",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of a person who stole three books"
 },
 {
   "FIELD1": "2201250018",
   "FIELD2": "Suspicious Person",
   "FIELD3": "1-25-22\n 1040",
   "FIELD4": "1-25-22\n 1040",
   "FIELD5": "A2 Lot",
   "FIELD6": "AN",
   "FIELD7": "GOA",
   "FIELD8": "Report of an unknown person accosting people at the location"
 },
 {
   "FIELD1": "2022-000008",
   "FIELD2": "Police Service\n (Criminal Damage)",
   "FIELD3": "1-25-22\n 0755",
   "FIELD4": "1-24-22\n 1355",
   "FIELD5": "CM330",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Report of someone removing the poster of the door"
 },
 {
   "FIELD1": "20210060",
   "FIELD2": "Cyber Stalking",
   "FIELD3": "1-24-22\n 1429",
   "FIELD4": "Fall 2021 Semester",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AL",
   "FIELD7": "Reported to\n Title IX",
   "FIELD8": "Complaint of on-line harassment and stalking"
 },
 {
   "FIELD1": "20210515",
   "FIELD2": "Cyber Stalking",
   "FIELD3": "1-24-22\n 1429",
   "FIELD4": "Fall 2021 Semester",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "AL",
   "FIELD7": "Reported to Title IX",
   "FIELD8": "Complaint of on-line harassment and stalking"
 },
 {
   "FIELD1": "2022-000006",
   "FIELD2": "Police Service",
   "FIELD3": "1-21-22\n 1540",
   "FIELD4": "1-21-22\n Previous",
   "FIELD5": "B3 Lot",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported vehicle tampering that did not occur on NOVA’s Clery Geography"
 },
 {
   "FIELD1": "2022-000005",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "1-21-22\n 1234",
   "FIELD4": "1-21-22\n 1200",
   "FIELD5": "B4 Lot",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported being approached by two different unknown males"
 },
 {
   "FIELD1": "2022-000004",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "1-21-22\n 1230",
   "FIELD4": "1-19-22\n Lunch Time",
   "FIELD5": "CF",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Complainant reported having his photo and video taken by three unknown males"
 },
 {
   "FIELD1": "2201190035",
   "FIELD2": "Suspicious Person",
   "FIELD3": "1-19-22\n 1426",
   "FIELD4": "1-19-22\n 1426",
   "FIELD5": "CM",
   "FIELD6": "AN",
   "FIELD7": "Advised",
   "FIELD8": "Report of two people stopping students in the area"
 },
 {
   "FIELD1": "2022-000003",
   "FIELD2": "Welfare Check",
   "FIELD3": "1-19-22\n 1037",
   "FIELD4": "1-19-22\n 1037",
   "FIELD5": "Not on Clery Geography",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Parent concerned for adult child not heard from which was already reported to LCSO"
 },
 {
   "FIELD1": "2201190011",
   "FIELD2": "Be on the Lookout",
   "FIELD3": "1-19-22\n 0825",
   "FIELD4": "1-19-22\n 0825",
   "FIELD5": "Dawes Ave",
   "FIELD6": "AL",
   "FIELD7": "Assisted",
   "FIELD8": "BOLO for a person whom may be suicidal"
 },
 {
   "FIELD1": "2201160002",
   "FIELD2": "Suspicious Activity",
   "FIELD3": "1-16-22\n 2132",
   "FIELD4": "1-16-22\n 2132",
   "FIELD5": "Seefeldt",
   "FIELD6": "WO",
   "FIELD7": "GOA",
   "FIELD8": "Report of a person getting in the way of snow removal and making crude remarks"
 },
 {
   "FIELD1": "2022-000001",
   "FIELD2": "Hit & Run",
   "FIELD3": "1-14-22\n 1024",
   "FIELD4": "1-14-22\n Previous",
   "FIELD5": "Storage Building",
   "FIELD6": "LO",
   "FIELD7": "Report Taken",
   "FIELD8": "Damage to the rolling gate entrance"
 },
 {
   "FIELD1": "2022-000002",
   "FIELD2": "Welfare Check",
   "FIELD3": "1-14-22\n 0949",
   "FIELD4": "1-14-22\n 0949",
   "FIELD5": "AL & MA",
   "FIELD6": "Bookstore",
   "FIELD7": "Report Taken Unfounded",
   "FIELD8": "Report of a missing person who was later found"
 },
 {
   "FIELD1": "2201100017",
   "FIELD2": "Suspicious\n Vehicle",
   "FIELD3": "1-10-22\n 1343",
   "FIELD4": "1-10-22\n 1343",
   "FIELD5": "Parking Garage",
   "FIELD6": "AN",
   "FIELD7": "Advised",
   "FIELD8": "Unit out with a person sleeping in a vehicle"
 },
 {
   "FIELD1": "2201100015",
   "FIELD2": "Threat Assessment",
   "FIELD3": "1-10-22\n 1048",
   "FIELD4": "1-10-22\n 1048",
   "FIELD5": "Brault",
   "FIELD6": "AN",
   "FIELD7": "Report Taken",
   "FIELD8": "Unit conducted a threat assessment upon an individual"
 },
 {
   "FIELD1": "2201040010",
   "FIELD2": "Police Service",
   "FIELD3": "1-4-22\n 1315",
   "FIELD4": "1-4-22\n 1315",
   "FIELD5": "Brault",
   "FIELD6": "AN",
   "FIELD7": "Assisted",
   "FIELD8": "Report of people sledding on hill"
 },
 {
   "FIELD1": "2201030013",
   "FIELD2": "Police Service",
   "FIELD3": "1-3-22\n 1828",
   "FIELD4": "1-3-22\n 1828",
   "FIELD5": "Brault",
   "FIELD6": "AN",
   "FIELD7": "Advised",
   "FIELD8": "Report of people sledding on hill"
 },
 {
   "FIELD1": "2201030011",
   "FIELD2": "Police Service",
   "FIELD3": "1-3-22\n 1612",
   "FIELD4": "1-3-22\n 1612",
   "FIELD5": "Brault",
   "FIELD6": "AN",
   "FIELD7": "Assisted",
   "FIELD8": "Report of people sledding on hill"
 },
 {
   "FIELD1": "2201030001",
   "FIELD2": "Suspicious\n Vehicle",
   "FIELD3": "1-3-22\n 0534",
   "FIELD4": "1-3-22\n 0534",
   "FIELD5": "Behind\n AFA",
   "FIELD6": "AL",
   "FIELD7": "GOA",
   "FIELD8": "White vehicle near dumpsters"
 }
]


# print(logsof2022)

list2 = []
for crime in logsof2022:
  # print(crime["FIELD6"])

  list2.append(crime["FIELD6"])
  # for crime.field6 in crime:
  #   print(e,b)

# print("this is list2", list2)


dictionary = {"AN" : 0, "LO" : 0, "MA" : 0, "AL" : 0, "WO" : 0, "Bookstore" : 0, "MEC" : 0, "Fairfax" : 0}



for i in list2:
  for value in dictionary:
    if i == value == "AN":
      dictionary["AN"] = dictionary["AN"] +1
    if i == value == "LO":
      dictionary["LO"] = dictionary["LO"] +1
    if i == value == "AL":
      dictionary["AL"] = dictionary["AL"] +1
    if i == value == "MA":
      dictionary["MA"] = dictionary["MA"] +1
    # if i == value == "Bookstore":
    #   dictionary["Bookstore"] = dictionary["Bookstore"] +1
    if i == value == "MEC":
      dictionary["MEC"] = dictionary["MEC"] +1
    if i == value == "Fairfax":
      dictionary["Fairfax"] = dictionary["Fairfax"] +1
    if i == value == "WO":
      dictionary["WO"] = dictionary["WO"] +1


dictionary2 = {}
# print(dictionary2)
for campus in list2:

  var = dictionary2.get(campus)

  if var:
    dictionary2[campus] = dictionary2[campus]+1
  else:
    dictionary2.update({campus : 1})


print(dictionary2)

list3 = []
for actualcrime in logsof2022:
  # print(actualcrime["FIELD8"])

  list3.append(actualcrime["FIELD8"])


# print(list3)



dictionary3 = {}
# print(dictionary3)
for ret in list3:

  var = dictionary3.get(ret)

  if var:
    dictionary3[ret] = dictionary3[ret]+1
  else:
    dictionary3.update({ret : 1})


# print(dictionary3)



sortedcrimes = dict(sorted(dictionary3.items(), key=lambda item: item[1]))

reversed_dict = sortedcrimes

# print(sortedcrimes)

@app.route('/')
def hello():
    return render_template("index.html", reversed_dict=reversed_dict, logsof2022=logsof2022, dictionary2=dictionary2)

#dictionary2 = campuses output


if __name__ == "__main__":
    app.run(debug=True)