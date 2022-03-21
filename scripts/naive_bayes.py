import csv
from math import log
from collections import (
    defaultdict,
    Counter,
)

def load_csv(path):
    """Load CSV data from a file.

    :param path: The path of the CSV file to load.
    :return: A list of the dataset.
    """
    with open(path, encoding='utf-8') as f:
        lines = csv.reader(f)
        dataset = list(lines)
    return dataset

class DiscreteFeatureVectors:
    """Collection of discrete feature vectors."""

    def __init__(self, use_smoothing):
        """Construct a container for discrete feature vectors.

        :param use_smoothing: A boolean to indicate whether to use smoothing.
        """
        self.use_laplace_smoothing = use_smoothing
        self.possible_categories = defaultdict(set)
        self.frequencies = defaultdict(lambda: defaultdict(lambda: Counter()))

    def add(self, label, index, feature):
        self.frequencies[label][index][feature] += 1
        self.possible_categories[index].add(feature)

    def probability(self, label, index, feature, num_label_instances):
        """Calculate probability with Laplace smoothing optionally."""
        frequency = self.frequencies[label][index][feature]
        frequency += 1 if self.use_laplace_smoothing else 0

        num_classes = len(self.possible_categories[index])
        num_label_instances += num_classes if self.use_laplace_smoothing else 0
        return frequency / num_label_instances


class NaiveBayes:
    def __init__(self, use_smoothing=True) -> None:
        self.priors = defaultdict(dict)
        self.label_counts = Counter()
        self.discrete_feature_vectors = DiscreteFeatureVectors(use_smoothing)
        self._is_fitted = False
    
    def fit(self, design_matrix, target_values):
        for i, training_example in enumerate(design_matrix):
            label = target_values[i]
            self.label_counts[label] += 1
            features = training_example
            for j, feature in enumerate(features):
                self.discrete_feature_vectors.add(label, j, feature)
        total_num_records = len(target_values)
        for label in set(target_values):
            self.priors[label] = self.label_counts[label] / total_num_records

        self._is_fitted = True
        
        return self
    
    def predict_record(self, test_record):
        """Predict the label for the test record.

        Maximizes the log likelihood to prevent underflow.

        :param test_record: Test record to predict a label for.
        :return: The predicted label.
        """

        self.check_is_fitted()

        likelihood = {k : log(v) for k, v in self.priors.items()}
        
        for label in self.label_counts:
            for i, feature in enumerate(test_record):
                probability = self._get_probability(i, feature, label)
                try:
                    likelihood[label] += log(probability)
                except ValueError:
                    raise ValueError(
                        f'Value {feature} never occurs with class {label}. Please set use_smoothing to True in the constructor.'
                    )
        print()
        for k, v in self.discrete_feature_vectors.frequencies.items():
            print(k, v)
            print()
        for k, v in self.discrete_feature_vectors.possible_categories.items():
            print(k, v)

        return max(likelihood, key=likelihood.get)
    
    def _get_probability(self, feature_idx, feature, label):
        return self.discrete_feature_vectors.probability(
            label=label,
            index=feature_idx,
            feature=feature,
            num_label_instances=self.label_counts[label],
        )
    
    
    def check_is_fitted(self):
        if not self._is_fitted:
            raise ValueError(
                f"This instance of {self.__class__.__name__} has not been fitted yet. Please call 'fit' before you call 'predict'."
            )
        return True if self._is_fitted else False

if __name__ == '__main__':
    dataset = load_csv('./dataset2.csv')
    
    design_matrix = [row[:-1] for row in dataset]
    target_values = [row[-1] for row in dataset]

    clf = NaiveBayes(use_smoothing=False)
    clf.fit(design_matrix, target_values)

    _record = ['<=30', 'medium', 'yes', 'fair']
    flag = clf.predict_record(_record)
    print(flag)
