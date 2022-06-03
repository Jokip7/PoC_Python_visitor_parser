
input = {
    "op": "add",
    1: 10,
    2: {
        "op": "add",
        1: 20,
        2: "Temperature"
    }
}

input_hot = {
    "op": "less_than",
    1: 1000000,
    2: {
        "op": "add",
        1: 20,
        2: "Temperature"
    }
}

operations = {
    "add": lambda a, b: a + b,
    "greater_than": lambda a, b: a > b,
    "less_than": lambda a, b: a < b
}



def my_eval(node, env):
    if type(node) is dict:
        # Evaluate the arguments and combine them
        arg1 = my_eval(node[1], env)
        arg2 = my_eval(node[2], env)
        result = operations[node["op"]](arg1, arg2)
    elif type(node) in (int, ):
        # Return ints and strings as-is
        result = node
    if node == 'Temperature':
        result = env[node]
    print(f"{node} -> {result}")
    return result

def test_leaf_nodes():
    assert my_eval(10) == 10

def test_variable_lookup():
    assert my_eval("Temperature", env={"Temperature": 123}) == 123

def hot_function():
    my_env = {
        'Temperature': 100
    }
    my_eval(input_hot, my_env)

def test_tree():
    assert my_eval(
        input,
        env={
            'Temperature': 100
        }
    ) == 60

def test_plaintree():
    result = my_eval(
        {
            "op": "add",
            1: 10,
            2: {
                "op": "add",
                1: 20,
                2: 30
            }
        },
        env = {}
    )
    assert result == 60

if __name__ == '__main__':
    hot_function()
