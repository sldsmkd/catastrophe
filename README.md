Developed using venv on Ubuntu 20.04 / WSL, which has Python3.8 as default

Install a venv, then use pip -r requirements.txt to get all the modules required

The microservice is dockerised, easiest way to build and start it is to run the build.sh script,
We're using 3.8 alpine as a base image; it will install all the modules in an underlying layer to speed things up

Most of the requirements have been met, with the following exceptions:

* No delete method on the service
* No table formatting on the CLI

It's also a bit raw because of the time limit. With some more time then unittests and less happy path assumption would be made. It's also not very efficient.

You may need to fiddle the path to the python executable in cli.py

CLI example:

```./cli.py users # get list of users
{'5a9ac18c7478810ea6c06381': 164, '58e007480aac31001185ecef': 31, '58f89c8d11658e00113ddd24': 1, '595579027b77520020799430': 1, '596ea14ed4d9720020401f7b': 1, '5c7da4bd70008708fb17c88f': 1, '5cd42b40cfdf230015bd7a44': 1, '5cd86adb1dc6d50015ec2f07': 1, '5d9d4a4468a764001553b387': 1, '5e10d6e51c78ab0015bc5b14': 1, '5e19d99e1fd6150015fa7353': 1, '5ebbf5cd8046d0001777601f': 1, '5ec4a7d60c796a00174d7b25': 1, '5ec93c89e11bba0017c67e18': 1, '5ea977d1cd53d20017d7d8b2': 1}
./cli.py user -i 58f89c8d11658e00113ddd24 # get facts for a user
['58f89cff11658e00113ddd26']
./cli.py fact -i 58f89cff11658e00113ddd26 # get a fact
Cats love to eat olives or for that matter anything preserved in brine.
./cli.py fact -i 58f89cff11658e00113ddd26 -o yaml # get a fact in yaml
Cats love to eat olives or for that matter anything preserved in brine.
...```