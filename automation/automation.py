import re

with open("assets/potential-contacts.txt","r") as file:
    file_content=file.read()

# print(file_content)

match_email = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', file_content)
# print(match_email[0])
match_email=set(match_email)
match_phone = re.findall(r'\d{3}-\d{3}-\d{4}|\d{3}-\d{4}', file_content)
# print(match_phone)



with open("assets/emails.txt", "w") as f:
    for email in match_email:
        f.write(email + "\n")

with open("assets/phone_numbers.txt", "w") as f:
    for phone in match_phone:
        if len(phone)==12:
         f.write( phone + "\n")
         
        if len(phone)==8:
          f.write( "206-"+ phone + "\n")