from distutils import extension


def main():
     print("Welcome to the email slicer ")
     print("")

     email_input = input("Input you email address: ")
     (username, domain) = email_input.split("@")
     (domain, extension) = domain.split(".")

     print("username : ", username)
     print("domain : ", domain)
     print("extension : ",extension)
while True:
     main()