def func_externa():
    var_externa = "Eu sou externa"
    
    def func_interna():
        nonlocal var_externa
        
        var_externa = "Eu fui modificada pela função interna"
        print(var_externa)
    
    func_interna()
    
    print(var_externa)

func_externa()