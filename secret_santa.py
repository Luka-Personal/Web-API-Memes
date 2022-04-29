import random
import re
# ცარიელი list-ები
givers = []
res = []
# მაილის შესამოწმებლად
regex = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'

print("\n"+"თამაშის დასაწყებად დაწერეთ  start"+"\n"
      "\n"+"თამაშიდან გასასვლელად დაწერეთ  exit"+"\n")

# მოთამაშეების დამატების ფუნქცია
def genInput():

    while True:
        person = input("შეიყვანეთ მოთამაშეს სახელი:\n").lower()
        # თამაშიდან გასვლისთვის
        if person == "exit":
            print("მშვიდობით"+"\n")
            exit()
        # თამაშის დასაწყებად
        if person == "start":
            break
        # მაილის შემოწმება
        if (re.search(regex, person)):
            res.append(person)
            random.shuffle(res)

        else:
            print("E-mail ვერ მოიძებნა Self-Destructing in 3...2..1...trolololo"+"\n")
        # ერთიდაიგივე მაილების წაშლა/შემოწმება
        for i in res:
            if i not in givers:
                givers.append(i)
    # არ მივცეთ უფლება მომხმარებელს სამ მოთამაშეზე ნაკლების შეყვანა
    if len(givers) < 3:
        givers.clear()
        res.clear()
        print("\n"+"გთხოვთ, შეიყვანეთ ორ მოთამაშეზე მეტი!"+"\n")
        genInput()

# გენერაციის ფუნქცია


def genSecretSanta():
    result = []
    restart = True

    while restart:
        restart = False
        receivers = givers[:]

        for i in range(len(givers)):
            giver = givers[i]
            # ვირჩევთ random recievers
            receiver = random.choice(receivers)

            # თუ მივედით ბოლო giver-ამდე და ის უდრის reciever-ს, გენერირება თავიდან დავიწყოთ
            if (giver == receiver and i == (len(givers) - 1)):
                restart = True
                break
            else:
                # დავრწმუნდეთ რომ giver and reciever არ არიან ტოლი
                while (receiver == giver):
                    receiver = random.choice(receivers)
                # დავამატოთ შედეგი
                result.append(giver + ' is buying for ' + receiver)
                # წავშალოთ reciever lıst-იდან
                receivers.remove(receiver)
    # დავპრინტოთ საბოლოო შედეგი
    for r in result:
        print(r)

# ფუნქციების "გაშვება?" :DDD
def main():
    genInput()
    genSecretSanta()


if __name__ == '__main__':
    main()
