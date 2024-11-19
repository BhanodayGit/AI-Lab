class UnificationError(Exception):
    pass

def is_variable(term):
    return isinstance(term, str) and term.startswith('?')

def unify(x, y, theta=None):
    if theta is None:
        theta = {}
    if x == y:
        return theta
    elif is_variable(x):
        return unify_variable(x, y, theta)
    elif is_variable(y):
        return unify_variable(y, x, theta)
    elif isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        for xi, yi in zip(x, y):
            theta = unify(xi, yi, theta)
        return theta
    elif isinstance(x, str) and isinstance(y, str):
        raise UnificationError(f"Cannot unify distinct constants: {x} and {y}")
    else:
        raise UnificationError(f"Cannot unify {x} and {y}")

def unify_variable(var, term, theta):
    
    if var in theta:
        return unify(theta[var], term, theta)
    elif term in theta:
        return unify(var, theta[term], theta)
    elif occurs_check(var, term, theta):
        raise UnificationError(f"Occurs check failed: {var} in {term}")
    else:
        theta[var] = term
        return theta

def occurs_check(var, term, theta):
    """
    Check if a variable occurs in a term under the current substitution theta.
    
    :param var: Variable to check
    :param term: Term to check within
    :param theta: Current substitution dictionary
    :return: True if occurs check fails, False otherwise
    """
    if var == term:
        return True
    elif is_variable(term) and term in theta:
        return occurs_check(var, theta[term], theta)
    elif isinstance(term, list):
        return any(occurs_check(var, t, theta) for t in term)
    else:
        return False

# Input Functionality
def get_input():
    try:
        term1 = eval(input("Enter the first term : "))
        term2 = eval(input("Enter the second term : "))
        return term1, term2
    except Exception as e:
        print("Invalid input format. Please use proper list notation.")
        raise e

# Main Program
if __name__ == "__main__":
    try:
        term1, term2 = get_input()
        result = unify(term1, term2)
        print("Unification successful! Substitution:", result)
    except UnificationError as e:
        print("Unification failed:", e)
    except Exception as e:
        print("Error:", e)
