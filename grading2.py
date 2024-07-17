import csv

# Function to read the answer Key CSV into a list of answers from the second column
def read_answers(filepath):
    answer_key = []
    with open(filepath, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            #answers are in the second column
            answer_key.append(row[1])  
    return answer_key

# Function to read exam answers CSV into a list, stripping off trailing period
def read_exam_answers(filepath):
    exam_answers = []
    with open(filepath, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # Remove trailing period from answer
            exam_answer = row[0].rstrip('.')  
            exam_answers.append(exam_answer)
    return exam_answers

# Function to compare the two and calculate score
def calculate_score(answer_key, exam_answers):
    correct_count = 0
    for i in range(len(exam_answers)):
        key_answer = answer_key[i]
        exam_answer = exam_answers[i]
        if key_answer == exam_answer:
            correct_count += 1

    #calculate score and print
    #lenht -1 to not account for the column name
    score = (correct_count / (len(answer_key)-1)) * 100  
    print(correct_count, "Out of", len(answer_key) -1)  
    
    return score

# File paths
answer_key_file = r"C:\\Users\\Data Engineer Intern\\Downloads\\Playfair Practictioner Exams Grading Sheets - Advanced Analytics Answer Key.csv"
exam_answers_file = r"C:\\Users\\Data Engineer Intern\\Downloads\\Sean Reynolds Exam Answers.csv"

# Call functions 
answer_key = read_answers(answer_key_file)
exam_answers = read_exam_answers(exam_answers_file)

# Calculate and display score
score = calculate_score(answer_key, exam_answers)
#round to two decimal places
score = round(score, 2)
print(f"The score for this exam is: {score}%")
