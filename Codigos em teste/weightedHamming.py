def weighted_hamming(data):
    """ Compute weighted hamming distance on categorical variables. For one variable, it is equal to 1 if
        the values between point A and point B are different, else it is equal the relative frequency of the
        distribution of the value across the variable. For multiple variables, the harmonic mean is computed
        up to a constant factor.

        @params:
            - data = a pandas data frame of categorical variables

        @returns:
            - distance_matrix = a distance matrix with pairwise distance for all attributes
    """

    # Compute pairwise weighted hamming distance
    def pairwise_weighted_hamming(point_a, point_b, attribute_value_dict, number_observations):
        """ Compute the pairwise weighted Hamming distance between two points in a data set.

            @params:
                - point_a = the first point coordinates to use
                - point_b = the second point coordinates to use
                - attribute_value_dict = a dictionary that stores for each attribute, for each value the number
                of occurrences

            @returns:
                - distance = the weighted Hamming distance value
            """

        # Create an empty array to store the weights for each attribute
        weights = np.zeros((len(point_a)))

        # Compute the weight for each attribute
        for i, attribute in enumerate(attribute_value_dict):
            if point_a[attribute] == point_b[attribute]:
                weights[i] = 1.0 * attribute_value_dict[attribute][point_a[attribute]] / number_observations
            else:
                weights[i] = 1

        # Compute the weighted Hamming distance and return it
        distance = hmean(weights)
        return distance

    # Create a dictionary for each attribute that stores a dictionary of the count of each value within that attribute
    attribute_value_count = dict.fromkeys(set(data))
    for attribute in attribute_value_count:
        attribute_value_count[attribute] = defaultdict(int)
        for value in data[attribute]:
            attribute_value_count[attribute][value] += 1

    # Get the number of observations
    number_observations = data.shape[0]

    # Initialize an empty array to store the distances
    distances = np.zeros(shape = (number_observations, number_observations))

    # Fill up only the upper triangle
    for i in range(number_observations):
        for j in range(i + 1, number_observations):
            distances[i][j] = pairwise_weighted_hamming(data.iloc[i], data.iloc[j], attribute_value_count,
                                                        number_observations)

    # Copy the upper triangle to the lower one
    for i in range(number_observations):
        for j in range(i, number_observations):
            distances[j][i] = distances[i][j]

    return distances
