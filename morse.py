from lark import Lark
import sys

morse_code = """
start: command+

?command: primitive | loop

primitive: ",-" -> gt
            | ",." -> lt
            | "." -> inc
            | "-" -> dec
            | ",_" -> out
            | "_," -> inp

loop: "__." command+ ".__"
"""
parser = Lark(morse_code)

parse_tree = parser.parse(input())

env = {
    'dp': 0,
    'mem': bytearray([0]*30000)
}

def run_tree(t, env):
    if t.data == 'start':
        for child in t.children:
            run_tree(child, env)
    elif t.data == 'gt':
        env['dp'] += 1
    elif t.data == 'lt':
        env['dp'] -= 1
    elif t.data == 'inc':
        env['mem'][env['dp']] += 1
    elif t.data == 'dec':
        env['mem'][env['dp']] -= 1
    elif t.data == 'out':
        print(chr(env['mem'][env['dp']]), end='')
    elif t.data == 'inp':
        env['mem'][env['dp']] = int(sys.stdin.read(3))
    elif t.data == 'loop':
        while env['mem'][env['dp']] != 0:
            for child in t.children:
                run_tree(child, env)
    else:
        raise SyntaxError("unknown tree")
        

run_tree(parse_tree, env) 
