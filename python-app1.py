name, surname, age, job = "Tugcan", "Yildiz", 39, "DevOps Engeneer"

# 6- Yukarida verilen değişkenler ile ekrana aşağidaki ifadeyi yazdirin.
#   "Benim adim Tugcan Yildiz, Yaşim 39 ve mesleğim mühendis."
# f.string metodu kullanarak
print(f"Benim adim {name} {surname}, Yaşim {age} ve mesleğim {job}.")
#ya da .format işlemi uygulayarak
print("Benim adim {} {}, Yaşim {} ve mesleğim {}".format(name, surname, age, job))
#ya da string birleştirme işlemi yaparsak:
print("Benim adim " + name + " " + surname + " Yaşim" + " " + str(age) + " ve mesleğim"+ " " + job)

# - "Hello World" ifadesindeki w harfini W harfi ile değiştirin.
s = "Hello World"
print(s[0:6] +  "W" + s[-4:])
# ya da .replace() metodu kullaniriz.
print(s.replace("w", "W"))

# - "abc" ifadesini yan yana 3 defa yazdirin.
s = "abc"
print(3*s)