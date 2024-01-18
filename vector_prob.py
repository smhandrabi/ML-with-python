# Create a vector V of dimension d.
# 1. Compute the norm; norm (V) = root(summation i=1 to d (V[i]^2))
# 2. Add it with another vector of same length.
# 3. Multiply with a scaler of value k.
# 4. Dot product with another vector w.
# 5. Inner product with vector v.
#  If there is any error point it out.

# V = 2i + 4j -3k       W = 4i - 3j + k

def coefficients(vector):

    def index_fn(eqn, x, a, b):
        index = 0
        for i in eqn[a:b]:
            if i == x:
                return index
            index += 1
        return -1
    
    def coeff_each(eqn, a, b):
        coeff = ''
        for i in eqn[a:b]:
            coeff = coeff + i
        coeff = int(coeff)
        return coeff

    def sign_check(eqn, a, b):
        for i in eqn[a:b]:
            if i == '+':
                return 1
            elif i == '-':
                return -1
        return 1 


    index_equality = index_fn(vector, '=', '', '')
    if index_equality != -1:
        new_vector = vector[index_equality:]
    index_i = index_fn(new_vector, 'i', '', '')
    index_j = index_fn(new_vector, 'j', '', '')
    index_k = index_fn(new_vector, 'k', '', '')

    if index_i == -1:
        coff_i = 0
    else:
        index_sign = index_fn(new_vector, '+' or '-', 0, index_i)
        coff_sign = sign_check(new_vector[:index_i])
        if index_sign != -1:
            new_vector = new_vector[index_sign:]
        coff_i = coeff_each(new_vector[:index_i]) * coff_sign
        new_vector = new_vector[index_i+1:]
    
    if index_j == -1:
        coff_j = 0
    else:
        index_sign = index_fn(new_vector, '+' or '-', 0, index_j)
        coff_sign = sign_check(new_vector[:index_j])
        if index_sign != -1:
            new_vector = new_vector[index_sign:]
        coff_j = coeff_each(new_vector[:index_j]) * coff_sign
        new_vector = new_vector[index_j+1:]
    
    if index_k == -1:
        coff_k = 0
    else:
        index_sign = index_fn(new_vector, '+' or '-', 0, index_k)
        coff_sign = sign_check(new_vector[:index_k])
        if index_sign != -1:
            new_vector = new_vector[index_sign:]
        coff_k = coeff_each(new_vector[:index_k]) * coff_sign
    
    return coff_i, coff_j, coff_k

    
eq1 = input("Enter 1st vector (V): ")
eq2 = input("Enter 2nd vector (W): ")

coefficients_v = coefficients(eq1)
coefficients_w = coefficients(eq2)

print(coefficients_v, coefficients_w)
