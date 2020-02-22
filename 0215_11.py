#플레이어 레벨을 표현하는 
playerlevel
run
jump
turn
showlevel
go 하면 run, jump, turn 함께 실행


beginnerlevel
run
jump
turn
showlevel

advancedlevel
run
jump
turn
showlevel

superlevel
run
jump
turn
showlevel

player
level 변수임. 
--init__()
upgradelevel()
play() #-> go 함수 호철하도록


플레이어 레벨을 표현하는 클래스를 상속관계로 구현해보자
1. 초급자레벨: run(o), jump(x), turn(x)
2. 중급자레벨: run(o), jump(o), turn(x)
3. 고급자레벨: run(o), jump(o), turn(o)