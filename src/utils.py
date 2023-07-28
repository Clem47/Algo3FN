import read

def canonic_decomp(F : list) -> list :
    """
        This function make a canonic decomposition of a list of functional dependencies.

        Arguments :
            F (list) : The list of functional dependencies.

        Returns :
            list : The list of functional dependencies after canonic decomposition.
    """
    F_canonic = []
    for key,values in F:
        if len(values) > 1 :
            for value in values:
                F_canonic.append((key, set({value})))
        else :
            F_canonic.append((key,values))
    return F_canonic

def isolate_atribute(F : list, A : set, C :list) -> set:
    """
        This function permit to isolate a list of attributs of the functional dependencies.

        Arguments :
            F (list) : The list of functional dependencies.
            A (set) : Set of isolated attributs.
            C (list) : List of attributs we want to isolate

        Returns :
            set : The set of attribute after isolating the attributs in C.
    """
    A = A.difference(read.get_all_attribut(C))
    B = read.get_all_attribut(F)
    B = B.difference(read.get_all_attribut(C))
    B = B.union(A)
    return B