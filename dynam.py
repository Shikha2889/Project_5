'''
Writing a module of functions that can be used to study the iteration of any function
For example, the module dynam  is going to contain a function
orbit(f,x0,n) that computes the first n terms of the orbit of x0 under function f
'''

def orbit(f, x0, n):

    """
    Compute the first `n` terms of the orbit of `x0` under
    the function `f`.
    Arguments:
    `f` - a function (should take one integer argument and return an integer
    )
    `x0` - a value of the type that `f` accepts as its argument
    `n` - the number of points to compute (a positive integer)

    `n` - the number of point to compute (a positive integer)
    Returns:
    A list of length `n` containing the values [ x0, f(x0), f(f(x0)), f(f(f(
    x0))), ... ]
    """
    list_1 = [x0]
    next_term = f(x0)
    list_1.append(next_term)
    print(n)
    num = 2;
    while num<n:
        next_term = f(next_term)
        list_1.append(next_term)
        num=num+1
    
    return list_1


def orbit_data(f, x0):
    """
    Repeatedly apply function `f` to initial value `x0` until some
    value is seen twice. Return dictionary of data about the observed
    behavior.
    Arguments:
    `f` - a function (should take one integer argument and return an integer
    )
    `x0` - a value of the type that `f` accepts as its argument
    Returns:
    Dictionary with the following keys (after each key is a description of
    the associated value):
    "initial": The part of the orbit up to, but not including, the first
    value that is ever repeated.
    "cycle": The part of the orbit between the first and second instances
    of
    the first value that appears twice, including the first but not
    the
    second. In other words, the entire orbit consits of the "initia
    l"
    part followed by the "cycle" repeating over and over again.
    Example: Suppose that applying f repeatedly to start value 11 gives this seq
    uence:
    11, 31, 12, 5, 6, 2, 8, 19, 17, 8, 19, 17, 8, 19, 17, 8, ...
    Then the return value would be:
    {
    "initial":[11, 31, 12, 5, 6, 2],
    "cycle": [8,19,17]
    }
    (If the orbit of `x0` doesn't end up in a cycle, it's ok for this function t
    o run forever
    trying to find one.)
    """
    initial= [x0]
    next_term = f(x0)
    initial.append(next_term)
    while True:
        next_term = f(next_term)
        if (next_term in initial[:-1]):
            repeated_term_index = initial.index(next_term)
            cycle = initial[repeated_term_index:]
            initial_original = initial[:repeated_term_index]
            break;
        else:
            initial.append(next_term)
    dict = {"initial":initial_original, "cycle":cycle}
    return dict



def eventual_period(f, x0):


    """
    Determine the length of the periodic cycle that `x0` ends up in.
    Arguments:
    `f` - a function (should take one integer argument and return an integer

    `f` - a function (should take one integer argument and return an integer
    )
    `x0` - a value of the type that `f` accepts as its argument
    Returns:
    The length of the periodic cycle that the orbit of `x0` ends up in.
    Example: Suppose that applying f repeatedly to start value 11 gives this seq
    uence:
    11, 31, 12, 5, 6, 2, 8, 19, 17, 8, 19, 17, 8, 19, 17, 8, ...
    Then the return value of eventual_period(f,11) would be 3, since the periodi
    c
    cycle contains the 3 values 8,19,17.
    (If the orbit of `x0` doesn't end up in a cycle, it's ok for this function t
    o run forever
    trying to find one.)
    """
    # PUT THE BODY OF eventual_period HERE AND DELETE THIS LINE
    dict = orbit_data(f,x0)
    cycle_value = dict.get("cycle")
    return len(cycle_value)

def steps_to_enter_cycle(f, x0):


    """
    Determine the length of the intial part of the orbit of `x0` under `f` befor
    e
    it enters a periodic cycle.
    Arguments:
    `f` - a function (should take one integer argument and return an integer
    )
    `x0` - a value of the type that `f` accepts as its argument
    Returns:
    The number of elements of the orbit of `f` before the first value that
    repeats.
    Example: Suppose that applying f repeatedly to start value 11 gives this seq
    uence:
    11, 31, 12, 5, 6, 2, 8, 19, 17, 8, 19, 17, 8, 19, 17, 8, ...
    Then the return value of steps_to_enter_cycle(f,11) would be 6, because ther
    e are 6
    values in the intial segment of the orbit (i.e. 11, 31, 12, 5, 6, 2) which a
    re followed by
    a periodic cycle.
    (If the orbit of `x0` doesn't end up in a cycle, it's ok for this function t
    o run forever
    trying to find one.)
    """
    dict = orbit_data(f,x0)
    initial_value = dict.get("initial")
    return len(initial_value)



def eventual_cycle(f, x0):


    """
    Return the periodic cycle that the orbit of x0 ends up in as a list.
    Arguments:
    `f` - a function (should take one integer argument and return an integer
    )
    `x0` - a value of the type that `f` accepts as its argument
    Returns:
    The earliest segment from the orbit of `x0` under `f` that repeats
    indefinitely thereafter, as a list.
    Example: Suppose that applying f repeatedly to start value 11 gives this seq
    uence:
    11, 31, 12, 5, 6, 2, 8, 19, 17, 8, 19, 17, 8, 19, 17, 8, ...
    Then eventual_cycle(f,x0) would return [8, 19, 17].
    (If the orbit of `x0` doesn't end up in a cycle, it's ok for this function t
    o run forever
    trying to find one.)
    """
    dict = orbit_data(f,x0)
    cycle_value = dict.get("cycle")
    return cycle_value


def smallest_first(L):


    """
    Rotates a list so that its smallest element appears first.
    Arguments:
    `L`: A list of integers, no two of them equal
    Returns:
    A list that is the result of moving the first element of `L` to the end,
    repeatedly, until the first element of `L` is the smallest element of the
    list.
    Example: smallest_first([46,41,28]) returns [28,46,41]
    Example: smallest_first([4,2,1]) returns [1,4,2]
    Example: smallest_first([9,8,7,6,5,4,3,2,1]) returns [1,9,8,7,6,5,4,3,2]
    """
    n=len(L)
    minimum = min(L)
    d = L.index(minimum)
    new_list = L[d:n]+L[0:d]
    return new_list




def find_cycles(f, start_vals):
    """
    Find all the periodic cycles of the function `f` that appear when you consider orbits of the elements of `start_vals`.
    Arguments:
    `f` - a function (should take one integer argument and return an integer)
    `start_vals` - a list of integers to use as starting values
    Returns:
    A list of lists, consisting of all the periodic cycles that are seen
    in the orbits of the start values from `start_vals`. Each cycle is
    given with its smallest entry appearing first, and any given cycle
    appears only once in the list.
    e.g. If `mwdp` is the mean with digit power function, then find_cycles(mwdp,
    [65,66,67])
    would return [ [28,46,41], [38,51] ] because both 65 and 67 end up in the [2
    8,46,41]
    cycle and 66 ends up in the [38,51] cycle.
    """
    # PUT THE BODY OF find_cycles HERE AND DELETE THIS LINE
    
    lst = []
    final_list = []
    final_list_sorted = []
    for x in start_vals:
        dict = orbit_data(f, x)
        lst = dict["cycle"]
        lst_A= sorted(lst)
        if lst_A not in final_list_sorted:
            final_list_sorted.append(lst_A)
            final_list.append(lst)

    return final_list 
   

