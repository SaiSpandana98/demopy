def main():
    order = "rcta"
    inputArray = ["car", "rat", "cat",]

    lengthArray = len(inputArray)
    sortStringArray(order, inputArray, lengthArray)

def sortStringArray(order, inputArray, lengthArray):
    inputArray = sorted(inputArray, key = lambda word: [order.index(s) for s in word])
    print(inputArray)

if __name__ == "__main__":
    main()



