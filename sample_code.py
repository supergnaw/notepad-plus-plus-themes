# This is a basic class
class BasicClass:
    _str_var: str = ""
    str_len: int = 0

    def __init__(self) -> None:
        hw_dict = {'Hello': "world"}
        print(hw_dict, 1234567890)

    # This is a property
    @property
    def str_var(self) -> str:
        return self._str_var

    # This is a variable setter
    @str_var.setter
    def str_var(self, str_val: str) -> None:
        self._str_var = str_val
        self.str_len = len(self.str_var)

    def str_append(self, str_input) -> int:
        self.str_var += str_input
        print(f"New string: {self.str_var}")
        return self.str_len


# The following code prints the following:
"""
{'Hello': 'world'} 1234567890
New string: new appendage
13
"""
BC = BasicClass()
print(BC.str_append("new appendage"))
