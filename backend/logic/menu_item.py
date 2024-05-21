
class MenuItem:

    _itemID: int
    _itemName: str
    _description: str
    _price: float
    
def __init__(self, itemID, itemName, description, price):
    self._itemID = itemID
    self._itemName = itemName
    self._description = description
    self._price = price