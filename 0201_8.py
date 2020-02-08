#개인 성적 입력(파이썬,C, 자바)
def inputScore(name, *score) :
    return score
def avgSubject() :
    pass
def avgStudent(line) :
    pass

def main() :
    score = []
    for i in range(5) :
        name = input('성함을 입력하세요: ')
        score[i] = input('파이썬, C, 자바 점수를 입력하세요: ')
        inputScore(name,score[i])
    print(score)
