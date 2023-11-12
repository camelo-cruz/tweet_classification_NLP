def accuracy(classifier, data):
    """Computes the accuracy of a classifier on reference data.

    Args:
        classifier: A classifier.
        data: Reference data.

    Returns:
        The accuracy of the classifier on the test data, a float.
    """
    ##################### STUDENT SOLUTION #########################
    # YOUR CODE HERE
    
    # true_labels = [0,1,1,1,1,0,0,1,0]
    # predicted_labels = [0,1,1,1,1,0,0,0,0]
    
    
    X = [tupla[0] for tupla in data]
    
    true_labels = [tupla[1] for tupla in data]
    predicted_labels = [classifier.predict(x) for x in X]
    
    
    correct = sum([1 for p, t in zip(predicted_labels, true_labels) if p == t])
    total = len(predicted_labels)    
    
    return float(correct/total)
    ################################################################


def f_1(classifier, data):
    """Computes the F_1-score of a classifier on reference data.

    Args:
        classifier: A classifier.
        data: Reference data.

    Returns:
        The F_1-score of the classifier on the test data, a float.
    """
    
    ##################### STUDENT SOLUTION #########################
    # YOUR CODE HERE
    
    X = [tupla[0] for tupla in data]
    
    true_labels = [tupla[1] for tupla in data]
    predicted_labels = [classifier.predict(x) for x in X]
    
    possible_labels = list(set(true_labels)) #not hardocode labels in evaluation
    
    positive = possible_labels[0]
    print('chosen positive class: ' + positive)
    negative = possible_labels[1]
    print('chosen negative class: ' + negative)
    
    
    tp = sum((p == positive and t == positive) for p, t in zip(predicted_labels, true_labels))
    fp = sum((p == positive and t == negative) for p, t in zip(predicted_labels, true_labels))
    fn = sum((p == negative and t == positive) for p, t in zip(predicted_labels, true_labels))
    
    try:
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
            
        f1_score = float(2 * precision * recall) / (precision + recall)
        
        return f1_score
    
    except Exception as e:
        
        print(f'{e} is happening with following valued tp: {tp}, fp: {fp}, fn: {fn}')
        
        return 0
    

    ################################################################


