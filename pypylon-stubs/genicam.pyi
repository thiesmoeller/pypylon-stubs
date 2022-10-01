from typing import List

class INode:
    pass

class IValue(INode):
    pass

class INodeMap:
    def GetNodes(self) -> List[INode]: ...
    def GetNode(self, value: str) -> IValue: ...

class IFloat(IValue):
    def SetValue(self, Value: float) -> None: ...

    Value: float
    Min: float
    Max: float

class IInteger(IValue):
    def SetValue(self, Value: int) -> None: ...

    Value: int
    Min: int
    Max: int
    Inc: int

class IEnumeration(IValue):
    def SetValue(self, Value: int | str) -> None: ...

    Symbolics: List[str]
    Value: str

class IBoolean(IValue):
    def SetValue(self, Value: bool) -> None: ...

    Value: bool

class ICommand(IValue):
    def Execute(self) -> None: ...

class IString(IValue):
    def SetValue(self, Value: str) -> None: ...

    Value: str
    MaxLength: int
    Length: int
