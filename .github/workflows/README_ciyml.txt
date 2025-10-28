The ci.yml file does the following: 

When someone pushes code or makes a Pull Request, GitHub runs this file and:

Starts a tiny virtual computer in the cloud.

Downloads your project onto that computer.

Installs Python and all the packages listed in requirements.txt.

Checks your code style. From the pyproject.toml file :

Is it nicely formatted?

Are there any small mistakes?

Runs the tests (pytest) to make sure the code actually works.

If everything passes ✅ → you get a green check mark on GitHub.
If something fails ❌ → GitHub shows you exactly what went wrong.