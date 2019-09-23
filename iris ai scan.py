import math
import turtle

def create_table(file_name):
    tupl = ()
    length = []
    width = []
    flower = []
    f = open(file_name,"r")
    for line in f:
        line = line.strip().split(",")
        length.append(float(line[0]))
        width.append(float(line[1]))
        flower.append(line[2])
    tupl += length,width,flower
    return tupl

def print_range_max_min(data):
    for i in range(len(data)):
        if i == 0:
            max_val1 = max(data[i])
            min_val1 = min(data[i])
            range1 = max_val1 - min_val1
        elif i == 1:
            max_val2 = max(data[i])
            min_val2 = min(data[i])
            range2 = max_val2 - min_val2
    print("Feature 1 - min: " + str(min_val1) + " max: " + str(max_val1) + " range: " + str(range1))
    print("Feature 1 - min: " + str(min_val2) + " max: " + str(max_val2) + " range: " + str(range2))

def find_mean(feature):
    acc = 0
    count = 0
    for i in range(len(feature)):
        acc += feature[i]
        count += 1
    return acc/count

def find_std_dev(feature, mean):
    total = 0
    count = 0
    for i in range(len(feature)):
        total += (feature[i] - mean) ** 2
        count += 1
    return math.sqrt(total/count)

def normalize_data(data):
    mean1 = 0
    mean2 = 0
    std_dev1 = 0
    std_dev2 = 0
    normalized_value_mean1 = 0
    normalized_value_mean2 = 0
    normalized_value_std_dev1 = 0
    normalized_value_std_dev2 = 0
    for i in range(2):
        if i == 0:
            mean1 = find_mean(data[i])
            std_dev1 = find_std_dev(data[i],mean1)
        elif i == 1:
            mean2 = find_mean(data[i])
            std_dev2 = find_std_dev(data[i],mean2)
    for k in range(2):
            if k == 0:
                temp_count = 0
                normalized_value_total1 = 0
                normalized_value_total2 = 0
                for norm_mean1 in range(len(data[k])):
                    data[k][norm_mean1] = ((data[k][norm_mean1] - mean1)/std_dev1)
                    normalized_value_total1 += data[k][norm_mean1] # norm total
                    temp_count += 1
                normalized_value_mean1 = normalized_value_total1/temp_count
                for norm_std_dev1 in range(len(data[k])):
                    normalized_value_total2 += ((data[k][norm_std_dev1]) - normalized_value_mean1) ** 2
                normalized_value_std_dev1 = normalized_value_total2/temp_count
            elif k == 1:
                temp_count = 0
                normalized_value_total1 = 0
                normalized_value_total2 = 0
                for norm_mean2 in range(len(data[k])):
                    data[k][norm_mean2] = ((data[k][norm_mean2] - mean2)/std_dev2)
                    normalized_value_total1 += data[k][norm_mean2]
                    temp_count += 1
                normalized_value_mean2 = normalized_value_total1/temp_count
                for norm_std_dev2 in range(len(data[k])):
                    normalized_value_total2 += ((data[k][norm_std_dev2]) - normalized_value_mean1) ** 2
                normalized_value_std_dev2 = normalized_value_total2/temp_count
    
    print("Feature 1 - mean: " + str(mean1) + " std dev: " + str(std_dev1))
    print("Feature 1 after normalization - mean: " + str(normalized_value_mean1) + " std dev: " + str(normalized_value_std_dev1))
    print("Feature 2 - mean: " + str(mean2) + " std dev: " + str(std_dev2))
    print("Feature 2 after normalization - mean: " + str(normalized_value_mean2) + " std dev: " + str(normalized_value_std_dev2))

def make_predictions(train_set, test_set):
    initial = 7
    test_set_list_x = []
    test_set_list_y = []
    test_set_list_name = []
    train_set_list_x = []
    train_set_list_y = []
    train_set_list_name = []
    test_set_list = []
    train_set_list = []
    pred_lst = []
    for i in range(3):
        for numbers in range(len(test_set[i])):
            if i == 0:
                test_set_list_x.append(test_set[i][numbers])
            elif i == 1:
                test_set_list_y.append(test_set[i][numbers])
            elif i == 2:
                test_set_list_name.append(test_set[i][numbers])
        for numbers2 in range(len(train_set[i])):
            if i == 0:
                train_set_list_x.append(train_set[i][numbers2])
            elif i == 1:
                train_set_list_y.append(train_set[i][numbers2])
            elif i == 2:
                train_set_list_name.append(train_set[i][numbers2])
    test_set_list += test_set_list_x, test_set_list_y, test_set_list_name
    train_set_list += train_set_list_x, train_set_list_y, train_set_list_name
    for l in range(len(test_set_list[0])):
        temp_name = ""
        temp_count = initial
        x2 = test_set_list[0][l]
        y2 = test_set_list[1][l]
        for k in range(len(train_set_list[0])):
            x1 = train_set_list[0][k]
            y1 = train_set_list[1][k]
            distance = find_dist(x1,y1,x2,y2)
            if distance <= temp_count:
                temp_count = distance
                temp_name = train_set_list[2][k]
            else:
                temp_count = temp_count
                temp_name = temp_name
        pred_lst.append(temp_name)
    return(pred_lst)

def find_dist(x1, y1, x2, y2):
    distance = math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
    return distance

def find_error(test_data, pred_lst):
    incorrect = 0
    total = len(test_data[2])
    for i in range(len(test_data[2])):
        if pred_lst[i] != test_data[2][i]:
            incorrect += 1
    return incorrect/total
        

def plot_data(train_data, test_data, pred_lst):
    draw_key()
    for  i in range(len(train_data[0])):
        if train_data[2][i] == "Iris-setosa":
            turtle.goto(125*train_data[0][i], 125*train_data[1][i])
            turtle.color("blue")
        elif train_data[2][i] == "Iris-versicolor":
            turtle.goto(125*train_data[0][i], 125*train_data[1][i])
            turtle.color("green")
        else:
            turtle.goto(125*train_data[0][i], 125*train_data[1][i])
            turtle.color("orange")
        turtle.dot(10)
    for k in range(len(test_data[0])):
        if pred_lst[k] == test_data[2][k]:
            if pred_lst[k] == "Iris-setosa":
                turtle.goto(125*test_data[0][k], 125*test_data[1][k])
                turtle.color("blue")
            elif pred_lst[k] == "Iris-versicolor":
                turtle.goto(125*test_data[0][k], 125*test_data[1][k])
                turtle.color("green")
            elif pred_lst[k] == "Iris-viriginica":
                turtle.goto(125*test_data[0][k], 125*test_data[1][k])
                turtle.color("orange")
            turtle.begin_fill()
            for l in range(5):
                if l == 0:
                    turtle.forward(5) # right
                    turtle.right(90)
                elif l == 4:
                    turtle.forward(5)
                else:
                    turtle.forward(10) # down
                    turtle.right(90)
            turtle.end_fill()
        else:
            turtle.goto(125*test_data[0][k], 125*test_data[1][k])
            turtle.color("red")
            turtle.begin_fill()
            for j in range(5):
                    if j == 0:
                        turtle.forward(5) # right
                        turtle.right(90)
                    elif j == 4:
                        turtle.forward(5)
                    else:
                        turtle.forward(10) # down
                        turtle.right(90)
            turtle.end_fill()

def draw_key():
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.setup(500,500)
    turtle.goto(180,0)
    turtle.write("petal length")
    turtle.goto(250,0)
    turtle.goto(0,0)
    turtle.penup()
    turtle.goto(10,-240)
    turtle.write("petal width")
    turtle.goto(0,-250)
    turtle.pendown()
    turtle.goto(0,0)
    turtle.goto(-250,0)
    turtle.goto(0,0)
    turtle.goto(0,250)
    for i in range(7):
        turtle.penup()
        if i >= 3:
            if i == 3:
                turtle.goto(-220,180)
                turtle.color("blue")
            elif i == 4:
                turtle.goto(-220,165)
                turtle.color("green")
            elif i == 5:
                turtle.goto(-220,150)
                turtle.color("orange")
            else:
                turtle.goto(-220,135)
                turtle.color("red")
            turtle.begin_fill()
            for k in range(5):
                if k == 0:
                    turtle.forward(5) # right
                    turtle.right(90)
                elif k == 4:
                    turtle.forward(5)
                else:
                    turtle.forward(10) # down
                    turtle.right(90)
            turtle.end_fill()
        elif i == 0:
            turtle.goto(-220,220)
            turtle.color("blue")
            turtle.dot(10)
        elif i == 1:
            turtle.goto(-220,205)
            turtle.color("green")
            turtle.dot(10)
        elif i == 2:
            turtle.goto(-220,190)
            turtle.color("orange")
            turtle.dot(10)
    for i in range(7):
        turtle.color("black")
        turtle.penup()
        if i == 0:
            turtle.goto(-210,213)
            turtle.write("Iris-setosa")
        elif i == 1:
            turtle.goto(-210,197)
            turtle.write("Iris-versicolor")
        elif i == 2:
            turtle.goto(-210,182)
            turtle.write("Iris-virginica")
        elif i == 3:
            turtle.goto(-210,167)
            turtle.write("predicted Iris-setosa")
        elif i == 4:
            turtle.goto(-210,153)
            turtle.write("predicted Iris-versicolor")
        elif i == 5:
            turtle.goto(-210,138)
            turtle.write("predicted Iris-virginica")
        elif i == 6:
            turtle.goto(-210,124)
            turtle.write("predicted incorrectly")


def main():
    train_data = create_table("iris_train.csv")
    print_range_max_min(train_data[:2])
    print()
    normalize_data(train_data)
    test_data = create_table("iris_test.csv")
    print()
    normalize_data(test_data)
    pred_lst = make_predictions(train_data, test_data)
    error = find_error(test_data, pred_lst)
    print()
    print("The error percentage is: ", error)
    plot_data(train_data, test_data, pred_lst)

main()
