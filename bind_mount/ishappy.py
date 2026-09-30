def isHappy(n):
    num_list = []

    while True:
        temp = 0
        current = n
        while current > 0:
            remain = current % 10
            temp += remain ** 2
            current //= 10

        if temp == 1:
            return True

        if temp in num_list:
            return False

        num_list.append(temp)
        n = temp


if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)
    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")
    print("Results saved to /app/bind_mount/output.txt")


