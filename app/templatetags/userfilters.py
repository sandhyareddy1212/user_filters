from django import template
register = template.Library()


def Swap(data):
    return data.swapcase()
register.filter('Swap',Swap)



def remove(data,arg):
    return data.replace(arg,'')
register.filter('remove',remove)


def count(data,sub):
    c=0
    for i in range(len(data)):
        if data[i:i+len(sub):]==sub:
            c+=1
    return c        
register.filter('count',count)