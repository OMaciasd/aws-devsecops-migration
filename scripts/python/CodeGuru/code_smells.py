def inefficient_function(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


if __name__ == "__main__":
    print(inefficient_function([1, 2, 3, 4, 5]))
