import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()


@st.dialog("Send Email")
def email_form():
    with st.form("email_form"):
        st.write("Send Email")
        from_email = st.text_input("From:", placeholder="Enter email address")
        subject = st.text_input("Subject:", placeholder="Enter email subject")
        body = st.text_area("Body:", placeholder="Enter email content")
        if st.form_submit_button("Send"):
            if from_email and subject and body:
                send_email(from_email, subject, body)
                st.success("Email sent successfully!")
            else:
                st.error("Please fill in all fields before sending the email.")


def send_email(from_email, subject, body):
    your_email = os.environ["EMAIL"]
    your_password = os.environ["EMAIL_PASSWORD"]

    msg = MIMEMultipart()
    msg['From'] = your_email
    msg['To'] = your_email
    msg['Subject'] = subject
    msg['Reply-To'] = from_email
    msg.attach(MIMEText(f"Received mail from {from_email} from the app.\n"
                        f"---------------------------------------------\n\n{body}", 'plain'))
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(your_email, your_password)
            server.send_message(msg)
            print("Email sent successfully!🚀")
    except Exception as e:
        print(f"Error sending email: {e}")


if __name__ == "__main__":
    send_email("recipient@example.com", "Test Email", "This is a test email sent from Python!")