import email 
import re
import csv

# Function to extract email body text
def get_email_body(eml_file):
    with open(eml_file, 'r') as file:
        msg = email.message_from_file(file)
    for part in msg.walk():
        if part.get_content_type() == 'text/plain':
            return part.get_payload()

# Function to get the multiple choice answers
def extract_answers(text):
    answers = re.findall(r'\b[A-E]\.', text)
    return answers

#function to save results
def save_to_csv(test_taker_name, answers):
    filename = f"{test_taker_name} Exam Answers.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Answer'])
        for answer in answers:
            writer.writerow([answer])
    print(f"Results saved to {filename}")


#function to get the name of the test taker
def extract_name(text):
    F_name_match = re.search(r"\*First Name\*\s+(\w+)", text, re.IGNORECASE)
    L_name_match = re.search(r"\*Last Name\*\s+(\w+)", text, re.IGNORECASE)
    
    F_name = F_name_match.group(1) if F_name_match else ""
    L_name = L_name_match.group(1) if L_name_match else ""
    
    return F_name + " " + L_name

# Main function
def main(eml_file):
    email_body = get_email_body(eml_file)
    name = extract_name(email_body)
    print ("Exam Results For: ", name)
    answers = extract_answers(email_body)
    save_to_csv(name, answers)

    #for answer in answers:
        #print(answer)
    
eml_file = 'C:\\Users\\Data Engineer Intern\\Downloads\\New submission from Data Engineering Practitioner Exam (1).eml' 
main(eml_file)
