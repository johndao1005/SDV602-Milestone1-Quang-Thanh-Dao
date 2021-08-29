class Test(object):
    def __init__(self,id,marks):
             self.__testID = id
             self.__maxMarks = marks
             self.__questions = []
             self.__numberofQuestions = 0
             self.__level = ""
             self.__dateSet = ""

    def setQuestion(self,question):
             self.__numberofQuestions += 1
             self.__questions.append(question)

class Question(object):
    def __init__(self,id,text,answer,marks,topic):
                  self.__questionID = id
                  self.__questionText = text
                  self.__answer = answer
                  self.__marks = marks
                  self.__topic = topic

if __name__ == "__main__":
       test = Test(1,100)
       test.setQuestion(Question(1,"Text","Answer",50,"Topic"))