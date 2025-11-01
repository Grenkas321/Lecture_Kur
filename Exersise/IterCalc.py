def itercalc():
    stack = []
    cmd = yield None
    while True:
        if cmd == '?':
            if stack:
                result = stack[-1]
                cmd = yield result
            else:
                print("Insufficient stack")
                cmd = yield None
        else:
            try:
                if cmd in ['+', '-', '*', '/']:
                    if len(stack) < 2:
                        print("Insufficient stack")
                    else:
                        b = stack.pop()
                        a = stack.pop()
                        if cmd == '+':
                            stack.append(a + b)
                        elif cmd == '-':
                            stack.append(a - b)
                        elif cmd == '*':
                            stack.append(a * b)
                        elif cmd == '/':
                            if b == 0:
                                print("Zero division")
                                stack.append(a)
                                stack.append(b)
                            else:
                                stack.append(a // b)
                else:
                    stack.append(int(cmd))
            except ValueError:
                print("Unknown command")
            cmd = yield None
