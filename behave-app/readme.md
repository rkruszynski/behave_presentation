### Before you look at the code
This is not a 'production version' of e2e tests. There can be found some misteakes, wrong implementations and examples of bad patterns. Some of them are due to lack of time (this is just a presentation project!), some of them were created by purpose - to fix during presentation, for future training, etc. (try to run test that creates user with short username!).
Some of various problems:
- there is no checking if user is created correctly (in real e2e tests this often causes 'false positive' or just wrong results for test)
- docstrings are only in cfparse.py file
- usernames and passwords are repeated in feature files, this is a wrong idea. This can be fixed by creating new step to log as last created user/first created user (all informations needed we have already in context!)
- docstrings are only on cfparse_steps. 


### Final_features
Folder named 'Final_features' is not a typical part of behave project. Obviously you can create subfolders in 'Features' folder to keep some features together. But this folder was created just for PtaQ presentation. There are not only feature files, but  working state od steps.py, cfparse_steps.py and environment.py files. All of them have `_final` suffix.
