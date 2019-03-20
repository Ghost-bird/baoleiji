import sys,os

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'baoleiji.settings')
    import django
    django.setup()
    from backend import main
    interactive_obj = main.ArgHandler(sys.argv)
    interactive_obj.call()

