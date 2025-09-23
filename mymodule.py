def my_add(a,b):
    return a+b

def my_sub(a,b):
    return a-b



class Character:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f'저는 {self.name}입니다.')
    
print(f'mymodule 안에서의 __name__:{__name__}')

if __name__ == "__main__":  ##__name__은 파이선에서 정해둔 변수이름.
    print(my_add(3,4))
    print(my_sub(6,5))
    wizard = Character('법사')
    wizard.speak()
