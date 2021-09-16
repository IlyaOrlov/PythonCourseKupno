import contextlib


@contextlib.contextmanager
def set_obj_attrs(obj, attrs):
    bkp_attrs = {}
    try:
        for p_name, p_value in attrs.items():
            if hasattr(obj, p_name):
                bkp_attrs[p_name] = getattr(obj, p_name)
                setattr(obj, p_name, p_value)
        yield obj
    finally:
        for p_name, p_value in bkp_attrs.items():
            setattr(obj, p_name, p_value)


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

s = Student("Ivan", "Ivanov")
print(s.name)
print(s.surname)
print('==========')
with set_obj_attrs(s, {'name': 'James', 'surname': 'Bond'}):
    print(s.name)
    print(s.surname)
print('==========')
print(s.name)
print(s.surname)














