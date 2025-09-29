# cs-117-lab3
Registers are limited in number and must be explicitly managed by the programmer. Each register has a specific purpose and you need to track what's stored where. Instructions in Assembly are very low level and specific-each instruction performs one simple operation. Even simple tasks require multiple instructions.
Assembly requires you to manage every detail manually, you work directly with hardware. In contrast, Python handles memory management, type conversions and complex operations automatically.
Python provides high level abstractions that handle complex operations automatically. Python's syntax is readable and concise-one line of Python can replace dozens or hundreds of Assembly instructions.
All three features provide crucial abstraction.
Variables let you store data without worrying about specific memory address or registers.
Functions provide reusable codeblocks
Loops abstract away the manual jump instructions and counter management required in Assembly.
Notes of compariosn table:
(x=5)Assembly uses CPU registers and Python uses named variables with automatic memory management.
(print())Assembly requires system interrupt call, Python provide a simple built in function.
(x+y)Assembly need explicit register operations, Python poerforms operations directly on variables.
