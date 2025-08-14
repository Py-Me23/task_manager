







file= open("emails.txt", "r")# how to readfrom a file
emails= file.read().split("\n")
print(emails)



user_name=""
for email in emails:
  user_name= email.split('@')[0]
  print(user_name)