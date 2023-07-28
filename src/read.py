def read_file(path_file :str) -> list:
    """
    That function create a list that will contain functional dependencies from a file that respect DOT language.

    Arguments :
        path_file (str) : The path of the file.

    Returns :
        dico : the list of functional dependencies.
    """
    dico = []
    file = open(path_file, "r")
    for l in file.readlines() :
        dico = make_split(l, dico)  
    file.close()
    return dico 

def make_split(l : str, dico : list)-> list:
    """
    This function translate a line of a file that respect the DOT language into a tuple that will be add to the list.

    Arguments :
        l (str) : A line from a file.
        dico (list) : The list of functional dependencies.

    Returns :
        list : The list of functional dependencies with a new tuple.
    """
    keys,values = set(),set()
    key,value = format (l)
    for k in key.split(',') :
        keys.add(k)
    for v in value.split(',') :
        values.add(v) 
    dico.append((keys, values))
    
    return dico

def format ( l : str) -> tuple:
    """
    This function translate a line that respect DOT language into a tuple (key + value).

    Arguments :
        l (str) : A line.

    Returns :
        tuple : The tuple.
    """
    key,value = l.split("->")
    key = key.replace(' ','')
    value = value.replace(' ','')
    key = key.replace('\n','')
    value = value.replace('\n','')
    return key,value

def print_file(pathFile :str) -> None:
    """
    That function permit to read a file.

    Arguments :
        pathFile (str) : The file.

    Returns :
        None.
    """
    fichier = open(pathFile, "r")
    print(fichier.read())
    fichier.close()


def get_all_attribut(F :str) -> set:
    """
    That function permit to get into a set all attributes of a file respecting the DOT language.

    Arguments :
        F (str) : The file.

    Returns :
        set : The set that contains all attributes.
    """
    all_attribut = set()
    for dep in F:
        key,value = dep
        all_attribut = key.difference(all_attribut).union(all_attribut)
        all_attribut = value.difference(all_attribut).union(all_attribut)
    return all_attribut
