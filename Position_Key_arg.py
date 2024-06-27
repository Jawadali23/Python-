def hello(name, age=20):
    print("Hello "+ name+ ' you are '+str(age)+' years old')

# hello('Jawad',19)


def hello(*args, **kwargs):
    print(args)
    print(kwargs)

# hello("Jawad",'Ali',age=20)

lst=list(('Jawad','Ali'))
dic_value={'age':20}

hello(*lst,**dic_value)


# Position Arguments
hello('Jawad','Ali')

# Keyword Arguments
hello(age=20)