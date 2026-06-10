#conferir o ano colocado
with open("life-expectancy.csv") as file:
    next(file)
    max_life = 0
    min_life = 999
    max_country = ""
    min_country = ""
    min_year = 0
    max_year = 0
    total_life = 0
    average = 0
    max_life_specific = 0
    min_life_specific = 999
    max_country_specific = ""
    min_country_specific = ""
    min_year_specific = 0
    max_year_specific = 0

    year_input = int(input("Enter the year of interest: "))
    for line in file:        
        parts = line.split(",")
        entity = parts[0]
        code = parts[1]
        year = int(parts[2])
        life_expectancy = float(parts[3])

        if min_life > life_expectancy:
            min_life = life_expectancy
            min_country = entity
            min_year = year

        if max_life < life_expectancy:
            max_life = life_expectancy
            max_country = entity
            max_year = year

        if year_input == year:
            total_life += life_expectancy
            average = total_life / len(entity)#It need to be fixed

            if min_life_specific > life_expectancy:
                min_life_specific = life_expectancy
                min_country_specific = entity

            if max_life_specific < life_expectancy:
                max_life_specific = life_expectancy
                max_country_specific = entity
        

    print(f"\nThe overall max life expectancy is: {max_life} from {max_country} in {max_year}")        
    print(f"The overall min life expectancy is: {min_life} from {min_country} in {min_year}")
    print(f"\nFor the year {year_input}:")
    print(f"The average life expectancy across all countries was {average:.2f}")
    print(f"The max life expectancy was in {max_country_specific} with {max_life_specific}")        
    print(f"The min life expectancy was in {min_country_specific} with {min_life_specific}")




        
