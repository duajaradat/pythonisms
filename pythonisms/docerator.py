from functools import wraps

def main(func):
    """
    Decorator to add docstring to a function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):

        origin=func(*args, **kwargs)
        return f"Hello {origin}"
    return wrapper
@main
def doc(text):
    """
    regular function that takes a text as string and returns it back 
    """
    return text