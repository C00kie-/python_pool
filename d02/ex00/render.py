import settings
import sys

#one day to do this !

def render():


    if len(sys.argv) != 2:
        raise Exception("there aren't any file here")

    li = sys.argv[1].split('.')
    print(li)
    if li[len(li)-1] != "template":
        raise Exception("not the right extension")

    with open(sys.argv[1], 'r') as f:
        for line in f :
            print(line.format(name = settings.name))


if __name__ == '__main__':
    try :
        render()
    except Exception as e:
        print(e)





#enregistrer vers file.html
