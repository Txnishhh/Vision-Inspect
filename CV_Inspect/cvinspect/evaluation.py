def classification_accuracy(predictions, ground_truth):
    if not ground_truth: return 0.0
    return sum(p == g for p,g in zip(predictions, ground_truth)) / len(ground_truth)

def per_class_metrics(predictions, ground_truth):
    labels = sorted(set(predictions) | set(ground_truth)); out = {}
    for label in labels:
        tp=sum(p==label and g==label for p,g in zip(predictions,ground_truth))
        fp=sum(p==label and g!=label for p,g in zip(predictions,ground_truth))
        fn=sum(p!=label and g==label for p,g in zip(predictions,ground_truth))
        out[label]={"precision":tp/(tp+fp) if tp+fp else 0.0,"recall":tp/(tp+fn) if tp+fn else 0.0}
    return out
