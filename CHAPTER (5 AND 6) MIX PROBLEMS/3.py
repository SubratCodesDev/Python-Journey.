a={"username":"SUBRAT@gamil.com","password":"harrypotter1122"}
aa=input("Enter your username:")
b=input("Enter your password:")
if aa==a.get("username") and b==a.get("password"):
    print("Login successfully")
elif aa!=a.get("username")or b!=a.get("password"):
    print("Username or password is incorrect")
else:
    print("Invalid infromation")
    