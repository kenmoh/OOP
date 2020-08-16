# To find a friend or for by the length of name
def friend_or_foe(*names):
    my_friends = []
    for name in names:
        for friends in name:
            if len(friends) == 4:
                my_friends.append(friends)
    return my_friends


list_of_names = ['Kenneth', 'Kemi', 'Rita', 'Hope', 'Emmy', 'Adam']
my_friends = friend_or_foe(list_of_names)
# print(my_friends)


# Function to Display the shortest word in a sentence
def smallest_words(words):
    all_words = []
    # print(len(words))
    new_words = words.split()
    for word in new_words:
        len_of_words = len(word)
        all_words.append(len_of_words)
    return min(all_words)

x = smallest_words('Just me ken')


def divisors(n):
    numbers = []
    divisors = [n for n in range(2, n)]
    for divisor in divisors:
        if n % divisor == 0:
            numbers.append(divisor)
    if numbers == []:
        return f'{n} is Prime'
    return numbers


f = divisors(14)
print(f)


# Create a phone number from a list of numbers
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

x = create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(x)
