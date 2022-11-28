array = [
    {
        "name":"Poland",
        "population":37780000
    },
    {
        "name":"Argentina",
        "population":45810000
    },
    {
        "name":"Saudi Arabia",
        "population":35340000
    },
    {
        "name":"Mexico",
        "population":130300000
    },
    {
        "name":"Germany",
        "population":83130000
    }
]
i = 0
while i<len(array):
    print(array[i]['name'], "-" ,array[i]['population'])
    i+=1