from utilities import send_email
import os
import json
from Logger import MyLogger
from dotenv import load_dotenv




logger = MyLogger(os.path.basename(__file__))

def main(request):

    logger.info("Email notification started. Getting environment variables.")
    sender_email = os.environ["sender_email"]
    sender_pass = os.environ["sender_pass"]
    error_email_receivers = os.environ["error_email_receivers"]
    error_email_body = os.environ["error_email_body"]
    emails_list = json.loads(os.environ["emails_list"])

    try:
        logger.info("Reading and parsing JSON from request.")
        request_json = request.get_json(silent=True)
        email_subject = request_json["subject"]
        email_body = request_json["body"]
        email_receivers_names = request_json["email_receivers_list"]
        email_receivers_names_list = email_receivers_names.split(",")
 
        logger.info("Creating list of receivers.")
        email_receivers_list = [emails_list[name] for name in email_receivers_names_list]

        logger.info("Sending email notification.")
        send_email(sender_email, sender_pass, email_subject, email_body, email_receivers_list)
        
        logger.info("Email notification success. Process finished.")
        return json.dumps({"success": True})
    
    except Exception as e:
        print(e)
        logger.error("Email notification failed. Process finished.")
        send_email(sender_email, sender_pass, email_subject, error_email_body + str(e), error_email_receivers)
        return json.dumps({"success": False})

