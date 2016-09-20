apt install python3-setuptools python3-pip python-pygments python3-matplotlib python3-scipy python3-numpy python3-networkx python3-pandas ipython3 python-pip python-setuptools unp htop
pip3 install jupyter sympy seaborn

jupyter notebook --generate-config

# In [1]: from notebook.auth import passwd
# In [2]: passwd()
# Enter password:
# Verify password:
# Out[2]: 'sha1:67c9e60bb8b6:9ffede0825894254b2e042ea597d771089e11aed'

# In ~/.jupyter/jupyter_notebook_config.py
# set:
# c.NotebookApp.password = u'sha1:5ddb45631bef:42970928cd1e3e00ff2417d6ffb371f767ba611a'
# c.NotebookApp.port = 9999