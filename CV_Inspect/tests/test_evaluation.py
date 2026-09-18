from cvinspect.evaluation import classification_accuracy, per_class_metrics

def test_accuracy():
    assert classification_accuracy(["circle","square"],["circle","square"]) == 1.0

def test_metrics():
    m=per_class_metrics(["circle","square","circle"],["circle","square","circle"])
    assert m["circle"]["precision"] == 1.0
    assert m["circle"]["recall"] == 1.0
