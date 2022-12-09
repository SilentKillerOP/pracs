def sgn(net_input): 
    if net_input <= 0:
     return -1
    return 1

def pattern_classiﬁer(n_iterations, input, weight, desired_output, learning_rate): 
    for iteration in range(n_iterations):
        print(f'Iteration {iteration+1}') 
        output = []
    for i, X in enumerate(input):
        net_input = 0
    for j in range(len(X)):
        net_input += weight[j]*X[j]
    generated_output = sgn(net_input) 
    output.append(generated_output)
    if generated_output != desired_output[i]:
      difference = desired_output[i] - generated_output 
    for position in range(len(weight)):
        weight[position] = ﬂoat("{:.2f}".format(weight[position] + learning_rate*difference*X[position]))
        print(f'Generated Output vector for Iteration {iteration+1} : {output}') 
        print(f'Weight vector after Iteration {iteration+1}: {weight}')
        print("------"*15)
        if output == desired_output:
            break
    return output, weight


def main(): 
    inputt = [
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],  # L starts here
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1],

    [0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],  # M starts here
    [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
]


    desired_output = [1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    initial_weight = [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1]
    learning_rate = 0.05
    n_iterations = 3
    classiﬁcation_output, weight_vector = pattern_classiﬁer(n_iterations, inputt, initial_weight,
                                                            desired_output, learning_rate)
    count = 0
    for i, output in enumerate(classiﬁcation_output):
        if output == desired_output[i]:
            count += 1

    accuracy = (count / len(inputt))*100 
    print(f'Accuracy of Classiﬁer : {accuracy} %')
    print('Classifying an Unknown Sample of L (Output = 1)') 
    unknown_sample = [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0]
    print('Unknown Sample : ', unknown_sample) 
    net_input = 0
    for i in range(len(unknown_sample)):
        net_input += weight_vector[i]*unknown_sample[i]
        predicted_output = sgn(net_input) 
    print('Predicted Output : ', predicted_output) 
    print("\n")
main()
