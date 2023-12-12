# nums = [1, 3, 5, 2, 4, 3]
# print(len(nums))                # "len"(lenght) ფუნქცია ითვლის სიაში მყოფ ელემენტებების რაოდენობას
                                  # ის ითვლის "string" ში სიმბოელების რაოდენობას


# surname = "gafrindashvili"
# print(len(surname))             # ითვლის ასოებს (space ები ითვლება)



# nums = [1, 3, 5, 2, 4, 3]
# set_of_nums = set(nums)             
# print(set_of_nums)
# {1, 2, 3, 4, 5}

# letters = ["a", "b", "c"]
# letters += ["d"]
# print(len(letters))

# age = 10
# age += 5
# print(age)                        # += არის დაეტოლოს და გაუტოლდეს ახალ მნიშვნელობას



# x = "abc"

# x*= 2                # 3 გამრავლდა 2 ზე

# print(len(x))



# nums = [1, 2, 3]
# nums.append(4,)                    # "append" არის ჩამატების ფუნქცია და ამატებს სიის ბოლოში
# print(nums)



# words = ["python", "fun"]
# words.insert(1, "is")                       # "insert" ფუნქცია ამატებს ელემენტს სასურველ ადგილას            
# print(words)




# შექმენით სია რომელშიც იქნება დედის და მამის სახელები და შემდეგ ამ სიაში ბოლოში ჩაამატეთ თქვენი თავი და 
#შუაში ჩაამატეთ ძმა და და ასშ. (inster და append ის გამოყენებით)

# family_names = ["irma", "jaba"]
# family_names.append("dato")
# family_names.insert(1,  "nuca")
# family_names.insert(2,  "aleqsi")
# print(family_names)



# letters = ['p', 'q', 'r', 's', 'p', 'u']
# print(letters.index('r'))                    
# print(letters.index('p'))                   # "index" ფუნქცია რომელიც გვიჩვენებს მერამდენე ადგილზეა ელემენტი
# print(letters.index('q'))                   #მნიშნელობა არ აქვს 1 ელემენტი რამდენჯერ წერია რომელიც პირველად ჩაიწერა იმას დაპრინტავს



# x = [2, 4, 5, 7, 4]
# y = x.index(4)
# print(y)


# x =  [1, 8, 42, 3]
# print(min(x))                 #მინიმალური რიცხვი სიიდან (ყველაზე პატარა)
# print(max(x))                 #მაქს რიცხვი სიიდან (ყველაზე დიდი)




# x = [2, 4, 6, 2, 7, 2, 9]

# print(x.count(2))               #ითვლის სიაში რამდენჯერ არის ელემენტი მოცემული

# x.remove(4)                   #შლის სიიდან კონრკრეტულ ელემეტენტს
# print(x)

# x.reverse()                   #აბრუნებს სიას უკუღმა
# print(x)

 

# nums =[2, 4, 8, 9, 5]

# nums.insert(1, 3)

# nums.remove(9)

# nums.insert(0, nums.count(8))      #დაითვალა რამდენი 8 იანი იყო და ჩაწერა სიაში

# print(nums[3])


# nums = [4, 5, 6]
# msg = "numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
# print(msg)



# nums = [4, 5, 6]
# msg = "numbers: {0} {3} {2}". format(nums[1], nums[1], nums[2])
# print(msg)




# family = ["irma", "nuca", "dato"]
# fam = "my mom is: {}".format(family([0]))
# print(fam)
# fam = "my bro is: {}".format(family([1]))
# print(fam)
# fam = "my name is: {}".format(family([2])) 
# print(fam)


# a = "my name is: {}".format("dato")
# print(a)

# a = "my name is: {} my surname is: {}".format("dato", "gafrindashvili")
# print(a)


# a = "my name is: {} my surname is: {}".format("dato", "gafrindashvili")
# print(a)

