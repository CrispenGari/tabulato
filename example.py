from tabulato import colorful_tabulate


headers = ["Name", "Student Number", "DOB", "Email Address"]

data = [
    ["John Doe", "S12345", "1995-07-15", "john@example.com"],
    ["Alice Smith", "S67890", "1998-03-22", "alice@example.com"],
    ["Bob Johnson", "S54321", "1997-11-10", "bob@example.com"],
    ["Emma Brown", "S98765", "1996-09-18", "emma@example.com"],
    ["Michael Lee", "S24680", "1999-05-30", "michael@example.com"],
    ["Sophia Wang", "S13579", "1994-12-05", "sophia@example.com"],
    ["David Chen", "S75310", "1992-04-08", "david@example.com"],
    ["Olivia Kim", "S36924", "1993-10-25", "olivia@example.com"],
]


colorful_tabulate(headers=headers, data=data, colorful=True, bold_header=True)
