#import re module
import re

#create function to validate email
def validate_email(email):
    #check for occurance in the email format abc@xyz.com
    email_pattern = "[a-zA-Z0-9]+@[a-zA-z]+.[a-zA-z]{2,4}"
    result = re.search(email_pattern, email)
    #check result and print the output
    if result is not None:
        print("Valid email")
    else:
        print("Invalid email")

#create function to validate bangladesh number
def validate_ban_num(mobilenum):
 #check for occurance in the format 01xxx xxxxxx
    mobile_pattern = '^?01[0-9]{3}[0-9]{6}$'
    mobile_result = re.search(mobile_pattern, mobilenum)
     #check result and print the output
    if mobile_result is not None:
        print("Valid number")
    else:
        print("Invalid number")

#function to validate us number
def validate_us_num(us_mobnum):
 #check for occurance in the format (xxx)xxx-xxxx
    us_num_pattern = '\(?[0-9]{3}\)?-? *[0-9]{3}-?*[0-9]{4}$'
    us_num_result = re.search(us_num_pattern, us_mobnum) 
     #check result and print the output
    if us_num_result is not None:
        print("Valid number")
    else:
        print("Invalid number")

#function to validate password entered
def pass_verification(password):
    #check f lenght of the oassword is correct
    if len(password<16):
        print("password must be 16 characters")
    else:
        pass_pattern = '[A-Za-z0-9!"#€%&/?=^*_.,:;]'
        pass_result = re.search(pass_pattern, password) 
        #check result and print the output
        if pass_result is not None:
            print("Valid password")
        else:
            print("Invalid password")