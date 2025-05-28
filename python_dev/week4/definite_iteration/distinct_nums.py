def distinct_numbers(my_list: list) -> list:
    """This function takes a list as an arg and returns a new list with only 
       distinct numbers from the org one in order of magnitude."""
    distinct_list = set(my_list)
    return list(distinct_list)


if __name__ == "__main__":
    print(distinct_numbers(my_list=[4, 4, 3, 2, 2, 1, 3, 3, 1]))