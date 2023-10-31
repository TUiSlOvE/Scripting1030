num_stars = int(input("請輸入星星數量："))
if num_stars % 2 == 0:
    print("給予的星星數請輸入單數")
else:
    for i in range(1, num_stars + 1, 2):
        spaces = " " * ((num_stars - i) // 2)
        stars = "*" * i
        print(spaces + stars)

    for i in range(num_stars - 2, 0, -2):
        spaces = " " * ((num_stars - i) // 2)
        stars = "*" * i
        print(spaces + stars)
