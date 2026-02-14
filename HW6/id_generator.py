def id_generator(n):
    if n<=0:
        raise ValueError('The argument must be greater than 0.')
    for i in range(n):
        yield int(i)