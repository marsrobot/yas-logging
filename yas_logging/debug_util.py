import inspect
import traceback


class debug_util:
    @staticmethod
    def code_location_object(n: int) -> str:
        stack = list(inspect.stack())
        if n >= len(stack):
            level = stack[-1]
        else:
            level = stack[n]
        res = {
            'function': level.function,
            'filename': level.filename,
            'lineno': level.lineno
        }
        return res

    @staticmethod
    def code_location(n: int) -> str:
        stack = list(inspect.stack())
        if n >= len(stack):
            level = stack[-1]
        else:
            level = stack[n]
        return '{} {}:{}'.format(level.function, level.filename, level.lineno)


class stack_trace_test:
    @staticmethod
    def f():
        return g()

    @staticmethod
    def g():
        traceback.print_stack()


if __name__ == '__main__':
    stack_trace_test.f()
