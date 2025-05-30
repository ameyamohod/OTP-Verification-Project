import random
import smtplib

#(1) Function to generate a 6-digit OTP randomly
def OTP_generation():
    OTP = random.randint(100000, 999999)  # Generate a random 6-digit OTP
    return OTP

#(2) Function to simulate sending the OTP to the user's email address
def send_otp_email(receiver_email, OTP):
    # Setting up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to the server (Use an app password if you have 2FA enabled)
    password = ""  # Senders credentials
    server.login("", password)

    # Creating the email content
    body = f"Your OTP is {OTP}."
    subject = "OTP Verification"
    message = f"Subject: {subject}\n\n{body}"

    # Send the OTP to the user's email address
    server.sendmail("Senders_email", receiver_email, message)
    print(f"OTP has been sent to {receiver_email}")
    
    server.quit()

#(3) Function to prompt the user to enter the OTP received in their email
def prompt_otp_entry():
    try:
        received_OTP = int(input("Enter the OTP you received: "))
        return received_OTP
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return prompt_otp_entry()  # Retry if invalid input

#(4) Function to verify if the entered OTP matches the generated OTP
def verify_otp(received_OTP, generated_OTP):
    if received_OTP == generated_OTP:
        return True
    else:
        return False

# Function to verify if the email is valid
def email_verification(receiver_email):
    email1 = ["gmail", "hotmail", "yahoo", "outlook"]
    email2 = [".com", ".in", ".org", ".edu", ".co.in"]
    count = 0

    for x in email1:
        if x in receiver_email:
            count += 1
    for y in email2:
        if y in receiver_email:
            count += 1

    if "@" not in receiver_email or count != 2:
        print("Invalid email ID")
        new_receiver_email = input("Enter correct email ID: ")
        return email_verification(new_receiver_email)
    return receiver_email

# Main function to manage OTP generation, sending, and verification
def otp_verification_system():
    receiver_email = input("Enter your email address: ")

    # Validate the email address
    valid_receiver_email = email_verification(receiver_email)

    # Generate OTP
    generated_OTP = OTP_generation()

    # Send OTP to the user's email
    send_otp_email(valid_receiver_email, generated_OTP)

    # Allow the user to enter OTP up to 3 times if incorrect
    attempts = 3
    while attempts > 0:
        received_OTP = prompt_otp_entry()  # Get OTP entered by the user

        # Verify OTP
        if verify_otp(received_OTP, generated_OTP):
            print("OTP verified successfully!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect OTP. You have {attempts} attempts left.")
            else:
                print("Incorrect OTP. You've used all attempts.")
                retry = input("Would you like to receive a new OTP? (yes/no): ").lower()
                if retry == "yes":
                    otp_verification_system()  # Restart the OTP verification process
                else:
                    print("OTP verification failed. Exiting system.")
                    break

# Run the OTP verification system
otp_verification_system()

  
