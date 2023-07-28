import utils
from table import Table

def FerTransAttr(F : list, A : set) -> set:
    """
    This function calculates the transitive closure of a set of attributes using a list of dependency relations.

    Arguments :
        F (list) : The list of functional dependencies.
        A (set) : The set of attributs at start.

    Returns :
        set : The final set of the attributs transitive closure.
    """
    tmp = A.copy()
    A_changed = True
    while A_changed:
        A_changed = False
        for dep in F:
            key,value = dep
            if key.issubset(tmp):
                if not value.issubset(tmp):
                   tmp.update(value)
                   A_changed = True
    return tmp

def CouvMinDF(F : list) -> list:
    """
    This function calculates the minimum coverage of functional dependencies.

    Arguments :
        F (list) : The list of functional dependencies.

    Returns :
        set : A list of functional dependencies after minimum coverage.
    """
    C = utils.canonic_decomp(F)
    C = delete_useless_dependency(C)
    return reduct_lef_member(C)

def DecompoDFen3FN(F : list, A : set) -> None:
    """
    This function calculates the minimum coverage of 3FN functional dependencies.

    Arguments:
        F (list): A list of functional dependencies.
        A (set): A set of attributes.

    Returns:
        None
    """
    tables = []
    C = CouvMinDF(F)
    B = utils.isolate_atribute(F,A,C)
    for attr in B:
        tables.append(Table(attr,set(attr),set(attr),set()))
    for dep in C :
        to_add = True
        key,value = dep
        name = ""
        i = 0
        for atrr in key :
            name = name + atrr 
            if ( i < len(key)-1):
                name = name + "_"
            i = i +1
        for table in tables :
            my_keys = table.get_key().replace(" ",",").split(",")
            my_set_of_key = set()
            for my_key in my_keys :
                my_set_of_key.add(my_key)
            if my_set_of_key == key:
                for attr in value :
                    table.value = table.value + ", "+ attr 
                to_add = False
        if to_add:
            tables.append(Table(name,key,key.union(value),set()))
    return tables

def delete_useless_dependency(C : list) ->list:
    """
        This function permit to delete useless dependency.

        Arguments :
            C (list) : The minimum coverage.

        Returns :
            list : The minimum coverage without useless dependency.
    """
    C_copy = C.copy()
    for dep in C:
        key,value = dep
        tmp = C_copy.copy()
        tmp.remove(dep)
        if value.issubset(FerTransAttr(tmp,key)):
           C_copy = tmp
    return C_copy

def reduct_lef_member(C : list) -> list :
    """
        That function will check that all attributs of a key are useful, the useless attributs get removed.

        Arguments :
            C (list) : The minimum coverage without useless dependency.

        Returns :
            list : The minimum coverage without useless attributs.
    """
    C_copy =[]
    for dep in C :
        key,value = dep
        key_copy = key.copy()
        if len(key)>1:
            for attr in key:
                key_copy.discard(attr)
                if not set(attr).issubset(FerTransAttr(C,key_copy)) :
                    key_copy.add(attr)
        C_copy.append((key_copy,value))    
    return C_copy

