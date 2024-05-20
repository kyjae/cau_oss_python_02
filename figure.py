"""클래스 Line과 함수 area_square,area_circle,area_regular_triangle을 가진 모듈입니다."""

import math #math 모듈의 pi와 sqrt를 사용하기 위해 모듈 불러오기

class Line:
    """외부에서 접근 불가능한 필드 __length(기본값 1)를 가진 클래스입니다.
    """

    def __init__(self,length=1):
        """객체가 생성될 때 입력받은 값으로 __length를 설정하는 메소드입니다. 값이 주어지지 않았을 경우 1로 설정됩니다.
        Args:
            length(int/float): __length에 저장될 값을 가진 변수입니다.
        Returns:
            아무 값도 리턴하지 않습니다.
        """
        if((type(length)==int or type(length)==float) and length>0):
            self.__length=length
        else:
            self.__length=1

    def set_length(self,length):
        """입력받은 값으로 __length를 설정하는 메소드입니다.
        Args:
            length(int/float): __length에 저장될 값을 가진 변수입니다.
        Returns:
            아무 값도 리턴하지 않습니다.
        """
        if((type(length)==int or type(length)==float) and length>0):
            self.__length=length

    def get_length(self):
        """Line 클래스의 필드인 __length의 값을 반환하는 메소드입니다.
        Returns:
            클래스의 필드인 __length를 반환합니다.
        """
        return self.__length
    
def area_square(line):
    """ 길이를 입력받아 정사각형의 넓이를 구하는 함수입니다.
    Args: 
        line(Line): 변의 길이를 지닌 클래스 객체입니다.
    Returns: 
        int/float: 정사각형의 넓이를 반환합니다. """
    if type(line) != Line:
        return 0
    return line.get_length()**2

def area_circle(line):
    """ 길이를 입력받아 원의 넓이를 구하는 함수입니다.
    Args: 
        line(Line): 반지름의 길이를 지닌 클래스 객체입니다.
    Returns: 
        int/float: 원의 넓이를 반환합니다. """
    if type(line) != Line:
        return 0
    return line.get_length()**2*math.pi

def area_regular_triangle(line):
    """ 길이를 입력받아 정삼각형의 넓이를 구하는 함수입니다.
    Args: 
        line(Line): 변의 길이를 지닌 클래스 객체입니다.
    Returns: 
        int/float: 정삼각형의 넓이를 반환합니다. """
    if type(line) != Line:
        return 0
    return line.get_length()**2*math.sqrt(3)/4