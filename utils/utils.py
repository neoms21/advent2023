def sort(arr:list, desc:bool):
     arr.sort(reverse=desc)
     
def has_special_char(text: str) -> bool:
    return any(c for c in text if not c.isalnum() and not c.isspace() and not c=='.')

def map_to_int(s:str):
     return int(s)