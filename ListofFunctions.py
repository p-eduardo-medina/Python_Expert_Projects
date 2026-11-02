def make_fun_lst(n1, n2):
    fun_lst = []
    for i in range(n1, n2):
        if i%2 == 1:
            def times_function(x, coeficient=i):
                return x * coeficient
            fun_lst.append(times_function)
        else:
            def add_function(x, constant=i):
                return x + constant
            fun_lst.append(add_function)
    return fun_lst

def make_fun_lst2(n1, n2):
	        return [(lambda x, k=k: x + k) if k%2 == 0 else (lambda x, k=k: x * k) for k in range(n1, n2)] #x debe proporcionarse como argumento a la función lambda, 
#k se pasa como argumento predeterminado para evitar el cierre de la variable k en el bucle.

fun_list = make_fun_lst2(5, 10)
print((fun_list[0](4), fun_list[1](14), fun_list[2](2))) 
