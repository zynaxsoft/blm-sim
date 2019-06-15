GCD_dict = {}
OGCD_dict = {}

def gcd(cls):
    GCD_dict.update({cls(None).name: cls})
    return cls

def ogcd(cls):
    OGCD_dict.update({cls().name: cls})
    return cls
