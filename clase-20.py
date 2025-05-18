"""Manejo de Excepciones y Errores en Python"""
# Excepciones
# Excepciones son errores que ocurren durante la ejecución de un programa.
# En Python, las excepciones son objetos que representan un error o una condición excepcional.  
# Cuando ocurre una excepción, Python genera un objeto de excepción y lo lanza (raise).
# Las excepciones pueden ser manejadas utilizando bloques try y except. 
# El bloque try contiene el código que puede generar una excepción, y el bloque except contiene el código que maneja la excepción.
# Ejemplo de manejo de excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero no permitida.")
# En este ejemplo, se intenta dividir 10 entre 0, lo que genera una excepción ZeroDivisionError.
# El bloque except captura la excepción y muestra un mensaje de error.
# También se pueden manejar múltiples excepciones utilizando múltiples bloques except.
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero no permitida.")
except Exception as e:
    print("Error:", e) 

# Tipos de Excepciones
# En Python, existen diferentes tipos de excepciones que se pueden manejar.

def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

# Imprimir la jerarquía comenzando desde la clase base Exception
print_exception_hierarchy(Exception)
"""
Exception
    ArithmeticError
        FloatingPointError
        OverflowError
        ZeroDivisionError
    AssertionError
    AttributeError
    BufferError
    EOFError
    ImportError
        ModuleNotFoundError
        ZipImportError
    LookupError
        IndexError
        KeyError
        CodecRegistryError
    MemoryError
    NameError
        UnboundLocalError
    OSError
        BlockingIOError
        ChildProcessError
        ConnectionError
            BrokenPipeError
            ConnectionAbortedError
            ConnectionRefusedError
            ConnectionResetError
        FileExistsError
        FileNotFoundError
        InterruptedError
        IsADirectoryError
        NotADirectoryError
        PermissionError
        ProcessLookupError
        TimeoutError
        UnsupportedOperation
    ReferenceError
    RuntimeError
        NotImplementedError
        PythonFinalizationError
        RecursionError
        _DeadlockError
    StopAsyncIteration
    StopIteration
    SyntaxError
        IndentationError
            TabError
        _IncompleteInputError
    SystemError
        CodecRegistryError
    TypeError
    ValueError
        UnicodeError
            UnicodeDecodeError
            UnicodeEncodeError
            UnicodeTranslateError
        NotShareableError
        UnsupportedOperation
    Warning
        BytesWarning
        DeprecationWarning
        EncodingWarning
        FutureWarning
        ImportWarning
        PendingDeprecationWarning
        ResourceWarning
        RuntimeWarning
        SyntaxWarning
        UnicodeWarning
        UserWarning
    InterpreterError
        InterpreterNotFoundError
    ExceptionGroup
"""
# La jerarquía de excepciones en Python es una estructura de clases que representa diferentes tipos de errores y excepciones que pueden ocurrir durante la ejecución de un programa.
# Cada clase de excepción hereda de una clase base, lo que permite agrupar excepciones relacionadas y manejarlas de manera más eficiente.
