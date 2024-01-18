# Create a vector V of dimension d.
# 1. Compute the norm; norm (V) = root(summation i=1 to d (V[i]^2))
# 2. Add it with another vector of same length.
# 3. Multiply with a scaler of value k.
# 4. Dot product with another vector w.
# 5. Inner product with vector v.
#  If there is any error point it out.

# V = 2i + 4j -3k       W = 4i - 3j + k

def coefficients(vector):

    def index_fn(eqn, x, a=0, b=0):
        index = 0
        if a != 0 or b != 0:
            for i in eqn[a:b]:
                if i == x:
                    return index
                index += 1
            return -1
        else:
            for i in eqn:
                if i == x:
                    return index
                index += 1
            return -1
    
    def coeff_each(eqn):
        coeff = ''
        for i in eqn:
            coeff = coeff + i
        coeff = int(coeff)
        return coeff

    def sign_check(eqn):
        for i in eqn:
            if i == '+':
                return 1
            elif i == '-':
                return -1
        return 1 


    index_equality = index_fn(vector, '=')
    if index_equality != -1:
        new_vector = vector[index_equality:]
    else:
        new_vector = vector

    index_i = index_fn(new_vector, 'i')
    if index_i == -1:
        coff_i = 0
    else:
        index_sign = index_fn(new_vector, '+', 0, index_i)
        if index_sign == -1:
            index_sign = index_fn(new_vector, '-', 0, index_i)
        coff_sign = sign_check(new_vector[:index_i])
        if index_sign != -1:
            new_vector = new_vector[index_sign+1:]
            index_i = index_i-(index_sign+1)
            coff_i = coeff_each(new_vector[:index_i]) * coff_sign
        else:
            coff_i = coeff_each(new_vector[:index_i]) * coff_sign
        new_vector = new_vector[index_i+1:]
    
    index_j = index_fn(new_vector, 'j')
    if index_j == -1:
        coff_j = 0
    else:
        index_sign = index_fn(new_vector, '+', 0, index_j)
        if index_sign == -1:
            index_sign = index_fn(new_vector, '-', 0, index_j)
        coff_sign = sign_check(new_vector[:index_j])
        if index_sign != -1:
            new_vector = new_vector[index_sign+1:]
            index_j = index_j-(index_sign+1)
            coff_j = coeff_each(new_vector[:index_j]) * coff_sign
        else:
            coff_j = coeff_each(new_vector[:index_j]) * coff_sign
        new_vector = new_vector[index_j+1:]
    
    index_k = index_fn(new_vector, 'k')
    if index_k == -1:
        coff_k = 0
    else:
        index_sign = index_fn(new_vector, '+', 0, index_k)
        if index_sign == -1:
            index_sign = index_fn(new_vector, '-', 0, index_k)
        coff_sign = sign_check(new_vector[:index_k])
        if index_sign != -1:
            new_vector = new_vector[index_sign+1:]
            index_k = index_k-(index_sign+1)
            coff_k = coeff_each(new_vector[:index_k]) * coff_sign
        else:
            coff_k = coeff_each(new_vector[:index_k]) * coff_sign
    
    return [coff_i, coff_j, coff_k]

    
eq1 = input("Enter 1st vector (V): ")
eq2 = input("Enter 2nd vector (W): ")

coefficients_v = coefficients(eq1)
coefficients_w = coefficients(eq2)

mag_vector1 = (coefficients_v[0] ** 2 + coefficients_v[1] ** 2 + coefficients_v[2] ** 2)**0.5
print("Norm of vector (V): ", mag_vector1)

add_vector = [coefficients_v[i] + coefficients_w[i] for i in range(3)]
print("Adding vector (V) with vector (V): ", add_vector)

inp_scaler = int(input("Enter a scaler number: "))
mult_scaler = [inp_scaler * coefficients_v[i] for i in range(3)]
print("Multipying vector (V) with the scalar: ",mult_scaler)

v_dot_w = 0
for i in range(3):
    v_dot_w = v_dot_w + (coefficients_v[i]*coefficients_w[i])
print("Vector (V) dot Vector (W): ", v_dot_w)
