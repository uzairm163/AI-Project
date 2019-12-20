import random
# create a master questions list of question objects
questionsList = []

# creating question class to contain question data
class Question:
    def __init__(self, question, group):
        self.question = question[0]
        self.direction = question[1]
        self.group = group
        self.A = True
        self.B = False
        self.scores = None

    def ask(self):
        """
        uses a while loop to ask user a question
        their answer determines the score which is returned
        returns answer value
        """
        while True:
            print(self.question)
            answer = input("YES or NO:\n")
            if answer.lower() == "yes" or answer.lower() == "no":
                answer = answer.lower()
                if answer == "yes":
                    answer = True
                    break
                else:
                    answer = False
                    break
            else:
                print("INVALID ANSWER! ANSWER AGAIN PLZ \n")
                continue
        if self.direction:
            if answer:  # answer was yes
                self.scores = questionScores(self.A, self.group)
                return None
            else:
                self.scores = questionScores(self.B, self.group)
                return None

        else:  # question answer is reversed
            if answer:
                self.scores = questionScores(self.B, self.group)
                return None
            else:
                self.scores = questionScores(self.A, self.group)
                return None

    def getQuestion(self):
        return self.question

    def getDirection(self):
        return self.direction

    def getScores(self):
        return self.scores


# creating questions, true value means they score fowards, false means they score reversed
opennessItems = [["\nQ.....  I have excellent ideas\t", True],
                 ["\nQ.....  I am quick to understand things\t", True],
                 ["\nQ.....  I use difficult words\t", True],
                 ["\nQ.....  I am full of ideas\t", True],
                 ["\nQ.....  I am not interested in abstractions\t", False],
                 ["\nQ.....  I do not have a good imagination\t", False],
                 ["\nQ.....  I have difficulty understanding abstract ideas\t", False]
                 ]

conscientiousnessItems = [["\nQ.....  You are always prepared", True],
                          ["\nQ.....  You pay attention to every detail", True],
                          ["\nQ.....  You get chores done right away", True],
                          ["\nQ.....  You like order", True],
                          ["\nQ.....  You follow a schedule", True],
                          ["\nQ.....  You like to do exactly whats required in your work", True],
                          ["\nQ.....  You leave your belongings around", False],
                          ["\nQ.....  You make a lot mess of things", False],
                          ["\nQ.....  You often forget to put things back in their proper place", False],
                          ["\nQ.....  You dont perform your duties", False]
                          ]

extroversionItems = [["\nQ.....  I am the life of the party", True],
                     ["\nQ.....  I don't mind being the center of attention", True],
                     ["\nQ.....  I feel comfortable around people", True],
                     ["\nQ.....  I start conversations", True],
                     ["\nQ.....  I talk to a lot of different people at parties", True],
                     ["\nQ.....  I don't talk a lot", False],
                     ["\nQ.....  I think a lot before i speak or act", False],
                     ["\nQ.....  I don't like to draw attention to myself", False],
                     ["\nQ.....  I am quiet around strangers", False],
                     ["\nQ.....  I have no intention of talking in large crowds", False]
                     ]

agreeablenessItems = [["\nQ.....  You become interested in people", True],
                      ["\nQ.....  You sympathize with other's feelings", True],
                      ["\nQ.....  You have a very soft heart", True],
                      ["\nQ.....  You take time out for others", True],
                      ["\nQ.....  You feel others' emotions", True],
                      ["\nQ.....  You make people feel easy doing something at work", True],
                      ["\nQ.....  You are not really interested in others", False],
                      ["\nQ.....  You like to insult people", False],
                      ["\nQ.....  You are not interested in other people's problems", False],
                      ["\nQ.....  You feel little bit concern for others", False]
                      ]

neuroticismItems = [["\nQ.....  I get irritated easily", True],
                    ["\nQ.....  I get stressed out easily", True],
                    ["\nQ.....  I get upset easily", True],
                    ["\nQ.....  I have frequent mood swings", True],
                    ["\nQ.....  I worry about things", True],
                    ["\nQ.....  I am much more anxious than most people", True],
                    ["\nQ.....  I am relaxed most of the time", False],
                    ["\nQ.....  I often feel sad", False]
                    ]

# function that creates question objects for each of the values in their respective lists


def createQuestions():

    print()
    print("Asalam O Alikum! This Myers–Briggs Type Indicator (MBTI) is an introspective self-report questionnaire with the purpose of indicating differing psychological preferences in how people perceive the world around them and make decisions.")
    print("\n^^^^^^ Developed by Hammad Shaikh , Muhammad Uzair , Ahsan Ishtiaq ^^^^^^\n")

    # creates openness questions
    print("\t\t\t\t\tIt includes... Openness Questions")
    for statement in opennessItems:
        question = Question(statement, "O")
        questionsList.append(question)

    print("\t\t\t\t\tIt includes... Conscientiousness Questions")
    for statement in conscientiousnessItems:
        question = Question(statement, "C")
        questionsList.append(question)

    print("\t\t\t\t\tIt includes... Extroversion Questions")
    for statement in extroversionItems:
        question = Question(statement, "E")
        questionsList.append(question)

    print("\t\t\t\t\tIt includes... Agreeableness Questions")
    for statement in agreeablenessItems:
        question = Question(statement, "A")
        questionsList.append(question)

    print("\t\t\t\t\tIt includes... Neuroticism Questions")
    for statement in neuroticismItems:
        question = Question(statement, "N")
        questionsList.append(question)

    print()
    print("************************************** Welcome To MYER'S BRIGG Personality Test ***********************************************")
    print()

    return None


# function that returns a list of answer values based on return value from ask() method in Question


def questionScores(answer, group):
    # scores goes in E, I, S, N, T, F, J, P
    scores = []
    if answer:
        if group == "N":
            scores.append(-0.18)  # E
            scores.append(0.14)  # I
            scores.append(-0.16)  # S
            scores.append(0.21)  # N
            scores.append(-0.29)  # T
            scores.append(0.36)  # F
            scores.append(-0.25)  # J
            scores.append(0.30)  # P
            return scores

        elif group == "E":
            scores.append(0.58)  # E
            scores.append(-0.58)  # I
            scores.append(-0.08)  # S
            scores.append(0.02)  # N
            scores.append(0.02)  # T
            scores.append(0.05)  # F
            scores.append(-0.06)  # J
            scores.append(0.03)  # P
            return scores

        elif group == "O":
            scores.append(-0.30)  # E
            scores.append(0.30)  # I
            scores.append(-0.60)  # S
            scores.append(0.71)  # N
            scores.append(-0.34)  # T
            scores.append(0.35)  # F
            scores.append(-0.07)  # J
            scores.append(0.03)  # P
            return scores

        elif group == "A":
            scores.append(-0.08)  # E
            scores.append(-0.01)  # I
            scores.append(-0.11)  # S
            scores.append(0.29)  # N
            scores.append(0.52)  # T
            scores.append(0.52)  # F
            scores.append(0.00)  # J
            scores.append(0.00)  # P
            return scores

        elif group == "C":
            scores.append(-0.11)  # E
            scores.append(0.01)  # I
            scores.append(0.03)  # S
            scores.append(0.03)  # N
            scores.append(0.02)  # T
            scores.append(0.02)  # F
            scores.append(0.56)  # J
            scores.append(0.62)  # P
            return scores

        else:
            return None

    else:
        if group == "N":
            scores.append(-0.24)  # E
            scores.append(0.26)  # I
            scores.append(-0.02)  # S
            scores.append(0.03)  # N
            scores.append(-0.16)  # T
            scores.append(0.18)  # F
            scores.append(0.01)  # J
            scores.append(0.00)  # P
            return scores

        elif group == "E":
            scores.append(-0.69)  # E
            scores.append(0.46)  # I
            scores.append(-0.18)  # S
            scores.append(0.16)  # N
            scores.append(0.09)  # T
            scores.append(0.05)  # F
            scores.append(-0.03)  # J
            scores.append(0.02)  # P
            return scores

        elif group == "O":
            scores.append(0.21)  # E
            scores.append(0.22)  # I
            scores.append(0.52)  # S
            scores.append(0.49)  # N
            scores.append(0.22)  # T
            scores.append(0.22)  # F
            scores.append(-0.24)  # J
            scores.append(0.24)  # P
            return scores

        elif group == "A":
            scores.append(0.12)  # E
            scores.append(-0.01)  # I
            scores.append(0.03)  # S
            scores.append(0.03)  # N
            scores.append(0.40)  # T
            scores.append(0.40)  # F
            scores.append(0.06)  # J
            scores.append(0.00)  # P
            return scores

        elif group == "C":
            scores.append(0.03)  # E
            scores.append(0.06)  # I
            scores.append(0.20)  # S
            scores.append(0.24)  # N
            scores.append(-0.28)  # T
            scores.append(-0.28)  # F
            scores.append(0.50)  # J
            scores.append(-0.41)  # P
            return scores

        else:
            return None


# function used to add all the scores together for the classification
def applyScores():
    global extroversion
    extroversion = 0
    global introversion
    introversion = 0
    global sensation
    sensation = 0
    global intuition
    intuition = 0
    global thinking
    thinking = 0
    global feeling
    feeling = 0
    global judging
    judging = 0
    global perceiving
    perceiving = 0

    for question in questionsList:
        scores = question.getScores()
        extroversion += scores[0]
        introversion += scores[1]
        sensation += scores[2]
        intuition += scores[3]
        thinking += scores[4]
        feeling += scores[5]
        judging += scores[6]
        perceiving += scores[7]
    return None

# function to ask all the questions once they are made
def askQuestions():
    for question in questionsList:
        question.ask()

    return None


# function to present the score of the test
def shareScore():
    score = ""
    print()
    print("This was your personality test! Your Personality type and overall score is written below: ")
    print("*******************************************************************************************")
    if extroversion >= introversion:
        score += "E"
    else:
        score += "I"

    if sensation >= intuition:
        score += "S"
    else:
        score += "N"

    if thinking >= feeling:
        score += "T"
    else:
        score += "F"

    if judging >= perceiving:
        score += "J"
    else:
        score += "P"
    print("Your Personality Type is: ", score)
    print("*******************************************************************************************")
    print("Overall Results: ")
    print("extroversion: ", str(extroversion))
    print("introversion: ", str(introversion))
    print("sensation: ", str(sensation))
    print("intuition: ", str(intuition))
    print("thinking: ", str(thinking))
    print("feeling: ", str(feeling))
    print("judging: ", str(judging))
    print("perceiving: ", str(perceiving))
    print("*******************************************************************************************")
    print("*******************************************************************************************")
    print()
    print("Thank You For Taking This Test\n")
    print("You can match your Personality type here from 16 different types of people around the globe:\n ") 
    print("^^^^^^ ISTJ Personality: ^^^^^^\n ISTJs are intimidating. They appear serious, formal, and proper. They also love traditions and old-school values that uphold patience, hard work, honor, and social and cultural responsibility. They are reserved, calm, quiet, and upright.\n ")
    print("^^^^^^ INFJ Personality: ^^^^^^\n INFJs are visionaries and idealists who ooze creative imagination and brilliant ideas. They have a different, and usually more profound, way of looking at the world\n")
    print("^^^^^^ INTJ Personality: ^^^^^^\n INTJs, as introverts, are quiet, reserved, and comfortable being alone. They are usually self-sufficient and would rather work alone than in a group\n")
    print("^^^^^^ ENFJ Personality: ^^^^^^\n ENFJs are people-focused individuals. They are extroverted, idealistic, charismatic, outspoken, highly principled and ethical, and usually know how to connect with others no matter their background or personality.\n")
    print("^^^^^^ ISTP Personality: ^^^^^^\n ISTPs are mysterious people who are usually very rational and logical, but also quite spontaneous and enthusiastic.\n")
    print("^^^^^^ ESFJ Personality: ^^^^^^\n ESFJs are the stereotypical extroverts. They are social butterflies, and their need to interact with others and make people happy usually ends up making them popular.\n ")
    print("^^^^^^ INFP Personality: ^^^^^^\n INFPs, like most introverts, are quiet and reserved. They prefer not to talk about themselves, especially in the first encounter with a new person. They like spending time alone in quiet places where they can make sense of what is happening around them.\n ")
    print("^^^^^^ ESFP Personality: ^^^^^^\n ESFPs have an Extraverted, Observant, Feeling and Perceiving personality, and are commonly seen as Entertainers. Born to be in front of others and to capture the stage \n")
    print("^^^^^^ ENFP Personality: ^^^^^^\n ENFPs have an Extraverted, Intuitive, Feeling and Perceiving personality. This personality type is highly individualistic and Champions strive toward creating their own methods, looks, actions, habits, and ideas\n")
    print("^^^^^^ ESTP Personality: ^^^^^^\n ESTPs have an Extraverted, Sensing, Thinking, and Perceptive personality. ESTPs are governed by the need for social interaction, feelings and emotions, logical processes and reasoning, along with a need for freedom.\n ")
    print("^^^^^^ ESTJ Personality: ^^^^^^\n ESTJs are organized, honest, dedicated, dignified, traditional, and are great believers of doing what they believe is right and socially acceptable. \n")
    print("^^^^^^ ENTJ Personality: ^^^^^^\n ENTJs are natural born leaders among the 16 personality types and like being in charge. They live in a world of possibilities and they often see challenges and obstacles as great opportunities to push themselves. \n")
    print("^^^^^^ INTP Personality: ^^^^^^\n INTPs are well known for their brilliant theories and unrelenting logic, which makes sense since they are arguably the most logical minded of all the personality types.People of this personality type aren’t interested in practical, day-to-day activities and maintenance, but when they find an environment where their creative genius and potential can be expressed.\n")
    print("^^^^^^ ISFJ Personality: ^^^^^^\n ISFJs are philanthropists and they are always ready to give back and return generosity with even more generosity. The people and things they believe in will be upheld and supported with enthusiasm and unselfishness. ISFJs are warm and kind-hearted.\n ")
    print("^^^^^^ ENTP Personality: ^^^^^^\n Those with the ENTP personality are some of the rarest in the world, which is completely understandable. Although they are extroverts, they don’t enjoy small talk and may not thrive in many social situations \n")
    print("^^^^^^ ISFJ Personality: ^^^^^^\n they have difficulties connecting to other people at first, they become warm, approachable, and friendly eventually. They are fun to be with and very spontaneous, which makes them the perfect friend to tag along in whatever activity\n")
    print("*******************************************************************************************")
    print("\nDeveloped by Hammad Shaikh , Muhammad Uzair , Ahsan Ishtiaq\n")
    print("\nInspired by Myers Briggs Personality test")
    print("*******************************************************************************************")

def main():
    createQuestions()
    askQuestions()
    applyScores()
    shareScore()
    return None

main()

