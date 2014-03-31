PLT PROJECT
Hi guys, welcome to the Repo! Don't worry, the name is temporary, just came up with something to use until we have a name for our language. If you're reading this, then you're able to pull from the remote on bitbucket which is great. If you want to make sure you're also able to push, add a few lines at the end of this file, commit and try to push. Please make sure you have configured your name and (preferably) email, as these are used to sign commits. If you are unsure if you have already set them, run "git config -l" and look for the values associated with the keys "user.name" and "user.email". To set these values run the following (don't leave John Doe though!):
	git config --global user.name "John Doe"
	git config --global user.email johndoe@example.com


SETUP SCRIPT
I have included a setup script (setup.sh) that adds a git alias that can be invoked by typing "git lg" which runs "git log" with some pretty formatting, including a branch history visualization. The script also sets the defualt push mode to simple, which means "git push" only pushes the current branch, instead of all branches setup to track a remote branch.

ANNOYING WINDOWS VS UNIX STUFF
Windows and Unix systems use different newline characters (actually Windows uses both a carriage-return and a linefeed character, while Unix only uses the linefeed character). The standard way to solve this is to use Unix style newlines in repos, and have all Windows users convert back and forth when commiting/checking out code. This is important for us because we have both Mac and Windows users. On Windows Git will do this automatically if you tell it to. Enable this by entering:
	git config --global core.autocrlf true

GOOD PRACTICE
1. Don't force push (especially to master), unless you have no other choice and know what you are doing. Not only does force push screw over anyone else tracking the branch you push to, it also breaks one of the best features of git, which is saving a history of everything we've ever written. If you force push to a branch, then all the code that anyone else has pushed since you last pulled will disappear.
2. Don't forget about branches. This may not be necessary, but if we find that we keep on stepping on each other toes by breaking things and creating merge conflicts, a very easy solution is to create a branch, work on a feature, and merge it back into master when it is done. This allows you to merge in any new features someone else may have added without requiring you to push half baked code onto everyone else.
3. Review before commiting. Please make sure you double check what you are commiting before you actually do so. This will help minimize annoying things like unresolved merge conflicts, build files and temporary files making it into the repo. "git status" will list all staged files, and "git diff" can be used to view changes in files. Note this is a much less painful experience if you use a GUI (see recomended software below).

RECOMENDED SOFTWARE (feel free to add to this list)
1. Sourcetree - Windows/OSX - http://www.sourcetreeapp.com/
	Far and away the best Git GUI I've ever seen. Slick, intuitive and aesthetically pleasing.
2. PyCharm - Windows/OSX/Linux - http://www.jetbrains.com/pycharm/download/index.html
	Jetbrains recently released a community version of their Python IDE. If you've used their Java IDE (IntelliJ) than this software will be very familiar to you. It has code completion comparable to that of Visual Studio, and compared to Eclipse plugins it is elegant, and easy to use.

Cool!
