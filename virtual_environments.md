# Python Virtual Environments

<br>

## Mac / Linux

#### Create an environment:
```
python3 -m venv <environment_name>
```

#### Activate an environment:
```
source <environment_name>/bin/activate
```

#### Deactivate an evironment:
```
deactivate
```

#### Example:
```
user_name@mac ~ % python3 -m venv demo_venv
user_name@mac ~ % 
user_name@mac ~ % 
user_name@mac ~ % source demo_venv/bin/activate
(demo_venv) user_name@mac ~ %
(demo_venv) user_name@mac ~ %
(demo_venv) user_name@mac ~ % deactivate
user_name@mac ~ % 
```

<br>

## Windows

#### Create an environment:
```
python -m venv <environment_name>
```

#### Activate an environment:
```
<environment_name>\Scripts\activate
```

#### Deactivate an evironment:
```
deactivate
```

#### Example:
```c
C:\Users\user_name\>python -m venv demo_venv
C:\Users\user_name\>
C:\Users\user_name\>
C:\Users\user_name\>demo_venv\Scripts\activate
(demo_venv) C:\Users\user_name\>
(demo_venv) C:\Users\user_name\>
(demo_venv) C:\Users\user_name\>deactivate
C:\Users\user_name\>
```
