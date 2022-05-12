# pytest-from-ground-zero
This is a new pytest repo that covers the best practices

## Note on Virtualenv
Checkout how if you run `pip freeze | wc -l` there are many package you may not want
Try `which python`

1. `virtualenv ~/.venv`
2. `vim ~/.bashrc` and put in `source ~/.venv/bin/activate`
3.  Verify the right python `which python` and try `pip freeze | wc -l`