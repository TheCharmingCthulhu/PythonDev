def Test(**kwargs):
    print kwargs


Test(attrs={'method':"POST", 'name':"Test"}, content="Hello World!")
