email=input()
ind=email.index("@")

username=""
domain=email[ind+1:]

for each_item in email:
    if(each_item=="@"):
        break
    else:
        username = username + each_item
print("Your Username is : " + username + " & domain is " + domain)