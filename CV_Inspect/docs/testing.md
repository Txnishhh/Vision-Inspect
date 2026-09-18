# Testing Approach

## Unit Tests
- File validation
- Triangle classification
- Square classification
- Rectangle classification
- Circle classification
- Geometric feature extraction

Run:
```bash
pytest -q
```

## Validation Test
Generate the included synthetic image:
```bash
python -m cvinspect.cli generate-sample --output data/sample_shapes.png
```

Then analyze it:
```bash
python -m cvinspect.cli analyze data/sample_shapes.png --output outputs --save-intermediate
```

Inspect:
- `outputs/annotated.png`
- `outputs/analysis.json`
- preprocessing images

## Expected Behavior
The sample contains several high-contrast geometric objects. The analyzer should detect multiple contours and report their estimated shapes and geometric features. Exact counts can vary slightly with OpenCV version and thresholding behavior.
