import requests
from bs4 import BeautifulSoup
import pprint 
import json


# res = requests.get("https://blogs.nvcc.edu/crimelog/january-2023/")
# print(res.json())

html_doc = """<table width="512">
    <tbody>
      <tr>
        <td width="64">Case<br>
          Number</td>
        <td width="64">Nature<br>
          Classification</td>
        <td width="64">Date/Time<br>
          Reported</td>
        <td width="64">Date/Time<br>
          Occurred</td>
        <td width="64">General<br>
          Location</td>
        <td width="64">Campus</td>
        <td width="64">Disposition</td>
        <td width="64">Description</td>
      </tr>
      <tr>
        <td width="64"></td>
        <td width="64"></td>
        <td width="64"></td>
        <td width="64"></td>
        <td width="64"></td>
        <td width="64"></td>
        <td width="64"></td>
        <td width="64"></td>
      </tr>
      <tr>
        <td width="64"></td>
        <td width="64"></td>
        <td width="64"></td>
        <td width="64"></td>
        <td width="64"></td>
        <td width="64"></td>
        <td width="64"></td>
        <td width="64"></td>
      </tr>
      <tr>
        <td width="64"></td>
        <td width="64"></td>
        <td width="64"></td>
        <td width="64"></td>
        <td width="64"></td>
        <td width="64"></td>
        <td width="64"></td>
        <td width="64"></td>
      </tr>
      <tr>
        <td width="64">2023-000017</td>
        <td width="64">Welfare Check</td>
        <td width="64">1-30-23<br>
          1447</td>
        <td width="64">1-30-23<br>
          1447</td>
        <td width="64">WAS</td>
        <td width="64">WO</td>
        <td width="64">Report Taken<p></p>
          <p>TOT Prince William County Police</p>
        </td>
        <td width="64">Report of a student expressing the desire to harm themselves</td>
      </tr>
      <tr>
        <td width="64">2023-000016</td>
        <td width="64">Disorderly Conduct<p></p>
          <p>(Public Intoxication)</p>
          <p>(Not Clery Reportable)</p>
        </td>
        <td width="64">1-28-23<br>
          1930</td>
        <td width="64">1-28-23<br>
          1930</td>
        <td width="64">Ernst Center</td>
        <td width="64">AN</td>
        <td width="64">Report Taken</td>
        <td width="64">Complainant observed an individual that was intoxicated&nbsp; at the location</td>
      </tr>
      <tr>
        <td width="64">2023-000015</td>
        <td width="64">Police Service</td>
        <td width="64">1-27-23<br>
          1719</td>
        <td width="64">1-27-23<br>
          Previous</td>
        <td width="64">email</td>
        <td width="64">MA</td>
        <td width="64">Report Taken<p></p>
          <p>NOVACares Report</p>
        </td>
        <td width="64">Professor received a concerning email from a former student</td>
      </tr>
      <tr>
        <td width="64">2023-000014</td>
        <td width="64">Suspicious Activity<p></p>
          <p>(Fraud)</p>
        </td>
        <td width="64">1-26-23<br>
          1829</td>
        <td width="64">Spring 2023 Semester</td>
        <td width="64">On-line</td>
        <td width="64">AL</td>
        <td width="64">Report Taken</td>
        <td width="64">Report of fraudulent students in&nbsp; several classes</td>
      </tr>
      <tr>
        <td width="64">2023-000013</td>
        <td width="64">Police Service<p></p>
          <p>(Harassment)</p>
        </td>
        <td width="64">1-26-23<br>
          1703</td>
        <td width="64">1-26-23<br>
          1700</td>
        <td width="64">CFH Prayer Room</td>
        <td width="64">AN</td>
        <td width="64">Report Taken<p></p>
          <p>TOT Student Conduct</p>
        </td>
        <td width="64">Complainant reported being harassed by another student</td>
      </tr>
      <tr>
        <td width="64">2023-000012</td>
        <td width="64">Domestic Violence</td>
        <td width="64">1-25-23<br>
          1050</td>
        <td width="64">1-24-23<br>
          1600</td>
        <td width="64">Not on Clery Geography</td>
        <td width="64">AN</td>
        <td width="64">Report Taken<p></p>
          <p>TOT Fairfax County Police</p>
          <p>Title IX Notified</p>
          <p>Cleared by Arrest</p>
        </td>
        <td width="64">Complainant reported a domestic violence incident that occurred the previous night</td>
      </tr>
      <tr>
        <td width="64">2023-000010</td>
        <td width="64">Welfare Check<br>
          (Domestic Violence)</td>
        <td width="64">1-22-23<br>
          1442</td>
        <td width="64">1-22-23<br>
          1442</td>
        <td width="64">Via Email<br>
          (Not on NOVA’s Clery Geography)</td>
        <td width="64">AN</td>
        <td width="64">Report Taken<p></p>
          <p>TOT Fairfax County Police</p>
        </td>
        <td width="64">Professor received an email from a student who was reporting domestic violence at home</td>
      </tr>
      <tr>
        <td width="64">2023-000009</td>
        <td width="64">Identity Theft</td>
        <td width="64">1-20-23<br>
          1120</td>
        <td width="64">1990’s</td>
        <td width="64">AN</td>
        <td width="64">AN</td>
        <td width="64">Report Taken</td>
        <td width="64">Complainant reported somebody used his information to attend classes in the 1990’s at NOVA</td>
      </tr>
      <tr>
        <td width="64">2023-000008</td>
        <td width="64">Hit &amp; Run</td>
        <td width="64">1-19-23<br>
          1913</td>
        <td width="64">1-19-23<br>
          1454</td>
        <td width="64">A2 Lot</td>
        <td width="64">LO</td>
        <td width="64">Report Taken<p></p>
          <p>Info Exchange</p>
        </td>
        <td width="64">Complainant reported damage to their parked vehicle</td>
      </tr>
      <tr>
        <td width="64">2023-000007</td>
        <td width="64">Hit &amp; Run</td>
        <td width="64">1-19-23<br>
          1500</td>
        <td width="64">1-17-23<br>
          Between<br>
          0900-1800</td>
        <td width="64">B10 Lot</td>
        <td width="64">AN</td>
        <td width="64">Report Taken</td>
        <td width="64">Report someone hit their vehicle and left a note with the wrong number</td>
      </tr>
      <tr>
        <td width="64">2301190038</td>
        <td width="64">Hit &amp; Run</td>
        <td width="64">1-19-23<br>
          1239</td>
        <td width="64">1-18-23<br>
          Between<br>
          0930-1230</td>
        <td width="64">Parking Garage</td>
        <td width="64">AN</td>
        <td width="64">Unfounded</td>
        <td width="64">Report of a hit and run which did not occur on NOVA property</td>
      </tr>
      <tr>
        <td width="64">2023-000006</td>
        <td width="64">Hit &amp; Run</td>
        <td width="64">1-19-23<br>
          1128</td>
        <td width="64">1-19-23<br>
          1128</td>
        <td width="64">B3 Lot</td>
        <td width="64">AN</td>
        <td width="64">Report Taken<p></p>
          <p>Info Exchange</p>
        </td>
        <td width="64">Person observed a hit and run in the parking lot</td>
      </tr>
      <tr>
        <td width="64">2023-000005</td>
        <td width="64">Stalking</td>
        <td width="64">1-18-23<br>
          1513</td>
        <td width="64">1-17-23<br>
          1900</td>
        <td width="64">Not on Clery Geography</td>
        <td width="64">LO</td>
        <td width="64">Report Taken<br>
          Title IX Notified</td>
        <td width="64">3rd party complaint reporting an incident of stalking which occurred at a private residence</td>
      </tr>
      <tr>
        <td width="64">2301180027</td>
        <td width="64">Police Service</td>
        <td width="64">1-18-23<br>
          1215</td>
        <td width="64">1-18-23<br>
          1150</td>
        <td width="64">Lake</td>
        <td width="64">AN</td>
        <td width="64">GOA</td>
        <td width="64">Report of a naked man in the lake</td>
      </tr>
      <tr>
        <td width="64">2023-000004</td>
        <td width="64">Disorderly Conduct</td>
        <td width="64">1-18-23<br>
          1137</td>
        <td width="64">1-18-22<br>
          1131</td>
        <td width="64">AA 2nd Floor</td>
        <td width="64">AL</td>
        <td width="64">Report Taken<p></p>
          <p>No Trespass Order Issued</p>
        </td>
        <td width="64">Complainant reported another person tried taking her property from her</td>
      </tr>
      <tr>
        <td width="64">PD230001501</td>
        <td width="64">DWI</td>
        <td width="64">1-12-23<br>
          2130</td>
        <td width="64">1-12-23<br>
          2130</td>
        <td width="64">WO Entrance</td>
        <td width="64">WO</td>
        <td width="64">Handled by Prince William County Police</td>
        <td width="64">One vehicle traffic accident which resulted in a DWI investigation</td>
      </tr>
      <tr>
        <td width="64">2023-000003</td>
        <td width="64">Fraud</td>
        <td width="64">1-11-23<br>
          1504</td>
        <td width="64">3-16-219<br>
          Unknown</td>
        <td width="64">Not on Clery Geography</td>
        <td width="64">AN</td>
        <td width="64">Report Taken</td>
        <td width="64">Complainant reported their SSN was used by someone else</td>
      </tr>
      <tr>
        <td width="64">2301110018</td>
        <td width="64">Be On The Lookout</td>
        <td width="64">1-11-23<br>
          1023</td>
        <td width="64">1-11-23<br>
          1023</td>
        <td width="64">Not on Clery Geography</td>
        <td width="64">MA</td>
        <td width="64">Assisted</td>
        <td width="64">VSP issued an alert for a missing adult</td>
      </tr>
      <tr>
        <td width="64">2301100029</td>
        <td width="64">Police Service<br>
          (Drug Investigation)</td>
        <td width="64">1-10-23<br>
          1647</td>
        <td width="64">1-10-23<br>
          1647</td>
        <td width="64">3rd Floor Garage</td>
        <td width="64">AN</td>
        <td width="64">GOA</td>
        <td width="64">Report of two men smoking marijuana near the elevator</td>
      </tr>
      <tr>
        <td width="64">2301100025</td>
        <td width="64">Police Service<br>
          (Missing Person)</td>
        <td width="64">1-10-23<br>
          1533</td>
        <td width="64">1-10-23<br>
          After 1000</td>
        <td width="64">AN</td>
        <td width="64">AN</td>
        <td width="64">Assisted</td>
        <td width="64">Father reported he could not find his daughter after dropping her off at 1000. She was located
        </td>
      </tr>
      <tr>
        <td width="64">2301050023</td>
        <td width="64">Abandoned Vehicle</td>
        <td width="64">1-5-22<br>
          1722</td>
        <td width="64">1-5-22<br>
          1722</td>
        <td width="64">Beauregard Parking Garage</td>
        <td width="64">AL</td>
        <td width="64">Unfounded</td>
        <td width="64">Report of an abandoned vehicle parked at the location</td>
      </tr>
      <tr>
        <td width="64">2301050010</td>
        <td width="64">Assist Other Agency</td>
        <td width="64">1-5-23<br>
          0854</td>
        <td width="64">1-5-23<br>
          0854</td>
        <td width="64">Brault</td>
        <td width="64">AN</td>
        <td width="64">Assisted</td>
        <td width="64">Unit assisted Alexandria Police Department</td>
      </tr>
      <tr>
        <td width="64">2301050004</td>
        <td width="64">Suspicious Vehicle</td>
        <td width="64">1-5-22<br>
          0520</td>
        <td width="64">1-5-22<br>
          0520</td>
        <td width="64">6th Level of Parking Garage</td>
        <td width="64">AN</td>
        <td width="64">Assisted</td>
        <td width="64">Report of a suspicious vehicle at the location</td>
      </tr>
      <tr>
        <td width="64">2301040031</td>
        <td width="64">Police Service<br>
          (Harassment)</td>
        <td width="64">1-4-23<br>
          1848</td>
        <td width="64">Unknown</td>
        <td width="64">Unknown</td>
        <td width="64">AN</td>
        <td width="64">TOT<br>
          Student Conduct</td>
        <td width="64">Female reported bullying and harassment that she wanted to report to student conduct</td>
      </tr>
      <tr>
        <td width="64">2301040002</td>
        <td width="64">Indecent Exposure</td>
        <td width="64">1-4-23<br>
          0040</td>
        <td width="64">1-4-23<br>
          0040</td>
        <td width="64">B3 Lot</td>
        <td width="64">AN</td>
        <td width="64">TOT<br>
          Fairfax County PD</td>
        <td width="64">Unit observed a couple having sex in a vehicle</td>
      </tr>
      <tr>
        <td width="64">2023-000001</td>
        <td width="64">Property Damage<br>
          Noncriminal</td>
        <td width="64">1-2-23<br>
          1630</td>
        <td width="64">Unknown</td>
        <td width="64">B1 Lot</td>
        <td width="64">AN</td>
        <td width="64">Report Taken</td>
        <td width="64">Unit observed a tree down in the parking lot</td>
      </tr>
      <tr>
        <td width="64">230101002</td>
        <td width="64">Suspicious Vehicle</td>
        <td width="64">1-1-23<br>
          1351</td>
        <td width="64">1-1-23<br>
          1351</td>
        <td width="64">Dawes &amp; Netherton</td>
        <td width="64">AL</td>
        <td width="64">Assisted</td>
        <td width="64">unoccupied vehicle left in the roadway</td>
      </tr>
    </tbody>
  </table>
"""
soup = BeautifulSoup(html_doc, 'html.parser')



soup.find_all('tr')

dict = {}
count =0 
for i in soup.find_all('tr'):
  b = i.get_text().strip("\n")
  dict[count] =b
  count+=1
  # print(i)
  # print("\n")
  # print("\n")
print(dict)
print("\n")

# for row in rows:
#     print row


pprint.pprint(dict)




