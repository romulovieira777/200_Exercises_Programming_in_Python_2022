"""
Exercise No. 03

The playway.csv file contains Playway's listing for March 2020. This file was loaded as follows to the content variable:

    with open("../Files/playway.csv") as file:
        content = file.read().splitlines()

content:

    ['Date,Open,High,Low,Close,Volume',
     '2020-03-02,305,324.5,283.5,310,64081',
     '2020-03-03,325.5,340.5,320,340.5,55496',
     '2020-03-04,324,340.5,315,330,36152',
     '2020-03-05,344,344,310,315,35992',
     '2020-03-06,306.5,307,291,305,32539',
     '2020-03-09,274,291,250,258,79402',
     '2020-03-10,278,284.5,256,264,35700',
     '2020-03-11,270,270,238.5,245,60445',
     '2020-03-12,218,228,196,197,94031',
     '2020-03-13,210,229,198.8,211,100412',
     '2020-03-16,205,248,197.8,240.5,50659',
     '2020-03-17,245,269,232.5,264,99480',
     '2020-03-18,264,280,251,270,70136',
     '2020-03-19,267,280,267,279.5,30732',
     '2020-03-20,297.5,307,280,280.5,43426',
     '2020-03-23,274,289,258,285,37098',
     '2020-03-24,305,309,296.5,309,31939',
     '2020-03-25,313,330,295,304,46724',
     '2020-03-26,300,309,295.5,300,27213',
     '2020-03-27,302,306.5,290,296,13466',
     '2020-03-30,299,300,287,300,10316',
     '2020-03-31,302.5,309,302,306.5,15698']

Transform the content of the file to get a dictionary containing two keys: 'Date' and 'Close'. The values for these keys
will be, respectively, lists consisting of all dates and closing prices. Convert closing prices to float type and print
this dictionary to the console as shown below.

Formatted result:

    {'Close': [310.0,
  340.5,
  330.0,
  315.0,
  305.0,
  258.0,
  264.0,
  245.0,
  197.0,
  211.0,
  240.5,
  264.0,
  270.0,
  279.5,
  280.5,
  285.0,
  309.0,
  304.0,
  300.0,
  296.0,
  300.0,
  306.5],
 'Date': ['2020-03-02',
  '2020-03-03',
  '2020-03-04',
  '2020-03-05',
  '2020-03-06',
  '2020-03-09',
  '2020-03-10',
  '2020-03-11',
  '2020-03-12',
  '2020-03-13',
  '2020-03-16',
  '2020-03-17',
  '2020-03-18',
  '2020-03-19',
  '2020-03-20',
  '2020-03-23',
  '2020-03-24',
  '2020-03-25',
  '2020-03-26',
  '2020-03-27',
  '2020-03-30',
  '2020-03-31']}

Expected result:

    {'Date': ['2020-03-02', '2020-03-03', '2020-03-04', '2020-03-05', '2020-03-06', '2020-03-09', '2020-03-10',
     '2020-03-11', '2020-03-12', '2020-03-13', '2020-03-16', '2020-03-17', '2020-03-18', '2020-03-19', '2020-03-20',
     '2020-03-23', '2020-03-24', '2020-03-25', '2020-03-26', '2020-03-27', '2020-03-30', '2020-03-31'],
     'Close': [310.0, 340.5, 330.0, 315.0, 305.0, 258.0, 264.0, 245.0, 197.0, 211.0, 240.5, 264.0, 270.0, 279.5, 280.5,
               285.0, 309.0, 304.0, 300.0, 296.0, 300.0, 306.5]}
"""
# Solution I
with open("../Files/playway.csv") as file:
    content = file.read().splitlines()

dates = []
closes = []
for line in content:
    if "Date" not in line:
        line = line.split(",")
        dates.append(line[0])
        closes.append(float(line[4]))

print({"Date": dates, "Close": closes})


# Solution II
with open("../Files/playway.csv") as file:
    content = file.read().splitlines()

data = [(line.split(',')[0], line.split(',')[4]) for line in content]
result = {
    data[0][0]: [data[1:][i][0] for i in range(len(data) - 1)],
    data[0][1]: [float(data[1:][i][1]) for i in range(len(data) - 1)]
    }
print(result)
