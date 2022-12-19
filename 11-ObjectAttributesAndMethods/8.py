class Arrays:
    @staticmethod
    def create_array(number_of_array_elements, value_of_array_elements):
        list = []
        for i in range(number_of_array_elements):
            list.append(value_of_array_elements)
        return list

    @staticmethod
    def create_array_with_random(number_of_array_elements, value_from, value_to):
        list = []
        import random
        for i in range(number_of_array_elements):
            list.append(random.randint(value_from,value_to))
        return list


    

arr1 =Arrays.create_array(10,4)
print(arr1)
arr2 =Arrays.create_array_with_random(10,-7,8)
print(arr2)