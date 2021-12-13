desc = input("Binary Description: ")

# Country
country = desc[0:2]
if country == "00":
    # Canada
    print("我觉得这是加拿大。") # I think this is Canada
    print("我爱加拿大因为我是加拿大人。") # I love Canada because I am Canadian
elif country == "01":
    # China
    print("我觉得这是中国。") # I think this is china
    print("我喜欢中国因为我爱中式食物。") # I like china because I love chinese style food

elif country == "10":
    print("我觉得这是印度。") # I think this is India
    print("我喜印度因为我爱印度的食物") # I like India because I love india's food
elif country == "11":
    # Africa
    print("我觉得这是非洲。") # I think this is Africa
    print("我喜欢非洲因为我爱非洲动物。") # I like africa because I love african animals

# Inside vs outside
insideOutside = desc[2]

if insideOutside == "0":
    # Inside
    print("这在室内。") # This is inside

    # Large or Small room
    smallLarge = desc[3]

    if smallLarge == 1:
        # Small room
        print("它是小楼。") # It is a small room
    else:
        # Big room
        print("他是大楼") # It is a large room

    # Type of Building
    building = desc[4:7]
    if building == "000":
        # House
        print("这楼是房子。")
    elif building == "001":
        # Store
        print("这楼是商店。")
    elif building == "010":
        # Restaurant
        print("这楼是饭店。")
    elif building == "011":
        # School
        print("这楼是学校。")
    elif building == "100":
        # Office
        print("这楼是办公室。")
    elif building == "101":
        # Hospital
        print("这楼是医院。")

else:
    # Outside 34567
    print("这在户外。")

    # Season
    season = desc[3:5]
    if season == "00":
        # Winter
        print("现在是冬天")
    elif season == "01":
        # Fall
        print("现在是秋天")

    elif season == "10":
        # Spring
        print("现在是春天")
    elif season == "11":
        # Summer
        print("现在是夏天")

    # Temperature
    temperature = desc[5]
    if temperature == "0":
        # Cold
        print("气温是冷。")
    elif temperature == "1":
        # Hot
        print("气温是热。")

    # Weather
    weather = desc[6:8]
    if weather == "00":
        # Snowing
        print("天气有下雪")
    elif weather == "01":
        # Raining
        print("天气有下雨")
    elif weather == "10":
        # Cloudy
        print("天气有多云")
    elif weather == "11":
        # Sunny
        print("天气有晴朗")

# Food
food = desc[8]
if food == "1":
    print("图片有食物。") # The image has food
    print("我要吃那个食物因为我不吃午餐。") # I want to eat that food because I didn't eat lunch

# Animals
animal = desc[9]
if animal == "1":
    dog = desc[10]
    if dog == "1":
        # Dog
        print("图片有一只狗。")
        print("我喜欢狗因为我的家有一只狗。他十大和黑色的和他加Luko。")
    else:
        # Animal that isn't a dog
        print("他有一只动物。")
        print("我讨厌那只动物因为它很丑。")

# People
people = desc[11]
if people == "1":
    # Number of Adults and children
    print("有X个大人和Y个儿童。")
    print("Now describe one of the people I'm too lazy to code this in and also its like 4 am bruh you are so stupid")
else:
    print("对不起老师...")

print("Finished")