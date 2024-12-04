def getNumbers(lines):
    list = []
    for line in lines:
        numbers = []
        temp = 0
        for c in line:
            if c.isdigit():
                temp = temp * 10 + int(c)
            else:
                numbers.append(temp)
                temp = 0
        list.append(numbers)
    return list

def determineSafetyStep2(numbers):
    count = 0;
    for number in numbers:
        status = determineSafetyLoop(number)
        if status != "Not safe":
            count += 1
        if status == "Not safe":
            for i in range(len(number)):
                updated_list = [element for j, element in enumerate(number) if j != i]
                status = determineSafetyLoop(updated_list)
                if status != "Not safe":
                    count += 1
                    break
    return count

                
def determineSafetyLoop(number):
    prev = number[0]
    status = ""
    for num in number[1:]:
            if prev == num:
                status = "Not safe"
                break
            if prev > num:
                if(abs(prev - num) > 3):
                    status = "Not safe"
                    break
                if status != "asc":
                    status = "des"
                    prev = num
                else:
                    status = "Not safe"
                    break

            if prev < num:
                if(abs(prev - num) > 3):
                    status = "Not safe"
                    break
                if status != "des":
                    status = "asc"
                    prev = num
                else:
                    status = "Not safe"
                    break
    return status

def determineSafetyStep1(numbers, count):
    for number in numbers:
        status = ""
        prev = number[0]
        for num in number[1:]:
            if prev == num:
                status = "Not safe"
                count -= 1
                break
            if prev > num:
                if(abs(prev - num) > 3):
                    status = "Not safe"
                    count -= 1
                    break
                if status != "asc":
                    status = "des"
                    prev = num
                else:
                    status = "Not safe"
                    count -= 1
                    break

            if prev < num:
                if(abs(prev - num) > 3):
                    status = "Not safe"
                    count -= 1
                    break
                if status != "des":
                    status = "asc"
                    prev = num
                else:
                    status = "Not safe"
                    count -= 1
                    break
    return count

def main():
    text_file = open("puzzle.txt","r")
    lines = text_file.readlines()
    count = len(lines)
    numbers = getNumbers(lines)
    answer1 = determineSafetyStep1(numbers, count)
    answer2 = determineSafetyStep2(numbers)
    print("The answer for step 1: " + str(answer1))
    print("The answer for step 2: " + str(answer2))

main()

