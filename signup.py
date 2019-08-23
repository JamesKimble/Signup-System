### Signup Python Program ###

## - Made By JamesTheWebDev - ##





####################
## Import Modules ##
####################

from datetime import datetime
import time
import keyboard
import string


#####################
## Custom Greeting ##
#####################


m = 5;
a = 12;
e = 19;

mrng = str(m);
aftn = str(a);
evng = str(e);

now = datetime.now();
 
# Current hour (24 hour clock) #
hour = now.strftime("%H");

greet = "";

if hour == mrng or hour < mrng and hour < aftn:
    greet = "morning";
if hour == aftn or hour > aftn and hour < evng:
    greet = "afternoon";
if hour == evng or hour > evng and hour > aftn:
    greet = "evening";




############
## Signup ##
############

def usersignup():

    print("\n");
    print("CREATE AN ACCOUNT: \n\n");
    ##############
    ## Username ##
    ##############
    def getusername():
        
        with open("details.txt") as unamechckr:
            chckr = unamechckr.read();
            global uname;
            uname = input("\nPlease create a username\n: ");
            invalidChars = set(string.punctuation.replace("_", " "))
            if any(char in invalidChars for char in uname):
                time.sleep(0.5);
                print("\nOops! We do not accept any special characers or spaces in usernames. Please try again.\n");
                time.sleep(2);
                getusername()
            if len(uname) < 3:
                time.sleep(0.5);
                print("\nOops! Your username is too short! Please try again.\n");
                time.sleep(2);
                getusername();
            if len(uname) > 15:
                time.sleep(0.5);
                print("\nOops! Your username is too long! Please try again.\n");
                time.sleep(2);
                getusername()
            if uname in chckr:
                time.sleep(0.5);
                print("\nOops! Someone is already using that Username! Please try again.\n");
                time.sleep(2);
                getusername()
            else:
                saveuname = open("details.txt", "a");
                saveuname.write("\n"+uname.upper()+"'S LOGIN CREDENTIALS: \n\n");
                saveuname.write("Username: " + uname + "\n");
                saveuname.close();
        unamechckr.close();
        
    getusername()


    ###################
    ## Email Address ##
    ###################
    def getemail():
        
        with open("details.txt") as emailchckr:
            chckr = emailchckr.read();
            global email
            email = input("\nPlease enter your email address\n: ");
            if "@" and "." not in email:
                time.sleep(0.5);
                print("\nOops! That email address is invalid. Please try again.\n");
                time.sleep(2);
                getemail()
            if len(email) < 5:
                time.sleep(0.5);
                print("\nOops! Your email is too short! Please try again.\n");
                time.sleep(2);
                getusername();
            if len(email) > 50:
                time.sleep(0.5);
                print("\nOops! Your email is too long! Please try again.\n");
                time.sleep(2);
                getemail()
            if email in chckr:
                print("\nOops! Someone is already using that email address!\n");
                getemail()
            else:
                saveemail = open("details.txt", "a");
                saveemail.write("Email address: " + email + "\n");
                saveemail.close();
        emailchckr.close();
        
    getemail()


    ##################
    ## Phone Number ##
    ##################
    def getphone():
        
        with open("details.txt") as phonechckr:
            chckr = phonechckr.read();
            global phone;
            phone = input("\nPlease enter your phone number\n: ");
            try:
                float(phone)
            except ValueError:
                time.sleep(0.5);
                print("\nThis phone number is invalid. Please try again.\n");
                time.sleep(2);
                getphone()
            if len(phone) < 7:
                time.sleep(0.5);
                print("\nOops! That phone number is too short! Please try again.\n");
                time.sleep(2);
                getphone()
            if len(phone) > 15:
                time.sleep(0.5);
                print("\nOops! That phone number is too long! Please try again.\n");
                time.sleep(2);
                getphone()
            if phone in chckr:
                time.sleep(0.5);
                print("\nOops! Someone is already using that phone number!\n");
                time.sleep(2);
                getphone()
            else:
                savephone = open("details.txt", "a");
                savephone.write("Phone number: " + phone + "\n");
                savephone.close();
        phonechckr.close();
        
    getphone()


    ##############
    ## Password ##
    ##############
    def getpassword():
        
        with open("details.txt") as pwrdcr8:
            newpwrd = pwrdcr8.read();
            global pwrd;
            pwrd = input("\nPlease create a new password\n: ");
            if len(pwrd) < 5:
                time.sleep(0.5);
                print("\nOops! Your password is too short! Please try again.\n");
                time.sleep(2);
                getpassword()
            if len(pwrd) > 15:
                time.sleep(0.5);
                print("\nOops! Your password is too long! Please try again.\n");
                time.sleep(2);
                getpassword()
            savepwrd = open("details.txt", "a");
            savepwrd.write("Password: " + pwrd + "\n");
            savepwrd.close();
        pwrdcr8.close();
        
    getpassword()

    time.sleep(1);

    print("\nPlease wait while we validate your credentials...\n");
    time.sleep(3);
    print("\nGood " + greet + " " + uname + "!\n");

        
usersignup()




    








