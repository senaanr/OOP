import random

class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices = choices
        self.answer = answer
        
    def check_answer(self,answer):
        if answer not in self.choices:
            raise ValueError("hatalı bilgi")
        return self.answer == answer
        
class Quiz:
    def __init__(self,questions):
        self.questions = random.sample(questions, len(questions))
        self.question_index = 0
        self.score = 0
        
    def getQuestion(self):
        return self.questions[self.question_index]
    
    def displayQuestion(self):
        question = self.getQuestion()
        
        print(f"Soru {self.question_index +1}: {question.text}")
        
        for q in question.choices:
            print("-"+q)
            
        answer = input("answer: ")
        if (question.check_answer(answer)):
            self.score += 1
            print("Congratulations, correct answer.")
        
        self.question_index +=1
        self.loadQuestion()
        
    def loadQuestion(self):
        if len(self.questions) == self.question_index:
            self.displayScore()
        else:
            self.displayProgress()
            self.displayQuestion() #aynı kod parçalarını tekrar çalıştırır
            
    def displayScore(self):
        print("Test Özetiniz".center(100))
        puan = 100/len(self.questions)
        toplamPuan = round(self.score * puan)
        print(f"Toplam {len(self.questions)} sorunun {self.score} tanesini bildiniz.")
        print("Kazandığınız Puan: ",toplamPuan)
    
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.question_index + 1
        
        print(f"Toplam {totalQuestion} sorunun {questionNumber}. sorusundasınız.".center(100,"*"))
        
q1 = Question("en iyi programlama dili hangisidir?", ["python","c#","java","dart"],"python")
q2 = Question("en popüler programlama dili hangisidir?", ["python","java","c#","dart"],"python")
q3 = Question("en çok kazandıran programlama dili hangisidir?", ["python","java","dart","c#"],"python")
q4 = Question("en sevilen programlama dili hangisidir?", ["python","java","dart","c#"],"python")
q5 = Question("en kolay programlama dili hangisidir?", ["python","java","dart","c#"],"python")

sorular = [q1,q2,q3,q4,q5]

#sonuc = q1.check_answer("python")
#print(sonuc)

quiz = Quiz(sorular)
#print(quiz.questions[0].text)
quiz.loadQuestion()

