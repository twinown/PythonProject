def same_case(a, b):
    return -1 if not (str(a).isalpha() and str(b).isalpha()) \
        else 1 if str(a).isupper() and (str(b).isupper()) else 0
   # return a.isupper() == b.isupper() if a.isalpha() and b.isalpha() else -1