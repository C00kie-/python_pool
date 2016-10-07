import settings
import sys

#one day to do this !

def render():


    #if len(sys.argv) != 2:
    #    raise Exception("there aren't any file here")

    try :
        len(sys.argv) == 2
    except Exception as e_argv:
        print(e_argv)

    li = sys.argv[1].split('.')
    #print(li)
    if li[len(li)-1] != "template":
        raise Exception("not the right extension")


    wfile = sys.argv[1].replace('.template', '.html')
    #print(wfile)

    fd = open(wfile,'w')

    with open(sys.argv[1], 'r') as f:
        for line in f :
            fd.write(line.format(name = settings.name,
            surname = settings.surname, age=settings.age,
            work=settings.work))


if __name__ == '__main__':
    try :
        render()
    except Exception as e:
        print(e)





#enregistrer vers file.html
