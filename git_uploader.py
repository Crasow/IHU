import git
import datetime

PATH_OF_GIT_REPO = r'E:\IHU\.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = str(datetime.date.today())


def git_push():
    try:
        repo = git.Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')


git_push()
