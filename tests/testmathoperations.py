from src.mathoperations import add,sub

def test_add():
    assert add(3,5)==8
    assert add(3,-3)==0


def test_sub():
    assert sub(3,5)==-2
    assert sub(3,-3)==6