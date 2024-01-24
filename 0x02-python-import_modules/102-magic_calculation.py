import dis

def magic_calculation(a, b):
    add, sub = None, None

    # Load add and sub functions from magic_calculation_102 module
    for instruction in dis.get_instructions(magic_calculation_102):
        if instruction.opname == 'LOAD_GLOBAL':
            if instruction.argval == 'add':
                add = locals()[instruction.argval]
            elif instruction.argval == 'sub':
                sub = locals()[instruction.argval]
            if add and sub:
                break

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)

# Test the function
result = magic_calculation(3, 5)
print(result)
