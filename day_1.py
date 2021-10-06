# DAY 1 NGULANG BELAJAR PYTHON 😭😭😢
from git import Repo
print("Hello " + input("siapa namamu ") + "!")
# Code diatas ini akan eksekusi input dulu nilai dari input yang kita masukkan akan menggantikan input("siapa namamu") => input yang kita masukkan


# exc
tes = input("Ngetes ?")
print(len(tes))
print(len(input("What is ur name ")))

# Exc 2
a = int(input("A:"))
b = int(input("B:"))
#a = 20
# b = 25
d = a
c = b
b = d
a = c
print(a)
print(b)


# Exc 3
print("Welcome to the band Name generator")
city_name = input("Whats the name of the city you grew up in ?")
print(city_name)
pet_name = input("Whats your pet name ?")
print(pet_name)
print(f"Your band name could be {city_name} {pet_name}")


# Code untuk push repo
# make sure .git folder is properly configured
PATH_OF_GIT_REPO = r'path\to\your\project\folder\.git'
COMMIT_MESSAGE = 'Belajar ngulang karena lupa 😭😭'


def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')


git_push()
