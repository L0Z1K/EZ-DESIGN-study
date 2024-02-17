# Week1 - Factory, Builder

Factory, Builder 패턴에 대해 공부합니다.

## Assignment

CPU, RAM, ROM으로 구성된 Computer를 구현합니다.

- CPU는 추상클래스입니다.
    - 일반적인 Factory 패턴으로 구현해 주세요.
    - CPUFactory에서 SingleCoreCPU, DoubleCoreCPU를 생성할 수 있습니다.
- RAM, ROM은 추상 클래스 Memory를 상속받습니다.
    - 각각은 Factory를 가지며, 각각의 Factory도 공통의 추상 클래스를 상속받게 Abstract factory 패턴으로 구현해 주세요.
- Computer는 Builder 패턴으로 구현해 주세요.
    - bootstrap을 하고 나면 아래 키를 가지는 dict 타입의 state를 반환합니다.
        - cpu processed
            - cpu가 process한 data list
        - ram(rom) data
            - ram(rom)의 현재 data

### Results

```bash
❯ python -m pytest tests/
================================== test session starts ===================================
platform linux -- Python 3.9.13, pytest-7.1.2, pluggy-1.0.0
rootdir: /home/baek/Study/EZ-DESIGN-study/week1/tests, configfile: pytest.ini
plugins: anyio-3.5.0
collected 9 items                                                                        

tests/test_computer.py .........                                                   [100%]

=================================== 9 passed in 0.02s ====================================
```

## What I learned

새롭게 배운 개념들을 정리해봅니다.

### Factory Method

궁극적인 목표는 객체 생성과 객체 사용을 분리하는 것이다. 객체 생성을 위해 Factory Method를 사용하면, main 함수에서 직접 객체를 생성하지 않고 Factory Method를 호출하여 생성하게 된다.

```python
def f(type: str):
    cpu: CPU
    if type == "single":
        cpu = SingleCoreCPU()
    elif type == "double":
        cpu = DoubleCoreCPU()
    else:
        raise ValueError("Invalid type")
    
    # ...cpu 사용...
```

위와 같은 코드에서 cpu 객체를 생성하는 부분을 Factory Method로 분리하면 아래와 같다.

```python
def f(type: str):
    cpu: CPU = CPUFactory.create(type)
    # ...cpu 사용...
```

Abstract Factory는 Factory Method를 한 단계 보다 더 높게 추상화한 것이라고 보면 된다. 한 Factory에서 CPU를 만들고, 다른 Factory에서 GPU를 만드는 식이면, 이들을 모두 묶어서 전자제품 만드는 Abstract Factory로 추상화할 수 있다. (근데 Abstract Factory까지 필요한 경우가 있을까.. 싶다.)

## References 

### Factory Method, Abstract Factory

- [refactoring.guru - Factory Method Pattern](https://refactoring.guru/ko/design-patterns/factory-method)
- [Youtube - The Factory Pattern in Python // Separate Creation From Use](https://www.youtube.com/watch?v=s_4ZrtQs8Do)
- [Blog - 💠 팩토리 메서드(Factory Method) 패턴 - 완벽 마스터하기](https://inpa.tistory.com/entry/GOF-%F0%9F%92%A0-%ED%8C%A9%ED%86%A0%EB%A6%AC-%EB%A9%94%EC%84%9C%EB%93%9CFactory-Method-%ED%8C%A8%ED%84%B4-%EC%A0%9C%EB%8C%80%EB%A1%9C-%EB%B0%B0%EC%9B%8C%EB%B3%B4%EC%9E%90)