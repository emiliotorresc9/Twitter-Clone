

from HashMaps import HashMap

def bmh(texto, patron):
    n = len(texto)
    m = len(patron)
    
    bad_char = HashMap()
    
    for char in texto:
        bad_char.put(char, m)
        
    for i in range(m-1):
        key = patron[i]
        value = m-1-i
        bad_char.put(key, value)
        
    i = 0
    while i <= n - m + 1:
        j = m - 1
        while j>=0 and texto[i+j] == patron[j]:
            j -= 1
            
        if j < 0:
            return i
        
        key = texto[i+j]
        
        try:
            i += bad_char.get(key)
        except:
            i += m
    return -1


texto = "abcxabxdabxabcdabcdabcy"
patron = "abcdabcy"

print(bmh(texto, patron))