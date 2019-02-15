def nexon(a,b):
    generator = []
    total_number = []
    generator_elements = 0
    for number in range(a,b):
        total_number.append(number)
        number_list = list(str(number))
        for number_count in range(len(number_list)):
            generator_elements += int(number_list[number_count])
        generator_elements += number
        generator.append(generator_elements)
        generator_elements = 0
    set_generator = set(generator)
    set_total_number = set(total_number)
    self_number = set_total_number - set_generator
    self_number_list = list(self_number)
    print(sum(self_number_list))

nexon(1,5000)

