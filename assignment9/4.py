def my_function():
    x = 1
    y = 2
    z = "hello"
    local_variable_count = len(locals())
    print(f"{local_variable_count} local variables: {locals()}")

my_function()

