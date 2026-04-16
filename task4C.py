def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         # 'this', 'is', 'confusing', 'code.', 'AVOID' 'SUCH.'
         # 'this', 'is', 'confusing', 'code.', 'AVOID' 'SUCH.'
         # .append makes direct changes to the original list
print()